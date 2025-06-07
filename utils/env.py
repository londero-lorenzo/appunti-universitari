from dotenv import load_dotenv
import os
import sys

def load_project_env(filename: str = ".env") -> None:
    current_path = os.getcwd()
    
    while True:
        env_file = os.path.join(current_path, filename)
        if os.path.isfile(env_file):
            load_dotenv(current_path)
            return env_file
        
        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:
            raise FileNotFoundError(f"{filename} non trovato a partire da {path}")
        
        current_path = parent_path

