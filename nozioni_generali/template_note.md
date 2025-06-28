---
title: "Template Note"
aliases: ["Template Note"]
tags: [università, "nozioni-generali", "template-note"]
created: 2025-06-28
---
# Template — Sezione "Fonti" nei file di appunti

Questo template descrive la struttura consigliata da utilizzare nella sezione `## Fonti` al termine di ciascun file `.md` degli appunti.

## Struttura consigliata

```markdown
## Fonti

- Contenuto: _<Titolo sezione principale>_: _<Sottosezioni o argomenti trattati>_
- Slide: <Titolo ufficiale del file o del pacchetto di slide>
- File: [`Nome descrittivo del file`](<URL_completo>)
- Autore: <Docente di riferimento>
- Corso: <Nome del corso>, <Dipartimento> — UniUD, A.A. <Anno accademico>
```

## Esempio pratico

```markdown
## Fonti

- Contenuto: _Organizzazione di un Sistema di Calcolo_: _Gestione delle Interruzioni_ e _La Memoria_
- Slide: Introduzione ai Sistemi Operativi
- File: [`Introduzione Ai Sistemi Operativi`](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand01.pdf)
- Autore: A. Formisano
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
```

## Linee guida

- Usare nomi file coerenti e descrittivi (es. `Introduzione Ai Sistemi Operativi`)
    
- I link ai file PDF devono essere **relativi**, così da funzionare sia su GitHub che in locale (es. Obsidian)
    
- Evitare abbreviazioni troppo ambigue nei nomi
    
- La sezione va posta **alla fine del documento**
