import os
import re
import requests
import traceback
import sys
import difflib

from utils.constants import TODO_ISSUE_PATTERN, TODO_ISSUE_EXCLUDED_EXTENSION, TODO_ISSUE_EXCLUDED_FOLDERS
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
        text_lines = text.strip().splitlines()
        self.path = standardize_path(path)
        self.title = text_lines[0]
        self.description_lines = "\n".join(text_lines[1:]).strip().splitlines()
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
        
    def is_similar(self, other, threshold=0.8):
        if not isinstance(other, TodoNote):
            return False
            
        ratio = difflib.SequenceMatcher(None, self.get_compound_text(), other.get_compound_text()).ratio()
        return ratio >= threshold, ratio
    
        
    def __repr__(self):
        return f"TodoNote(title={self.title}, path={self.path}{self.create_row_position_link_metadata()})"

   
class RemoteTodoNote(TodoNote):
    def __init__(self, path, title, state, raw_rows):
        row_splitted = raw_rows.split('-')
        start = row_splitted[0]
        super().__init__(path, " ".join([line.strip() for line in title.splitlines()]), state, int(start))
        
        if len(row_splitted) == 2:
            end = row_splitted[1]
            end = int(end[1:])
            self.rows[1] = end
            self.multiline = True
    
    def add_description_line(self, line):
        self.description_lines.append(line.strip())
        if not self.is_multiline():
            self.multiline = True
        
class LocalTodoNote(TodoNote):
    def __init__(self, path, text, state, start_line, end_line):
        super().__init__(path, text, state, start_line)
        self.rows[1] = self.rows[0] + end_line
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
            "title": "Github",
            "number": 6,
            "labels":[
                {"name": "todo"}
            ]
        },{
            "title": "Sistemi Operativi",
            "number": 5,
            "labels":[
                {"name": "todo"}
            ]
        },{
            "title": "Materie",
            "number": 4,
            "labels":[
                {"name": "todo"}
            ]
        },{
            "title": "Filters Test",
            "number": 3,
            "labels":[
                {"name": "todo"}
            ]
        }]
        issues_by_name = {}
        for issue in issues:
            issue_labels = issue.get("labels", None) or []
            if not any(label.get("name") == "todo" for label in issue_labels):
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
            issue_labels = issue.get("labels", None) or []
            if not any(label.get("name") == "todo" for label in issue_labels):
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
            6: ""
            #5: "- sistemi-operativi\n  - teoria\n    - 03--processi-e-thread\n      - processi\n        - nozione\n          - pcb_e_context_switch.md\n            - [ ] [Creare esempio grafico per PCB e Context Switch](/londero-lorenzo/appunti-universitari/blob/main/sistemi-operativi/teoria/03--processi-e-thread/processi/nozione/pcb_e_context_switch.md?plain=1#L130)\n",
            #4: "- materie\n  - README.md\n    - [ ] [spostare tutte le materie universitarie qui](/londero-lorenzo/appunti-universitari/blob/main/materie/README.md?plain=1#L1-L9)\n\n          Cartelle interessate:\n          - machine-learning\n          - nozioni_generali\n          - poo\n          - sistemi-operativi\n          - tecnologie_web_per_il_cloud\n\n",
            #3: "- filters_test\n  - secondo_livello\n    - secondo_test.md\n      - [ ] [Questo è un formato TODO utilizzabile nei vari markdown](/londero-lorenzo/appunti-universitari/blob/main/filters_test/secondo_livello/secondo_test.md?plain=1#L4)\n\n  - test.md\n    - [ ] [Questo è un formato TODO utilizzabile nei vari markdown](/londero-lorenzo/appunti-universitari/blob/main/filters_test/test.md?plain=1#L57)\n\n    - [ ] [Questo è un formato TODO lungo inline utilizzabile nei vari markdown. Lorem ipsum dolor\n          sit amet, consectetur adipiscing elit. Quisque porttitor tincidunt mauris, et iaculis\n          lacus fringilla et. Integer vitae sollicitudin est. Curabitur ultricies gravida nisi at\n          pulvinar. Nulla at porttitor augue. Nulla et nisi ut turpis dignissim lobortis quis vitae\n          elit. Aenean tristique erat eget mi semper laoreet. Donec vestibulum accumsan consectetur.\n          Fusce congue purus sit amet diam semper rhoncus. Nunc non ex interdum, cursus massa a,\n          sollicitudin nunc. Nam a imperdiet elit, vel rutrum augue. Morbi sit amet feugiat ligula.\n          Sed aliquam nulla non nibh scelerisque, et consequat quam consequat. Duis sed est id ex\n          volutpat elementum nec in orci. Aenean a enim vel enim facilisis finibus. Maecenas sed\n          massa et justo aliquam ultrices vitae eget nisi. Cras cursus malesuada purus in\n          ullamcorper.](/londero-lorenzo/appunti-universitari/blob/main/filters_test/test.md?plain=1#L61)\n\n    - [ ] [Questo è un formato TODO multilinea utilizzabile nei vari markdown](/londero-lorenzo/appunti-universitari/blob/main/filters_test/test.md?plain=1#L66-L72)\n\n          Cras in massa nec urna pharetra vehicula. Vestibulum lectus est, auctor ac nisi.\n          In pharetra ultricies neque in condimentum. Aliquam erat volutpat. Cras laoreet.\n          Quisque et nisl interdum, sodales orci quis, mattis nulla. Suspendisse molestie.\n\n\n    - [ ] [Questo è un formato TODO multilinea lungo utilizzabile nei vari markdown](/londero-lorenzo/appunti-universitari/blob/main/filters_test/test.md?plain=1#L77-L92)\n\n          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent elit nunc, vehicula sit\n          amet elit varius, sagittis sagittis lacus. Duis non nibh risus. Phasellus efficitur justo\n          vitae efficitur suscipit. Duis luctus dolor nec tellus porta cursus. Orci varius natoque\n          penatibus.\n          Vivamus posuere nunc vitae nisl sodales, ac laoreet nulla porttitor. Ut id felis ut lectus\n          porta dictum. Vestibulum et massa eu enim convallis vestibulum. Integer laoreet leo eget\n          magna pulvinar cursus. Duis in pulvinar leo. Pellentesque vehicula mauris a molestie.\n          Nulla vestibulum lectus eget dui tincidunt pellentesque. Praesent vel nibh non felis\n          pharetra lobortis. Donec odio neque, faucibus vitae mattis eu, mattis eu ex. Cras\n          venenatis lorem augue. Proin feugiat ex nec sollicitudin ullamcorper. Sed risus nibh,\n          gravida quis ligula.\n\n"
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
        todo_title = match.group("todo")
        path = match.group("path")
        path = path[len(f"/{REPO}/blob/{branch}/"):]
        todo_row = match.group("row")
        state = "open" if status_char == " " else "closed"
        todos.append(RemoteTodoNote(path, todo_title, state, todo_row))

        todo_matches.append(match.group(0).strip())


    body_lines = body.splitlines()
    
    indent = 0
    last_todo = None
    for line in body_lines:
        if not line:
            continue
        if last_todo is not None and len(line) - len(line.lstrip()) >= indent:
            todos[last_todo].add_description_line(line)
            continue
        else:
            last_todo = None
        
        for i, match in enumerate(todo_matches):
            if match in line:
                indent = line.find(re.sub(r"- \[[ |x]\] ", "", match))
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
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in TODO_ISSUE_EXCLUDED_FOLDERS]
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
                        start_line_number = content[:match.start()].count("\n") + 1
                        end_line_number = content[match.start():match.end()].count("\n")
                        if issue_name in todos_by_subject:
                            todos_by_subject[issue_name].append(LocalTodoNote(rel_path, text, 'open', start_line_number, end_line_number))
                        else:
                            print(f"::warning file={rel_path},line={start_line_number}::Unable to match TODO with issue `{issue_name}`")

    return todos_by_subject
    
    

"""
TODO(github): raggiungere livello di similitudine 1.0 tra TODO locali e remoti

Attualmente la similitudine viene calcolata con soglia all’80%, il che permette 
di considerare uguali TODO con testo simile. L’obiettivo ideale è arrivare a
1.0, cioè garantire che i TODO siano *identici* sia in locale che su GitHub
Issues.

Problema:
- Non esiste ancora una funzione che trasformi il testo markdown in una
  struttura dati equivalente a quella ottenuta dalla conversione dei commenti
  nei file.
- Il confronto quindi rimane soggetto a piccole discrepanze dovute a formattazioni
  arbitrarie.

Proposta:
- Utilizzare direttamente, già in fase di esportazione dal file, la funzione
  `wrap_todo_text`.
- Questo permette di standardizzare il testo locale e renderlo già compatibile
  con quello generato da GitHub Actions, evitando conversioni ridondanti e
  potenziali differenze arbitrarie.
"""


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
                are_similar, ratio = found.is_similar(existing)
                if are_similar:
                    DEBUG_LOG(f"{found} added for similarity to {existing}, ratio level: {ratio}")
                    #DEBUG_LOG(f"local body: {found.get_compound_text()}")
                    #DEBUG_LOG(f"remote body: {existing.get_compound_text()}")
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
            
    duplicate_detected = False

    for i, task_i in enumerate(updated_tasks):
        for j in range(i + 1, len(updated_tasks)):
            task_j = updated_tasks[j]
            if (
                task_i.get_title().strip() == task_j.get_title().strip()
                and task_i.get_path() == task_j.get_path() and task_i.state != task_j.state
            ):
                duplicate_detected = True
                print(
                    f"::error file={task_i.get_path()},line={task_i.rows[0]}::"
                    f"Duplicate TODO detected between entries at lines {task_i.rows[0]} and {task_j.rows[0]} "
                    f"(title='{task_i.get_title().strip()}')."
                )

    if duplicate_detected:
        raise Exception("Duplicate TODOs detected during issue merging operation")


    return updated_tasks


# =====================
# MAIN
# =====================

if __name__ == "__main__":
    try:
        issues_map = get_issues_map()
    except Exception as e:
        print(f"::error::Failed to generate issues map from GitHub Issues: {e}")
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
        
    DEBUG_LOG("Online issue map: ", issues_map, sep='\n')
    
    try:
        global_local_todos = extract_todos_from_files(issues_map)
    except Exception as e:
        print(f"::error::Failed to extract todos: {e}")
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
                print(f"::notice::Issue {issue_number} updated ({subject})")
            else:
                print(f"::notice::No changes for {subject}")
            DEBUG_LOG("======================================== END ISSUE MERGING ========================================")
            
        except Exception as e:
            print(f"::error::Issue {issue_number} ({subject}) update failed: {e}")
            traceback.print_exc(file=sys.stderr)
            
