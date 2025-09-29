---
title: Cloud Come Sistema Distribuito
aliases:
  - Cloud Come Sistema Distribuito
tags:
  - cloud-computing
  - modelli-cloud
  - cloud-come-sistema-distribuito
created: 2025-06-20
---
# Cloud come sistema distribuito

Il cloud computing è fondamentalmente un sistema distribuito, cioè un insieme di risorse hardware e software che risiedono su più macchine geograficamente disperse ma funzionano in modo integrato per fornire servizi agli utenti finali.

## Caratteristiche principali

### 1. Risorse distribuite e accesso trasparente

- Le risorse di calcolo (CPU, memoria, storage) sono distribuite su più data center sparsi in varie località geografiche.
    
- Gli utenti accedono a queste risorse tramite Internet senza doversi preoccupare della loro posizione fisica o dell’infrastruttura sottostante.
    
- La distribuzione consente di migliorare la disponibilità e la tolleranza ai guasti, poiché se un nodo o un data center ha problemi, le richieste possono essere deviate altrove.
    

### 2. Indipendenza dalla localizzazione fisica

- L’utente non conosce né gestisce direttamente dove vengono eseguite le sue applicazioni o dove sono archiviati i suoi dati.
    
- Questa astrazione è possibile grazie a meccanismi di virtualizzazione, orchestrazione e networking avanzato.
    

### 3. Scalabilità e elasticità

- Il sistema distribuito permette di scalare facilmente le risorse, aggiungendo o rimuovendo nodi senza interruzioni.
    
- L’elasticità si traduce nella capacità di adeguare dinamicamente le risorse in base al carico di lavoro, pagando solo per ciò che si utilizza.
    

### 4. Modelli di servizio e astrazione

- I vari livelli di servizio (IaaS, PaaS, SaaS) si basano su questa infrastruttura distribuita, offrendo diversi gradi di controllo e responsabilità.
    
- L’utente può scegliere il livello di astrazione più adatto alle proprie esigenze, dalla gestione diretta delle macchine virtuali (IaaS) fino all’uso di applicazioni completamente gestite (SaaS).
    

### 5. Gestione e orchestrazione

- Dietro le quinte, sofisticati software di gestione coordinano la distribuzione dei carichi, l’allocazione delle risorse, la sicurezza e la manutenzione.
    
- Tecnologie come container orchestration (es. Kubernetes) e software-defined networking facilitano la gestione di queste infrastrutture distribuite.
    

## Vantaggi del modello distribuito nel cloud

- **Affidabilità:** la distribuzione geografica e la ridondanza riducono i rischi di interruzione del servizio.
    
- **Prestazioni:** il posizionamento intelligente delle risorse avvicina i dati e i servizi agli utenti finali, migliorando la latenza.
    
- **Costo-efficienza:** con la condivisione delle risorse tra più utenti e la possibilità di adattare l’uso al momento, si ottimizza il rapporto costi/benefici.
    
- **Flessibilità:** permette di supportare carichi di lavoro variabili e nuovi scenari applicativi in tempi rapidi.


---

## 📚 Fonti e riferimenti  
- Slide: `03-Cloud-1.pdf`  
- Titolo: `Cloud come sistema distribuito`