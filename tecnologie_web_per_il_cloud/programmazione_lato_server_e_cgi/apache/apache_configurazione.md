---
title: "Apache Configurazione"
aliases: ["Apache Configurazione"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "apache", "apache-configurazione"]
created: 2025-06-21
---
# 🛠️ Configurazione di Apache HTTP Server

In questo file vediamo **dove e come configurare Apache**, con particolare attenzione alla distribuzione tipica su Ubuntu/Linux.

---

## 📂 File e directory principali

| Percorso                        | Descrizione                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| `/etc/apache2/`                | Radice della configurazione di Apache                                       |
| `/etc/apache2/apache2.conf`    | File principale di configurazione                                           |
| `/etc/apache2/ports.conf`      | Definizione delle porte su cui Apache ascolta                              |
| `/etc/apache2/sites-available/`| Configurazioni dei virtual host disponibili                                 |
| `/etc/apache2/sites-enabled/`  | Configurazioni dei virtual host attivi (link simbolici da `sites-available`)|
| `/etc/apache2/mods-available/` | Moduli disponibili                                                          |
| `/etc/apache2/mods-enabled/`   | Moduli attivi (link simbolici da `mods-available`)                          |
| `/var/www/html/`               | DocumentRoot predefinita (contenuti serviti su http://localhost/)          |

---

## 🔌 Attivare/disattivare moduli e siti

### Moduli

Apache usa script semplificati per attivare/disattivare moduli:

```bash
sudo a2enmod nome_modulo   # abilita
sudo a2dismod nome_modulo  # disabilita
```

Esempio:

```bash
sudo a2enmod rewrite
sudo systemctl restart apache2
```

---

### Siti (Virtual Host)

Apache gestisce **virtual host** tramite file `.conf` dentro `sites-available/`.

Per attivare/disattivare un sito:

```bash
sudo a2ensite nome_sito.conf
sudo a2dissite nome_sito.conf
```

Poi riavvia:

```bash
sudo systemctl reload apache2
```


---

## 🌐 Configurare le porte

Modifica il file `/etc/apache2/ports.conf` per specificare su quali porte ascoltare:

```apache
Listen 80 Listen 8080
```

Poi, dentro i VirtualHost:

```apache
<VirtualHost *:80>
	ServerName www.miosito.com
	DocumentRoot /var/www/html
</VirtualHost>
```

---

## 🏗️ Struttura dei file di configurazione

### File principale: `apache2.conf`

Include i file modulari:

```apache

IncludeOptional mods-enabled/*.load
IncludeOptional mods-enabled/*.conf

IncludeOptional sites-enabled/*.conf

```
### Struttura consigliata (Ubuntu)

- Le configurazioni modulari sono **divise per cartelle**:
    
    - `mods-enabled/` per i moduli attivi
        
    - `conf-enabled/` per altri file `.conf`
        
    - `sites-enabled/` per i siti attivi
        

Questa struttura rende Apache più **manutenibile** e consente attivazione dinamica.

---

## 🧾 Esempio semplice di VirtualHost

```apache
<VirtualHost *:80>
    ServerAdmin webmaster@example.com
    ServerName example.com
    DocumentRoot /var/www/example

    ErrorLog ${APACHE_LOG_DIR}/example_error.log
    CustomLog ${APACHE_LOG_DIR}/example_access.log combined
</VirtualHost>
```


---

## 🔐 Permessi e sicurezza

- I file serviti da Apache devono avere **permessi di lettura** per l’utente `www-data`.
    
- Le directory devono essere **attraversabili** (`x`) dallo stesso utente.
    

Esempio:

```bash
`chmod -R o+rX /var/www/html`
```

## 🔄 Riavvio e test della configurazione

Per applicare modifiche:

```bash
`sudo systemctl restart apache2`
```

Per verificare la correttezza della configurazione:

```bash
`apachectl configtest # o sudo apache2ctl configtest`
```

Output previsto:

```text
`Syntax OK`
```

---

## 🔗 Collegamenti utili

- Torna a `apache_installazione.md`
    
- Prosegui con `apache_funzionamento.md`
    
- Documentazione ufficiale: [https://httpd.apache.org/docs/](https://httpd.apache.org/docs/)
    

---

## 📁 Note organizzative

- Cartella: `cloud_computing/apache/`
    

---

## 📚 Fonti e riferimenti

Slide: `04-Cloud-AWS-1.pdf`  
Titoli: `Configurazione processi`, `File importanti`, `Radice`, `Apache 2.0`, `Tipici contenuti`
