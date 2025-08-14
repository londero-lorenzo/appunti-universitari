import os
from types import SimpleNamespace


DEBUG = SimpleNamespace(
    MODE_KEY = "DEBUG_MODE",
    PYTHON = {
        "PYTHONPATH": ".;.github"
    },
    GITHUB_ACTIONS = {
        "GITHUB_ACTIONS": "1",
        "GITHUB_REPOSITORY": "londero-lorenzo/appunti-universitari",
        "GITHUB_TOKEN": "fake"
    },
    GIT = SimpleNamespace(
        GIT_TRACE= "GIT_TRACE",
        GIT_FLUSH = "GIT_FLUSH"
    )
)

DEBUG_ENABLED = not not int(os.getenv(DEBUG.MODE_KEY, 0))
GITHUB_ACTIONS_ENABLED = not not int(os.getenv("GITHUB_ACTIONS", 0))


def DEBUG_LOG(data, *args, **kwargs):
    if DEBUG_ENABLED:
        print("\033[32m[DEBUG]\033[0m " + str(data), *args, **kwargs)
        

EXCALIDRAW_FILE_EXTENSION = ".excalidraw.md"


if GITHUB_ACTIONS_ENABLED:
    # Costanti per il funzionamento del caricamento dei TODO sulle issue:
 
    TODO_ISSUE_PATTERN = { ".md": r"<!--\s*TODO\((?P<issue_name>.*?)\):\s*(?P<text>.*?)-->"}
    
    TODO_ISSUE_EXCLUDED_EXTENSION = [EXCALIDRAW_FILE_EXTENSION]

else:

    # Costanti per il funzionamento degli script locali
    import re
    from utils import env


    env.load_project_env()


    PROJECT_ROOT_KEY = "PROJECT_ROOT"

    VAULT_ROOT = os.getenv(PROJECT_ROOT_KEY)


    EXCALIDRAW_FILE_EXTENSION = ".excalidraw.md"

    # percorsi per i workflow scripts 

    WORKFLOW_SCRIPTS_HOME = ".github"
    WORKFLOW_SCRIPTS_PACKAGE = "workflow_scripts"


    WORKFLOW_SCRIPTS_HOME = os.path.join(VAULT_ROOT, WORKFLOW_SCRIPTS_HOME)
    WORKFLOW_SCRIPTS_LOCATION = os.path.join(WORKFLOW_SCRIPTS_HOME, WORKFLOW_SCRIPTS_PACKAGE)


    WORKFLOW_SCRIPTS_LOGS_HOME = os.path.join(WORKFLOW_SCRIPTS_LOCATION, "logs")

    if not os.path.exists(WORKFLOW_SCRIPTS_LOGS_HOME):
        os.makedirs(WORKFLOW_SCRIPTS_LOGS_HOME)


    # nomi per filtri markdown usati da git config

    WORKFLOW_SCRIPTS_FILTER_DUMP_LOG = "FILTER_DUMP.txt"
    WORKFLOW_SCRIPTS_FILTER_DUMP_LOG = os.path.join(WORKFLOW_SCRIPTS_LOGS_HOME, WORKFLOW_SCRIPTS_FILTER_DUMP_LOG)

    MARKDOWN_FILTER_NAME = "markdown"
    MARKDOWN_CLEAN_FILTER_NAME = "markdown_clean"
    MARKDOWN_CLEAN_FILTER_ERROR_LOG = "markdown_clean_error.log"

    MARKDOWN_CLEAN_FILTER_ERROR_LOG = os.path.join(WORKFLOW_SCRIPTS_LOGS_HOME, MARKDOWN_CLEAN_FILTER_ERROR_LOG)

    MARKDOWN_SMUDGE_FILTER_NAME = "markdown_smudge"
    MARKDOWN_SMUDGE_FILTER_ERROR_LOG = "markdown_smudge_error.log"

    MARKDOWN_SMUDGE_FILTER_ERROR_LOG = os.path.join(WORKFLOW_SCRIPTS_LOGS_HOME, MARKDOWN_SMUDGE_FILTER_ERROR_LOG)


    REGEX_PATTERN_WIKILINK = r'!\[\[([^\|\]]+?\.excalidraw\.md#\^frame=[^\|\]]+)(?:\|(.*))?\]\]'
    REGEX_PATTERN_SVGLINK = r'!\[([^|\]]*)(?:\|(.*))?\]\((.*)\)'

    REGEX_PATTERN_LATEX = r'(\$\$.*?\$\$)|(\$(?!\$).*?\$)'

    WIKILINK_REGEX = re.compile(REGEX_PATTERN_WIKILINK, re.MULTILINE)
    SVGLINK_REGEX = re.compile(REGEX_PATTERN_SVGLINK, re.MULTILINE)
    LATEX_REGEX = re.compile(REGEX_PATTERN_LATEX, re.MULTILINE | re.DOTALL)


    WIKI_MAP_JSON = os.path.join(VAULT_ROOT, "Excalidraw", "wiki-map.json")

    WIKI_MAP_PARAMETER_KEYS = SimpleNamespace(
        wikilink_key="wikilink",
        svglink_key="svglink",
        source_key="source",
        frameId_key="frameId"
    )


