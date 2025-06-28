---
title: "Php Cloud Aws S3"
aliases: ["Php Cloud Aws S3"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-Cloud-aws-s3"]
created: 2025-06-28
---
## 🧾 Cos'è S3
- **S3 (Simple Storage Service)**: servizio di storage oggetti di Amazon.
- Pensato per dati binari di grandi dimensioni (fino a **5 TB per oggetto**).
- Simula un file system via HTTP, organizzato in:
  - **Bucket** (max 100 per account)
  - **Oggetti**, ciascuno con:
    - un nome univoco
    - una ACL (Access Control List)

### ✅ Caratteristiche
- Accesso via API REST o SDK
- Ridondanza e fault-tolerance automatica
- Diversi livelli di storage:
  - **Standard**
  - **Infrequent Access**
  - **Glacier** (archiviazione a basso costo e accesso lento)

## 📦 Glacier
- Ideale per backup e dati poco usati
- Costi:
  - 🔻 Storage molto economico
  - 🔺 Accesso lento e più costoso
- Tempi di recupero: da minuti a ore

## ⚙️ Storage Classes
- [Link alle classi ufficiali](https://aws.amazon.com/it/s3/storage-classes/)
- Esempi:
  - `S3 Intelligent-Tiering`
  - `S3 One Zone-IA`
  - `S3 Glacier Deep Archive`

---

## 💻 Uso con PHP

### 📦 SDK AWS per PHP
- Versione consigliata: v3+
- Object Oriented, PHP ≥ 5.5
- Installazione:
```bash
  composer require aws/aws-sdk-php
```

---
### 🔐 Gestione Credenziali

1. **Variabili ambiente**
    
2. **File `~/.aws/credentials`**:
``` ini
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```
3. **Oggetto PHP**:
```php
$credentials = new Aws\Credentials\Credentials('key', 'secret');
```
---
## ⚠️ Best Practices e Attenzioni

### 🕒 Sincronizzazione oraria

- Il server deve avere un orario preciso (max ±15 minuti di differenza da AWS).
    
- Configurare `date.timezone` in `php.ini`.
    

### 🌀 Exponential Backoff (upload resiliente)

- Tentativi multipli con attese esponenziali:  
    1s → 2s → 4s → … fino a N volte.
    
- Utile in caso di timeout o errori temporanei.
    

### 📊 Costi da ricordare

- Le **API chiamate sono fatturate**: attenzione a loop o debug mal configurato.
    
- Monitorare uso con **AWS CloudWatch**.
    

---

## 🧰 Funzionalità avanzate S3

- **Multipart Upload** per file di grandi dimensioni
    
- **uploadDirectory**: carica un'intera directory
    
- **downloadBucket**: scarica un bucket intero
    
- **Versioning**: conserva versioni precedenti dei file
    
- **Lifecycle Rules**: automatizza il passaggio tra classi (es. da Standard a Glacier)
    
- **Event Notification**: trigger via SNS, Lambda, SQS
    

---

## 🌍 CDN con CloudFront

- Migliora distribuzione geografica dei contenuti
    
- Può essere abbinato a S3 per distribuzione immagini/video
    
- Setup tramite:
    
    - Console grafica AWS
        
    - O programmaticamente via SDK
        

---
## Note tecniche

### ❗️Common issues

- Problemi con `cURL` o certificati SSL
    
    - Risolti installando:
		```bash
		sudo apt-get install ca-certificates   
		```
+ Problemi con `include_path` in ambienti locali (es. MAMP)
	- Correggere via `php.ini` o impostazioni specifiche del progetto
---
## 🔒 Sicurezza

- Usa sempre connessioni HTTPS
    
- Gestisci permessi dei bucket: **accesso pubblico disabilitato di default**
    
- Abilita **Server-Side Encryption (SSE)** se necessario:
    
    - `SSE-S3`
        
    - `SSE-KMS`
---
## Da ricordare

- I nomi dei bucket devono essere univoci globalmente
    
- La creazione di bucket può richiedere tempo: usare `waitUntil('BucketExists')`
    
- Cloud = latenza: accettare tempi di risposta non deterministici