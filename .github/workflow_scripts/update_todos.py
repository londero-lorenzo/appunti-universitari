import os
import re
import requests
import traceback
import sys
import difflib

from utils.constants import TODO_ISSUE_PATTERN, TODO_ISSUE_EXCLUDED_EXTENSION
from utils.constants import DEBUG_LOG, DEBUG_ENABLED

# =====================
# CONFIG
# =====================
REPO = os.getenv("GITHUB_REPOSITORY")
if not REPO:
    raise EnvironmentError("GITHUB_REPOSITORY not found in environment")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_TOKEN not found in environment")
    
    
def standardize_path(path):
    return path.strip('\\').strip('/').replace('\\', '/')

class TodoNote:
    
    
    def __init__(self, path, text, state, start_row):
        text_lines = text.splitlines()
        self.path = standardize_path(path)
        self.title = text_lines[0]
        self.description_lines = [line for line in text_lines[1:] if line.strip()]
        if state == 'open' or state == 'closed':
            self.state = state
        else:
            raise Exception(f"Available states: ['open', 'closed'], not: {state}")
        
        self.rows = [start_row, start_row]
        self.multiline = False
    
    
    def create_row_position_link_metadata(self):
        data = f"?plain=1#L{self.rows[0]}"
        
        if self.is_multiline() and self.is_open():
            data += f"-L{self.rows[1]}"
            
        return data
        
    def set_closed(self):
        self.state = 'closed'
        
    def get_compound_text(self):
        return (self.title + '\n' + self.get_description().strip()).strip()
    
    def get_description(self):
        return "\n".join(self.description_lines)
        
    def get_description_splitted(self):
        return self.description_lines
     
    def is_multiline(self):
        return self.multiline
    
    def get_path(self):
        return self.path
    
    def get_title(self):
        return self.title
        
    def is_open(self):
        return self.state == 'open'
        
    def is_closed(self):
        return self.state == 'closed'
        
    def __repr__(self):
        return f"TodoNote(title={self.title}, path={self.path}{self.create_row_position_link_metadata()})"

   
class RemoteTodoNote(TodoNote):
    def __init__(self, path, text, state, raw_rows):
        row_splitted = raw_rows.split('-')
        start = row_splitted[0]
        super().__init__(path, text, state, int(start))
        
        if len(row_splitted) == 2:
            end = row_splitted[1]
            end = int(end[1:])
            self.rows[1] = end
            self.multiline = True
    
    def add_description_line(self, line):
        self.description_lines.append(line)
        if not self.is_multiline():
            self.multiline = True
        
class LocalTodoNote(TodoNote):
    def __init__(self, path, text, state, rows):
        super().__init__(path, text, state, rows)
        
        self.rows[1] = self.rows[0] + text.count('\n')
        if self.rows[1] > self.rows[0]:
            self.multiline = True
        
        
        
    
    

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
    if DEBUG_ENABLED:
        issues = [{
            "title": "Materie",
            "number": 4,
            "labels":{
                "name": "todo"
            }
        },{
            "title": "Filters Test",
            "number": 3,
            "labels":{
                "name": "todo"
            }
        }]
        issues_by_name = {}
        for issue in issues:
            issue_labels = issue.get("labels", None)
            if not issue_labels or issue_labels.get("name", '') != "todo":
                continue

            issue_name = issue.get("title", "").strip()
            issue_number = issue.get("number", "")
            if issue_name and issue_number:
                issues_by_name[issue_name] = issue_number
                
        return issues_by_name
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
            issue_labels = issue.get("labels", None)
            if not issue_labels or issue_labels != "todo":
                continue

            issue_name = issue.get("title", "").strip()
            issue_number = issue.get("number", "")
            if issue_name and issue_number:
                issues_by_name[issue_name] = issue_number

        page += 1
        

    return issues_by_name

def get_issue_body(issue_number):
    if DEBUG_ENABLED:
        data = {
            4: "- materie\n  - README.md\n    - [ ] [spostare tutte le materie universitarie qui\n\n          Cartelle interessate:\n          - machine-learning\n          - nozioni_generali\n          - poo\n          - sistemi-operativi\n          - tecnologie_web_per_il_cloud](/londero-lorenzo/appunti-universitari/blob/main/materie/README.md?plain=1#L1)\n    - [ ] [Variante 2](/londero-lorenzo/appunti-universitari/blob/main/materie/README.md?plain=1#L44)",
            3: "- filters_test\n  - test.md\n    - [ ] [Questo è un formato TODO utilizzabile nei vari markdown](/londero-lorenzo/appunti-universitari/blob/main/filters_test/test.md?plain=1#L55)\n\n    - [x] [Questo è un formato TODO multilinea utilizzabile nei vari markdown](/londero-lorenzo/appunti-universitari/blob/main/filters_test/test.md?plain=1#L66)\n\n          Cras in massa nec urna pharetra vehicula. Vestibulum lectus est, auctor ac nisi.\n          In pharetra ultricies neque in condimentum. Aliquam erat volutpat. Cras laoreet.\n          Quisque et nisl interdum, sodales orci quis, mattis nulla. Suspendisse molestie."
        }
        return data.get(issue_number, '')
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}"
    r = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
    r.raise_for_status()
    body = r.json().get("body")
    return body or ""

def update_issue_body(issue_number, body):
    if DEBUG_ENABLED:
        DEBUG_LOG(f"issue number: {issue_number}")
        DEBUG_LOG("issue body:")
        print(body)
        return
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
        
def wrap_todo_text(text, left_margin, max_total_len= 100):
    max_line_len = max_total_len - len(left_margin)
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) - 1 + len(word) + 1 > max_line_len:
            lines.append(" ".join(current_line))
            current_line = [word]
        else:
            current_line.append(word)

    if current_line:
        lines.append(" ".join(current_line))

    return ("\n" + " " * len(left_margin)).join(lines)

def build_markdown(tree, indent=0):
    branch = get_current_branch()
    md = []
    for key, subtree in sorted(tree.items()):
        if key == '_todos':
            for todo in subtree:
                indent_plus_marker = '  ' * indent + f"- [{'x' if todo.is_closed() else ' ' }] "
                title_todo_text = wrap_todo_text(todo.get_title(), indent_plus_marker)
                md.append(indent_plus_marker + f"[{title_todo_text}](/{REPO}/blob/{branch}/{todo.get_path()}{todo.create_row_position_link_metadata()})\n")
                if todo.is_multiline():
                    md.append("\n".join([" " * len(indent_plus_marker) + wrap_todo_text(row, indent_plus_marker) for row in todo.get_description_splitted()])+ '\n'*2)
                
        else:
            md.append('  ' * indent + f"- {key}")
            md.extend(build_markdown(subtree, indent+1))
    return md

def build_markdown_tree(todos):
    tree = nested_dict()
    for todo in todos:
        parts = todo.get_path().split('/')
        insert_path(tree, parts, todo)
    return '\n'.join(build_markdown(tree))

def parse_issue_body_to_todos(body, base_path=""):
    branch = get_current_branch()
    todos = []
    todo_matches = []
    for match in re.finditer(r"\s*- \[(?P<status> |x)\] \[(?P<todo>.+?)\]\((?P<path>[^\s)]+)(?:\?[^\s]+#L(?P<row>[^\s]+?)?)\)", body, flags= re.MULTILINE | re.DOTALL):
        status_char = match.group("status")
        todo_text = match.group("todo")
        path = match.group("path")
        path = path[len(f"/{REPO}/blob/{branch}/"):]
        todo_row = match.group("row")
        state = "open" if status_char == " " else "closed"
        todos.append(RemoteTodoNote(path, todo_text, state, todo_row))

        todo_matches.append(match.group(0).strip())


    body_lines = body.splitlines()
    
    indent = None
    last_todo = None
    for line in body_lines:
        if not line:
            continue
        
        if last_todo and len(line) - len(line.lstrip()) >= indent:        
            todos[last_todo].add_description_line(line)
            continue
        else:
            last_todo = None
        
        for i, match in enumerate(todo_matches):
            if match in line:
                indent = line.find(re.sub(r"^- \[[ |x]\] ", "", match))
                last_todo = i
                break;
        
        
    return todos
    
    
def beautify_issue_name(name):
    name = re.sub(r"[_-]+", " ", name)
    exclude_words = {"di", "e", "per", "del", "della", "dell", "dei", "degli"}
    words = [
        w.capitalize() if w.lower() not in exclude_words else w.lower()
        for w in name.split()
    ]
    return " ".join(words)
    



def extract_todos_from_files(isses_map):
    todos_by_subject = {subj: [] for subj in isses_map}
    for root, _, files in os.walk("."):
        for f in files:
            if sum([f.endswith(file_ext) for file_ext in TODO_ISSUE_PATTERN]) > 0 and \
                sum([f.endswith(file_ext) for file_ext in TODO_ISSUE_EXCLUDED_EXTENSION]) == 0:
                path = os.path.join(root, f)
                rel_path = os.path.relpath(path, ".")
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    content = fh.read() 
                    ext = os.path.splitext(rel_path)[1]
                    pattern = re.compile(TODO_ISSUE_PATTERN[ext], re.DOTALL)
                    todos = pattern.finditer(content)
                    for i, match in enumerate(todos):
                        if DEBUG_ENABLED and i == 0:
                            DEBUG_LOG("TODOs found at: ", rel_path)
                        issue_name = beautify_issue_name(match.group("issue_name").strip())
                        text = match.group("text")
                        if issue_name in todos_by_subject:
                            line_number = content[:match.start()].count("\n") + 1
                            todos_by_subject[issue_name].append(LocalTodoNote(rel_path, text, 'open', line_number))
    return todos_by_subject
    
    
def is_similar(a, b, threshold=0.8):
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    return ratio >= threshold, ratio

def merge_todos_into_issue(remote_todos, local_todos):
    updated_tasks = []
    matched_existing = set()

    for f, found in enumerate(local_todos):
        f_path = found.get_path()
        f_text = found.get_compound_text()
        matched = False
        for i, existing in enumerate(remote_todos):
            e_path = existing.get_path()
            e_text = existing.get_compound_text()
            if (standardize_path(e_path)) == (standardize_path(f_path)):
                are_similar, ratio = is_similar(e_text, f_text)
                if are_similar:
                    DEBUG_LOG(f"{found} added for similarity to {existing}, ratio level: {ratio}")
                    matched_existing.add(i)
                    updated_tasks.append(found)
                    matched = True
                    break
        if not matched:
            DEBUG_LOG(f"{found} added because it was not found in remote issues")
            updated_tasks.append(found)

    for i, existing in enumerate(remote_todos):
        if i not in matched_existing:
            DEBUG_LOG(f"{existing} closed because it was not found in local issues")
            existing.set_closed()
            updated_tasks.append(existing)

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
        
    DEBUG_LOG("Online issue map: ", issues_map, sep='\n')
    
    try:
        global_local_todos = extract_todos_from_files(issues_map)
    except Exception as e:
        print(f"[ERROR] Failed to extract todos: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
            
    for subject, issue_number in issues_map.items():
        try:
            DEBUG_LOG("======================================= START ISSUE MERGING =======================================")
            local_todos = global_local_todos.get(subject, [])
            if DEBUG_ENABLED:
                DEBUG_LOG("Local todos: ", build_markdown_tree(local_todos), sep='\n')
            remote_body = get_issue_body(issue_number)
            remote_todos = parse_issue_body_to_todos(remote_body, base_path=subject)
            if DEBUG_ENABLED:
                DEBUG_LOG("Remote todos: ", build_markdown_tree(remote_todos), sep='\n')
            new_body = merge_todos_into_issue(remote_todos, local_todos)
            if new_body != remote_body:
                update_issue_body(issue_number, build_markdown_tree(new_body))
                print(f"[OK] Issue {issue_number} updated ({subject})")
            else:
                print(f"[NOCHANGE] No changes for {subject}")
            DEBUG_LOG("======================================== END ISSUE MERGING ========================================")
            
        except Exception as e:
            print(f"[ERROR] Issue {issue_number} ({subject}) update failed: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            
