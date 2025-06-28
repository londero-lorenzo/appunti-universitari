---
title: "Php Soa"
aliases: ["Php Soa"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-soa"]
created: 2025-06-28
---
# Architettura Orientata ai Servizi (SOA)

## 💡 Concetti Chiave

### Cos'è un **Servizio**
- Entità autonoma e indipendente, capace di fornire funzionalità di diversa complessità.
- Può essere semplice (es. risposta a una richiesta) o complesso (es. orchestrazione di processi).
- Implementato come software, è indipendente dalla piattaforma.

---

### 🌐 Service Orientation (SO)
- **Paradigma di sviluppo** che costruisce applicazioni componibili da servizi indipendenti pubblicati in rete.
- Ogni servizio può essere:
  - **Descritto**
  - **Pubblicato**
  - **Ricercato**
  - **Invocato**

---

## 🧭 Principi Fondamentali della SO

| Principio               | Descrizione |
|-------------------------|-------------|
| **Standardized Service Contract** | Espone le capacità sotto forma di contratto formale |
| **Loose Coupling**       | Bassa dipendenza tra componenti |
| **Service Abstraction**  | Nasconde i dettagli implementativi |
| **Service Reusability**  | Servizi riusabili in più contesti |
| **Service Autonomy**     | Controllo sul proprio ambiente |
| **Service Statelessness**| Idealmente senza stato per prestazioni |
| **Service Discoverability**| Ricercabilità tramite descrizione adeguata |
| **Service Composability**| Progettato per essere integrato |

---

## 🖥️ Service-Oriented Computing (SOC)

### Cos'è
- **Disciplina** che integra:
  - Sistemi distribuiti
  - Middleware
  - Ingegneria del software
  - Linguaggi e database
  - Rappresentazione della conoscenza

### Obiettivi
- Aumentare interoperabilità
- Favorire federazione tra sistemi
- Ridurre dipendenza dai fornitori (vendor lock-in)
- Allineare business e IT
- Migliorare ROI e agilità organizzativa

---

## 🏗️ Service-Oriented Architecture (SOA)

### Cos'è
- Stile architetturale per implementare SO
- Include strumenti per:
  - pubblicazione
  - descrizione
  - scoperta
  - utilizzo dei servizi

### Indipendenza Tecnologica
- SOA è **agnostica alla tecnologia**
- Web Services (SOAP/WSDL) sono implementazione comune

---

## 🧩 Ruoli nella SOA

| Ruolo        | Funzione |
|--------------|----------|
| **Service Provider** | Espone e pubblica i servizi |
| **Service Client**   | Scopre e utilizza i servizi |
| **Service Registry** | Repository con metadati dei servizi |

### Operazioni
1. **Publish**: pubblicazione nel registry
2. **Find**: ricerca del servizio
3. **Bind**: collegamento e invocazione

---

## 📦 Esempio di Processo

- Azienda che funge da intermediario tra produttori e clienti.
- Flusso: ordine → magazzino → verifica credito → spedizione → fatturazione.
- Gestito da servizi integrati e orchestrati.

---

## 🔢 Livelli di Adozione della SOA
1. **Adozione locale**: adattamento di software esistenti
2. **Organizzazione basata su SOA**: servizi comuni e standard
3. **SOA tra organizzazioni**: collaborazione tra imprese

---

## 📏 Quality of Service (QoS)

### Dimensioni principali
- **Disponibilità**
- **Accessibilità**
- **Performance** (throughput, latency)
- **Affidabilità**
- **Scalabilità**
- **Sicurezza**
- **Conformità a SLA**

### SLA - Service Level Agreement
- Contratto che specifica:
  - Obiettivi di qualità
  - Penalità
  - Servizi offerti
  - Periodo di validità

---

## 🔐 Note Finali
- La **qualità** e la **standardizzazione** sono centrali per rendere i servizi componibili, affidabili e interoperabili.
- **Web Services REST e SOAP** sono due approcci concreti che verranno approfonditi in laboratorio.

---

## 📚 Fonti e riferimenti
- T. Erl, *Service-Oriented Architecture: Concepts, Technology, and Design*
- T. Erl, *Principles of Service Design*
- M. Papazoglou, *Web Services: Principles and Technology*
- Papazoglou et al., *Service-Oriented Computing: State of the Art and Research Challenges*, IEEE Computer, 2007
- `11-SOA.pdf`
