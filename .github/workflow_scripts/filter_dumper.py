import sys
import traceback
import os
from datetime import datetime
import pprint
from utils.constants import WORKFLOW_SCRIPTS_FILTER_DUMP_LOG

def main():
    filename = sys.argv[1].strip('\\').strip("'") if len(sys.argv) > 1 else "<unknown file>"
    input_text = sys.stdin.read()
   
    log_file = WORKFLOW_SCRIPTS_FILTER_DUMP_LOG
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, 'a', encoding='utf-8') as f:
        def log_section(title, content):
            sep = "=" * 60
            f.write(f"\n{sep}\n[{title}]\n{sep}\n{content}\n")

        # Sezione 1: Info generali
        log_section("INFO GENERALI",
            f"Timestamp: {now}\n"
            f"Filename: {filename}\n"
            f"Directory corrente: {os.getcwd()}\n"
        )

        # Sezione 2: Variabili ambientali importanti
        log_section("VARIABILI AMBIENTALI IMPORTANTI",
            f"PYTHONPATH: {os.environ.get('PYTHONPATH')}\n"
            f"GIT_DIR: {os.environ.get('GIT_DIR')}\n"
            f"GIT_WORK_TREE: {os.environ.get('GIT_WORK_TREE')}\n"
            f"GIT_PREFIX: {os.environ.get('GIT_PREFIX')}\n"
            f"PATH: {os.environ.get('PATH')}\n"
            f"SHELL: {os.environ.get('SHELL')}\n"
            f"MSYSTEM: {os.environ.get('MSYSTEM')}\n"
        )

        # Sezione 3: Info Python
        log_section("INFO PYTHON",
            f"Eseguibile: {sys.executable}\n"
            f"Versione: {sys.version}\n"
            f"sys.path:\n{pprint.pformat(sys.path)}\n"
        )

        # Sezione 4: Anteprima input
        log_section("ANTEPRIMA INPUT",
            f"Lunghezza totale: {len(input_text)}\n"
            f"Primi 200 caratteri:\n{repr(input_text[:200])}\n"
        )

        # Sezione 5: Dump completo variabili ambiente
        log_section("DUMP COMPLETO AMBIENTE",
            pprint.pformat(dict(os.environ))
        )

    # Scrive anche su stderr così lo vedi in tempo reale
    print(f"{now} [DUMP] Dump creato su {log_file}", file=sys.stderr)

    sys.exit(1)

if __name__ == '__main__':
    main()
