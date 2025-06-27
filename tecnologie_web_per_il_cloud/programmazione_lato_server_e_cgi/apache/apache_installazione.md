---
title: "Apache Installazione"
aliases: ["Apache Installazione"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "apache", "apache-installazione"]
created: 2025-06-21
---
# 🛠️ Installazione di Apache su Ubuntu EC2

Questa guida descrive come **installare, configurare e avviare Apache** su un’istanza **Amazon EC2 con sistema Ubuntu**, partendo da zero.

---

## 🚀 1. Attivare un'istanza EC2

1. Accedi alla console AWS.
2. Seleziona "Launch Instance".
3. Scegli un'**AMI Ubuntu** (es. Ubuntu Server 22.04 LTS).
4. Seleziona un tipo di istanza compatibile con il **Free Tier** (es. `t2.micro`).
5. Genera una nuova chiave SSH `.pem` e scaricala.
6. Avvia l’istanza e annota l’**indirizzo IP pubblico** o DNS.

---

## 🔐 2. Collegarsi all’istanza via SSH

Apri il terminale e posizionati nella directory contenente la chiave `.pem`, poi connettiti con:

```bash
ssh -i path/alla/chiave.pem ubuntu@<ip-pubblico>
```

>🔐 Assicurati che il file `.pem` abbia permessi `chmod 400` per motivi di sicurezza:
``` bash
 chmod 400 path/alla/chiave.pem
```

---

## 💻 3. Comandi base utili

|Comando|Descrizione|
|---|---|
|`pwd`|Mostra la directory corrente|
|`ls` / `ls -l`|Lista file (formato semplice/dettagli)|
|`cd`|Torna alla home|
|`cd ..`|Sale di un livello|
|`mkdir`|Crea una directory|
|`nano file`|Modifica un file (testuale)|

---

## 🌐 4. Installare Apache

Aggiorna i pacchetti e installa Apache:


```bash
`sudo apt update sudo apt install apache2`
```


Una volta installato, avvia il servizio (se non già attivo):

```bash
`sudo systemctl start apache2`
```

Verifica lo stato:

```bash
`sudo systemctl status apache2`
```

---

## 🔎 5. Testare Apache

Apri il browser e vai all’**IP pubblico** della tua istanza:

```
`http://<ip-pubblico>`
```

Dovresti vedere la **pagina di benvenuto di Apache**.

---

## 🔄 6. Abilitare Apache all’avvio

Per rendere il servizio persistente al reboot:

```bash
`sudo systemctl enable apache2`
```

---

## 📁 7. DocumentRoot (predefinita)

La directory da cui Apache serve i file è:

```
`/var/www/html`
```

Se non è già stata creata una pagina HTML di prova:

```bash
`echo "<h1>Apache funziona!</h1>" | sudo tee /var/www/html/index.html`
```

---
## 🧪 8. Verifica porte aperte

Assicurati che il gruppo di sicurezza EC2 permetta il traffico sulla porta **80** (HTTP) e/o **443** (HTTPS).

---

## 🔗 Collegamenti utili

- Torna a [`README.md`](tecnologie_web_per_il_cloud/programmazione_lato_server_e_cgi/apache/README.md)
    
- Approfondisci: [Apache Configurazione](apache_configurazione.md)


---

## 📁 Note organizzative

- Cartella: `cloud_computing/apache/`
    

---

## 📚 Fonti e riferimenti

Slide: `04-Cloud-AWS-1.pdf`  
Titoli: `Attivare un'istanza EC2`, `Shell`, `Apache`, `Installazione ed attivazione su Ubuntu`
