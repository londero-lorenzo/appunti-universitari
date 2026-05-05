---
title: "15 Gestione della Concorrenza"
aliases: ["15 Gestione della Concorrenza"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "15-gestione-della-concorrenza"]
created: 2026-05-05
---
# Controllo della concorrenza
- Unità di misura del carico applicativo del DBMS: **transazioni per secondo** (tps)
- gestore della concorrenza: 
	- passa operazioni di lettura/scrittura sotto di lui
	- riordinare le operazioni
# Anomalie delle transazioni concorrenti
- perdita di aggiornamento
- lettura sporca
- aggiornamento fantasma
- letture inconsistenti
- inserimento fantasma
>[!example]
>$t\_{1}:r(x),x:=x+1,w(x)$
>$t\_{2}:r(x),x:=x+1,w(x)$
>Prendo il valore di x dal disco e lo scopo della transazione $t\_{1}$ è quella di aumentare il valore di x di 1
>$t\_{2}$ legge x e aumenta di uno il valore di x

## Perdita di aggiornamento

| Transizione 1                 | Transizione 2                                         |
| ----------------------------- | ----------------------------------------------------- |
| bot<br>$r\_{1}(x)$<br>$x:=x+1$ |                                                       |
|                               | bot<br>$r\_{2}(x)$<br>$x:=x+1$<br>$w\_{2}(x)$<br>commit |
| $w\_{1}(x)$<br>commit          |                                                       |
>[!example]
>- se x = 2
>- parte $t\_{1}$ e legge x = 2
>- parte $t\_{2}$ e legge x = 2
>	- aumenta x = 3
>	- committa
>- poi continua $t\_{1}$ con x = 3
>- commita
>- quindi alla fine x = 3 ma dovrebbe essere = 4

- una scrittura viene persa 

## Lettura sporca
| Transizione 1                               | Transizione 2                                         |
| ------------------------------------------- | ----------------------------------------------------- |
| bot<br>$r\_{1}(x)$<br>$x:=x+1$<br>$w\_{1}(x)$ |                                                       |
|                                             | bot<br>$r\_{2}(x)$<br>$x:=x+1$<br>$w\_{2}(x)$<br>commit |
| abort                                       |                                                       |
- nel momento in cui faccio un abort le operazioni di $t\_1$ devono essere cancellate
- torniamo allo stato precedente x = 2
## Aggiornamento fantasma
| Transizione 1                                                 | Transizione 2                                                                               |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| bot<br>$s:=0$<br>$r\_{1}(x); r\_{1}(y)$<br>$s:=s+x$<br>$s:=s+y$ |                                                                                             |
|                                                               | bot<br>$r\_{2}(z);z:=z+10000$<br>$r\_{2}(y);y:=y-10000$<br>$w\_{2}(y)$<br>$w\_{2}(z)$<br>commit |
| $r\_{1}(z)$<br>$s:=s+z$<br>commit                              |                                                                                             |
## Letture inconsistenti
- Quando una transazione esegue solo operazioni di lettura
- ripete più e più volte in istanti successivi la lettura dello stesso dato
>[!tip] Una transazione che accede due o più volte alla base di dati deve trovare lo stesso valore per ciascun dato letto e non risenta dell'effetto di altre transazioni

| Transizione 1        | Transizione 2                                         |
| -------------------- | ----------------------------------------------------- |
| bot<br>$r\_{1}(x)$    |                                                       |
|                      | bot<br>$r\_{2}(x)$<br>$x:=x+1$<br>$w\_{2}(x)$<br>commit |
| $r\_{1}(x)$<br>commit |                                                       |
## Inserimento fantasma
Questa anomalia si chiama spesso **lettura fantasma** (_phantom read_).

L’idea è questa: una transazione non sta leggendo una singola riga precisa, ma sta leggendo **un insieme di righe scelte tramite un predicato**.

Per esempio:

> Calcola il voto medio degli studenti del secondo anno di Informatica.

Immaginiamo questa tabella:

|Studente|Anno|Corso|Voto|
|---|--:|---|--:|
|Anna|2|Informatica|28|
|Luca|2|Informatica|24|
|Marco|1|Informatica|30|

La transazione `T1` fa:

```sql
SELECT AVG(voto)
FROM studenti
WHERE anno = 2 AND corso = 'Informatica';
```

Il risultato è:

```text
(28 + 24) / 2 = 26
```

Quindi `T1` ottiene **26**.

Ora, mentre `T1` è ancora in corso, un’altra transazione `T2` inserisce un nuovo studente che soddisfa lo stesso predicato:

```sql
INSERT INTO studenti VALUES ('Giulia', 2, 'Informatica', 18);
COMMIT;
```

Adesso la tabella contiene:

|Studente|Anno|Corso|Voto|
|---|--:|---|--:|
|Anna|2|Informatica|28|
|Luca|2|Informatica|24|
|Marco|1|Informatica|30|
|Giulia|2|Informatica|18|

Se `T1` ripete la stessa query:

```sql
SELECT AVG(voto)
FROM studenti
WHERE anno = 2 AND corso = 'Informatica';
```

ottiene:

```text
(28 + 24 + 18) / 3 = 23.33
```

Quindi nella **stessa transazione** `T1`:

- la prima lettura restituisce **26**;
    
- la seconda lettura restituisce **23.33**.
    

Il problema non è che una riga già letta è stata modificata. Il problema è che è comparsa una **nuova riga** che prima non esisteva e che ora soddisfa il predicato:

```sql
WHERE anno = 2 AND corso = 'Informatica'
```

Per questo si dice che non basta bloccare solo i dati già presenti. Infatti, quando `T1` ha fatto la prima lettura, la riga di Giulia non esisteva ancora. Quindi non poteva essere bloccata come riga specifica.

Bisognerebbe invece impedire anche l’inserimento di nuove righe che rientrano in quel predicato. In altre parole, bisognerebbe proteggere non solo le tuple esistenti, ma anche “l’intervallo logico” o “l’insieme potenziale” di righe che soddisfano quella condizione.

In sintesi:

```text
T1 legge: studenti del secondo anno di Informatica → media = 26

T2 inserisce: Giulia, secondo anno, Informatica, voto 18

T1 rilegge: studenti del secondo anno di Informatica → media = 23.33
```

La nuova riga è il **fantasma**, perché appare tra una lettura e l’altra e cambia il risultato dell’aggregazione.

## Formalizzazione della nozione di transizione
### Definizione formale di transazione

Nella teoria del controllo della concorrenza, una **transazione** viene vista in modo semplificato.

Si considerano solo le operazioni di:

- **lettura**;
    
- **scrittura**.
    

Di solito, nella definizione formale si ignorano:

- l’istruzione iniziale `begin transaction`;
    
- l’istruzione finale `end transaction`;
    
- l’esito finale della transazione, cioè `commit` oppure `abort`.
    

A volte si assume anche che una transazione non legga o scriva più volte lo stesso dato.

---

### Definizione

Una **transazione** è una sequenza di azioni di lettura e scrittura.

Le azioni vengono indicate così:

- $r\_i(x)$ indica che la transazione $t\_i$ legge il dato $x$;
    
- $w\_i(x)$ indica che la transazione $t\_i$ scrive il dato $x$.
    

L’indice $i$ serve a identificare la transazione.

Per esempio:

- $r\_1(x)$ significa: la transazione $t\_1$ legge $x$;
    
- $w\_1(y)$ significa: la transazione $t\_1$ scrive $y$.
    

---

### Osservazione importante

In questa rappresentazione non si guarda al contenuto interno della transazione.

Non interessa sapere, ad esempio, se la transazione sta facendo una somma, una media, un aggiornamento di saldo o altro.

Dal punto di vista del controllo della concorrenza, interessa solo sapere:

1. quali dati vengono letti;
    
2. quali dati vengono scritti;
    
3. in quale ordine avvengono queste operazioni.
    

Quindi una transazione viene trattata come un oggetto sintattico formato solo da letture e scritture.

---

### Esempio

Consideriamo la transazione $t\_1$:

$$  
r\_1(x)\ r\_1(y)\ w\_1(x)\ w\_1(y)  
$$

Questa transazione fa, nell’ordine:

1. legge il dato $x$;
    
2. legge il dato $y$;
    
3. scrive il dato $x$;
    
4. scrive il dato $y$.
    

Quindi possiamo dire che $t\_1$ è una sequenza di azioni di lettura e scrittura sui dati $x$ e $y$.
# Nozione di schedule
**Modello interleaving**: transizioni eseguite in modo concorrente

**Schedule:** sequenza di operazioni di ingresso/uscita relative ad un dato insieme di transazioni concorrenti.

>[!example]
>$S\_{1]:r\_{1}(x)r\_{2}(z)w\_{1}(x)w\_{2}(z)$

- Controllo della concorrenza eseguito dallo **scheduler**
	- tiene traccia di tutte le operazioni eseguite dalle transazioni
	- decide se accettare o rifiutarle

## Schedule seriale
- individuare opportune condizioni da imporre agli schedule per garantire che l'esecuzione delle corrispondenti transazioni sia corretta
- schedule S si dice **seriale** se per ogni transazione $t$, tutte le azioni di $t$ compaiono in S in sequenza, senza essere inframezzate da azioni di altre transazioni

>[!example] Schedule seriale $S\_{2}$ in cui le transazioni $t\_{0},t\_{1},t\_{2}$ vengono eseguite in sequenza:
>$S\_{2} : r\_{0}(x) r\_{0}(y) w\_{0}(x) r\_{1}(y) r\_{1}(x) w\_{1}(y) r\_{2}(x) r\_{2}(y) r\_{2}(z) w\_{2}(z)$

## Schedule serializzabile
>[!definition] 
>Serializzabile
>>L'esecuzione di uno schedule $S\_i$ è corretta quando produce lo stesso risultato prodotto da un qualunque schedule seriale $S\_j$ delle stesse transazioni.

## Cosa vuol dire produrre lo stesso risultato ?
### Equivalenza di vista
- si basa su:
	- relazione legge
	- scritture finali

#### Relazione legge
un’operazione di lettura $r\_{i}(x)$ legge da un’operazione di scrittura
$w\_{j}(x)$ (legge($r\_{i}(x), w\_{j}(x)$)) se e solo se 
- $w\_{j}(x)$ precede $r\_{i}(x)$
- non vi è alcun $w\_{k}(x)$ compreso tra $w\_{j}(x)$ e $r\_{i}(x)$.
#### Scritture finali
Un'operazione di scritture $w\_{i}(x)$ è una scrittura finale se è l'ultima scrittura dell'oggetto $x$ che appare nello schedule.
### Equivalenza rispetto alle viste

Due schedule $S\_i$ e $S\_j$ si dicono **equivalenti rispetto alle viste**, e si indicano con:

$$  
S\_i \approx\_V S\_j  
$$

se soddisfano entrambe le seguenti condizioni:

1. hanno la stessa **relazione legge**;
    
2. hanno le stesse **scritture finali**.
    

In altre parole, due schedule sono equivalenti rispetto alle viste se ogni transazione legge gli stessi valori e, alla fine, gli stessi oggetti vengono scritti dalle stesse transazioni.

---

### Serializzabilità rispetto alle viste

Uno schedule si dice **serializzabile rispetto alle viste** se è equivalente rispetto alle viste a uno schedule seriale.

Formalmente, uno schedule $S$ è serializzabile rispetto alle viste se esiste uno schedule seriale $S\_s$ tale che:

$$  
S \approx\_V S\_s  
$$

L’insieme degli schedule serializzabili rispetto alle viste si indica con:

$$  
VSR  
$$

Quindi:

$$  
VSR = {S \mid S \text{ è equivalente rispetto alle viste a uno schedule seriale}}  
$$
