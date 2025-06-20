---
title: Implementazione WSL
aliases:
  - Implementazione WSL
tags:
  - nozioni-generali
  - implementazione-WSL
created: 2025-06-20
---
## ℹ️ Cos'è WSL e requisiti minimi

**WSL (Windows Subsystem for Linux)** è una funzionalità di Windows che consente di eseguire un ambiente **GNU/Linux** direttamente su Windows, **senza utilizzare una macchina virtuale completa né il dual boot**. È utile per sviluppatori che vogliono usare strumenti Linux restando in Windows.

WSL è particolarmente adatto a:
- sviluppo web e backend (PHP, Node.js, Python, ecc.)
- ambienti di compilazione Linux
- uso di strumenti CLI tipici di Unix

Esistono due versioni principali:
- **WSL 1**: più leggero, meno compatibile col kernel Linux
- **WSL 2**: basato su un vero kernel Linux, con compatibilità estesa e performance superiori, consigliato per la maggior parte degli utenti

### 🔧 Requisiti minimi per WSL 2

Per usare **WSL 2**, è necessario:

- **Windows 10** versione **2004** (maggio 2020) o superiore, con **Build 19041** o superiore  
  *(per verificarlo: `winver`)*
- **Virtualizzazione abilitata** nel BIOS/UEFI (Intel VT-x o AMD-V)
- **Windows 11** è pienamente compatibile con WSL 2 e già predisposto

> ⚠️ Su versioni Home di Windows, WSL 2 funziona normalmente (non serve Windows Pro).

---
## ✅ 1. Installare WSL e Ubuntu

### 1.1 Abilitare WSL

Aprire **PowerShell come amministratore** ed eseguire il comando seguente per installare WSL 2 con Ubuntu di default:

```powershell
wsl --install
```

#### ⚠️ Attenzione
>`Riavviare il sistema se richiesto.

### 1.2 Installare manualmente una distribuzione specifica
Aprire **PowerShell**, cercare una distribuzione specifica tra quelle che appaiono eseguendo questo comando:

```powershell
wsl --list --online
```

Una volta identificata la distribuzione digitare:

```powershell
wsl --install -d NOME-DISTRIBUZIONE
```

> _Una volta completata l'installazione, inserire nuovo nome utente e password._