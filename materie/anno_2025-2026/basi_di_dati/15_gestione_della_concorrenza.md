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

# Gestione della concorrenza nei DBMS

Fonte slide: _Tecnologia di un Database Server — Gestione della concorrenza_, Angelo Montanari, Università di Udine.

---

## 1. Perché serve il controllo della concorrenza

Un DBMS deve servire contemporaneamente molte applicazioni e molti utenti.  
Il carico di lavoro di un DBMS si misura spesso in **transazioni per secondo**, abbreviato **tps**.

Esempi:

- sistemi bancari;
    
- sistemi finanziari;
    
- carte di credito;
    
- prenotazioni aeree.
    

In questi contesti è impossibile eseguire fisicamente le transazioni una alla volta.  
Per migliorare le prestazioni, il DBMS esegue le transazioni in modo **concorrente**, cioè intrecciando le loro operazioni.

Il problema è che l’esecuzione concorrente può generare risultati scorretti.

Il compito del **controllo della concorrenza** è quindi:

> permettere l’esecuzione concorrente delle transazioni, ma garantendo un risultato equivalente a una corretta esecuzione seriale.

---

## 2. Architettura del controllo della concorrenza

Nel DBMS intervengono diversi componenti:

- **gestore delle transazioni**, che riceve operazioni come `begin`, `commit`, `abort`;
    
- **gestore dei metodi d’accesso**, che richiede letture e scritture;
    
- **gestore della concorrenza**, o **scheduler**, che decide se accettare o ritardare le operazioni;
    
- **tabella dei lock**, usata per controllare quali risorse sono bloccate;
    
- **gestore della memoria secondaria**, che accede concretamente alla base di dati.
    

Nota importante:

> leggere o scrivere un dato significa, a livello fisico, leggere o scrivere il blocco o la pagina che contiene quel dato.

Quindi il controllo della concorrenza può avvenire su diversi livelli: singolo record, pagina, tabella, intera base di dati.

---

# 3. Anomalie delle transazioni concorrenti

Quando due o più transazioni vengono eseguite in modo intrecciato, possono verificarsi anomalie.

Le principali sono:

1. **perdita di aggiornamento**;
    
2. **lettura sporca**;
    
3. **aggiornamento fantasma**;
    
4. **letture inconsistenti**;
    
5. **inserimento fantasma**.
    

---

## 3.1 Perdita di aggiornamento

Si verifica quando due transazioni modificano lo stesso dato, ma una modifica sovrascrive l’altra.

Esempio:

```text
t1: r1(x), x := x + 1, w1(x)
t2: r2(x), x := x + 1, w2(x)
```

Supponiamo che `x = 10`.

Esecuzione concorrente:

```text
r1(x)      // t1 legge 10
r2(x)      // t2 legge 10
w2(x)      // t2 scrive 11
w1(x)      // t1 scrive 11
```

Risultato finale:

```text
x = 11
```

Ma il risultato corretto sarebbe:

```text
x = 12
```

perché entrambe le transazioni volevano incrementare `x`.

L’aggiornamento di `t2` viene perso perché `t1` scrive un valore calcolato a partire da una vecchia lettura.

---

## 3.2 Lettura sporca

Una **lettura sporca** si verifica quando una transazione legge un valore scritto da un’altra transazione che poi abortisce.

Esempio:

```text
t1:
r1(x)
x := x + 1
w1(x)
abort

t2:
r2(x)
x := x + 1
w2(x)
commit
```

Il problema è che `t2` ha letto un valore prodotto da `t1`, ma `t1` alla fine abortisce.

Quindi `t2` ha lavorato su un dato che non avrebbe mai dovuto esistere stabilmente nella base di dati.

---

## 3.3 Aggiornamento fantasma

L’aggiornamento fantasma si verifica quando una transazione legge un insieme di dati mentre un’altra transazione modifica parte di quell’insieme.

Esempio concettuale:

```text
t1 vuole calcolare:
s = x + y + z

t2 sposta valore da y a z:
y := y - 10000
z := z + 10000
```

Se `t1` legge `x` e `y` prima della modifica, ma legge `z` dopo la modifica, ottiene una somma inconsistente.

Il problema non è che il totale reale sia cambiato: magari `t2` ha solo spostato valore da `y` a `z`.

Il problema è che `t1` vede una base di dati “a metà”, cioè in uno stato che non corrisponde né a prima né a dopo la transazione `t2`.

---

## 3.4 Letture inconsistenti

Questa anomalia si verifica quando una transazione legge più volte lo stesso dato e ottiene valori diversi, perché nel frattempo un’altra transazione lo ha modificato.

Esempio:

```text
t1:
r1(x)
...
r1(x)

t2:
r2(x)
x := x + 1
w2(x)
commit
```

Se `t1` legge `x` prima e dopo la modifica di `t2`, allora vede due valori diversi nella stessa transazione.

Idealmente, una transazione dovrebbe avere una visione stabile della base di dati.

---

## 3.5 Inserimento fantasma

L’inserimento fantasma riguarda query basate su predicati.

Esempio:

```sql
SELECT AVG(voto)
FROM Studenti
WHERE anno = 2;
```

Se una transazione calcola questa media due volte, ma tra le due letture un’altra transazione inserisce un nuovo studente del secondo anno, la seconda media può essere diversa.

Il problema è che non basta bloccare solo le tuple già presenti: bisogna impedire anche l’inserimento di nuove tuple che soddisfano il predicato.

Per evitare questa anomalia servono i **lock di predicato**.

---

# 4. Formalizzazione delle transazioni

Dal punto di vista teorico, una transazione viene vista come una sequenza di operazioni di lettura e scrittura.

Si ignorano:

- `begin transaction`;
    
- `commit`;
    
- `abort`;
    
- calcoli interni;
    
- istruzioni SQL dettagliate.
    

Una transazione è quindi rappresentata come:

```text
t1: r1(x) r1(y) w1(x) w1(y)
```

Dove:

- `r1(x)` significa che la transazione `t1` legge l’oggetto `x`;
    
- `w1(x)` significa che la transazione `t1` scrive l’oggetto `x`.
    

L’indice identifica la transazione.

---

# 5. Schedule

Quando più transazioni vengono eseguite in modo concorrente, le loro operazioni vengono intrecciate.

Uno **schedule** è una sequenza temporale di operazioni di lettura e scrittura appartenenti a transazioni concorrenti.

Esempio:

```text
S1: r1(x) r2(z) w1(x) w2(z)
```

Significa che:

1. `t1` legge `x`;
    
2. `t2` legge `z`;
    
3. `t1` scrive `x`;
    
4. `t2` scrive `z`.
    

Lo schedule descrive quindi l’ordine effettivo delle operazioni sulla base di dati.

---

## 5.1 Commit-proiezione

Per semplificare lo studio teorico, inizialmente si assume che l’esito delle transazioni sia noto a priori.

Quindi si eliminano dallo schedule tutte le transazioni abortite.

Questa operazione prende il nome di:

```text
schedule = commit-proiezione
```

Questa semplificazione però non permette di studiare bene anomalie come la lettura sporca, perché la lettura sporca dipende proprio da dati prodotti da transazioni poi abortite.

---

# 6. Schedule seriale

Uno schedule è **seriale** se le transazioni vengono eseguite una dopo l’altra, senza intrecci.

Esempio:

```text
S2:
r0(x) r0(y) w0(x)
r1(y) r1(x) w1(y)
r2(x) r2(y) r2(z) w2(z)
```

Qui:

1. prima termina `t0`;
    
2. poi termina `t1`;
    
3. poi termina `t2`.
    

Gli schedule seriali sono considerati corretti, perché non presentano interferenze tra transazioni.

Il problema è che sono poco efficienti.

---

# 7. Schedule serializzabile

Uno schedule concorrente è considerato corretto se produce lo stesso risultato di uno schedule seriale.

Uno schedule si dice **serializzabile** se è equivalente a uno schedule seriale delle stesse transazioni.

Idea fondamentale:

> non è necessario eseguire fisicamente le transazioni una alla volta; basta che il risultato sia come se fossero state eseguite una alla volta.

Esistono diversi criteri di equivalenza, quindi esistono diversi tipi di serializzabilità.

I principali sono:

- serializzabilità rispetto alle viste;
    
- serializzabilità rispetto ai conflitti.
    

---

# 8. Equivalenza rispetto alle viste

L’equivalenza rispetto alle viste si basa su due concetti:

1. relazione **legge**;
    
2. insieme delle **scritture finali**.
    

---

## 8.1 Relazione legge

Una lettura `ri(x)` legge da una scrittura `wj(x)` se:

1. `wj(x)` precede `ri(x)`;
    
2. tra `wj(x)` e `ri(x)` non c’è nessun’altra scrittura di `x`.
    

In simboli:

```text
legge(ri(x), wj(x))
```

Esempio:

```text
w1(x) r2(x)
```

Qui `r2(x)` legge il valore scritto da `w1(x)`.

Ma nello schedule:

```text
w1(x) w3(x) r2(x)
```

`r2(x)` non legge da `w1(x)`, bensì da `w3(x)`, perché `w3(x)` è l’ultima scrittura di `x` prima della lettura.

---

## 8.2 Scritture finali

Una scrittura è finale se è l’ultima scrittura di un certo oggetto nello schedule.

Esempio:

```text
w1(x) w2(x) w3(y)
```

Le scritture finali sono:

```text
w2(x)
w3(y)
```

perché:

- `w2(x)` è l’ultima scrittura di `x`;
    
- `w3(y)` è l’ultima scrittura di `y`.
    

---

## 8.3 Equivalenza rispetto alle viste

Due schedule sono equivalenti rispetto alle viste se hanno:

1. la stessa relazione `legge`;
    
2. le stesse scritture finali.
    

Uno schedule è **view-serializable**, cioè serializzabile rispetto alle viste, se è equivalente rispetto alle viste a uno schedule seriale.

La classe degli schedule serializzabili rispetto alle viste si indica con:

```text
VSR
```

---

## 8.4 Problema della VSR

Il problema della serializzabilità rispetto alle viste è la complessità.

Verificare se due schedule specifici sono equivalenti rispetto alle viste è relativamente semplice.

Invece verificare se uno schedule è equivalente a qualche schedule seriale è molto costoso, perché bisognerebbe confrontarlo con molti possibili schedule seriali.

Questo problema è **NP-hard**.

Per questo nella pratica si usa un criterio più restrittivo, ma più semplice da verificare:

```text
serializzabilità rispetto ai conflitti
```

---

# 9. Equivalenza rispetto ai conflitti

L’equivalenza rispetto ai conflitti si basa sulla nozione di **azioni in conflitto**.

Due azioni sono in conflitto se:

1. appartengono a transazioni diverse;
    
2. operano sullo stesso oggetto;
    
3. almeno una delle due è una scrittura.
    

---

## 9.1 Tipi di conflitto

I conflitti possibili sono:

### Lettura-scrittura

```text
ri(x) wj(x)
```

Due transazioni diverse accedono allo stesso oggetto e una scrive.

### Scrittura-lettura

```text
wi(x) rj(x)
```

Una transazione scrive e l’altra legge lo stesso oggetto.

### Scrittura-scrittura

```text
wi(x) wj(x)
```

Due transazioni scrivono lo stesso oggetto.

Non c’è conflitto tra due letture:

```text
ri(x) rj(x)
```

perché leggere non modifica il dato.

---

## 9.2 Equivalenza rispetto ai conflitti

Due schedule sono equivalenti rispetto ai conflitti se:

1. contengono le stesse operazioni;
    
2. ogni coppia di operazioni in conflitto compare nello stesso ordine in entrambi gli schedule.
    

Uno schedule è **conflict-serializable** se è equivalente rispetto ai conflitti a uno schedule seriale.

La classe degli schedule serializzabili rispetto ai conflitti si indica con:

```text
CSR
```

---

# 10. Rapporto tra VSR e CSR

Vale la relazione:

```text
CSR ⊂ VSR
```

Cioè:

- ogni schedule serializzabile rispetto ai conflitti è anche serializzabile rispetto alle viste;
    
- non ogni schedule serializzabile rispetto alle viste è serializzabile rispetto ai conflitti.
    

Quindi CSR è una condizione:

- sufficiente;
    
- ma non necessaria.
    

È più restrittiva, ma più semplice da verificare.

---

# 11. Grafo dei conflitti

Per verificare se uno schedule è in CSR si costruisce il **grafo dei conflitti**.

## 11.1 Costruzione del grafo

Il grafo ha:

- un nodo per ogni transazione;
    
- un arco orientato `ti -> tj` se esiste una coppia di azioni in conflitto in cui un’azione di `ti` precede un’azione di `tj`.
    

Esempio:

```text
ri(x) wj(x)
```

genera un arco:

```text
ti -> tj
```

perché l’operazione di `ti` viene prima e confligge con quella di `tj`.

---

## 11.2 Criterio di serializzabilità

Proposizione fondamentale:

> uno schedule è in CSR se e solo se il suo grafo dei conflitti è aciclico.

Quindi:

```text
grafo aciclico  => schedule serializzabile rispetto ai conflitti
grafo ciclico   => schedule non serializzabile rispetto ai conflitti
```

Se il grafo è aciclico, l’ordinamento topologico dei nodi dà uno schedule seriale equivalente.

---

## 11.3 Metodo pratico per gli esercizi.

---

## 11.3 Metodo pratico

Per verificare se uno schedule è conflict-serializable:

1. individua le transazioni;
    
2. crea un nodo per ogni transazione;
    
3. scorri lo schedule da sinistra a destra;
    
4. per ogni coppia di operazioni su stesso oggetto e in conflitto, aggiungi un arco;
    
5. verifica se il grafo ha cicli;
    
6. se non ha cicli, trova un ordinamento topologico.
    

Esempio di risposta da esame:

```text
Il grafo dei conflitti è aciclico, quindi lo schedule appartiene a CSR.
Un possibile ordinamento seriale equivalente è t1, t3, t2.
```

Oppure:

```text
Il grafo contiene il ciclo t1 -> t2 -> t1, quindi lo schedule non appartiene a CSR.
```

---

# 12. Limiti del grafo dei conflitti

Anche se il controllo di aciclicità è lineare, nella pratica il metodo è troppo oneroso.

Motivi:

- in un sistema reale ci sono molte transazioni attive;
    
- ogni transazione accede a molte pagine;
    
- il grafo cambia continuamente;
    
- nei database distribuiti bisognerebbe ricostruire il grafo combinando archi osservati da server diversi.
    

Per questo nella pratica si usano protocolli più semplici da gestire, come il **locking a due fasi**.

---

# 13. Locking a due fasi

Il **locking** protegge le operazioni di lettura e scrittura tramite primitive di lock.

Le primitive principali sono:

```text
read lock
write lock
unlock
```

---

## 13.1 Lock condiviso

Il **read lock** è un lock condiviso.

Serve per leggere.

Più transazioni possono avere contemporaneamente un read lock sullo stesso oggetto.

Esempio:

```text
t1 legge x
t2 legge x
```

Questo è consentito, perché nessuna delle due modifica `x`.

---

## 13.2 Lock esclusivo

Il **write lock** è un lock esclusivo.

Serve per scrivere.

Se una transazione ha un write lock su `x`, nessun’altra transazione può avere né read lock né write lock su `x`.

Esempio:

```text
t1 scrive x
t2 vuole leggere x
```

`t2` deve aspettare.

---

## 13.3 Transazioni ben formate

Una transazione è ben formata se:

- ogni lettura è preceduta da un read lock;
    
- ogni scrittura è preceduta da un write lock;
    
- ogni lock viene poi rilasciato con unlock.
    

Esempio:

```text
r_lock1(x)
r1(x)
unlock1(x)
```

Oppure:

```text
w_lock1(x)
w1(x)
unlock1(x)
```

---

## 13.4 Compatibilità dei lock

La tabella base è:

|Richiesta|Risorsa libera|Risorsa in read lock|Risorsa in write lock|
|---|---|---|---|
|read lock|OK|OK|No|
|write lock|OK|No|No|
|unlock|errore|OK / dipende|OK / libera|

Interpretazione:

- una lettura può coesistere con altre letture;
    
- una scrittura non può coesistere con nessun’altra operazione;
    
- un unlock su una risorsa letta da più transazioni libera davvero la risorsa solo quando l’ultimo lettore rilascia il lock.
    

Per gestire più lettori, il DBMS usa un contatore.

---

# 14. Il protocollo 2PL

La sola compatibilità dei lock garantisce la mutua esclusione, ma non basta a garantire la serializzabilità.

Serve un vincolo aggiuntivo:

> dopo aver rilasciato un lock, una transazione non può acquisirne altri.

Questo è il protocollo **2PL**, cioè **Two-Phase Locking**.

---

## 14.1 Le due fasi del 2PL

Ogni transazione ha due fasi:

### Fase crescente

La transazione acquisisce lock.

```text
numero di lock posseduti aumenta
```

### Fase calante

La transazione rilascia lock.

```text
numero di lock posseduti diminuisce
```

Una volta iniziata la fase calante, non si può più tornare alla fase crescente.

---

## 14.2 Esempio corretto 2PL

```text
lock1(x)
lock1(y)
r1(x)
w1(y)
unlock1(x)
unlock1(y)
```

La transazione acquisisce prima tutti i lock necessari, poi li rilascia.

---

## 14.3 Esempio non corretto 2PL

```text
lock1(x)
r1(x)
unlock1(x)
lock1(y)
w1(y)
unlock1(y)
```

Non è 2PL, perché dopo aver rilasciato `x`, la transazione acquisisce un nuovo lock su `y`.

---

# 15. Rapporto tra 2PL e CSR

Vale:

```text
2PL ⊂ CSR
```

Cioè:

- ogni schedule prodotto da transazioni che rispettano 2PL è serializzabile rispetto ai conflitti;
    
- non ogni schedule in CSR può essere prodotto da 2PL.
    

Quindi 2PL è una condizione sufficiente per garantire CSR.

È però ancora più restrittivo della CSR.

---

# 16. 2PL e anomalie

Il 2PL evita:

- perdita di aggiornamento;
    
- aggiornamento fantasma;
    
- letture inconsistenti.
    

Per esempio, nell’aggiornamento fantasma, se `t1` deve leggere `x`, `y`, `z`, acquisisce i lock necessari.  
Se `t2` sta modificando `y` e `z`, `t1` viene messa in attesa finché `t2` non rilascia i lock.

In questo modo `t1` non vede una base di dati a metà.

---

# 17. Lettura sporca e 2PL stretto

Il 2PL normale non basta a evitare completamente le letture sporche se consideriamo commit e abort.

Per evitare la lettura sporca si usa il **2PL stretto**.

Regola:

> i lock di una transazione possono essere rilasciati solo dopo il commit o l’abort.

Quindi:

```text
lock
operazioni
commit / abort
unlock
```

Nel 2PL stretto, una transazione non può leggere dati scritti da un’altra transazione non ancora conclusa.

Questa è la versione usata nei sistemi commerciali.

---

# 18. Inserimento fantasma e lock di predicato

Finora i lock sono stati definiti su oggetti già presenti nella base di dati.

Ma per evitare l’inserimento fantasma non basta bloccare le tuple esistenti.

Esempio:

```sql
SELECT AVG(voto)
FROM Studenti
WHERE anno = 2;
```

Bisogna impedire che un’altra transazione inserisca una nuova tupla con:

```sql
anno = 2
```

Per questo servono i **lock di predicato**.

Un lock di predicato blocca non solo le tuple già esistenti, ma anche l’insieme logico definito da una condizione.

Nei DBMS relazionali i lock di predicato vengono realizzati:

- tramite indici;
    
- oppure, se gli indici non bastano, bloccando intere relazioni.
    

---

# 19. Controllo basato sui timestamp

Un altro metodo di controllo della concorrenza è basato sui **timestamp**.

Un timestamp è un identificatore che stabilisce un ordine temporale totale tra eventi o transazioni.

Nel metodo TS:

- ogni transazione riceve un timestamp all’inizio;
    
- lo schedule viene accettato solo se rispetta l’ordine seriale imposto dai timestamp.
    

In pratica:

> se `t1` ha timestamp minore di `t2`, il sistema vuole che l’effetto sia come se `t1` venisse prima di `t2`.

---

## 19.1 Parametri associati agli oggetti

A ogni oggetto `x` sono associati due valori:

```text
WTM(x)
RTM(x)
```

Dove:

- `WTM(x)` è il timestamp della transazione che ha eseguito l’ultima scrittura di `x`;
    
- `RTM(x)` è il massimo timestamp tra le transazioni che hanno letto `x`.
    

---

## 19.2 Regole per la lettura

Richiesta:

```text
rt(x)
```

La transazione con timestamp `t` vuole leggere `x`.

Regola:

```text
se t < WTM(x) allora la transazione viene uccisa
altrimenti la lettura è accettata
```

Se la lettura viene accettata:

```text
RTM(x) = max(RTM(x), t)
```

Significato:

> una transazione non può leggere un dato scritto da una transazione “più giovane”, cioè con timestamp maggiore.

---

## 19.3 Regole per la scrittura

Richiesta:

```text
wt(x)
```

La transazione con timestamp `t` vuole scrivere `x`.

Regola:

```text
se t < WTM(x) oppure t < RTM(x), la transazione viene uccisa
altrimenti la scrittura è accettata
```

Se la scrittura viene accettata:

```text
WTM(x) = t
```

Significato:

> una transazione non può scrivere un dato già scritto o già letto da transazioni che, secondo l’ordine dei timestamp, dovrebbero venire dopo di lei.

---

## 19.4 Esempio metodo TS

Supponiamo:

```text
RTM(x) = 7
WTM(x) = 5
```

Richieste:

```text
r6(x)   ok
r7(x)   ok
r9(x)   ok, RTM(x) diventa 9
w8(x)   no, perché 8 < RTM(x) = 9
w11(x)  ok, WTM(x) diventa 11
r10(x)  no, perché 10 < WTM(x) = 11
```

---

# 20. Limiti del metodo TS

Il metodo timestamp è semplice, ma ha diversi limiti.

Il principale è che può uccidere molte transazioni.

Nel 2PL una transazione può essere messa in attesa.  
Nel metodo TS, invece, se una richiesta viola l’ordine dei timestamp, la transazione viene abortita e riavviata.

Questo può essere costoso.

Inoltre, anche il metodo TS assume inizialmente la commit-proiezione.  
Per gestire commit e abort reali, bisogna bufferizzare le scritture e renderle definitive solo dopo il commit.

---

# 21. Varianti del metodo TS

## 21.1 Pre-write

La **pre-write** è una segnalazione anticipata dell’intenzione di scrivere.

Serve allo scheduler per ritardare letture che potrebbero causare il fallimento successivo della scrittura.

In pratica:

> invece di lasciare che una lettura venga fatta e poi uccidere una transazione, il sistema può bloccare prima alcune operazioni problematiche.

---

## 21.2 Multiversioni

Il metodo multiversione mantiene più copie dello stesso oggetto.

Quando una transazione scrive `x`, la vecchia versione non viene eliminata: viene creata una nuova versione.

Esempio:

```text
x1, x2, x3, ...
```

Ogni versione è associata al timestamp della transazione che l’ha prodotta.

Vantaggio:

> le letture non vengono mai rifiutate, perché ogni transazione può leggere la versione coerente con il proprio timestamp.

---

## 21.3 Regole con multiversione

Per una lettura:

```text
rt(x)
```

la lettura è sempre accettata.

La transazione legge la versione di `x` più recente tra quelle con timestamp minore o uguale a `t`.

Per una scrittura:

```text
wt(x)
```

la richiesta può ancora essere rifiutata se viola l’ordine rispetto alle versioni esistenti o rispetto alle letture già avvenute.

---

# 22. Relazione tra VSR, CSR, 2PL e TS

Le classi sono collegate così:

```text
VSR è la classe più generale
CSR è contenuta in VSR
2PL è contenuto in CSR
TS è contenuto in CSR
2PL e TS si intersecano, ma nessuno contiene l’altro
```

Schema concettuale:

```text
VSR
└── CSR
    ├── 2PL
    └── TS
```

Con intersezione non vuota tra 2PL e TS.

Quindi:

- esistono schedule in TS ma non in 2PL;
    
- esistono schedule in 2PL ma non in TS;
    
- esistono schedule sia in 2PL sia in TS.
    

---

# 23. Differenze tra 2PL e TS

|Aspetto|2PL|TS|
|---|---|---|
|Gestione conflitti|transazioni in attesa|transazioni uccise e riavviate|
|Ordine di serializzazione|imposto dai conflitti|imposto dai timestamp|
|Problema principale|deadlock|molti abort/restart|
|Costo tipico|attesa|rollback e riavvio|
|Uso pratico|molto usato, soprattutto 2PL stretto|usato in varianti|

In generale, i DBMS commerciali usano varianti di queste tecniche, cercando di ridurne gli svantaggi.

---

# 24. Lock manager

Il **lock manager** è il componente che gestisce le richieste di lock.

Le primitive tipiche sono:

```text
read lock(T, x, errorcode, timeout)
write lock(T, x, errorcode, timeout)
unlock(T, x)
```

Dove:

- `T` è la transazione;
    
- `x` è la risorsa;
    
- `errorcode` indica se la richiesta è riuscita;
    
- `timeout` è il tempo massimo che la transazione è disposta ad attendere.
    

---

## 24.1 Possibili situazioni

### Richiesta immediatamente accolta

La risorsa è disponibile.

Il lock manager:

1. assegna la risorsa;
    
2. aggiorna le tabelle interne;
    
3. lascia proseguire la transazione.
    

---

### Richiesta non immediatamente accolta

La risorsa è già bloccata in modo incompatibile.

Il lock manager:

1. inserisce la transazione in una coda;
    
2. sospende il processo;
    
3. concede la risorsa quando diventa disponibile.
    

---

### Scatto del timeout

Se la transazione aspetta troppo, può scattare il timeout.

A quel punto:

- la richiesta fallisce;
    
- la transazione può fare rollback;
    
- oppure può riprovare a chiedere il lock.
    

Importante:

> il fallimento di una richiesta di lock non implica automaticamente il rilascio degli altri lock già acquisiti.

---

# 25. Granularità dei lock

La granularità indica il livello al quale si applica il lock.

Possibili livelli:

- intera base di dati;
    
- tabella;
    
- frammento o partizione;
    
- insieme di tuple;
    
- singola tupla;
    
- campo di una tupla.
    

---

## 25.1 Lock troppo grossolani

Esempio: lock a livello di tabella.

Vantaggi:

- semplice da gestire;
    
- meno lock da memorizzare.
    

Svantaggi:

- riduce il parallelismo;
    
- aumenta la probabilità di conflitti.
    

---

## 25.2 Lock troppo fini

Esempio: lock a livello di singola tupla o campo.

Vantaggi:

- aumenta il parallelismo;
    
- riduce i conflitti inutili.
    

Svantaggi:

- aumenta il numero di lock;
    
- aumenta il costo di gestione;
    
- una transazione può fallire dopo aver già fatto molto lavoro.
    

---

# 26. Lock gerarchico

Il lock gerarchico permette di gestire lock a diversi livelli di granularità in modo efficiente.

La base di dati viene vista come una gerarchia:

```text
DB
├── Tabella
│   ├── Frammento
│   │   ├── Tupla
│   │   └── Tupla
```

L’idea è che prima di bloccare un nodo basso della gerarchia bisogna segnalare l’intenzione sui nodi superiori.

---

## 26.1 Tipi di lock gerarchico

|Lock|Significato|
|---|---|
|`SL`|shared lock, lock condiviso|
|`XL`|exclusive lock, lock esclusivo|
|`ISL`|intention shared lock|
|`IXL`|intention exclusive lock|
|`SIXL`|shared + intention exclusive lock|

---

## 26.2 ISL

`ISL` significa:

> ho intenzione di prendere un lock condiviso su qualche discendente.

Esempio:

```text
voglio leggere una tupla di una tabella
```

Prima metto `ISL` sulla tabella, poi `SL` sulla tupla.

---

## 26.3 IXL

`IXL` significa:

> ho intenzione di prendere un lock esclusivo su qualche discendente.

Esempio:

```text
voglio modificare una tupla
```

Prima metto `IXL` sulla tabella, poi `XL` sulla tupla.

---

## 26.4 SIXL

`SIXL` significa:

> leggo tutto il nodo corrente, ma potrei modificare qualche discendente.

Esempio:

```text
leggo tutta una tabella, ma aggiorno alcune tuple
```

---

## 26.5 Regole del lock gerarchico

Le regole principali sono:

1. i lock si richiedono partendo dalla radice e scendendo;
    
2. i lock si rilasciano partendo dal basso e risalendo;
    
3. per chiedere `SL` o `ISL` su un nodo, bisogna avere `ISL` o `IXL` sul padre;
    
4. per chiedere `IXL`, `XL` o `SIXL` su un nodo, bisogna avere `IXL` o `SIXL` sul padre;
    
5. il lock manager usa una tabella di compatibilità.
    

---

# 27. Deadlock

Il **deadlock**, o blocco critico, si verifica quando due o più transazioni rimangono bloccate in attesa reciproca.

Esempio:

```text
t1 ha lock su x e vuole y
t2 ha lock su y e vuole x
```

Schedule:

```text
rlock1(x)
rlock2(y)
r1(x)
r2(y)
w1(y)   // t1 aspetta y
w2(x)   // t2 aspetta x
```

`t1` aspetta `t2`, ma `t2` aspetta `t1`.

Nessuna delle due può proseguire.

---

# 28. Tecniche per gestire i deadlock

Ci sono tre tecniche principali:

1. timeout;
    
2. rilevamento;
    
3. prevenzione.
    

---

## 28.1 Timeout

Ogni transazione può attendere una risorsa per un tempo massimo.

Se il tempo scade:

- la richiesta fallisce;
    
- la transazione viene abortita o riavviata.
    

Vantaggio:

- semplice;
    
- usato spesso nei sistemi commerciali.
    

Svantaggio:

- scegliere il timeout è difficile.
    

Se il timeout è troppo alto:

```text
il deadlock viene risolto tardi
```

Se il timeout è troppo basso:

```text
si rischia di abortire transazioni che stavano solo aspettando normalmente
```

---

## 28.2 Deadlock detection

Il sistema controlla periodicamente le relazioni di attesa tra transazioni.

Si costruisce un grafo di attesa:

```text
ti -> tj
```

significa:

```text
ti aspetta una risorsa posseduta da tj
```

Se il grafo contiene un ciclo, c’è un deadlock.

Esempio:

```text
t1 -> t2 -> t1
```

Il sistema sceglie una vittima da abortire per rompere il ciclo.

---

## 28.3 Deadlock prevention

La prevenzione cerca di impedire la nascita del deadlock.

Una possibile tecnica è richiedere tutti i lock necessari all’inizio.

Problema:

- spesso la transazione non sa in anticipo tutte le risorse che userà;
    
- il metodo è rigido;
    
- riduce il parallelismo.
    

Un’altra tecnica usa i timestamp.

Una transazione può aspettare un’altra solo se i timestamp rispettano una certa relazione.

Così si impedisce la formazione di cicli.

Svantaggio:

> molte transazioni vengono uccise anche quando non ci sarebbe stato un vero deadlock.

Per questo la prevenzione non è molto usata nei DBMS commerciali.

---

# 29. Politiche interrompenti e non interrompenti

Quando bisogna scegliere una transazione da abortire, si parla di scelta della **vittima**.

Esistono due tipi di politiche.

---

## 29.1 Politiche interrompenti

Una transazione può essere uccisa anche mentre possiede una risorsa.

In questo modo rilascia la risorsa e permette ad altre transazioni di proseguire.

---

## 29.2 Politiche non interrompenti

Una transazione può essere uccisa solo quando effettua una nuova richiesta.

Quindi non viene interrotta mentre sta semplicemente usando risorse già acquisite.

---

## 29.3 Problema della starvation

Se si sceglie sempre di uccidere la transazione che ha svolto meno lavoro, può verificarsi starvation.

Una transazione giovane o appena iniziata può essere continuamente abortita perché risulta sempre quella che ha “perso meno lavoro”.

Soluzione possibile:

> mantenere invariato il timestamp delle transazioni abortite e riavviate, così diventano progressivamente più anziane e acquistano priorità.

---

# 30. Concorrenza in SQL:1999

SQL:1999 distingue tra:

- transazioni **read-only**;
    
- transazioni **read-write**.
    

Le transazioni read-write sono il default.

Le transazioni read-only:

- non modificano il contenuto della base di dati;
    
- non modificano lo schema;
    
- possono essere gestite con soli lock condivisi.
    

---

# 31. Livelli di isolamento

Il programmatore può scegliere di rinunciare ad alcuni requisiti di isolamento per aumentare le prestazioni.

SQL prevede quattro livelli:

1. `serializable`;
    
2. `repeatable read`;
    
3. `read committed`;
    
4. `read uncommitted`.
    

---

## 31.1 Serializable

È il livello più forte.

Garantisce tutti i requisiti di isolamento.

Usa:

- 2PL stretto;
    
- lock di predicato.
    

Evita tutte le anomalie:

- perdita di aggiornamento;
    
- lettura sporca;
    
- letture inconsistenti;
    
- aggiornamento fantasma;
    
- inserimento fantasma.
    

---

## 31.2 Repeatable read

Applica il 2PL stretto anche ai lock di lettura, ma a livello di tupla.

Garantisce che, se una transazione legge una tupla, quella tupla non cambi durante la transazione.

Evita:

- perdita di aggiornamento;
    
- lettura sporca;
    
- letture inconsistenti;
    
- aggiornamento fantasma su tuple già lette.
    

Non evita completamente:

- inserimento fantasma.
    

Motivo:

> non impedisce necessariamente l’inserimento di nuove tuple che soddisfano un predicato.

---

## 31.3 Read committed

Garantisce che una transazione legga solo dati già confermati da commit.

Evita:

- lettura sporca;
    
- perdita di aggiornamento.
    

Non evita:

- letture inconsistenti;
    
- aggiornamento fantasma;
    
- inserimento fantasma.
    

Esempio:

```text
t1 legge x
t2 modifica x e fa commit
t1 rilegge x
```

`t1` può vedere un valore diverso, perché `read committed` non garantisce letture ripetibili.

---

## 31.4 Read uncommitted

È il livello più debole.

Una transazione può leggere dati non ancora confermati.

Può presentare quasi tutte le anomalie:

- lettura sporca;
    
- letture inconsistenti;
    
- aggiornamento fantasma;
    
- inserimento fantasma.
    

Non presenta perdita di aggiornamento se le scritture continuano a essere gestite con lock esclusivi fino a commit o abort.

Spesso viene usato solo per transazioni read-only.

---

# 32. Tabella riassuntiva dei livelli di isolamento

|Livello|Lettura sporca|Letture inconsistenti|Inserimento fantasma|Perdita aggiornamento|
|---|---|---|---|---|
|Serializable|evitata|evitata|evitata|evitata|
|Repeatable read|evitata|evitata|possibile|evitata|
|Read committed|evitata|possibile|possibile|evitata|
|Read uncommitted|possibile|possibile|possibile|evitata|

---

# 33. Riassunto generale

La gestione della concorrenza serve a permettere l’esecuzione simultanea di più transazioni senza compromettere la correttezza della base di dati.

Le anomalie principali sono:

```text
perdita di aggiornamento
lettura sporca
aggiornamento fantasma
letture inconsistenti
inserimento fantasma
```

Il concetto centrale è la **serializzabilità**:

> uno schedule concorrente è corretto se è equivalente a uno schedule seriale.

Esistono due criteri principali:

```text
VSR = serializzabilità rispetto alle viste
CSR = serializzabilità rispetto ai conflitti
```

La VSR è più generale ma difficile da verificare.  
La CSR è più restrittiva ma pratica, perché si verifica tramite il grafo dei conflitti.

Il protocollo più importante nella pratica è il **2PL**, soprattutto nella versione **2PL stretto**.

Il 2PL garantisce schedule in CSR, ma può causare deadlock.

Il metodo basato sui timestamp evita i deadlock, ma può causare molti abort e restart.

I DBMS commerciali usano varianti ottimizzate di questi metodi.

---

# 34. Mappa concettuale finale

```text
Concorrenza
├── Problema
│   ├── più transazioni contemporanee
│   └── rischio di anomalie
│
├── Anomalie
│   ├── perdita di aggiornamento
│   ├── lettura sporca
│   ├── aggiornamento fantasma
│   ├── letture inconsistenti
│   └── inserimento fantasma
│
├── Schedule
│   ├── seriale
│   ├── serializzabile
│   ├── VSR
│   └── CSR
│
├── CSR
│   └── grafo dei conflitti
│       ├── aciclico = serializzabile
│       └── ciclico = non serializzabile
│
├── Protocolli
│   ├── 2PL
│   │   ├── fase crescente
│   │   ├── fase calante
│   │   ├── 2PL stretto
│   │   └── lock di predicato
│   │
│   └── Timestamp
│       ├── RTM
│       ├── WTM
│       ├── restart
│       └── multiversioni
│
├── Lock
│   ├── condiviso
│   ├── esclusivo
│   ├── gerarchico
│   └── granularità
│
├── Deadlock
│   ├── timeout
│   ├── detection
│   └── prevention
│
└── SQL
    ├── serializable
    ├── repeatable read
    ├── read committed
    └── read uncommitted
```

---

# 35. Domande tipiche da esame

## Che cos’è uno schedule?

Uno schedule è una sequenza temporale di operazioni di lettura e scrittura appartenenti a transazioni concorrenti.

---

## Quando uno schedule è seriale?

Uno schedule è seriale se tutte le operazioni di ogni transazione compaiono consecutive, senza essere intervallate da operazioni di altre transazioni.

---

## Quando uno schedule è serializzabile?

Uno schedule è serializzabile se produce lo stesso effetto di uno schedule seriale delle stesse transazioni.

---

## Che differenza c’è tra VSR e CSR?

VSR usa l’equivalenza rispetto alle viste, basata su relazione legge e scritture finali.  
CSR usa l’equivalenza rispetto ai conflitti, basata sull’ordine delle operazioni in conflitto.

CSR è contenuta in VSR.

---

## Come si verifica se uno schedule è in CSR?

Si costruisce il grafo dei conflitti.  
Se il grafo è aciclico, lo schedule è in CSR.  
Se il grafo ha cicli, lo schedule non è in CSR.

---

## Che cos’è il 2PL?

È un protocollo di locking in cui ogni transazione ha due fasi:

1. acquisizione dei lock;
    
2. rilascio dei lock.
    

Dopo aver rilasciato un lock, la transazione non può acquisirne altri.

---

## Che differenza c’è tra 2PL e 2PL stretto?

Nel 2PL normale i lock possono essere rilasciati prima del commit.  
Nel 2PL stretto i lock vengono rilasciati solo dopo commit o abort.

Il 2PL stretto evita la lettura sporca.

---

## Che cos’è un lock di predicato?

È un lock applicato non a una singola tupla, ma a tutte le tuple che soddisfano una certa condizione.

Serve a evitare l’inserimento fantasma.

---

## Che differenza c’è tra 2PL e timestamp?

Nel 2PL le transazioni in conflitto vengono messe in attesa.  
Nel metodo timestamp le transazioni che violano l’ordine temporale vengono uccise e riavviate.

---

## Che cos’è un deadlock?

È una situazione in cui due o più transazioni aspettano reciprocamente il rilascio di risorse, quindi nessuna può proseguire.

---

## Come si risolve un deadlock?

Con:

- timeout;
    
- rilevamento dei cicli nel grafo di attesa;
    
- prevenzione tramite regole sui lock o timestamp.
    

---

## Qual è il livello di isolamento più forte in SQL?

`serializable`.

Garantisce il massimo isolamento ed evita tutte le anomalie.

---

## Qual è il livello più debole?

`read uncommitted`.

Permette anche letture di dati non confermati e può causare letture sporche.