import os
import sys
import subprocess
import venv
import platform
from utils.constants import PROJECT_ROOT_KEY

VENV_DIR = ".notesVenv"
REQUIREMENTS_FILE = "requirements.txt"


SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
VENV_DIR = os.path.join(SCRIPT_DIR, VENV_DIR)
REQUIREMENTS_FILE = os.path.join(SCRIPT_DIR, REQUIREMENTS_FILE)

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
        return os.path.join(VENV_DIR, "Scripts", "pip.exe")
    else:
        return os.path.join(VENV_DIR, "bin", "pip")

def get_activate_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'activate.bat')
    else:
        return os.path.join(VENV_DIR, 'bin', 'activate')
    
    
def get_python_path():
    if os.name == 'nt':
        return os.path.join(VENV_DIR, 'Scripts', 'python.exe')
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
    def install_wikilink_filter():
    

        filter_name = "wikilink"
        
        wikilink_clean_name = "wikilink_clean"
        wikilink_smudge_name = "wikilink_smudge"

        script_clean_path = os.path.abspath(os.path.join("utils", f"{wikilink_clean_name}.py"))
        script_smudge_path = os.path.abspath(os.path.join("utils", f"{wikilink_smudge_name}.py"))

        if not os.path.isfile(script_clean_path) or not os.path.isfile(script_smudge_path):
            print("ERROR: One or both filter scripts not found.")
            sys.exit(1)
        python_path = get_python_path()
        clean_command = f"{python_path} -m utils.{wikilink_clean_name}"
        smudge_command = f"{python_path} -m utils.{wikilink_smudge_name}"
        
        if os.name == "nt":
            clean_command = clean_command.replace("\\", "\\\\")
            smudge_command = smudge_command.replace("\\", "\\\\")


        subprocess.check_call([
            "git", "config", f"filter.{filter_name}.clean", clean_command
        ])
        subprocess.check_call([
            "git", "config", f"filter.{filter_name}.smudge", clean_command
        ])

        print(f"Git filter '{filter_name}' installed.")
    
    
    
    print("Installing git filters...")
    install_wikilink_filter()

   
    
def main():
    if os.path.isdir(VENV_DIR):
        print(f"Virtual environment already exists in {VENV_DIR}")
    else:
        create_virtualenv()
    add_project_root_to_venv()
    install_filters()
    install_requirements()
    print("Setup completed.")
    print(f"To activate the environment manually:\n")

    if os.name == 'nt':
        print(f" {VENV_DIR}\\Scripts\\activate.bat")
    else:
        print(f" source {VENV_DIR}/bin/activate")
    
    print()
    input("Press ENTER to quit.")

if __name__ == "__main__":
    main()