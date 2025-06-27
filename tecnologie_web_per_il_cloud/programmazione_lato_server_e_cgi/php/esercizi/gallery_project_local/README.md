---
title: "Readme"
aliases: ["Readme"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "esercizi", "gallery-project-local", "README"]
created: 2025-06-21
---
# Progetto PHP: Galleria di Immagini

## Descrizione

Questo progetto è un’applicazione web dinamica per la gestione di una galleria di immagini.  
Permette di visualizzare una pagina indice con miniature e di navigare tra le immagini a dimensione originale.

---

## Obiettivi di apprendimento

- Generazione dinamica dei contenuti HTML  
- Creazione dinamica di link tra pagine e immagini  
- Uso delle funzioni PHP per accedere e leggere il filesystem del server  
- Manipolazione e ricerca di stringhe in PHP  
- Trasmissione di dati tramite query string nell’URI  
- Invio di file tramite form HTML  

---

## Struttura dell’applicazione

- Una singola galleria di immagini  
- Le immagini sono memorizzate in una sottocartella (`gallery/images`) all’interno della directory web  
- Pagina indice che mostra miniature di dimensioni fisse  
- Pagina di visualizzazione singola immagine con navigazione “precedente” e “successiva”  
- Configurazioni e funzioni comuni separate in file dedicati  

---

## Preparazione ambiente

Per mettere in piedi l’applicazione, creare la cartella della galleria sotto la root del server web:

```bash
mkdir -p /var/www/html/gallery/images
```

Copiare le immagini nella cartella `images`.

## Contenuti

- `index.php`: pagina indice con miniature e link
    
- `image.php`: pagina di visualizzazione singola immagine con navigazione
    
- `functions.php`: funzioni PHP per gestione file, generazione HTML, ecc.
    
- `config.php`: configurazioni generali (dimensioni miniature, percorsi, ecc.)

---
## Note

- Il progetto si basa su semplificazioni (una sola galleria) per facilitare la comprensione
    
- L’obiettivo è approfondire l’uso di PHP per interagire dinamicamente con il filesystem e generare pagine web
    

---

## Riferimenti

- Materiale didattico: `08-PHP-gallery.pdf`
    
- Documentazione PHP: [https://www.php.net/manual/](https://www.php.net/manual/)

---

## Come iniziare

1. Creare la cartella `gallery/images` nel server web
    
2. Copiare immagini nella cartella
    
3. Caricare il progetto nella cartella `gallery` sotto la root web
    
4. Accedere via browser a `http://<tuo-server>/gallery/index.php`
    
5. Navigare la galleria dinamica

