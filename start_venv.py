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
        for key, value in env_args.items():
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
        for key, value in env_args.items():
            command += f'export {key}="{value}" && echo "  - \033[32m{key}\033[0m = {value}" && '
        
        # Change the PS1 prompt to green and tag [DEBUG]
        command += f"export PS1=\"({VENV_DIR.split(os.sep)[-1]}) \\[\\033[32m\\][DEBUG]\\[\\033[0m\\] \\u@\\h:\\w\\$ \""

    open_venv_shell(command)


        
def _print_debug_env():
    from utils.constants import DEBUG
    print(f"{DEBUG.MODE_KEY} = ", os.environ.get(DEBUG.MODE_KEY))
    for key in DEBUG.PYTHON:
        print(f"{key} = ", os.environ.get(key))
    for key in DEBUG.GITHUB_ACTIONS:
        print(f"{key} = ", os.environ.get(key))
    print(f"{DEBUG.GIT.GIT_TRACE} = ", os.environ.get(DEBUG.GIT.GIT_TRACE))
    print(f"{DEBUG.GIT.GIT_FLUSH} = ", os.environ.get(DEBUG.GIT.GIT_FLUSH))


def handle_debug(actions):
    from utils.constants import DEBUG
    env_args = {DEBUG.MODE_KEY: '1'}

    if any(action != "show" for action, _ in actions):
        env_args.update(DEBUG.PYTHON)

    action_map = {
        "enable_trace": lambda val: env_args.update({DEBUG.GIT.GIT_TRACE: str(val or 1)}),
        "enable_flush": lambda val: env_args.update({DEBUG.GIT.GIT_FLUSH: str(val or 1)}),
        "enable_github_actions_mode": lambda val: env_args.update(DEBUG.GITHUB_ACTIONS),
    }

    for action, value in actions:
        if action == "show":
            _print_debug_env()
            return
        elif action in action_map:
            action_map[action](value)
        else:
            print(f"[WARN] Unknown debug command: {action}")
            return

    if any(action != "show" for action, _ in actions):
        start_debug_environment(env_args)

    if do_show:
        _print_debug_env()

        
        
def main():
    parser = argparse.ArgumentParser(
        prog='Environment starter',
        description='Start virtual environment in cli or git debug mode.',
        add_help=True)
    subparsers = parser.add_subparsers(dest='command')
    
    debug_parser = subparsers.add_parser('debug')
    debug_parser.add_argument(
        'debug_actions', nargs='+',
        help="Debug di actions: enable_trace [lvl] enable_flush [lvl] enable_github_actions_mode show"
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