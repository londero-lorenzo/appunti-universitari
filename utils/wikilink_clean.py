import sys
import re
import json
from utils.constants import REGEX_PATTERN_WIKILINK, WIKI_MAP_JSON, WIKI_MAP_PARAMETER_KEYS

regex = re.compile(REGEX_PATTERN_WIKILINK, re.MULTILINE)

def main():
    input_text = sys.stdin.read()
    
    try:
        with open(WIKI_MAP_JSON, 'r') as f:
            wiki_map = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load wiki map: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert to dict for fast lookup
    wiki_dict = {item[WIKI_MAP_PARAMETER_KEYS.wikilink_key]: item[WIKI_MAP_PARAMETER_KEYS.svglink_key] for item in wiki_map if WIKI_MAP_PARAMETER_KEYS.wikilink_key in item and WIKI_MAP_PARAMETER_KEYS.svglink_key in item}

    matches = regex.findall(input_text)

    for match in matches:
        if len(match) != 2:
            continue
        internal_link_with_frame, metadata = match
        wikilink = f"![[{internal_link_with_frame}]]"
        if metadata:
            wikilink_with_metadata = f"![[{internal_link_with_frame}|{metadata}]]"
        else:
            wikilink_with_metadata = wikilink
            
        svg = wiki_dict.get(wikilink)

        if not svg:
            print(f"[WARN] No SVG found for {wikilink_with_metadata}", file=sys.stderr)
            continue

        input_text = input_text.replace(wikilink_with_metadata, svg)

    sys.stdout.write(input_text)

if __name__ == '__main__':
    main()
