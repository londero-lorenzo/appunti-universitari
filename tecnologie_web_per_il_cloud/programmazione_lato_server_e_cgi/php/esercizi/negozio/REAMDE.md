---
title: "Reamde"
aliases: ["Reamde"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "esercizi", "negozio", "REAMDE"]
created: 2025-06-21
---
# Negozio Online v1 – Caso di studio PHP

## Descrizione generale

Un negozio online semplificato per imparare o ripassare concetti fondamentali di PHP dinamico e gestione dati senza database.  
Si basa su:

- Visualizzazione prodotti
    
- Carrello e utenti **non implementati** (versione base)
    
- Memorizzazione prodotti nel filesystem, senza DBMS
    

---

## Cosa si impara

- Generazione dinamica di contenuto HTML e CSS
    
- Creazione di link dinamici
    
- Accesso e manipolazione del filesystem dal server PHP
    
- Passaggio di dati via query string nell’URI
    

---

## Struttura del progetto

- Cartella principale: `negozio/`
    
- File chiave:
    

|File|Descrizione|
|---|---|
|`index.php`|Pagina principale, vetrina prodotti|
|`prodotti.php`|Archivio completo dei prodotti|
|`inserisci.php`|Pagina per inserire nuovi prodotti|
|`config.php`|Configurazione (costanti, parametri globali)|
|`funzioni.php`|Funzioni PHP di supporto|
|`db/`|Sottocartella per dati prodotti (file)|

---

## Funzionalità attese

- Visualizzazione prodotti in ordine alfabetico (o altro criterio)
    
- Inserimento prodotti tramite form e salvataggio su file
    
- Navigazione tra pagine del negozio
    

---

## Note importanti

- Non si usa database nella prima versione, solo file system per semplicità.
    
- L’implementazione del carrello e della gestione utenti è rimandata a versioni successive.
    
- La struttura e codice mirano a facilitare la comprensione della programmazione PHP lato server.