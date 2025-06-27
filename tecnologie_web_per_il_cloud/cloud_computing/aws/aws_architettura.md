---
title: Aws Architettura
aliases:
  - Aws Architettura
tags:
  - aws
  - aws-architettura
created: 2025-06-20
---
# Architettura di Amazon Web Services (AWS)

## Struttura geografica

AWS organizza la propria infrastruttura in:

- **Regioni**: aree geografiche distinte identificate da nomi come `us-east-1`, `eu-west-1`, ecc. Ogni regione è indipendente e l’utente può scegliere in quale regione distribuire dati e applicazioni in base a criteri legali o di prossimità al mercato.

- **Availability Zones (AZ)**: singoli data center o gruppi di data center all’interno di una regione, con indipendenza elettrica e di rete per garantire alta affidabilità e tolleranza ai guasti. Le AZ sono connesse tramite linee a bassa latenza.

La possibilità di replicare risorse su più AZ permette di aumentare la resilienza e la disponibilità del servizio.

## Sicurezza

- **Access Identifier e chiavi di accesso**: identificano in modo sicuro l’account e le sue chiamate API.

- **Access Control List (ACL)**: gestisce i permessi sugli oggetti.

- **IAM (Identity and Access Management)**: sistema di gestione utenti e permessi, per definire chi può accedere a quali risorse, con un controllo granulare.

---

## Fonti

- Slide: `04-Cloud-AWS-1.pdf`  
- Titoli: *Amazon Web Services (AWS) – Un caso di studio* , *Architettura della nuvola*, *Regioni*, *Availability zone*
