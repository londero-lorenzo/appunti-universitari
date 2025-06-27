---
title: "Chmod"
aliases: ["Chmod"]
tags: [università, "nozioni-generali", "linux", "chmod"]
created: 2025-06-21
---
# 🧾 Permessi in Linux e comando `chmod`

Linux è un sistema multiutente: ogni file e directory ha **permessi** che ne determinano l’accesso, suddivisi tra:

- **Owner** (utente proprietario)
- **Group** (gruppo associato)
- **Others** (tutti gli altri, anche detti "world")

---

## 🔍 Visualizzare i permessi

Il comando `ls -l` mostra i permessi:

```bash
ls -l /etc/passwd
-rw-r--r-- 1 root root 981 Sep 20 16:32 /etc/passwd
```

Significato:

```
-|---|---|---|
 | u | g | o
d|rw-|r--|r--

```

- `d` = directory (cartella)
	
- `r` = read (lettura)
    
- `w` = write (scrittura)
    
- `x` = execute (esecuzione/attraversamento directory)
    
- `-` = permesso assente


---

## 🔄 Il comando `chmod`

`chmod` cambia i permessi di un file o directory.

### 🔢 Modalità ottale

Ogni gruppo di permessi (rwx) viene tradotto in binario e poi in ottale:

- `rwx` = 111 = `7`
    
- `rw-` = 110 = `6`
    
- `r--` = 100 = `4`
    

Esempio:

```bash
chmod 744 f1  # rwxr--r--
```

### 📝 Modalità simbolica

Più leggibile:

```bash
chmod u=rwx,go=r f1  # owner = rwx, group & others = r
```

Operatori:

- `+` → aggiunge permessi
    
- `-` → rimuove
    
- `=` → imposta esattamente
    

Esempio:

```bash
chmod g+r f1      # aggiunge lettura al gruppo
chmod g=r f1      # imposta solo lettura al gruppo (toglie eventuali altri)
```


---

## 📂 Esempio completo


```bash
cd /var/www
chmod -R a+rX html
cd html
nano index.html
```

Significato:

- Tutti (`a`) possono leggere e attraversare (`+rX`) le directory e i file
    
- `nano` apre il file per la modifica

---

## ❗ Permesso di esecuzione sulle directory

Per “entrare” in una directory (usare `cd`, o accedere a un file in essa), serve il **permesso di esecuzione `x`** sulla directory.

---

## 🔗 Collegamenti utili

- Esempio pratico di permessi in un web server: `apache_permessi.md`
    

---

## 📁 Note organizzative

- Cartella: `nozioni_generali/`

