import os
import re
import requests
import traceback
import sys

from utils.constants import GITHUB_TODO_ISSUE_PATTERN, TODO_ISSUE_PATTERN, TODO_ISSUE_EXCLUDED_EXTENSION

# =====================
# CONFIG
# =====================
REPO = os.getenv("GITHUB_REPOSITORY")
if not REPO:
    raise EnvironmentError("GITHUB_REPOSITORY not found in environment")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_TOKEN not found in environment")
   

# =====================
# FUNCTIONS
# =====================

def get_current_branch():
    branch = os.getenv("GITHUB_REF_NAME")
    # Fallback for backward compatibility
    if not branch:
        branch = os.getenv("GITHUB_REF", "refs/heads/main").split("/")[-1]
    
    return branch
    
def get_issues_map():
    url = f"https://api.github.com/repos/{REPO}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    params = {
        "state": "all",
        "per_page": 100
    }

    issues_by_name = {}
    page = 1
    while True:
        params["page"] = page
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()

        issues = r.json()
        if not issues:
            break

        for issue in issues:
            match = re.match(GITHUB_TODO_ISSUE_PATTERN, issue["title"])
            if match:
                issue_name = match.group("issue_name").strip()
                issues_by_name[issue_name] = issue["number"]

        page += 1
        

    return issues_by_name

def get_issue_body(issue_number):
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}"
    r = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    r.raise_for_status()
    body = r.json().get("body")
    return body or ""

def update_issue_body(issue_number, body):
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}"
    r = requests.patch(url,
                       json={"body": body},
                       headers={"Authorization": f"token {GITHUB_TOKEN}"})
    r.raise_for_status()
    
from collections import defaultdict

def nested_dict():
    return defaultdict(nested_dict)

def insert_path(tree, parts, todo):
    if not parts:
        return
    head, *tail = parts
    if tail:
        insert_path(tree[head], tail, todo)
    else:
        tree[head].setdefault('_todos', []).append(todo)

def build_markdown(tree, indent=0):
    branch = get_current_branch()
    md = []
    for key, subtree in sorted(tree.items()):
        if key == '_todos':
            for todo_path, todo_text, todo_state, todo_row in subtree:
                md.append('  ' * indent + f"- [{'x' if todo_state == 'closed' else ' ' }] [{todo_text}](/{REPO}/blob/{branch}/{todo_path}?plain=1#L{todo_row})")
        else:
            md.append('  ' * indent + f"- {key}")
            md.extend(build_markdown(subtree, indent+1))
    return md

def build_markdown_tree(todos):
    tree = nested_dict()
    for path, *todo in todos:
        path = path.replace(os.sep, '/')
        parts = path.strip('/').split('/')
        insert_path(tree, parts, (path, *todo))
    return '\n'.join(build_markdown(tree))
    

def parse_issue_body_to_todos(body, base_path=""):
    branch = get_current_branch()
    todos = []
    for line in body.splitlines():
        stripped = line.strip()
        m_task = re.match(r"^- \[(?P<status> |x)\] \[(?P<todo>.+?)\]\((?P<path>.+[^?])(?:\?.+#L(?P<row>.+))\)$", stripped)

        if m_task:
            status_char = m_task.group("status")
            todo_text = m_task.group("todo")
            path = m_task.group("path")
            path = path[len(f"/{REPO}/blob/{branch}/"):]
            todo_row = int(m_task.group("row"))
            stato = "open" if status_char == " " else "closed"
            todos.append((path, todo_text.strip(), stato, todo_row))
        else:
            continue
    
    return todos
    
def beautify_issue_name(name):
    name = re.sub(r"[_-]+", " ", name)
    exclude_words = {"di", "e", "per", "del", "della", "dell", "dei", "degli"}
    words = [
        w.capitalize() if w.lower() not in exclude_words else w.lower()
        for w in name.split()
    ]
    return " ".join(words)
    
def standardize_path(path):
    return path.strip('\\').strip('/').replace('\\', '/')


def extract_todos_from_files(isses_map):
    todos_by_subject = {subj: [] for subj in isses_map}
    for root, _, files in os.walk("."):
        for f in files:
            if sum([f.endswith(file_ext) for file_ext in TODO_ISSUE_PATTERN]) > 0 and \
                sum([f.endswith(file_ext) for file_ext in TODO_ISSUE_EXCLUDED_EXTENSION]) == 0:
                path = os.path.join(root, f)
                rel_path = os.path.relpath(path, ".")
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    for line_number, line in enumerate(fh):
                        for match in re.finditer(TODO_ISSUE_PATTERN[os.path.splitext(rel_path)[1]], line):
                            issue_name = beautify_issue_name(match.group("issue_name").strip())
                            text = match.group("text").strip()
                            if issue_name in todos_by_subject:
                                todos_by_subject[issue_name].append((rel_path, text, 'open', line_number + 1))
    return todos_by_subject


def merge_todos_into_issue(existing_todos, found_todos):
    existing_map = {(standardize_path(path), text, row): (standardize_path(path), text, state, row) for path, text, state, row in existing_todos}
    found_map = {(standardize_path(path), text, row): (standardize_path(path), text, state, row) for path, text, state, row in found_todos}

    updated_tasks = []

    for key, todo in found_map.items():
        updated_tasks.append(todo)
    for key, todo in existing_map.items():
        if key not in found_map:
            path, text, _, row = todo
            updated_tasks.append((path, text, 'closed', row))

    return updated_tasks

# =====================
# MAIN
# =====================

if __name__ == "__main__":
    try:
        issues_map = get_issues_map()
    except Exception as e:
        print(f"[ERROR] Failed to generate issues map from GitHub Issues: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
    try:
        todos = extract_todos_from_files(issues_map)
    except Exception as e:
        print(f"[ERROR] Failed to extract todos: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)

    for subject, issue_number in issues_map.items():
        try:
            found_todos = todos.get(subject, [])
            existing_body = get_issue_body(issue_number)
            existing_todos = parse_issue_body_to_todos(existing_body, base_path=subject)

            new_body = merge_todos_into_issue(existing_todos, found_todos)
            if new_body != existing_body:
                update_issue_body(issue_number, build_markdown_tree(new_body))
                print(f"[OK] Issue {issue_number} updated ({subject})")
            else:
                print(f"[NOCHANGE] No changes for {subject}")
        except Exception as e:
            print(f"[ERROR] Issue {issue_number} ({subject}) update failed: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            
