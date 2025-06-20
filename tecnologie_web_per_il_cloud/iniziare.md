---
title: "Iniziare"
aliases: ["Iniziare"]
tags: [università, "tecnologie-web-per-il-cloud", "iniziare"]
created: 2025-06-19
---
# Configurare un ambiente PHP su Windows utilizzando WSL

Questa guida illustra come configurare un ambiente **PHP** completo su **Windows** tramite **WSL (Windows Subsystem for Linux),** utilizzando **Ubuntu** come distribuzione e gestendo correttamente i permessi della cartella `/var/www/html` per lo sviluppo lato server.

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
Aprire il Microsoft Store, cercare Ubuntu 22.04 LTS e installarla con il seguente comando:

```powershell
wsl --install -d Ubuntu-22.04 
```

> _Una volta completata l'installazione, inserire nuovo nome utente e password._

## 🔧 2. Configurare il sistema operativo Linux
### 2.1 Aggiornare i pacchetti di sistema
All’avvio della shell Ubuntu, aggiornare l’indice dei pacchetti e il sistema eseguendo:

```bash
sudo apt update && sudo apt upgrade
```

## 🌐 3. Installare lo stack LAMP
### 3.1 Installare Apache, PHP e MySQL
Installare il server web Apache, l’interprete PHP e il database MySQL con:

```bash
sudo apt install apache2 php libapache2-mod-php php-mysql mysql-server
```

### 3.2 Avviare Apache
Eseguire il comando:

```bash
sudo service apache2 start
```

### 3.3 Verificare il funzionamento del server
Aprire il browser su Windows e visitare:

```
http://localhost
```

> _Se tutto è configurato correttamente, dovrebbe apparire la pagina di benvenuto di Apache._

## 🛠️ 4. Gestire i permessi su /var/www/html
### Problema
La cartella `/var/www/html` è di proprietà **`root:root`**, e ciò impedisce la modifica diretta dei file senza utilizzare `sudo`.

### Obiettivo
Configurare i permessi in modo che sia possibile lavorare con i file `PHP` senza **elevare i privilegi**, mantenendo comunque l’accesso del server web.

### 4.1 Aggiungere l’utente corrente al gruppo `www-data`
Eseguire il comando:

```bash
sudo usermod -aG www-data $USER
```

> Chiudere e riaprire la shell, oppure applicare immediatamente il cambiamento con:

```bash
newgrp www-data
```

### 4.2 Modificare la proprietà della cartella
Eseguire il comando:

```bash
sudo chown -R $USER:www-data /var/www/html
```

### 4.3 Impostare i permessi corretti
Eseguire il comando:

```bash
sudo chmod -R 775 /var/www/html
```

>In questo modo, il proprietario e il gruppo www-data potranno leggere, scrivere ed eseguire, mentre gli altri utenti avranno solo permessi di lettura ed esecuzione.

### 4.4 Impostare l’ereditarietà del gruppo
Abilitare l’**inheriting** del gruppo tramite **setgid** per garantire che tutti i nuovi file creati nella directory ereditino il gruppo `www-data`:

```bash
sudo chmod g+s /var/www/html
```

