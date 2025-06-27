---
title: "Aws Cloudfront"
aliases: ["Aws Cloudfront"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "aws", "aws-servizi", "aws-cloudfront"]
created: 2025-06-20
---
# 🌍 Amazon CloudFront – Content Delivery Network


Amazon CloudFront è il **servizio CDN (Content Delivery Network)** di AWS, progettato per **distribuire contenuti** (statici e dinamici) a **bassa latenza** e **alta velocità**, sfruttando una rete globale di edge location.

---

## 🚀 Obiettivo

Distribuire contenuti web (immagini, video, file statici, API, siti web, ecc.) **in modo rapido e sicuro** agli utenti finali, riducendo i tempi di risposta.

---

## 🌐 Funzionamento

1. L’utente effettua una richiesta per un contenuto (es. immagine, video, HTML).
2. La richiesta viene indirizzata automaticamente alla **edge location** più vicina.
3. Se il contenuto è già **in cache** → risposta immediata.
4. Se non è in cache → CloudFront lo recupera dal server **origin** (es. Amazon S3, EC2, Load Balancer o server esterno) e lo memorizza.

---

## 🏗️ Caratteristiche principali

- **Caching distribuito** geograficamente su edge location (centinaia nel mondo)
- **Riduzione della latenza**: i dati viaggiano meno in rete
- **Supporto a HTTPS** con certificati TLS/SSL
- **Controllo d’accesso** tramite signed URLs o signed cookies
- **Integrazione con altri servizi AWS**: S3, EC2, Elastic Load Balancer, Lambda@Edge

---

## 🧰 Esempi di utilizzo

- Distribuzione di immagini statiche per siti e-commerce
- Accelerazione di siti web
- Streaming di video on demand
- Protezione da attacchi DDoS grazie all’integrazione con AWS Shield

---

## 💰 Costi

- Pay-as-you-go: basati su **GB trasferiti**, **numero di richieste**, e **regione geografica**
- Costi ridotti rispetto al caricamento diretto da S3 o EC2, grazie al caching

🔗 Stima dei costi: [AWS Pricing – CloudFront](https://aws.amazon.com/it/cloudfront/pricing/)

---

## 🔗 Collegamenti utili

- Torna a [`aws_servizi.md`](./aws_servizi.md)
- Vedi anche: [`aws_s3.md`](./aws_s3.md), [`aws_ec2.md`](tecnologie_web_per_il_cloud/cloud_computing/aws/aws_servizi/aws_ec2/README.md)
- Introduzione: [`aws_intro.md`](../aws_intro.md)

---

## 📚 Fonte
Slide: `04-Cloud-AWS-1.pdf`  
Titoli: *Amazon Web Services (AWS) – Un caso di studio*, *Amazon CloudFront*
Documentazione ufficiale: [Amazon CloudFront](https://aws.amazon.com/it/cloudfront/)