---
title: "Php Ws1"
aliases: ["Php Ws1"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-WS1"]
created: 2025-06-28
---
## 1. Cos'è un Web Service "standard"

**Definizione W3C**:  
Un Web Service è un'applicazione software identificata da un URI, con interfacce descritte tramite XML e accessibile via protocolli Internet standard (HTTP, SMTP, FTP).

**Caratteristiche**:
- Accessibile da remoto
- Interoperabile tra piattaforme
- Basato su XML per messaggi e interfacce
- Definizione formale tramite WSDL

---

## 2. Attori principali (SOA)

- **Service Provider**: fornitore del servizio  
- **Service Requestor (Client)**: consumatore  
- **Service Registry**: punto centrale per registrare/cercare (es. UDDI)

---

## 3. Tecnologie fondamentali

### ✴ XML
Struttura i dati, usato in messaggi e descrizioni.

### ✴ SOAP (Simple Object Access Protocol)
Protocollo XML per lo scambio dati:
- `<Envelope><Header/><Body/></Envelope>`
- Supporta RPC, request-response, messaggi asincroni, attachments
- Utilizza HTTP POST con `Content-Type: text/xml`

### ✴ WSDL
Descrive il servizio in XML:
- **Types**: tipi definiti
- **Messages**: input/output
- **Port Types**: endpoint
- **Bindings**: protocolli e codifiche
- **Services**: indirizzi reali

### ✴ UDDI
Registro pubblico dei WS. Ricerca/pubblicazione.

---

## 4. SOAP: Dettagli tecnici

- XML-based, estensibile
- POST HTTP, content-type `text/xml`
- Supporta `<Fault>`, MIME attachments, header opzionali
- Due stili:
  - **RPC-style**: invocazione procedura
  - **Document-style**: invio documento XML

---

## 5. Vantaggi e svantaggi SOAP

### ✅ Vantaggi
- Standard aperto
- Interoperabilità
- Supportato ovunque
- Firewall-friendly

### ❌ Svantaggi
- Verboso (XML)
- HTTP non adatto a tutti gli scenari
- No gestione stato (stateless)
- Più lento di alternative REST

---

## 6. Estensioni e standard correlati

- **WS-Security**: firma, crittografia, autenticazione  
- **WS-Policy**: QoS e aspetti non funzionali  
- **WS-Coordination / WS-Transaction**: transazioni distribuite  
- **BPEL, WS-CDL**: composizione di WS

---

## 7. Web Services REST

- Accesso a **risorse** tramite URI
- Metodi HTTP: GET, POST, PUT, DELETE
- Dati via JSON o XML
- Nessun WSDL

### ✅ Vantaggi REST
- Semplice, leggero
- Scalabile
- Ideale per web/mobile

---

## 8. JSON

Formato leggero, leggibile, ideale per REST API.  
Esempio:
```json
{ "utente": "Mario", "email": "mario@example.com" }
```

---
## 9. Web Services in PHP

- Supporto tramite `SoapClient` / `SoapServer`

- PHP ≥8: installare `php8.x-soap`

### Esempio PHP:

```php
$requestor = new SoapClient("https://.../currencyrates151?WSDL");
$cambio = $requestor->GetRate(array("CurrencyFrom" => "EUR", "CurrencyTo" => "USD"));
echo $cambio->GetRateResponse;

```

---
## 10. Esempio reale (currency WS)

- **WSDL**: `https://ws.strikeiron.com/HouseofDev/currencyrates151?WSDL`

- Operazione: `GetRate(CurrencyFrom, CurrencyTo)`

- Restituisce il tasso di cambio tra valute

---
## 📚 Fonti e riferimenti  
Slide: `12-WS1.pdf`