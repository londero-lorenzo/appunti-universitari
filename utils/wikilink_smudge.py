import sys
import re
import json
from utils.constants import REGEX_PATTERN_SVGLINK, WIKI_MAP_JSON

regex = re.compile(REGEX_PATTERN_SVGLINK, re.MULTILINE)

def main():
    input_text = sys.stdin.read()
    
    try:
        with open(WIKI_MAP_JSON, 'r') as f:
            wiki_map = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load wiki map: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert to dict for fast lookup
    wiki_dict = {item[WIKI_MAP_PARAMETER_KEYS.svglink_key]: item[WIKI_MAP_PARAMETER_KEYS.wikilink_key] for item in wiki_map if WIKI_MAP_PARAMETER_KEYS.svglink_key in item and WIKI_MAP_PARAMETER_KEYS.wikilink_key in item}

    matches = regex.findall(input_text)

    for match in matches:
        if len(match) != 3:
            continue
        alt_name, metadata, internal_link  = match
        svglink = f"![{alt_name}]({internal_link})"
        if metadata:
            svglink_with_metadata = f"![{alt_name}|{metadata}]({internal_link})"
        else:
            svglink_with_metadata = svglink
            
        wikilink = wiki_dict.get(svglink)

        if not wikilink:
            print(f"[WARN] No WIKI-LINK found for alt='{alt_name}', path='{internal_link}'", file=sys.stderr)
            continue

        input_text = input_text.replace(svglink_with_metadata, wikilink)

    sys.stdout.write(input_text)

if __name__ == '__main__':
    main()
