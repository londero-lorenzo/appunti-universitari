---
title: Aws Ec2 Ami
aliases:
  - Aws Ec2 Ami
tags:
  - aws-ec2-ami
created: 2025-06-21
---
## 🧱 Cos’è un’AMI (Amazon Machine Image)

Un'**AMI (Amazon Machine Image)** è un'immagine che contiene **tutto il necessario per avviare un'istanza EC2**, ovvero:

- Un **sistema operativo** (es. Linux, Windows)
- Software opzionale preinstallato (es. web server, database, ambienti runtime)
- Configurazioni di sistema e permessi

### 📦 Cosa include una AMI?

- Root volume EBS (con OS + software)
- Dati di configurazione (es. utenti, pacchetti, script di bootstrap)
- Permessi di accesso (può essere pubblica, privata o condivisa)
- Eventualmente **volumi aggiuntivi**

### 🔄 Relazione tra AMI e istanza

- Quando avvii una nuova **istanza EC2**, essa è una **copia eseguibile** di un'AMI.
- Puoi creare un’AMI personalizzata a partire da un’istanza già configurata:
  - Utile per **replicare ambienti** o fare backup completi.

---

> 🧠 Le AMI sono simili ai **template di macchine virtuali** in ambienti tradizionali, ma pensate per un uso cloud scalabile e automatizzato.

---

## 📦 Che AMI scegliere?

Un'AMI (Amazon Machine Image) rappresenta l'immagine di partenza da cui viene creata l’istanza EC2. Contiene:

- Un sistema operativo
- Eventuale software preinstallato (es. Apache, PHP, MySQL)
- Configurazioni di default

### 🔍 Come scegliere l'AMI giusta?

Dipende principalmente dal **software che si vuole usare fin dall’inizio**:

- Se serve **piena personalizzazione**, si può partire da un'AMI minimale e installare tutto manualmente.
- Se si desidera un ambiente già pronto (es. LAMP stack, Node.js, Python), conviene scegliere un’AMI preconfigurata.

### 🧱 Tipologie di AMI disponibili

| Tipo           | Caratteristiche |
|----------------|-----------------|
| **Amazon Linux** | AMI ufficiale AWS, leggera, sicura e ottimizzata per EC2. **Molto minimale** (es. manca persino Apache). |
| **Ubuntu**        | Popolare per ambienti di sviluppo. Ottimo supporto della community. |
| **Red Hat / CentOS / SUSE** | Scelte enterprise, spesso a pagamento. |
| **Community AMI** | Immagini pubblicate da utenti o organizzazioni esterne (⚠️ attenzione alla sicurezza). |
| **Marketplace AMI** | Immagini a pagamento con software commerciale incluso (es. SAP, Tableau, Windows Server + SQL). |

### 🆓 Free Tier e scelte consigliate

Nel contesto didattico o di test, si consiglia:

- **Ubuntu Linux** su istanza `t2.micro` o `t3.micro`  
  → entrambe gratuite nel **Free Tier AWS**

🔗 [Free Tier EC2 – AWS](https://aws.amazon.com/it/free/)

---

> 🧠 Nota: anche se l’AMI è solo il punto di partenza, si può sempre **configurare l’istanza manualmente** dopo il lancio (via SSH o script di bootstrap).


