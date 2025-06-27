---
title: "Apache Permessi"
aliases: ["Apache Permessi"]
tags: [università, "tecnologie-web-per-il-cloud", "cloud-computing", "apache", "apache-permessi"]
created: 2025-06-21
---
# 🔐 Permessi per Apache HTTP Server

Apache è un server multiutente che gira normalmente con l’utente `www-data` (su Ubuntu). Per poter servire correttamente file e directory, è fondamentale che **i permessi siano impostati correttamente**.

---

## 📂 Directory accessibili

Affinché Apache possa leggere un file, devono essere rispettate **due condizioni**:

1. Il file deve essere **leggibile** dall’utente `www-data`
2. La directory contenente il file deve essere **attraversabile** da `www-data` (permesso `x`)

Esempio:

```bash
chmod o+x /var/www
chmod o+rx /var/www/html
chmod o+r /var/www/html/index.html
```


---

## 🧑‍💻 Esempio: configurare i permessi

Se stai servendo pagine statiche da `/var/www/html`, puoi assegnare i permessi in modo ricorsivo con:

```bash
sudo chmod -R o+rX /var/www/html
```

Questo comando:

- Aggiunge il permesso di **lettura** per altri utenti (`o+r`) sui file
    
- Aggiunge il permesso di **attraversamento** (`+x`) solo sulle **directory**

---

## 🧠 Nota sulla sicurezza

Non è consigliabile dare permessi troppo permissivi (es. `777`) perché:

- Qualsiasi utente del sistema potrebbe modificare i file (scrittura)
    
- Compromette la sicurezza in ambienti multiutente o server esposti
    

---

## 📚 Approfondimento consigliato

Per maggiori dettagli sui permessi di file e directory in Linux, e sull’utilizzo di `chmod` (sia modalità simbolica che ottale), vedi:

📄 `nozioni_generali/chmod.md`

---

## 📁 Note organizzative

- Cartella: `cloud_computing/apache/`

---
## 📚 Fonti e riferimenti

Slide: `06-EC2-web.pdf`  
Titoli: `I permessi dei file`, `Il comando chmod`, `Privilegi dei file: come?`
