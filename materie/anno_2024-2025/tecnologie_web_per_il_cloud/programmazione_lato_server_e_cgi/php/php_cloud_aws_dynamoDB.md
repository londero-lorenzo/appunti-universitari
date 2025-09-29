---
title: "Php Cloud Aws Dynamodb"
aliases: ["Php Cloud Aws Dynamodb"]
tags: [università, "tecnologie-web-per-il-cloud", "programmazione-lato-server-e-cgi", "php", "php-Cloud-AWS-DynamoDB"]
created: 2025-06-28
---
## 1. 📘 Introduzione a dati e informazioni

- I **dati** sono simboli senza significato intrinseco.
- L’**informazione** è un dato interpretato (es. risponde a una domanda).
- I sistemi informativi raccolgono, archiviano e manipolano dati.

## 2. 🧱 Cos’è un database?

- È un insieme di dati organizzati e persistenti.
- Fondamentale per le organizzazioni.
- I dati cambiano poco, ma le procedure evolvono.
- I **DBMS** (Database Management System) risolvono:
  - Condivisione
  - Duplicazioni e inconsistenze
  - Sicurezza e backup

## 3. 🧠 Modelli di dati

- **Gerarchico**
- **A grafo**
- **Relazionale** (tabelle, righe = record, colonne = attributi)
- **A oggetti**
- **NoSQL** (schemaless, chiave-valore)

## 4. 🗃️ NoSQL – DynamoDB

- No schema fisso, ogni item può avere attributi diversi e multivalore.
- DynamoDB è **serverless**, altamente scalabile e adatto per grandi volumi.
- Supporta:
  - **Chiave-valore** e **document store**
  - **Query** su chiavi
  - **Scan** su tutti gli attributi

## 5. ☁️ AWS e database

- **RDS** = Relational Data Service (relazionali)
- **DynamoDB** = NoSQL, serverless, dimensioni virtualmente illimitate
- Altri: ElastiCache, Neptune, DocumentDB

## 6. ⚙️ Operazioni con DynamoDB in PHP

### 6.1 Setup client

```php
$client = new Aws\DynamoDb\DynamoDbClient([
  'region' => 'eu-south-1',
  'version' => 'latest',
  'credentials' => new Aws\Credentials\Credentials('key', 'secret')
]);
```

### 6.2 Creare una rubrica

```php

$client->createTable([

  'TableName' => 'rubrica',

  'AttributeDefinitions' => [

    ['AttributeName' => 'nome', 'AttributeType' => 'S'],

    ['AttributeName' => 'cognome', 'AttributeType' => 'S']

  ],

  'KeySchema' => [

    ['AttributeName' => 'nome', 'KeyType' => 'HASH'],

    ['AttributeName' => 'cognome', 'KeyType' => 'RANGE']

  ],

  'ProvisionedThroughput' => ['ReadCapacityUnits' => 5, 'WriteCapacityUnits' => 5]

]);

```

### 6.3 Inserire item  

```php

$item = [

  'nome' => ['S' => 'Homer'],

  'cognome' => ['S' => 'Simpson'],

  'telefono' => ['N' => '123456789']

];

$client->putItem(['TableName' => 'rubrica', 'Item' => $item]);

```

### 6.4 Query e Scan

```php

$iterator = $client->getIterator('Query', [

  'TableName' => 'rubrica',

  'KeyConditions' => [

    'nome' => [

      'AttributeValueList' => [['S' => 'Homer']],

      'ComparisonOperator' => 'EQ'

    ]

  ]

]);

```

### 6.5 Estrazione dati con scan  

```php

$lista = $client->scan(['TableName' => 'rubrica']);

foreach ($lista['Items'] as $item) {

  print_r($item);

}

```

---
## 7. 🧪 Debugging in PHP

  
```php

print_r($variabile);

var_dump($oggetto);

var_export($array);

memory_get_usage();

memory_get_peak_usage();

```

  

## 8. 🧾 Verifica costi e uso

  

- **Account activity**: mostra costi correnti.

- **Usage reports**: log dettagliati in CSV/XML con ore, byte, ecc.

  - Attenzione a separatori decimali!

  - Utilizzabili con pivot in Excel.
---
## 📚 Fonti e riferimenti  
Slide: `16-Cloud-AWS-DynamoDB.pdf`