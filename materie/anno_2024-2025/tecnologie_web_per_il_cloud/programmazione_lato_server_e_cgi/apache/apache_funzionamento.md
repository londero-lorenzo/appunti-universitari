---
title: "Apache Funzionamento"
aliases: ["Apache Funzionamento"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "apache", "apache-funzionamento"]
created: 2025-06-21
---
# ⚙️ Funzionamento di Apache HTTP Server

Apache è un server web modulare, multipiattaforma e altamente configurabile. Questa guida descrive **come funziona internamente**, la struttura dei processi, le **porte utilizzate**, la gestione tramite moduli e i principali file coinvolti.

---

## 🔄 Fasi di elaborazione di una richiesta HTTP

Quando un client invia una richiesta HTTP, Apache:

1. **Traduce l’URI** in un percorso file del filesystem.
2. **Verifica l’identità** dell’utente (autenticazione base/digitale).
3. **Controlla i privilegi di accesso** (file `.htaccess`, regole Directory).
4. **Determina il tipo MIME** della risorsa.
5. Esegue eventuali **"fixups"** e azioni aggiuntive (moduli speciali).
6. **Invia la risposta** al client.
7. **Registra l’evento** nei log (accessi, errori, ecc.).

---

## 🧩 Struttura modulare

Apache è **interamente basato su moduli**, ognuno dei quali gestisce una fase o estende le funzionalità.

- ✳️ Moduli "core": compilati con Apache, es. `mod_auth`, `mod_dir`, `mod_mime`
- 🧩 Moduli esterni: es. `mod_php`, `mod_ssl`, `mod_cgi`
- ⚙️ Moduli personalizzati: puoi sviluppare i tuoi

La configurazione dei moduli si trova in:

```
/etc/apache2/mods-available/  
/etc/apache2/mods-enabled/
```


Abilitazione/disabilitazione tramite:

```bash
sudo a2enmod nome_modulo
sudo a2dismod nome_modulo
```

---

## 🧠 Architettura a processi

Apache funziona come **processo padre + figli**:

- Il processo padre:
    - legge i file di configurazione
        
    - apre le porte (es. 80, 443)
        
    - avvia i processi figli
    
- I **figli gestiscono le connessioni** dei client.
    - Eseguono come utente Apache (`www-data`, `apache`…)


Configurazione dei processi (`mpm_prefork`, `mpm_worker`):

```apache

MinSpareServers 5
MaxSpareServers 20
StartServers 8
MaxClients 150
MaxRequestsPerChild 100

```

> 🔁 Apache può riutilizzare le connessioni (HTTP/1.1) → parametri `KeepAlive`, `Timeout`, ecc.

---

## 🌐 Porte usate

|Porta|Scopo|Note|
|---|---|---|
|80|HTTP (non cifrato)|default per contenuti pubblici|
|443|HTTPS (SSL/TLS)|richiede configurazione SSL|
|8080|Alternativa a 80|spesso usata in sviluppo|
|8000|Alternativa per test|simile a 8080|

> ⚠️ Se Apache ascolta porte <1024, deve essere avviato da **utente root**.


---

## 📂 Directory e file importanti

|Percorso|Contenuto|
|---|---|
|`/etc/apache2/`|Radice di configurazione|
|`apache2.conf`|File principale di configurazione|
|`sites-enabled/`|Siti attivi|
|`mods-enabled/`|Moduli attivi|
|`/var/www/html/`|DocumentRoot di default (contenuti visibili via browser)|
|`/var/log/apache2/`|Log di accesso e errori|

> 📝 I file di configurazione sono modulari e includono le directory `conf-enabled/`, `mods-enabled/`, ecc.


---

## 🔐 Privilegi dei file serviti

Perché Apache possa **servire correttamente i file**, devono valere:

- I file devono essere leggibili dall’utente `www-data`
    
- Le directory devono essere **attraversabili** (eseguibili) da `www-data`
    
- Le pagine utente (`~/public_html`) richiedono:
    
    - directory utente + `public_html`: eseguibili da tutti
        
    - file HTML leggibili da tutti
        

Esempio:


```bash
chmod a+x ~/public_html
chmod a+r ~/public_html/index.html
```

---

## 🔗 Collegamenti utili

- Torna a [Installazione Apache](apache_installazione.md)
    
- Prosegui con [Configurazione Apache](apache_configurazione.md)
    
- Documentazione ufficiale: [https://httpd.apache.org/docs/](https://httpd.apache.org/docs/)
    

---

## 📁 Note organizzative

- Cartella: `cloud_computing/apache/`
    

---

## 📚 Fonti e riferimenti

Slide: `04-Cloud-AWS-1.pdf`  
Titoli: `Il server Web Apache`, `Attività di Apache`, `I moduli`, `File importanti`, `Radice dei documenti`, `Esecuzione di Apache`, `Configurazione processi`, `Privilegi`

