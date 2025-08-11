import os
import sys
import subprocess
import argparse
import venv
import platform
from utils.constants import PROJECT_ROOT_KEY
from utils.constants import WORKFLOW_SCRIPTS_LOCATION, WORKFLOW_SCRIPTS_HOME, WORKFLOW_SCRIPTS_PACKAGE, MARKDOWN_FILTER_NAME, MARKDOWN_CLEAN_FILTER_NAME, MARKDOWN_SMUDGE_FILTER_NAME


VENV_DIR = ".notesVenv"
REQUIREMENTS_FILE = "requirements.txt"


SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, VENV_DIR)
REQUIREMENTS_FILE = os.path.join(SCRIPT_DIR, REQUIREMENTS_FILE)   

def check_virtualenv(venv_dir):
    if os.path.isdir(venv_dir):
        print(f"Virtual environment already exists in `{venv_dir}`")
        return True
    return False
    
def print_activation_instructions(venv_dir):
    print("\nSetup completed.")
    print("To activate the environment manually:\n")
    if os.name == 'nt':
        print(f"  {venv_dir}\\Scripts\\activate.bat")
    else:
        print(f"  source {venv_dir}/bin/activate")
    print()

def create_virtualenv():
    print("Creating virtual environment...")
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(VENV_DIR)
    
def add_project_root_to_venv():
    print("Adding project root path to `.env` file...")
    
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write(f"{PROJECT_ROOT_KEY}={SCRIPT_DIR}")
    else:
        with open('.env', 'r') as f:
            env_variables = f.read()
        
        lines_post = []
        for line in env_variables.split("\n"):
            key, value = line.split("=")
            if key == PROJECT_ROOT_KEY:
                lines_post.append("=".join([key, SCRIPT_DIR]))
            else:
                lines_post.append("=".join([key, value]))
        
        env_post = "\n".join(lines_post)
        
        with open('.env', 'w') as f:
            f.write(env_post)
            
def get_pip_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, "Scripts", "pip.exe").replace(os.sep, '/')
    else:
        return os.path.join(VENV_DIR, "bin", "pip")

def get_activate_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'activate.bat').replace(os.sep, '/')
    else:
        return os.path.join(VENV_DIR, 'bin', 'activate')
    
    
def get_python_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'python.exe').replace(os.sep, '/')
    else:
        return os.path.join(VENV_DIR, 'bin', 'python')

def install_requirements():
    pip_path = get_pip_path()

    if not os.path.isfile(REQUIREMENTS_FILE):
        print(f"Error: {REQUIREMENTS_FILE} not found in {SCRIPT_DIR}")
        sys.exit(1)

    print(f"Installing packages from {REQUIREMENTS_FILE}...")
    subprocess.check_call([pip_path, "install", "-r", REQUIREMENTS_FILE])
   

 

def install_filters():
    def install_markdown_filter():

        script_clean_path = os.path.join(WORKFLOW_SCRIPTS_LOCATION, f"{MARKDOWN_CLEAN_FILTER_NAME}.py")
        script_smudge_path = os.path.join(WORKFLOW_SCRIPTS_LOCATION, f"{MARKDOWN_SMUDGE_FILTER_NAME}.py")

        if not os.path.isfile(script_clean_path) or not os.path.isfile(script_smudge_path):
            print("ERROR: One or both filter scripts not found.")
            sys.exit(1)

        python_path = get_python_path()
        if os.name == 'nt':  # Windows
            clean_command = f'export PYTHONPATH="{SCRIPT_DIR};{WORKFLOW_SCRIPTS_HOME}"; "{python_path}" -m {WORKFLOW_SCRIPTS_PACKAGE}.{MARKDOWN_CLEAN_FILTER_NAME} %f'
            smudge_command = f'export PYTHONPATH="{SCRIPT_DIR};{WORKFLOW_SCRIPTS_HOME}"; "{python_path}" -m {WORKFLOW_SCRIPTS_PACKAGE}.{MARKDOWN_SMUDGE_FILTER_NAME} %f'
        else: # Unix-like
            clean_command = f'export PYTHONPATH="{SCRIPT_DIR}:{WORKFLOW_SCRIPTS_HOME}"; "{python_path}" -m {WORKFLOW_SCRIPTS_PACKAGE}.{MARKDOWN_CLEAN_FILTER_NAME} %f'
            smudge_command = f'export PYTHONPATH="{SCRIPT_DIR}:{WORKFLOW_SCRIPTS_HOME}"; "{python_path}" -m {WORKFLOW_SCRIPTS_PACKAGE}.{MARKDOWN_SMUDGE_FILTER_NAME} %f'

        subprocess.check_call([
            "git", "config", f"filter.{MARKDOWN_FILTER_NAME}.clean", clean_command
        ])
        subprocess.check_call([
            "git", "config", f"filter.{MARKDOWN_FILTER_NAME}.smudge", smudge_command
        ])

        print(f"Git filter '{MARKDOWN_FILTER_NAME}' installed.")

    print("Installing git filters...")
    install_markdown_filter()
    
def disable_markdown_filter():
    subprocess.run([
            "git", "config", "--unset", f"filter.{MARKDOWN_FILTER_NAME}.clean"
        ])
    subprocess.run([
            "git", "config", "--unset", f"filter.{MARKDOWN_FILTER_NAME}.smudge"
        ])
    print(f"Git filter '{MARKDOWN_FILTER_NAME}' disabled.")
    
def disable_filters():
    print("Disabling git filters...")
    disable_markdown_filter()

    
def main():
    parser = argparse.ArgumentParser(
        prog='Environment Setup',
        description='Setup virtual environment and install filters.',
        add_help=True)
    parser.add_argument(
        '-r', '--reload_filters',
        help="Reload git clean and smudge filters only.",
        action='store_true'
    )
    parser.add_argument(
        '-d', '--disable_filters',
        help="Disable git filters.",
        action='store_true'
    )
    
    args = parser.parse_args()
    
    actions_to_perform = (args.reload_filters or args.disable_filters or None) != None
    
    try:
        if not check_virtualenv(VENV_DIR):
            if not actions_to_perform:
                create_virtualenv()
                add_project_root_to_venv()
            else:
                print("Unable to perform required action, install first the environment.")
                sys.exit(1)
        if not args.disable_filters:
            install_filters()
        else:
            disable_filters()

        if not actions_to_perform:
            install_requirements()
            print_activation_instructions(VENV_DIR)
        elif args.reload_filters:
            print("Filters reload completed.")
        elif args.disable_filters:
            print("Filters deactivation completed.")
    except Exception as e:
        print(f"Error during setup: {e}", file=sys.stderr)
        sys.exit(1)

    if sys.stdin.isatty() and not actions_to_perform:
        input("Press ENTER to quit.")

if __name__ == "__main__":
    main()