---
title: Aws Servizi
aliases:
  - Aws Servizi
tags:
  - aws
  - aws-servizi
created: 2025-06-20
---
# 📦 Panoramica dei servizi AWS


Amazon Web Services (AWS) è una piattaforma cloud offerta da Amazon che fornisce una vasta gamma di servizi infrastrutturali e applicativi, sia di tipo **IaaS** che **PaaS**, accessibili tramite web service.

L’approccio di AWS si basa su **modularità, scalabilità e accesso programmabile** ai servizi, che possono essere combinati tra loro per costruire soluzioni su misura.

---

## 🔧 Tipologie principali di servizi

| Tipo di servizio | Esempi                     | Categoria |
|------------------|----------------------------|-----------|
| Storage          | Amazon S3, Glacier         | IaaS      |
| Computazione     | Amazon EC2, Lambda         | IaaS / PaaS |
| Reti             | VPC, CloudFront, Route 53  | IaaS      |
| Database         | RDS, DynamoDB              | PaaS      |
| Analisi          | Athena, Redshift           | PaaS      |
| Sicurezza        | IAM, KMS, CloudTrail       | ---       |
| DevOps           | CloudFormation, CodeDeploy | ---       |

---

## 🧩 Caratteristiche comuni

- Accesso via API REST o SOAP
- Utilizzabili da CLI, SDK, console web
- Sistema di pagamento **pay-as-you-go**
- Scalabilità automatica
- Metriche e strumenti di monitoraggio integrati

---

## 🔗 Collegamenti ai singoli servizi

Puoi approfondire i servizi specifici nei file dedicati:

- [`aws_s3.md`](./aws_s3.md): il servizio di storage ad oggetti
- [`aws_ec2.md`](tecnologie_web_per_il_cloud/cloud_computing/aws/aws_servizi/aws_ec2/README.md): macchine virtuali scalabili
- [`aws_cloudfront.md`](./aws_cloudfront.md): distribuzione CDN
- [`aws_altri_servizi.md`](./aws_altri_servizi.md): panoramica su Lambda, DynamoDB e altri

---

## 📁 Note organizzative

Questo file appartiene alla cartella `aws/aws_servizi/` e funge da **indice dei servizi AWS** trattati in dettaglio.  
Per una visione generale su AWS, vedere anche:

- [`aws_intro.md`](../aws_intro.md)
- [`aws_architettura.md`](../aws_architettura.md)
- [`aws_sicurezza.md`](../aws_sicurezza.md)


---

## 📚 Fonte
Slide: `04-Cloud-AWS-1.pdf`  
Titolo: *Amazon Web Services (AWS) – Un caso di studio*