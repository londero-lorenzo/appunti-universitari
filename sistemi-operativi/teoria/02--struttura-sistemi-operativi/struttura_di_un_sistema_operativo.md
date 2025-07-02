---
title: Struttura di Un Sistema Operativo
aliases:
  - Struttura di Un Sistema Operativo
created: 2025-06-30
---
# Struttura di un Sistema Operativo

>[!abstract]
>Questo capitolo descrive le diverse **architetture organizzative** con cui è possibile realizzare un sistema operativo, evidenziando i vantaggi e svantaggi di ciascun approccio.

---

## Struttura Monolitica

>[!definition]
>**Struttura Monolitica**  
>>Organizzazione in cui tutte le funzionalità del sistema operativo sono contenute in un unico blocco di codice eseguibile (il kernel), in grado di accedere direttamente a ogni componente.

- Tutte le componenti sono contenute nel kernel.
- Massima efficienza → **comunicazioni dirette** tra funzioni.
- Scarsa modularità → difficile manutenzione e debug.
- Tutto il codice esegue in modalità privilegiata → **bassa sicurezza**.
- Esempi: **MS-DOS**, primi **UNIX**.

>[!example]
>Struttura semplice nel **MS-DOS**
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=rB4MQLZGd0P7l2exH8cZP]]
>------------------------
>Struttura semplice in **UNIX**
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=f4f_eavbIxgvDWcjlTBqg|100%]]



---

## Struttura Stratificata

>[!definition]
>**Struttura Stratificata**  
>>Organizzazione a livelli, in cui ogni strato interagisce **solo con quelli inferiori**, nascondendo l’implementazione interna e migliorando modularità e manutenibilità.

- Maggiore modularità: implementazione più isolata.
- Debug più semplice.
- Peggioramento delle performance per via delle interfacce obbligate.
- Ogni livello ha **interfacce ben definite** verso il basso.

>[!example]
>Struttura stratificata tipica:
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=O1zj-fDGaS1wC1nzZM9g2|75%]]

---

## Struttura a Microkernel

>[!definition]
>**Microkernel**  
>>Architettura in cui il kernel contiene **solo le funzionalità minime** (gestione memoria, comunicazione, IPC[^1]), mentre tutto il resto è esterno, non eseguito in modalità kernel.
>
>[^1]: Un meccanismo di comunicazione inter processo è essenziale per il funzionamento di un sistema operativo strutturato a microkernel. Tale meccanismo abilita la comunicazione e lo scambio di dati tra diversi processi a livello utente e tra un processo a livello utente e il kernel.


- Migliore **modularità**, **portabilità** e **sicurezza**.
	- non necessita di tutte le funzionalità esterne
	- modifiche minime per essere implementato per un nuovo hardware
	- meno codice in modalità privilegiata
- **Performance inferiore** per via delle comunicazioni frequenti tra processi.
- Fallimenti nei moduli esterni **non compromettono** il kernel.
- Usato in ambienti critici o embedded.

>[!example]
>Struttura a microkernel tipica:
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=B8N508JBRkS96QYH3nmWu|100%]]


---

## Struttura Modulare

>[!definition]
>**Struttura Modulare**  
>>Approccio ibrido che carica **moduli dinamici** a runtime, mantenendo un kernel centrale compatto ma estendibile.

- Caricamento dinamico di moduli.
- Maggiore **flessibilità** e **efficienza** rispetto ai microkernel.
- Moduli possono comunicare direttamente senza passare dal kernel.
- Ispirato alla **programmazione ad oggetti**.

>[!example]
>Struttura modulare per sistema Solaris:
>
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=GSFENhdWcIQyNmOU0BqNY]]
>
>Struttura modulare per sistema Linux:
>
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=LAFa5LKgA9-toVgxh9DND|100%]]


---

## Strutture Ibride (nella pratica)

>[!info]
>**I sistemi operativi reali sono spesso ibridi.**

- **Linux**, **Windows**, **Solaris**: kernel monolitico con moduli caricabili.
- **macOS/iOS**: derivati da Unix BSD, combinano microkernel, moduli, e livelli.
- **Android**: basato su Linux, con layer VM (Dalvik/ART) per esecuzione Java.


---

## 📚 Fonti

- Slide: _[Struttura dei Sistemi Operativi](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand02.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
