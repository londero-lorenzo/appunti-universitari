---
title: Aws S3
aliases:
  - Aws S3
tags:
  - aws
  - aws-servizi
  - aws-s3
created: 2025-06-20
---
# 🗂️ Amazon S3 – Simple Storage Service


Amazon S3 (Simple Storage Service) è un servizio di **object storage** scalabile e altamente disponibile, utilizzabile tramite richieste HTTP. Rappresenta una delle fondamenta di AWS, utilizzata per memorizzare e recuperare dati in forma binaria.

---

## 🧱 Caratteristiche principali

- Archiviazione di **oggetti binari** (da **1 byte a 5 TB** per oggetto)
- Ogni oggetto è identificato da:
  - un **nome univoco** all’interno del bucket
  - una **ACL** (Access Control List) per la gestione dei permessi
- I dati sono:
  - **fault-tolerant**, con ridondanza automatica
  - accessibili **tramite HTTP**, come se fossero file su web

---

## 🪣 Bucket

- Gli oggetti sono organizzati in **bucket**, ovvero contenitori virtuali
- Limiti:
  - Max **100 bucket per account**
  - Nome del bucket **globale e univoco**
    - Utilizzato come parte dell’**URI** dell’oggetto

>📎 *Esempio URL oggetto:*
>     [http://sitepoint-aws-cloud-book.s3.amazonaws.com/maggie.jpg](http://sitepoint-aws-cloud-book.s3.amazonaws.com/maggie.jpg)


---

## 🧊 S3 Glacier – Archiviazione a lungo termine

Amazon S3 Glacier è una variante di S3 progettata per l'**archiviazione sicura e a basso costo** di grandi quantità di dati a cui si accede raramente.

- **Ottimizzato per backup e archivi**
- **Costo basso** per lo storage
- **Tempi di recupero molto lunghi** (diversi minuti/ore)
- Ideale per dati storici, log o snapshot

---

## 📦 Classi di storage disponibili

Amazon S3 supporta diverse **classi di storage**, ottimizzate per specifici casi d’uso:

| Classe                  | Utilizzo tipico                     | Costo  |
| ----------------------- | ----------------------------------- | ------ |
| S3 Standard             | Accesso frequente                   | 💲💲💲 |
| S3 Intelligent-Tiering  | Accesso variabile                   | 💲💲   |
| S3 Standard-IA          | Accesso infrequente                 | 💲     |
| S3 One Zone-IA          | Infrequente, ma su una sola AZ      | 💲     |
| S3 Glacier              | Archiviazione a lungo termine       | 💲     |
| S3 Glacier Deep Archive | Archiviazione molto a lungo termine | 💲💲🕒 |

🔗 [Dettagli ufficiali sulle classi di storage](https://aws.amazon.com/it/s3/storage-classes/)

---

## 🔗 Collegamenti utili

- Torna a [`aws_servizi.md`](./aws_servizi.md)
- Vedi anche: [`aws_ec2.md`](tecnologie_web_per_il_cloud/cloud_computing/aws/aws_servizi/aws_ec2/README.md), [`aws_architettura.md`](../aws_architettura.md)


---

## 📚 Fonte
Slide: `04-Cloud-AWS-1.pdf`  
Titolo: *Amazon Web Services (AWS) – Un caso di studio*, *Amazon S3*, *S3 Glacier*,   
Documentazione: [Storage Classes – Amazon S3](https://aws.amazon.com/it/s3/storage-classes/)