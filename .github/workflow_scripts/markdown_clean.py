import sys
import traceback
import re
import os
import json
from datetime import datetime
from utils.constants import WIKILINK_REGEX, SVGLINK_REGEX, LATEX_REGEX, WIKI_MAP_JSON, WIKI_MAP_PARAMETER_KEYS, MARKDOWN_CLEAN_FILTER_ERROR_LOG

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
        svglink = wiki_dict.get(wikilink.strip('/').strip('\\').replace('\\', '/'))
        
        if not svglink:
            print(f"[WARN] No SVG found for {wikilink}", file=sys.stderr)
            continue
        
        if metadata:
            wikilink_with_metadata = f"![[{internal_link_with_frame}|{metadata}]]"
            svglink_alt_name, _, svglink_internal_link = SVGLINK_REGEX.findall(svglink)[0]
            svglink = f"![{svglink_alt_name}|{metadata}]({svglink_internal_link})"
        else:
            wikilink_with_metadata = wikilink

        input_text = input_text.replace(wikilink_with_metadata, svglink)
    
    return input_text
    
def extract_latex_outside_codeblocks(text, regex):
    codeblocks = text.split("```")
    # indici pari = fuori dai blocchi, dispari = dentro
    results = []
    for i in range(0, len(codeblocks), 2):  # solo parti fuori dai codeblock
        segment = codeblocks[i]
        results.extend(regex.findall(segment))
    return results

    
def clean_latex(input_text, latex_matches):
    for match in latex_matches:
        multiline_latex, inline_latex = match
        
        latex = multiline_latex or inline_latex
        
        cleaned_latex = re.sub(r'(?<!\\)([_*])', r'\1', latex)
        input_text = input_text.replace(latex, cleaned_latex, 1) 
        
    return input_text




def main():
    filename = sys.argv[1].strip('\\').strip("'") if len(sys.argv) > 1 else "<unknown file>"
    input_text = sys.stdin.read()
    
    try:       
        wikilink_matches = WIKILINK_REGEX.findall(input_text)
        
        if wikilink_matches:
            input_text = clean_wikilink(input_text, wikilink_matches)
            
        latex_matches = extract_latex_outside_codeblocks(input_text, LATEX_REGEX)

        if latex_matches:
            input_text = clean_latex(input_text, latex_matches)


        sys.stdout.write(input_text)
    except Exception as e:
        log_file = MARKDOWN_CLEAN_FILTER_ERROR_LOG
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_msg = f"{now} [ERROR] Failed to apply markdown clean filter on `{filename}`: {e}\n"
        end_msg = "\n" + "-"*len(error_msg) + "\n"
        with open(log_file, 'a') as f:
            f.write(error_msg)
            print(error_msg, file= sys.stderr)
            traceback.print_exc(file=f)
            traceback.print_exc(file=sys.stderr)
            f.write(end_msg)
            print(end_msg)
        sys.exit(1)

if __name__ == '__main__':
    main()
