import sys
import re
import json
from utils.constants import WIKILINK_REGEX, SVGLINK_REGEX, LATEX_REGEX, WIKI_MAP_JSON, WIKI_MAP_PARAMETER_KEYS

def clean_wikilink(input_text, wikilink_matches):
    try:
        with open(WIKI_MAP_JSON, 'r') as f:
            wiki_map = json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load wiki map: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert to dict for fast lookup
    wiki_dict = {
        item[WIKI_MAP_PARAMETER_KEYS.wikilink_key]: item[WIKI_MAP_PARAMETER_KEYS.svglink_key]
        for item in wiki_map 
        if WIKI_MAP_PARAMETER_KEYS.wikilink_key in item and WIKI_MAP_PARAMETER_KEYS.svglink_key in item
    }

    for match in wikilink_matches:
        if len(match) != 2:
            continue
        internal_link_with_frame, metadata = match
        
        wikilink = f"![[{internal_link_with_frame}]]"
        svglink = wiki_dict.get(wikilink)
        
        if metadata:
            wikilink_with_metadata = f"![[{internal_link_with_frame}|{metadata}]]"
            svglink_alt_name, _, svglink_internal_link = SVGLINK_REGEX.findall(svglink)[0]
            svglink = f"![{svglink_alt_name}|{metadata}]({svglink_internal_link})"
        else:
            wikilink_with_metadata = wikilink
            


        if not svglink:
            print(f"[WARN] No SVG found for {wikilink_with_metadata}", file=sys.stderr)
            continue

        input_text = input_text.replace(wikilink_with_metadata, svglink)
    
    return input_text
    
    
def clean_latex(input_text, latex_matches):
    for match in latex_matches:
        multiline_latex, inline_latex = match
        
        latex = multiline_latex or inline_latex
        
        cleaned_latex = re.sub(r'(?<!\\)([_*])', r'\_', latex)
        input_text = input_text.replace(latex, cleaned_latex, 1) 
        
    return input_text



def main():
    input_text = sys.stdin.read()
    
    wikilink_matches = WIKILINK_REGEX.findall(input_text)
    
    if wikilink_matches:
        input_text = clean_wikilink(input_text, wikilink_matches)
        
    latex_matches = LATEX_REGEX.findall(input_text)
    
    if latex_matches:
        input_text = clean_latex(input_text, latex_matches)


    sys.stdout.write(input_text)

if __name__ == '__main__':
    main()
