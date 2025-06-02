# Convenzione per i Messaggi di Commit

Ogni messaggio di commit dovrebbe seguire la seguente struttura:
```
<tipo>(<scopo>): descrizione in italiano
```


## Tipi supportati

| Tipo       | Scopo                                                                 |
|------------|-----------------------------------------------------------------------|
| `build`    | Modifiche che riguardano il sistema di build o configurazioni esterne |
| `chore`    | Attività di manutenzione, non modifica né codice né contenuti principali |
| `docs`     | Modifiche solo alla documentazione                                    |
| `feat`     | Aggiunta di nuove funzionalità o contenuti                            |
| `fix`      | Correzione di bug o problemi                                          |
| `refactor` | Refactoring del codice o struttura senza modificare comportamento     |
| `style`    | Cambiamenti legati alla formattazione (spazi, indentazione, virgole) |
| `test`     | Aggiunta o modifica di test                                           |

## Esempi

```text
chore(obsidian): caricata struttura della vault
docs(commit-style): aggiunta guida con struttura e parole chiave per i messaggi di commit
feat(algoritmi): aggiunti appunti su RBTree e BTree
fix(link): corretti link interni nel README principale
refactor(cartelle): riorganizzata la struttura dei file


# Regole generali
- Usare i verbi all'infinito nella descrizione (aggiungere, correggere, rimuovere, ecc.).

- Mantienere la descrizione sintetica e chiara, in italiano.

- Specificare sempre lo scopo tra parentesi, se utile (es. docs(readme), feat(algoritmi)).

- Per commit più grandi, aggiungere una descrizione più lunga nel corpo del commit (non nel titolo).