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

La programmazione lato server consiste nell’inserire codice eseguibile dal server all’interno o accanto ai documenti web, con l’obiettivo di generare contenuti dinamici da inviare al browser.

---

## ⚙️ Obiettivo comune

Tutte le tecniche mirano a generare, su richiesta del client, **flussi di dati** in formati tipici del Web:

- HTML, CSS
- Immagini (JPEG, GIF, PNG)
- File JSON, XML
- *(e in generale qualsiasi risorsa che un browser possa interpretare)*

---

## 🔄 Interazione server ↔ programma

Il server web (es. Apache, Nginx) è responsabile dell’attivazione dell’esecuzione server-side. Le principali modalità di attivazione sono:

| Tecnologia                          | Descrizione                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| **CGI (Common Gateway Interface)**  | Esegue un **nuovo processo per ogni richiesta**. Codice esterno.           |
| **mod_php / mod_python / mod_perl** | Codice integrato nel processo del server. Più efficiente.                  |
| **FastCGI**                         | Processo persistente. Riutilizzabile tra più richieste.                    |
| **Server applicativi / Framework**  | Esempi: Node.js, PHP-FPM, Flask. Gestione interna delle richieste HTTP.   |

📎 Vedi anche: [Common Gateway Interface](./cgi.md)

---

## 🧱 Dove risiede il codice

- In file **esterni** (es. CGI script in `/usr/lib/cgi-bin/`)
- **All’interno dei documenti HTML**, tramite pseudo-tag (es. `<?php ... ?>`)
- Integrato nel server tramite **moduli** (es. `mod_php`, `mod_wsgi`)
- In **server applicativi** separati che ricevono le richieste (es. Express, Django)

---

## 🚀 Modalità di esecuzione

| Modalità                        | Caratteristiche                                     |
|---------------------------------|-----------------------------------------------------|
| **Processo nuovo per richiesta** | → Semplice ma inefficiente (CGI classico)          |
| **Processo persistente**         | → Prestazioni superiori (FastCGI, mod_php)         |
| **Server dedicato**              | → Architetture moderne (Node.js, Flask, PHP-FPM)   |

---

## 🧠 Funzionamento degli script embedded

Quando il browser richiede una risorsa come `file.php`, il server:

1. Identifica il file come dinamico (es. da estensione `.php`)
2. Passa il file al modulo/interprete PHP
3. L’interprete **esegue** lo script:
   - individua ogni blocco `<?php ... ?>`
   - **interpreta il contenuto**
   - sostituisce lo pseudo-tag con l’output generato
4. Il documento finale (HTML puro) viene inviato al client.

📎 Vedi anche: [Funzionamento Apache](./apache/apache_funzionamento.md)

### Esempio
#### `file.php` (originale):

```php
<h1>Esempio con PHP</h1>
<p><?php echo "Questo è uno script"; ?></p>
```

#### Output inviato al browser:

```html
<h1>Esempio con PHP</h1>
<p>Questo è uno script</p>
```

---

## ♻️ Script multipli e variabili

Se il file contiene più blocchi `<?php ... ?>`, **ogni blocco è interpretato** in ordine, e lo stato viene mantenuto tra uno e l’altro:

```php
<?php $x = "ciao"; ?>
...
<?php echo $x; ?>
```

---

## 🔎 Confronto con CGI

- Se lo script è l’unico contenuto del file, il suo comportamento è simile a un CGI.
    
- Tuttavia, mentre CGI richiede un processo esterno, **moduli come `mod_php` eseguono direttamente nel contesto del server**, risultando più efficienti.
    

---

## 🌐 Linguaggi di scripting lato server

|Linguaggio|Descrizione|
|---|---|
|**PHP**|Diffusissimo. Ampio ecosistema (CMS, framework). Open source.|
|**ASP.NET**|Tecnologia Microsoft. Integrata con IIS e .NET.|
|**Python**|Usato via WSGI (es. Flask, Django)|
|**JavaScript (Node.js)**|Architettura full-JS lato client/server|

---

## 📌 Considerazioni pratiche

- Le tecniche classiche (es. CGI) sono semplici ma **poco scalabili**.
    
- Le tecniche moderne (es. PHP-FPM, Node.js, FastCGI) sono **ottimizzate per le performance**.
    
- La scelta dipende da:
    
    - carico atteso e frequenza richieste,
        
    - linguaggio preferito,
        
    - supporto server.
        

---

## 📚 Fonti e riferimenti

- Slide: `02-latoserver.pdf`
    
- Titoli: `Programmazione lato server`, `Tecniche di Programmazione Lato Server`




