import os
import argparse
import platform
import subprocess
import sys
from setup import VENV_DIR
from setup import get_activate_path

def open_venv_shell(alternative_command= ""):
    activate_path = get_activate_path()
    
    if os.name == 'nt':
        cmd = f'cmd.exe /k "{activate_path} && '
        if alternative_command:
            cmd += alternative_command
        else:
            cmd += 'echo Environment activated. Type `exit` to exit.'
        cmd += '"'
        subprocess.run(cmd)
    else:
        shell = os.environ.get('SHELL', '/bin/bash')
        cmd = f'{shell} -c "source {activate_path}; '
        if alternative_command:
            cmd += alternative_command + '; '
        else:
            cmd += 'echo Environment activated. Type `exit` to exit.; '
        cmd += f'exec {shell}"'
        subprocess.run(cmd)

def start_debug_environment(env_args):
    if os.name == 'nt':  # Windows
        command = (
            "echo \033[32m====================================\033[0m && "
            "echo \033[32m[DEBUG ENVIRONMENT STARTED]\033[0m && "
            "echo Environment activated. Type `exit` to exit. && "
            "echo \033[32m====================================\033[0m && "
            "echo. && "
        )
        
        command += "echo Debug parameters: && "
        for key, value in env_args:
            command += f'set "{key}={value}" && echo  - \033[32m{key}\033[0m = {value} && '
        
        # NOTE: Windows 10+ supports ANSI, otherwise you will need Colorama or a workaround.
        command += 'echo ==================================== && '
        command += f"set PROMPT=({VENV_DIR.split(os.sep)[-1]}) $E[32m[DEBUG]$E[0m $P$G"

    else:  # Unix-like
        command = (
            'echo "\033[32m====================================\033[0m" && '
            'echo "\033[32m[DEBUG ENVIRONMENT STARTED]\033[0m" && '
            'echo "Environment activated. Type `exit` to exit." && '
            'echo "\033[32m====================================\033[0m" && '
            'echo "" && '
        )
        
        command += 'echo "Debug parameters:" && '
        for key, value in env_args:
            command += f'export {key}="{value}" && echo "  - \033[32m{key}\033[0m = {value}" && '
        
        # Change the PS1 prompt to green and tag [DEBUG]
        command += f"export PS1=\"({VENV_DIR.split(os.sep)[-1]}) \\[\\033[32m\\][DEBUG]\\[\\033[0m\\] \\u@\\h:\\w\\$ \""

    open_venv_shell(command)


        
def handle_debug(actions):
    env_args = [("DEBUG_MODE", '1')]
    for action, value in actions:
        if action == "enable_trace":
            env_args.append(("GIT_TRACE", str(value or 1)))
        elif action == "enable_flush":
            env_args.append(("GIT_FLUSH", str(value or 1)))
        elif action == "show":
            print("DEBUG_MODE = ", os.environ.get("DEBUG_MODE"))
            print("GIT_TRACE =", os.environ.get("GIT_TRACE"))
            print("GIT_FLUSH =", os.environ.get("GIT_FLUSH"))
            return
        else:
            print(f"[WARN] Unknown debug command: {action}")
            return
    start_debug_environment(env_args)
   
        
        
def main():
    parser = argparse.ArgumentParser(
        prog='Environment starter',
        description='Start virtual environment in cli or git debug mode.',
        add_help=True)
    subparsers = parser.add_subparsers(dest='command')
    
    debug_parser = subparsers.add_parser('debug')
    debug_parser.add_argument(
        'debug_actions', nargs='+',
        help="Debug di actions: enable_trace [lvl] enable_flush [lvl] show"
    )
    
    args = parser.parse_args()
    
    if args.command == "debug":
        tokens = args.debug_actions
        actions = []
        i = 0
        while i < len(tokens):
            action = tokens[i]
            value = None
            if i+1 < len(tokens) and tokens[i+1].isdigit():
                value = int(tokens[i+1])
                i += 1
            actions.append((action, value))
            i += 1
        handle_debug(actions)
    else:
        open_venv_shell()

if __name__ == '__main__':
    main()