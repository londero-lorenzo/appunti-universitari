---
title: CGI
aliases:
  - CGI
tags:
  - programmazione-lato-server-e-cgi
  - CGI
created: 2025-06-20
---
# 🧬 Common Gateway Interface (CGI)

La **CGI** (Common Gateway Interface) è stato **il primo metodo standard** per generare dinamicamente contenuti web.  
Ha segnato l’inizio della programmazione lato server, ed è ancora utile per capire il meccanismo fondamentale alla base delle richieste dinamiche.

---

## 📜 Cos'è la CGI?

- È un **protocollo** per far comunicare un **server web** (come Apache) con un **programma eseguibile**.
- Il **programma CGI** viene **eseguito per ogni richiesta**, produce una risposta dinamica e la restituisce al client.
- Apache gestisce CGI tramite il modulo `mod_cgi`.

---

## 🔗 Interazione tra server e CGI

### ✅ Funzionamento
1. Il client effettua una richiesta HTTP (es. tramite form).
2. Il server individua l’URI come una **risorsa CGI**.
3. Lancia il **programma CGI** come **nuovo processo**.
4. Il programma riceve:
	- parametri dell’utente (via `environment variables` o `stdin`)
	- metadati della richiesta
5. Il programma **genera l'intera risposta HTTP** e la scrive su `stdout`.
6. Il server inoltra la risposta al client.

---

## 📂 Dove si trovano i programmi CGI?

Per motivi di sicurezza, Apache li esegue **solo in percorsi specifici** come:

```bash
/var/www/cgi-bin/
```

- È una directory **predefinita e protetta**
    
- Solo file eseguibili (es. script Perl o Bash)
    
- Il client **non può scaricare il file** CGI, può solo attivarlo

---

## 📥 Input al programma CGI

### 🔸 Metodo GET

- I parametri sono inclusi nell’URI (es. `?nome=Anna`)
    
- Accessibili tramite la **variabile d’ambiente** `QUERY_STRING`


### 🔸 Metodo POST

- I dati sono nel corpo della richiesta
    
- Il server scrive i dati su **`stdin`**
    
- La lunghezza è disponibile in `CONTENT_LENGTH`
    
- Il tipo MIME (**Multipurpose Internet Mail Extensions**) è indicato in `CONTENT_TYPE`:
	- _MIME si riferisce al tipo di contenuto della risposta HTTP generata dal programma CGI_


### 🧪 Altre variabili d’ambiente

| Variabile        | Significato                    |
| ---------------- | ------------------------------ |
| `PATH_INFO`      | URI richiesto                  |
| `CONTENT_TYPE`   | MIME type dei dati POST        |
| `CONTENT_LENGTH` | Lunghezza della richiesta POST |
| `REMOTE_ADDR`    | IP del client                  |
| `QUERY_STRING`   | Parametri passati via GET      |

---

## 📤 Output del programma CGI

Il CGI **scrive su stdout** la risposta da inviare al client, che deve essere **una risposta HTTP valida**, ad esempio:

```html
`Content-type: text/html

<html>
	<body>
		<p>Hello, world!</p>
	</body>
</html>`
```

---

## 🧪 Esempio minimo in Perl

```perl
#!/usr/bin/perl
print "Content-type: text/html\r\n\r\n";
print "<html>\n";
print "<head><title>Titolo</title></head>\n";
print "<body><p>Ciao, Plutone.</p></body>";
print "</html>";
```

Salvato in `/var/www/cgi-bin/ciao.pl` e reso eseguibile:

```bash
`chmod +x ciao.pl`
```

---

## 📄 Esempio di form HTML che invoca uno script CGI

```html
<form method="post" action="/cgi-bin/registro.pl">
  Nome: <input type="text" name="nome"><br>
  Cognome: <input type="text" name="cognome"><br>
  Email: <input type="text" name="email"><br>
  <input type="submit" value="Invia">
</form>
```



---

## 🧰 Script Perl per ricevere e salvare i dati (semplificato)

```perl
#!/usr/bin/perl
use URI::Escape;

# Recupera i dati (GET o POST)
my $params = '';
if ($ENV{'REQUEST_METHOD'} eq 'POST') {
    read(STDIN, $params, $ENV{'CONTENT_LENGTH'});
} else {
    $params = $ENV{'QUERY_STRING'};
}

# Parsing parametri
my %FORM;
foreach my $coppia (split(/&/, $params)) {
    my ($k, $v) = split(/=/, $coppia);
    $FORM{$k} = uri_unescape($v);
}

# Salva su file
if ($FORM{'nome'} && $FORM{'cognome'} && $FORM{'email'}) {
    open(FILE, ">>visitatori.txt");
    print FILE "Nome: $FORM{'nome'}\n";
    print FILE "Cognome: $FORM{'cognome'}\n";
    print FILE "Email: $FORM{'email'}\n";
    print FILE "*****\n";
    close(FILE);
}

# Risposta HTML
print "Content-type: text/html\r\n\r\n";
print "<html><body><h2>Dati registrati</h2>";
print "<p>Nome: $FORM{'nome'}</p>";
print "<p>Cognome: $FORM{'cognome'}</p>";
print "<p>Email: $FORM{'email'}</p>";
print "</body></html>";

```

---

## 🛠️ Linguaggi supportati

Un programma CGI può essere scritto in **qualsiasi linguaggio**, purché:

- possa accedere alle **variabili d'ambiente**
    
- legga da **stdin** e scriva su **stdout**
    

### Linguaggi comuni:

- ✅ **Perl** (il più diffuso storicamente)
    
- ✅ Shell Script
    
- ✅ C
    
- ✅ Python
    
- ✅ PHP (fuori da mod_php)
    
- ✅ qualsiasi eseguibile Unix-like

---

## ⚠️ Limiti della CGI classica

|Problema|Descrizione|
|---|---|
|⚙️ 1 processo per richiesta|Costoso in termini di risorse|
|❌ Nessun riuso|Nessuna persistenza tra richieste|
|📉 Performance scarse|Poco scalabile su alto traffico|

🔁 Soluzioni moderne:

- **FastCGI**
    
- **mod_php**, **mod_wsgi**
    
- **PHP-FPM**, **Node.js**, **framework dedicati**

---

>📎 Vedi anche: [Tecniche di programmazione lato server](./tecniche.md) per il confronto tra CGI, FastCGI e altri approcci.