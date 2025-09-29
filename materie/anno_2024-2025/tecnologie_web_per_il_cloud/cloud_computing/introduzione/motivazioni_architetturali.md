---
title: Motivazioni Architetturali
aliases:
  - Motivazioni Architetturali
tags:
  - cloud-computing
  - introduzione
  - motivazioni-architetturali
created: 2025-06-20
---
# 🏗️ Motivazioni Architetturali del Cloud Computing

## ⚙️ Il problema: limiti delle infrastrutture tradizionali

In un’infrastruttura ICT tradizionale, le prestazioni sono vincolate all’hardware:

- **Potenza di calcolo** → CPU e RAM
- **Memoria** → Hard Disk
- **Rete** → Banda acquistata

> Solitamente strumenti più potenti implicano **costi elevati**, ma diventano **obsoleti rapidamente** (ciclo di vita hardware breve).

---

## 📉 Utilizzo inefficiente delle risorse

Analisi dei data center tradizionali mostra un **utilizzo medio reale delle risorse compreso tra il 5% e il 20%**.

Questo significa:

- Hardware spesso sottoutilizzato
- Spese elevate per risorse che non vengono pienamente sfruttate
- Scarsa flessibilità nella risposta ai carichi variabili

---

## 🧮 Dimensionamento: un dilemma

Due strategie classiche di progettazione:

| Strategia                            | Vantaggi                              | Svantaggi                              |
|--------------------------------------|---------------------------------------|----------------------------------------|
| 📉 **Per il carico medio**           | Costi contenuti                       | Non gestisce i picchi di traffico      |
| 📈 **Per i picchi di utilizzo**      | Gestione efficace dei picchi          | Costi molto alti e risorse spesso inutilizzate |

> Entrambe le strategie risultano **subottimali** per scenari con carichi di lavoro variabili nel tempo.

---

## 🚀 La soluzione: virtualizzazione ed elasticità

Il **cloud computing** risolve queste inefficienze grazie a:

- **Virtualizzazione delle risorse**: CPU, storage, rete, ecc.
- **Elasticità**: capacità di scalare dinamicamente in base al carico

📌 _“Usare 1000 server per un’ora costa come usare un server per 1000 ore”_

---

## 🎯 Approccio cloud: vantaggi architetturali

- Acquisto di **prestazioni on-demand** solo quando necessarie
- **Ignoranza deliberata** del funzionamento interno: l’utente non deve conoscere _come_ o _dove_ siano gestite le risorse
- Spostamento della computazione e dello storage **dal device locale al cloud**

---

## 📚 Fonti e riferimenti  
Slide: `03-Cloud-1.pdf`  
Titoli: `Ragioni/I`, `Ragioni/II`, `Soluzione: Cloud`  
