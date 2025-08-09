from types import SimpleNamespace

import re

PROJECT_ROOT_KEY = "PROJECT_ROOT"

REGEX_PATTERN_WIKILINK = r'!\[\[([^\|\]]+?\.excalidraw\.md#\^frame=[^\|\]]+)(?:\|(.*))?\]\]'
REGEX_PATTERN_SVGLINK = r'!\[([^|\]]*)(?:\|(.*))?\]\((.*)\)'

REGEX_PATTERN_LATEX = r'(\$\$.*?\$\$)|(\$(?!\$).*?\$)'

WIKILINK_REGEX = re.compile(REGEX_PATTERN_WIKILINK, re.MULTILINE)
SVGLINK_REGEX = re.compile(REGEX_PATTERN_SVGLINK, re.MULTILINE)
LATEX_REGEX = re.compile(REGEX_PATTERN_LATEX, re.MULTILINE | re.DOTALL)


WIKI_MAP_JSON = ".\Excalidraw\wiki-map.json"

WIKI_MAP_PARAMETER_KEYS = SimpleNamespace(
    wikilink_key="wikilink",
    svglink_key="svglink",
    source_key="source",
    frameId_key="frameId"
)

