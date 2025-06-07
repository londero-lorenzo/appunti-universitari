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
   
   
    
def main():
    if os.path.isdir(VENV_DIR):
        print(f"Virtual environment already exists in {VENV_DIR}")
    else:
        create_virtualenv()
    add_project_root_to_venv()
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