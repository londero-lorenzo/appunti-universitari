---
title: Aws Ec2 Accesso
aliases:
  - Aws Ec2 Accesso
tags:
  - aws-ec2-accesso
created: 2025-06-21
---
## 🔐 Accesso a un’istanza EC2

### Connessione via SSH

Per accedere a un’istanza EC2:

1. **Scarica la chiave privata (.pem)** generata da AWS al momento della creazione.
2. Prendi nota dell'**IP pubblico o DNS** dell’istanza.
3. Connettiti via terminale con:

```bash
ssh -i /percorso/chiave.pem ubuntu@<ip-o-dns>
```

> L'accesso tramite username/password è possibile ma sconsigliato per motivi di sicurezza.

---

## 🔧 Comandi Linux base utili
| Comando        | Descrizione                            |
| -------------- | -------------------------------------- |
| `pwd`          | Mostra la directory corrente           |
| `ls` / `ls -l` | Lista file (formato semplice/dettagli) |
| `cd <path>`    | Cambia directory                       |
| `cd`           | Torna alla home                        |
| `cd ..`        | Sale di un livello                     |
| `mkdir`        | Crea una directory                     |
| `nano file`    | Modifica un file (editor testuale)     |

>🧠 nano: Ctrl+X per uscire, Y per salvare, Ctrl+O per salvare senza uscire

---

### 🔐 Permessi file

- `chmod a+x file` → rende il file eseguibile da tutti
    
- `chmod a+r file` → rende il file leggibile da tutti
    

---

### ⌨️ Trucchi shell utili

- Freccia ↑ → recupera comandi precedenti
    
- `Tab` → autocompleta nomi di file e comandi

---

## 📚 Approfondimenti

- [Guida SSH AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

