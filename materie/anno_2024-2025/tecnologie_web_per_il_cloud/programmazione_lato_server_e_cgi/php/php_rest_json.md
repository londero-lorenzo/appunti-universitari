---
title: "Php Rest Json"
aliases: ["Php Rest Json"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-rest-json"]
created: 2025-06-28
---
## 📌 Cos'è REST?
- **REST** = Representational State Transfer.
- Paradigma architetturale per lo sviluppo di servizi web.
- Si basa su risorse identificate tramite URI.
- Ogni risorsa è manipolabile attraverso i metodi HTTP standard:
  - `GET`: Recupera informazioni.
  - `POST`: Crea nuove risorse.
  - `PUT`: Aggiorna risorse esistenti.
  - `DELETE`: Elimina risorse.

## 🌐 Caratteristiche di un Web Service RESTful
- URI significative (es: `/ordini/123`).
- Scambio dati tramite **JSON** o **XML**.
- Nessun bisogno di WSDL.
- Richiede **documentazione esplicita**.
- Status code HTTP **semantici** (es. `201 Created`, `404 Not Found`).

## 🧩 JSON: struttura e uso
- Formato leggero per lo scambio dati.
- Basato su:
  - **Oggetti** (object): coppie chiave/valore.
  - **Array**: liste ordinate di valori.
- Valori possibili: stringhe, numeri, booleani, null, oggetti, array.
- In PHP:
  ```php
  $json = json_encode($variabile);
  $variabile = json_decode($json);
  ```

## Esempio in PHP

```php
$vettore = [
  'primo' => 1,
  'secondo' => ['a', 'b', 'c'],
  'terzo' => "ultimo"
];
$json = json_encode($vettore);
echo $json;

$nuovo = json_decode($json);
var_dump($nuovo);
```

---
## Mapping risorse REST

| Metodo | URI            | Operazione            |
| ------ | -------------- | --------------------- |
| GET    | `/cliente/123` | Legge un cliente      |
| POST   | `/cliente/`    | Crea un nuovo cliente |
| PUT    | `/cliente/123` | Aggiorna cliente 123  |
| DELETE | `/cliente/123` | Cancella cliente 123  |

---
## Parsing manuale per PUT/DELETE

```php
if ($_SERVER['REQUEST_METHOD'] == 'PUT') {
  parse_str(file_get_contents('php://input'), $_PUT);
}
```

---
## Test delle richieste REST

- Tramite `curl`:
``` bash
curl -X PUT http://localhost/cliente/123 -d "nome=Mario"
```
+ Servizi online: [https://testuri.org](https://testuri.org), Postman.
---

## Rewrite URL in Apache

+ Abilitazione:
```bash
sudo a2enmod rewrite
```
+ Regole in .htaccess:
```apacheconf
RewriteEngine on
RewriteRule ^cliente/(\w*)$ /azienda/service.php?res=cliente&id=$1 [L]
```
---
## 🔐 Sicurezza e Best Practices

- Usare **HTTPS** per ogni endpoint.

- Autenticazione: Basic, Token (JWT), OAuth2.

- Validare l'input server-side.

- Limitare metodi HTTP abilitati.

- Gestire correttamente gli status code:
	- `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `500 Internal Server Error`.
---
## 📦 Versionamento API

- Versioni esplicite negli URI:  
    `/api/v1/clienti`
    
- Oppure tramite header custom:
```bash
Accept: application/vnd.azienda.v1+json
```
---
## Documentazione automatica

- **OpenAPI / Swagger**:
    
    - Specifica standard per documentare e testare API REST.
    
    - Link utile: [https://swagger.io](https://swagger.io)
---
## 🔧 Framework REST consigliati per PHP

- [Slim Framework](https://www.slimframework.com/)
    
- Laravel (include RESTful routing avanzato)
    
- Symfony
---
## Conclusione

Un'API REST ben progettata:

- È leggibile e intuitiva.
    
- Usa i metodi HTTP in modo semantico.
    
- Fornisce risposte coerenti con il protocollo.
    
- Può essere facilmente documentata, testata e consumata da vari client.
---
## 📚 Fonti e riferimenti  
Slide: `13-REST-JSON.pdf`
