import sys
import re
import json
from utils.constants import REGEX_PATTERN_SVGLINK, REGEX_PATTERN_LATEX, WIKI_MAP_JSON, WIKI_MAP_PARAMETER_KEYS

SVGLINK_REGEX = re.compile(REGEX_PATTERN_SVGLINK, re.MULTILINE)
LATEX_REGEX = re.compile(REGEX_PATTERN_LATEX, re.MULTILINE | re.DOTALL)

def smudge_svglink(input_text, svglink_matches):
    try:
        with open(WIKI_MAP_JSON, 'r') as f:
            wiki_map = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load wiki map: {e}", file=sys.stderr)
        sys.exit(1)

    wiki_dict = {
        item[WIKI_MAP_PARAMETER_KEYS.svglink_key]: item[WIKI_MAP_PARAMETER_KEYS.wikilink_key]
        for item in wiki_map
        if WIKI_MAP_PARAMETER_KEYS.svglink_key in item and WIKI_MAP_PARAMETER_KEYS.wikilink_key in item
    }

    for match in svglink_matches:
        if len(match) != 3:
            continue
        alt_name, metadata, internal_link = match

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

    return input_text


def smudge_latex(input_text, latex_matches):
    for match in latex_matches:
        multiline_latex, inline_latex = match
        
        latex = multiline_latex or inline_latex
        smudged_latex = re.sub(r'\\([_*])', '\1', latex)
        
        input_text = input_text.replace(latex, smudged_latex, 1)

    return input_text


def main():
    input_text = sys.stdin.read()

    svglink_matches = SVGLINK_REGEX.findall(input_text)

    if svglink_matches:
        input_text = smudge_svglink(input_text, svglink_matches)

    latex_matches = LATEX_REGEX.findall(input_text)

    if latex_matches:
        input_text = smudge_latex(input_text, latex_matches)


    sys.stdout.write(input_text)


if __name__ == '__main__':
    main()
