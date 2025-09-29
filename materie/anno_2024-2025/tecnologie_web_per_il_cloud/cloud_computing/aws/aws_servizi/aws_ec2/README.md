---
title: "Readme"
aliases: ["Readme"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "aws", "aws-servizi", "aws-ec2", "README"]
created: 2025-06-21
---
# 💻 Amazon EC2 – Elastic Compute Cloud

## 🧩 Cos’è EC2?

Amazon EC2 (Elastic Compute Cloud) è il servizio di AWS che permette di accedere a **istanze virtuali di calcolo**, scalabili e configurabili, con diverse modalità di pagamento.

- Ogni istanza è una **copia eseguibile di un’immagine** (AMI, Amazon Machine Image)
- L’istanza emula un server fisico (CPU, RAM, disco, ecc.)
- Può essere configurata e accesa/spenta in base alle esigenze

---

## 🧱 Componenti principali

| Componente | Descrizione |
|------------|-------------|
| **AMI** (Amazon Machine Image) | Sistema operativo + software (es. Linux, Windows, DB, server web). Possono essere predefinite o personalizzate. |
| **Istanza** | Copia attiva di un’AMI. Può essere scelta tra varie configurazioni (es. RAM, CPU, tipo di disco). |
| **Volume EBS** | Disco virtuale persistente che può essere collegato all’istanza. |

---

## ⚙️ Modalità di utilizzo e pagamento

Consulta il file [`aws_ec2_istanze.md`](./aws_ec2_istanze.md) per approfondire:

- Tipologie di istanza (On-demand, Reserved, Spot, Burstable)
- Persistenza delle risorse (temporanee vs permanenti)
- Dettaglio costi EC2, EBS, banda e confronto con S3
- Nomi delle istanze e significato

---

## 🌐 Networking e IP

- Ogni istanza ha un indirizzo IP pubblico e DNS associato
- È possibile usare **Elastic IPs** (IP statici pubblici) assegnabili a più istanze in caso di failover

---

## 🧬 Famiglie di istanze

EC2 è organizzato in **famiglie di istanze**, ciascuna ottimizzata per uno scopo (es. calcolo, memoria, storage, GPU).

📄 Dettagli completi in [`aws_ec2_istanze.md`](./aws_ec2_istanze.md#🧬-famiglie-di-istanze)

| Famiglia | Scopo | Esempi |
|----------|-------|--------|
| **T** | Uso generale, burstable | T2, T3 |
| **M** | Uso generico stabile | M3, M4 |
| **C** | Calcolo intensivo | C3, C4 |
| **R** | Ottimizzate per memoria | R3 |
| **I / D** | Ottimizzate per storage | I2, D2 |
| **G** | GPU (ML, rendering) | G2 |

---

## 🚀 Funzionalità avanzate

EC2 può essere esteso con servizi AWS per renderlo **scalabile, resiliente e monitorabile**:

🔧 Le funzionalità dettagliate sono spiegate in [`aws_ec2_funzioni_avanzate.md`](./aws_ec2_funzioni_avanzate.md)

| Servizio | Funzione principale |
|----------|---------------------|
| **ELB** (Elastic Load Balancer) | Bilancia il traffico tra più istanze |
| **CloudWatch** | Monitoraggio risorse e metrica |
| **Auto Scaling** | Aggiunta/rimozione automatica di istanze |
| **CloudFormation** | Provisioning infrastrutturale automatico |
| **Spot Instances** | Computazione a basso costo tramite asta |

---

## 📏 Misura della potenza di calcolo

- Amazon EC2 utilizza le **vCPU** (virtual CPU), ovvero hyperthread dei core fisici.
- Il vecchio sistema **ECU (EC2 Compute Unit)** è deprecato.
- Le performance variano in base alla **famiglia e generazione** dell’istanza.

📄 Consulta la sezione dedicata in [Funzioni avanzate](./aws_ec2_funzioni_avanzate.md)


---

## 🔗 Collegamenti utili

- Torna a [`aws_servizi.md`](aws_servizi.md)
- Vedi anche: [`aws_s3.md`](aws_s3.md), [`aws_cloudfront.md`](aws_cloudfront.md)
- Introduzione: [`aws_intro.md`](aws_intro.md)
- Prezzi aggiornati: [https://aws.amazon.com/it/ec2/pricing/on-demand/](https://aws.amazon.com/it/ec2/pricing/on-demand/)


---

## ## 📘 Esempi di uso

- Applicazioni web scalabili
- Backend per microservizi
- Analisi dati, ambienti di test/dev/staging
- Progetti machine learning (GPU)

---

## 📚 Fonte
Slide: `04-Cloud-AWS-1.pdf`  
Titolo: *Amazon Web Services (AWS) – Un caso di studio*, *Amazon EC2/I*, *AWS: immagini, istanze, volumi*, *Amazon EC2/2: istanze*, *Descrivere la potenza di calcolo*, *Virtual CPU*, *Famiglie di istanze EC2*, *I nomi delle istanze*, *Ottimizzazione, un esempio: Tx*, *Amazon EC2/4: altre funzioni*
Approfondimenti: [Documentazione ufficiale EC2](https://aws.amazon.com/ec2/)