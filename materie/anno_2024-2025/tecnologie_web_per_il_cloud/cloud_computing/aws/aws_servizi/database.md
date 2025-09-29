---
title: "Database"
aliases: ["Database"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "aws", "aws-servizi", "database"]
created: 2025-06-20
---
# 🗄️ Database in AWS


## 📊 Tipologie di database su AWS

AWS offre diverse soluzioni di **database gestiti**, sia relazionali che non relazionali (**NoSQL**), scalabili e replicati automaticamente.

### ✅ Categorie principali

| Nome         | Tipo  | Descrizione sintetica                          |
| ------------ | ----- | ---------------------------------------------- |
| **Aurora**   | SQL   | Database relazionale ad alte prestazioni       |
| **RDS**      | SQL   | MySQL, Oracle, PostgreSQL, SQL Server, MariaDB |
| **DynamoDB** | NoSQL | Archivio chiave-valore, altamente scalabile    |
| **SimpleDB** | NoSQL | Per piccole basi di dati, schema-less          |

Tutti questi servizi gestiscono automaticamente backup, failover, e replicazione geografica.

---

## 🧮 Amazon RDS – Relational Database Service

- Permette di **eseguire istanze di database relazionali** su infrastruttura gestita
- Supporta vari motori: MySQL, Oracle, PostgreSQL, SQL Server, MariaDB, Aurora
- Le istanze sono simili a quelle EC2, ma ottimizzate per il DB
- Supporta:
  - Backup automatici
  - Aggiornamenti software
  - Replica multi-zona
  - Storage configurabile (da 5 GB a 1 TB o più)
- Ideale per applicazioni tradizionali con schema rigido e integrità relazionale

---

## 📦 Amazon Aurora

- Motore compatibile con MySQL e PostgreSQL
- Progettato da AWS per massimizzare prestazioni e disponibilità
- Può offrire fino a **5 volte le prestazioni di MySQL** su hardware equivalente
- Replica automatica in 6 copie su 3 Availability Zones
- Flessibilità nella scalabilità del carico in lettura

> 🔐 È una delle soluzioni consigliate per servizi mission-critical

---

## 🌐 Amazon DynamoDB – NoSQL

- Database **chiave-valore e documento**, serverless
- Altamente scalabile e distribuito, a **bassa latenza anche su scala massiva**
- Supporta:
  - Accessi in tempo reale
  - Auto scaling e throughput configurabile
  - Controllo fine degli accessi con IAM
- Utilizzato per: giochi online, e-commerce, IoT, log analytics

---

## 📉 Amazon SimpleDB – NoSQL semplice

- Alternativa leggera a DynamoDB, per **piccole basi di dati**
- Funziona con **domini** (equivalenti a tabelle), max 100 per account
- Fino a 10 GB per dominio, e 25 scritture/sec
- Schema-less:
  - Gli item (righe) hanno **attributi** dinamici (fino a 256)
  - Ogni attributo può avere **più valori** (max 1024 byte ciascuno)

### 🔎 Operazioni disponibili

- Query di confronto: `=`, `!=`, `<`, `>`, `<=`, `>=`, `STARTS-WITH`
- Operatori logici: `AND`, `OR`, `NOT`
- Set: `INTERSECTION`, `UNION`

---

## 🧠 Amazon EMR – Elastic MapReduce

- Sistema per **analisi di grandi volumi di dati** usando Hadoop (MapReduce)
- Adatto a:
  - Analisi di log
  - Machine Learning distribuito
  - Elaborazione di dati scientifici
- Funziona come una **pipeline distribuita**:
  > "1000 server per un’ora" invece che "1 server per 1000 ore"

> EMR permette di risparmiare tempo e costi nelle applicazioni CPU-intensive o basate su Big Data.

---

## 🔗 Collegamenti utili

- Torna a [`aws_servizi.md`](./aws_servizi.md)
- Altri servizi: [`aws_s3.md`](./aws_s3.md), [`aws_ec2.md`](tecnologie_web_per_il_cloud/cloud_computing/aws/aws_servizi/aws_ec2/README.md)
- Documentazione ufficiale:
  - [Amazon RDS](https://aws.amazon.com/rds/)
  - [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
  - [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
  - [Amazon EMR](https://aws.amazon.com/emr/)


---
## 📚 Fonte
Slide: `04-Cloud-AWS-1.pdf`  
Titolo: *Amazon Web Services (AWS) – Un caso di studio*