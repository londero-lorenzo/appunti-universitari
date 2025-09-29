---
title: Servizi Offerti dal Sistema Operativo
aliases:
  - Servizi Offerti dal Sistema Operativo
created: 2025-06-30
---
# Servizi Offerti dal Sistema Operativo

> [!abstract]
> Panoramica delle funzionalità di base fornite dal sistema operativo all'utente e ai programmi in esecuzione.

---

## Servizi di Base

- **Interfaccia utente**
  Il sistema operativo può fornire diversi tipi di interfaccia:
	- [[#Interprete di Comandi|CLI (Command Line Interface)]]
	- [[#Interfaccia Grafica|GUI (Graphical User Interface)]]
	- Interfaccia batch (a lotti)

- **Esecuzione di programmi**  
  Caricamento in memoria ed esecuzione di programmi.

- **Operazioni di Input/Output**  
  Il sistema operativo funge da interfaccia tra utente/programma e dispositivi di I/O.

- **Gestione del file system**  
  Supporta operazioni su file e directory: creazione, lettura, scrittura, ricerca.

- **Gestione degli accessi e dei privilegi**

- **Comunicazione tra processi**  
  Due tecniche principali:
	- Shared Memory
	- Message Passing

---

## Altri Servizi di Base

- **Rilevamento e gestione degli errori**  
  Il sistema deve rilevare guasti hardware, errori software o violazioni e reagire per garantire consistenza e affidabilità.

- **Assegnazione delle risorse**  
  Il sistema decide come allocare CPU, memoria e dispositivi applicando strategie efficienti.

- **Contabilizzazione dell’uso delle risorse**  
  Raccolta di informazioni/statistiche utili per ottimizzazione delle prestazioni e controllo delle attività.

- **Protezione e sicurezza**  
  Fondamentali nei sistemi multiutente.

---

## Interfaccia con l’Utente

### Interprete di Comandi

- Di solito è un processo utente chiamato **shell**
- Riceve una stringa, la decodifica e la esegue
- Esegue:
	- **Built-in**: comandi interni alla shell
	- **Programmi esterni**: utility di sistema

### Interfaccia Grafica

- Fornisce una metafora visuale (es. scrivania virtuale)
- Permette interazione con oggetti grafici
- Coordina dispositivi come tastiera, mouse, schermo

---

## 📚 Fonti

- Contenuto: _Servizi Offerti dal Sistema Operativo_
- Slide: [_Struttura dei Sistemi Operativi_](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand02.pdf)
- Autore: A. Formisano
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
