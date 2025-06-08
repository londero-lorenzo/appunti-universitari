import os
import re
import sys
import glob
import argparse
from datetime import datetime
import yaml
from utils import env
from utils import constants

env.load_project_env()


VAULT_ROOT = os.getenv(constants.PROJECT_ROOT_KEY)


LOWERCASE_WORDS = {
    "di", "del", "della", "dei", "degli", "delle",
    "a", "con", "in", "su", "per", "tra", "fra", "e", "o"
}

DEFAULT_TAGS = [] #["università"]

def split_and_capitalize(string: str, delimiter: str) -> str:
    parts = string.split(delimiter)
    return delimiter.join(p.capitalize() for p in parts)

def format_title(filename: str) -> str:
    base = filename.replace('_', ' ')
    words = base.split()
    formatted = []
    for i, word in enumerate(words):
        lw = word.lower()
        if i > 0 and lw in LOWERCASE_WORDS:
            formatted.append(lw)
        else:
            formatted.append(split_and_capitalize(word, '-'))
    return ' '.join(formatted)

def format_tags_from_path(rel_path: str) -> list:
    parts = rel_path.replace("\\", "/").split('/')
    tags = []
    for part in parts:
        name = os.path.splitext(part)[0]
        if name and name != '..':
            tag = name.replace('_', '-')
            tags.append(tag)
    return tags

def process_markdown_file(filepath: str, output: str):
    if not output or output in {'.', '/', '\\'}:
        output = filepath
    if os.path.isdir(output):
        output = os.path.join(output, os.path.basename(filepath))
    
    print(f"Processing {filepath}...")
    rel_path = os.path.relpath(filepath, VAULT_ROOT)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    title = format_title(filename)
    tags = format_tags_from_path(rel_path)
    
    frontmatter = {
        "title": title,
        "aliases": [title],
        "tags": DEFAULT_TAGS + tags,
        "created": datetime.now().strftime("%Y-%m-%d")
    }
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_regex = r"^---\n(.*?\n)---\n"
    match = re.match(frontmatter_regex, content, flags=re.DOTALL)
    
    existing_created = None
    if match:
        old_fm_block = content[0:match.end()] ## get old initial block
        inner = old_fm_block.strip().split('\n')[1:-1] ## exclude "---"
        old_fm_dict = yaml.safe_load("\n".join(inner))
        if not sum([key in old_fm_dict for key in frontmatter]) == len(frontmatter):
            print(f"Properties loaded not match with pattern: default.md")
            return None
        existing_created = old_fm_dict.get("created", None)
    
    created_value = existing_created or datetime.now().strftime("%Y-%m-%d")
    frontmatter["created"] = created_value
    new_fm = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False, allow_unicode=True)
    new_fm_block = f"---\n{new_fm}---\n"
    
    if match:
        new_content = new_fm_block + content[match.end():]
    else:
        new_content = new_fm_block + content
    
    with open(output, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"File {'overwritten.' if filepath == output else f'saved to `{output}`'}")



def batch_process(pattern: str, output: str, suppress_warnings: bool):
    files = [f for f in glob.glob(pattern, recursive=True) if f.lower().endswith(".md")]
    if not files:
        location = f"at {pattern}" if '*' not in pattern else f"with pattern {pattern}"
        print(f"Error: no markdown files found {location}.")
        sys.exit(1)

    print(f"Found {len(files)} markdown file(s):")
    for f in files:
        print(f"  • {f}")

    for filepath in files:
        if not suppress_warnings:
            ans = input(f"\n→ Proceed with `{filepath}`? [Y/n] ")
            if ans.upper() != 'Y':
                print("  Skipped.")
                continue
        process_markdown_file(filepath, output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Template frontmatter updater")
    parser.add_argument("-f", "--file", help="Markdown file path or glob pattern to process.", type=str, required=True)
    parser.add_argument("-o", "--output", help="Target file or directory for the updated markdown output.", type=str, default=None)
    parser.add_argument("-s", "--suppress_warnings", help="Suppress overwrite confirmation prompts.", action='store_true')

    args = parser.parse_args()
    
    batch_process(args.file, args.output, args.suppress_warnings)