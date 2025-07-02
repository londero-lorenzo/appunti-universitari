---
title: Macchine Virtuali
aliases:
  - Macchine Virtuali
created: 2025-07-02
---
# Macchine Virtuali

>[!abstract]
>Le **macchine virtuali** (VM) consentono l’esecuzione di ambienti separati che emulano sistemi di elaborazione completi, isolati tra loro ma condividenti le risorse hardware sottostanti.

---

## Cos'è una Macchina Virtuale?

>[!definition]
>**Macchina Virtuale**  
>>Software che **emula un’intera architettura hardware**, offrendo un’interfaccia identica a quella di una macchina fisica. Consente di eseguire sistemi operativi e applicazioni su hardware diverso da quello originale.

### Caratteristiche principali:

- Esegue su un hardware reale ma **emula** processore, memoria, dispositivi, ecc.
- Ogni VM può ospitare un diverso sistema operativo.
- Le risorse reali vengono **condivise tra le VM**.
- L’**isolamento** tra VM garantisce maggiore sicurezza.
- Può essere usata per test, retrocompatibilità, sandboxing.

---

## Esempio di Funzionamento

- Il sistema operativo ospite (host OS) crea l’**illusione** di avere processori e memoria separati per ciascuna VM.
- Ogni VM crede di essere l’unico sistema attivo sulla macchina fisica.
- Il comportamento è simile a quello dei **processi utente**, ma con un'interfaccia a basso livello completa.

---

## Efficienza e Prestazioni

>[!info]
>**Efficienza delle VM**  
>>- Le VM hanno una CPU virtualizzata → **più lenta** della CPU reale.  
>>- Tuttavia, le operazioni di **I/O possono essere più veloci**, grazie all’emulazione rapida dei dispositivi (non fisici).  
>>- Il compromesso tra isolamento e prestazioni è uno dei punti chiave nella progettazione dei sistemi virtualizzati.

---

## Schema: Macchina Reale vs Virtuale

- Macchina **non virtuale** (a): sistema operativo e programmi girano direttamente sull’hardware.
- Macchina **virtuale** (b): ogni sistema operativo gira su una VM, astratta dall’hardware fisico.

>[!example]
>![[sistemi-operativi/teoria/02--struttura-sistemi-operativi/struttura_sistemi_operativi_schema.md#^frame=N_wek8Fa5dY5owevrfahV|100%]]

---

## Vantaggi delle Macchine Virtuali

- Uso **condiviso** dell’hardware → maggiore efficienza economica.
- **Isolamento** tra ambienti → un crash in una VM **non compromette** le altre.
- Possibilità di **eseguire software legacy** o sistemi operativi diversi.
- Strumento fondamentale per:
  - test e sviluppo
  - cloud computing
  - ambienti sicuri e controllati (sandbox)


---

## 📚 Fonti

- Slide: _[Struttura dei Sistemi Operativi](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand02.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
