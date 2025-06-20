---
title: Tecniche
aliases:
  - Tecniche
tags:
  - programmazione-lato-server-e-cgi
  - tecniche
created: 2025-06-20
---
# 🧰 Tecniche di programmazione lato server

La programmazione lato server può essere implementata attraverso diverse tecniche, che si differenziano in base a:

- la **modalità di interazione** tra server web e programma eseguito,
- il **luogo dove risiede il codice**,
- il **meccanismo con cui viene mandato in esecuzione**.

---

## ⚙️ Obiettivo comune

Tutte le tecniche mirano a generare, su richiesta del client, **flussi di dati** in formati tipici del Web come:

- (X)HTML
- CSS
- JPEG, GIF
- *(ma in generale qualsiasi file che un browser possa interpretare)*

---

## 🔄 Interazione server ↔ programma

Il **server web** è responsabile dell’attivazione del programma server-side. Il meccanismo di attivazione dipende dalla tecnologia adottata:

| Tecnologia        | Descrizione |
|------------------|-------------|
| **CGI (Common Gateway Interface)** | Il server esegue un nuovo processo per ogni richiesta. Codice esterno. |
| **mod_php / mod_python / mod_perl** | Il codice è integrato nel processo del server (es. Apache), evita fork. |
| **FastCGI** | Processo persistente riutilizzato per più richieste. Più efficiente della CGI. |
| **Framework/Server applicativi** | L'interprete o la VM (es. Node.js, Java servlet container) gestisce direttamente le richieste. |

*(La sezione CGI è trattata nel dettaglio nel file [Common Gateway Interface](./cgi))*

---

## 📍 Dove risiede il codice

- In file **esterni** al server web (es. CGI script in `/usr/lib/cgi-bin/`)
- **Integrato nel server** tramite moduli (es. `mod_php`, `mod_wsgi`)
- In **processi intermedi**, come middleware o server dedicati (es. Flask, Express.js)

---

## 🚀 Modalità di esecuzione

| Modalità | Caratteristiche |
|---------|------------------|
| **Processo nuovo per richiesta** | → Semplice, ma inefficiente (CGI classico) |
| **Processo persistente** | → Ottime prestazioni (FastCGI, mod_php, framework moderni) |
| **Server applicativo dedicato** | → Gestione completa lato applicazione (es. Node.js, Python con Flask, PHP-FPM) |

---

## 📌 Considerazioni pratiche

- Le tecniche più semplici (es. CGI) sono facili da configurare ma **scalano male**.
- Le tecniche moderne (es. FastCGI, PHP-FPM, Node.js) offrono **migliori performance e controllo**.
- La scelta della tecnica dipende da:
  - esigenze di performance,
  - linguaggio utilizzato,
  - architettura dell'applicazione,
  - supporto offerto dal server web in uso.

---

> 📎 Approfondimento consigliato: [Common Gateway Interface](./cgi.md) per dettagli sulla tecnica CGI.
