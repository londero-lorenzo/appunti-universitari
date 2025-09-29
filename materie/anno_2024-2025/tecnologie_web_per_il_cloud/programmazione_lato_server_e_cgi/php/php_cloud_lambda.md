---
title: "Php Cloud Lambda"
aliases: ["Php Cloud Lambda"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-cloud-lambda"]
created: 2025-06-28
---
## Introduzione al Serverless Computing

- **Serverless** = paradigma di esecuzione cloud → da **IaaS** a **PaaS**
    
- Il server è completamente gestito dal provider
    
- Il client fornisce solo il codice da eseguire
    
- Modalità di pagamento: **pay-as-you-go**
    
    - EC2: paghi per ore macchina attiva
        
    - Serverless: paghi per **invocazioni** e/o **dati trasferiti**

## ⚙️ Architettura basata su eventi

- Il codice è attivato da **eventi**
    
- Esempi:
    
    - Caricamento immagini/dati → trigger funzione
        
    - Click su sito web → trigger
        
    - Input da sensori IoT
        

## 🧩 FaaS – Function as a Service

- Funzioni autonome, **stateless**, indipendenti dallo storage
    
- Ambienti predefiniti e limitati rispetto a EC2
    
- Esempi:
    
    - Google App Engine: Java, PHP, Node.js, Python, etc.
        
    - **AWS Lambda**: Java, Node.js, C#, Python (e altri)
        

---

## 🛠️ AWS Lambda

- Servizio serverless per eccellenza su AWS
    
- Funzioni Lambda:
    
    - Codice + eventi di trigger (es. S3, DynamoDB, API Gateway)
        
- Supporto linguaggi: Java, Node.js, Python, C# (altri via layer)
    
- Costi:
    
    - 1M richieste/mese + 400.000 GB-sec (gratuito)
        
    - Extra: 0,20$/milione richieste, 0,00001667$/GB-sec
        
- Casi d’uso:
    
    - Event-driven microservices
        
    - Risposte scalabili e parallele
        

---

## 🔁 Orchestrazione: AWS Step Functions

- Permette di comporre funzioni Lambda in flussi logici
    
- Orchestrazione visuale senza codice
    
- Tipologie:
    
    - **Sequenze**
        
    - **Condizioni**
        
    - **Esecuzioni parallele**
        

---

## ⚙️ Composizione di Web Services

### 📌 Modalità

- **Orchestrazione**: controllo centralizzato (una sola entità esegue)
    
- **Coreografia**: entità multiple che cooperano secondo regole condivise

---

## 📚 Fonti e riferimenti  
Slide: `18-Cloud-Lambda.pdf`

