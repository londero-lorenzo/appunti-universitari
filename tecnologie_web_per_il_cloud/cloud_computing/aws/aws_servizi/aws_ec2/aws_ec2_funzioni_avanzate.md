---
title: Aws Ec2 Funzioni Avanzate
aliases:
  - Aws Ec2 Funzioni Avanzate
tags:
  - aws-ec2-funzioni-avanzate
created: 2025-06-21
---
# ⚙️ Amazon EC2 – Funzionalità Avanzate e Strumenti Collegati

Questa sezione descrive i principali strumenti e servizi AWS collegati a EC2 che permettono di costruire infrastrutture **scalabili, resilienti e automatizzate**.

---

## 🔁 ELB – Elastic Load Balancer

- Bilancia il traffico tra più istanze EC2, anche su diverse **Availability Zones**.
- Migliora **disponibilità e tolleranza ai guasti**.
- Può essere associato a **Auto Scaling** per architetture dinamiche.
- Supporta protocolli: HTTP, HTTPS, TCP, UDP.

> 📌 Esistono diversi tipi di ELB: Application Load Balancer, Network Load Balancer, Gateway Load Balancer.

---

## 📈 CloudWatch

- Servizio di **monitoraggio e osservabilità**.
- Raccoglie metriche (CPU, memoria, rete, dischi, ecc.) e consente:
  - Allarmi e notifiche (es. via email o SNS)
  - Logging centralizzato
  - Attivazione di **azioni automatiche**

> 🔄 CloudWatch è spesso usato in combinazione con Auto Scaling per aumentare o ridurre risorse in base al carico.

---

## 📊 Auto Scaling

- Gestisce automaticamente il numero di istanze EC2 in funzione di metriche e politiche configurabili.
- Supporta:
  - **Scalabilità orizzontale** (più istanze → più capacità)
  - **Riduzione automatica** per risparmio nei momenti di inattività
  - **Istanze Spot** per ottimizzazione dei costi

> 💡 Auto Scaling usa le soglie definite in CloudWatch per prendere decisioni.

---

## 🧱 CloudFormation

- Strumento per il **provisioning automatico** di infrastrutture complesse (stack).
- Utilizza **template YAML o JSON** per descrivere risorse (EC2, RDS, ELB, S3...).
- Permette:
  - Versionamento dell’infrastruttura
  - Replica identica in ambienti diversi (dev, test, prod)
  - Deploy di architetture complete con un singolo comando

> 📦 Esempio d’uso: creazione di un’app web con EC2 + RDS + ELB tramite un unico template.

---

## 🧠 Ottimizzazione: istanze burstable (serie T)

- Le istanze **Tx** (es. `t2.micro`, `t3.small`) sono istanze **a crediti CPU**:
  - Accumulano crediti nel tempo quando utilizzano meno CPU
  - I crediti vengono spesi quando servono picchi di calcolo
- Ideali per:
  - Web server leggeri
  - CMS
  - Backend API a basso traffico

> ✅ Perfette per ambienti dev/test o carichi discontinui → ottimo bilanciamento costi/prestazioni.

---

## 🔗 Collegamenti utili

-  **Panoramica EC2** → [`README.md`](./README.md)
-  **Famiglie e costi istanze** → [EC2 Istanze](./aws_ec2_istanze.md)
-  **Documentazione CloudFormation** → [docs.aws.amazon.com/cloudformation](https://docs.aws.amazon.com/cloudformation/)
-  **Prezzi EC2 aggiornati** → [aws.amazon.com/ec2/pricing](https://aws.amazon.com/ec2/pricing/)

---

## 📁 Note organizzative

- Cartella: `aws/aws_servizi/aws_ec2/`

---

## 📚 Fonti e riferimenti  
Slide: `04-Cloud-AWS-1.pdf`  
Titoli:  
- *Amazon EC2/4: altre funzioni*  
- *CloudWatch*, *Elastic Load Balancer*, *Auto Scaling*, *CloudFormation*  
- *Ottimizzazione, un esempio: Tx*
