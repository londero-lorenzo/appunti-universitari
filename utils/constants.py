from types import SimpleNamespace


PROJECT_ROOT_KEY = "PROJECT_ROOT"

REGEX_PATTERN_WIKILINK = r'!\[\[([^\|\]]+?\.excalidraw\.md#\^frame=[^\|\]]+)(?:\|(.*))?\]\]'
REGEX_PATTERN_SVGLINK = r'!\[([^|\]]*)(?:\|(.*))?\]\((.*)\)'

REGEX_PATTERN_LATEX = r'(\$\$.*?\$\$)|(\$(?!\$).*?\$)'

WIKI_MAP_JSON = ".\Excalidraw\wiki-map.json"

WIKI_MAP_PARAMETER_KEYS = SimpleNamespace(
    wikilink_key="wikilink",
    svglink_key="svglink",
    source_key="source",
    frameId_key="frameId"
)

