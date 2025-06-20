---
title: Input Utente
aliases:
  - Input Utente
tags:
  - programmazione-lato-server-e-cgi
  - input-utente
created: 2025-06-20
---
# 📝 Input dell'utente: form, GET e POST

In un'applicazione web lato server, l'input dell'utente avviene tipicamente attraverso **form HTML**.  
I dati inseriti vengono inviati al server, che può generare **risposte personalizzate** in base a tali input.

---

## 🔄 Interazione tra client e server

Il programma lato server deve poter:

- **ricevere i dati inviati dal client**, come parametri nei form,
- **generare una risorsa dinamica** da restituire al browser.

Questa interazione richiede una **interfaccia ben definita** tra:

- il **server HTTP** (es. Apache),
- e il **programma lato server** (es. script PHP o CGI).

---

## 📤 Struttura del form HTML

```html
<form action="esempio.php" method="GET">
  <input type="text" name="nome" />
  <input type="submit" value="Invia" />
</form>
```

### ➕ Risultato:

- I dati dei campi con attributo `name` vengono **passati come parametri**
    
- L'output può essere, ad esempio:  
    `esempio.php?nome=Mario` (nel caso di `GET`)

---

## 📦 Metodi di invio: GET vs POST

| Metodo   | Caratteristiche                                                           |
| -------- | ------------------------------------------------------------------------- |
| **GET**  | I parametri sono codificati nell'URL, visibili nella barra del browser    |
| **POST** | I parametri sono inclusi nel **corpo della richiesta HTTP**, non visibili |

---

## 🔍 Metodo GET

- I dati sono codificati come coppie `parametro=valore` separate da `&`
    
- L'URL ha questa forma:
	```
	`http://www.sito.it/script.php?utente=lisa&id=1`
	```
- Vantaggi:
    - Permette di **bookmarkare** o condividere la pagina
	
- Svantaggi:
    - Non adatto a dati sensibili (es. password)
        
    - Limitazioni di lunghezza dell’URL
- ⚠️ **Il metodo GET non dovrebbe mai essere usato per produrre effetti sul server!**  
	    (Es. modifiche a database o cancellazioni)

---

## 🔒 Metodo POST

- I parametri vengono trasmessi **nel corpo** della richiesta HTTP
    
- L'URL **non cambia**
    
- È preferito per:
    - invio di dati **riservati**
        
    - **form lunghi** o **upload di file**


---

## 🔁 Esempio pratico: differenza tra GET e POST

**GET:**

```html
<form action="ricerca.php" method="GET">   
	<input type="text" name="query" />
</form>`
```


**POST:**

```html
<form action="login.php" method="POST">
	<input type="text" name="username" /> 
	<input type="password" name="password" />
</form>`
```

---

## 📌 Nota tecnica

Quando un form HTML viene inviato:

- ogni input con un `name` diventa un **parametro**
    
- i dati vengono automaticamente associati ai parametri
    
- il **server web** li rende accessibili al programma lato server
    

Esempio in PHP:

```php
$nome = $_GET['nome'];   // se method="GET"
$pw   = $_POST['password']; // se method="POST"`
```

---

> 🧠 Approfondimento consigliato: [Cookie](./cookie.md) per comprendere come mantenere i dati tra richieste successive.