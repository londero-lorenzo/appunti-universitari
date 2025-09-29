---
title: Livelli di Astrazione Cloud
aliases:
  - Livelli di Astrazione Cloud
tags:
  - cloud-computing
  - modelli-cloud
  - livelli-di-astrazione-cloud
created: 2025-06-20
---
# Livelli di astrazione nel Cloud Computing

La virtualizzazione è il cuore del cloud computing e permette di condividere risorse fisiche tra più utenti e applicazioni, astrarre l’hardware e semplificare la gestione. Tuttavia, il livello di astrazione influisce direttamente sul controllo che l’utente ha sulle risorse e sulla facilità di scalabilità.

## Impatto della virtualizzazione sul controllo

- **Basso livello di astrazione (es. IaaS)**
    
    - L’utente ha un controllo quasi totale sull’ambiente virtuale: può configurare sistemi operativi, installare software e gestire risorse come se fosse un server fisico.
        
    - Maggiore libertà, ma anche maggior responsabilità nella gestione e nella sicurezza.
        
- **Alto livello di astrazione (es. PaaS, SaaS)**
    
    - L’utente usa ambienti preconfigurati o servizi software completi, con minor controllo sull’infrastruttura sottostante.
        
    - La gestione dell’hardware e della piattaforma è delegata al provider cloud.
        

## Impatto della virtualizzazione sulla scalabilità

- Con **maggiore astrazione**, la scalabilità diventa più semplice e spesso automatizzata (es. scaling automatico di istanze PaaS o SaaS).
    
- Con **minore astrazione** (IaaS), la scalabilità richiede più intervento manuale o la configurazione di sistemi di orchestrazione e gestione.
    

## Esempi estremi

- **Amazon EC2 (IaaS)**: fornisce risorse molto vicine all’hardware, quindi più difficili da scalare automaticamente, ma molto flessibili.
    
- **Google App Engine (PaaS)**: offre un ambiente altamente astratto e scalabile, limitando la libertà ma semplificando lo sviluppo e la scalabilità.


---
## 📚 Fonti e riferimenti  
Slide: `03-Cloud-1.pdf`  
Titolo: `Diversi livelli di astrazione`
