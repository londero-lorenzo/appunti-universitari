---
title: Cookie
aliases:
  - Cookie
tags:
  - programmazione-lato-server-e-cgi
  - cookie
created: 2025-06-20
---
# 🍪 Cookie nel contesto della programmazione lato server

I **cookie** sono piccoli frammenti di dati che un server può chiedere al browser di **memorizzare localmente sul client**, per poi recuperarli in richieste future.  
Sono utilizzati per **mantenere lo stato** in applicazioni web, dove ogni richiesta HTTP è di per sé indipendente (stateless).

---

## 🗂️ A cosa servono i cookie

- ✳️ **Mantenere lo stato** tra diverse visite o pagine (es. login)
- 🛒 **Gestire sessioni utente** (es. contenuto del carrello)
- 👁️ **Tracciare il comportamento dell’utente** per finalità analitiche o pubblicitarie
- 🎯 **Personalizzare il contenuto** (es. preferenze lingua)

---

## ⚙️ Come funzionano

1. Il **server** invia un cookie tramite una **intestazione HTTP** nella risposta (header `Set-Cookie`)
2. Il **browser** lo salva localmente (in RAM o su disco)
3. A ogni richiesta successiva verso lo stesso dominio, il **browser invia il cookie** al server (header `Cookie`)

---

### 📥 Esempio: intestazione di risposta HTTP che imposta un cookie

```
Set-Cookie: SESSIONID=126763902; Path=/; Domain=.esempio.it; Expires=Wed, 13-Mar-2022 09:02:04 GMT
```


---

## 🧾 Struttura di un cookie

Un cookie è definito da:

| Attributo | Significato |
|----------|-------------|
| **Domain** | Il dominio per cui il cookie è valido |
| **Path** | La porzione di URL dove il cookie è attivo |
| **Expires** | Data di scadenza (oppure sessione browser) |
| **Name** | Il nome della variabile |
| **Value** | Il valore memorizzato |

---

### 📄 Esempio in formato XML

```xml
<dict>
  <key>Domain</key>
  <string>.blablabla.it</string>
  <key>Path</key>
  <string>/</string>
  <key>Expires</key>
  <date>2022-03-13T09:02:04Z</date>
  <key>Name</key>
  <string>SESSIONID</string>
  <key>Value</key>
  <string>126763902</string>
</dict>
```

---


## 🧠 Considerazioni

- I cookie **agiscono come variabili residenti sul client**, ma sono accessibili anche dal server
    
- Un cookie può essere **impostato da un programma lato server** come PHP, Node.js, ecc.
    
- I cookie sono una **base tecnica per gestire le sessioni** (vedi anche `PHPSESSID`)

---

## ⚠️ Limiti e privacy

- I cookie possono contenere solo **stringhe brevi** (pochi KB)
    
- Possono essere **bloccati** o **limitati** dai browser moderni
    
- Vengono spesso usati per **tracciamento** (es. Google Analytics, pubblicità)

---

## 🛠️ Esempio in PHP


```php
// Impostare un cookie valido per 1 ora
setcookie("utente", "lisa", time() + 3600, "/"); 

// Leggere il cookie 
echo $_COOKIE['utente'];
```

---

>📎 Approfondimento consigliato: [limiti_lato_server](./limiti_lato_server) per capire i problemi legati all’assenza di stato.