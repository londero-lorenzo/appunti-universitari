---
title: "Capitolo 6"
aliases: ["Capitolo 6"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-6"]
created: 2026-05-05
---
# Reti di Calcolatori — Chapter 6
# Congestion Control and Resource Allocation

## 1. Problema generale

In una rete a commutazione di pacchetto, molte sorgenti condividono le stesse risorse:

- **banda dei link**;
- **buffer dei router e degli switch**;
- **capacità di elaborazione dei dispositivi intermedi**.

Quando troppi pacchetti competono per lo stesso link, si formano code nei router. Se la coda cresce troppo:

1. il buffer si riempie;
2. i nuovi pacchetti vengono scartati;
3. la rete entra in **congestione**.

Il problema centrale del capitolo è quindi:

> Come allocare in modo efficace ed equo le risorse di rete tra utenti/flussi concorrenti?

---

## 2. Congestion Control vs Resource Allocation

**Congestion control** e **resource allocation** sono due facce dello stesso problema.

### Resource Allocation

La rete cerca di assegnare risorse ai flussi in modo preventivo.

Esempio:

- un router riserva una certa banda a un flusso;
- stabilisce quale traffico ha priorità;
- decide quali pacchetti inviare prima.

Se l’allocazione è fatta bene, la congestione può essere evitata prima che si verifichi.

### Congestion Control

Il controllo della congestione interviene quando la congestione si è già manifestata o viene percepita.

Esempio tipico:

- un pacchetto viene perso;
- TCP interpreta la perdita come segnale di congestione;
- il mittente riduce la velocità di trasmissione.

### Congestion Avoidance

La **congestion avoidance** cerca invece di evitare che la congestione si verifichi.

L’idea è:

> non aspettare che la coda sia piena, ma rilevare segnali precoci di congestione e rallentare prima che i pacchetti vengano persi in massa.

Esempi:

- RED;
- tecniche basate sull’aumento dell’RTT;
- algoritmi moderni come Vegas o BBR.

---

## 3. Dove si può intervenire?

Il controllo della congestione coinvolge sia:

- **host finali**;
- **router/switch interni alla rete**.

### Nei router

I router possono usare diverse **discipline di accodamento** per decidere:

- in quale ordine trasmettere i pacchetti;
- quali pacchetti scartare;
- come distribuire la banda tra i flussi.

Esempi:

- FIFO;
- Priority Queuing;
- Fair Queuing;
- RED.

### Negli host

Gli host, soprattutto i mittenti TCP, regolano la velocità di invio.

TCP usa variabili come:

- `CongestionWindow`;
- `AdvertisedWindow`;
- `ssthreshold`.

---

# 4. Modello di rete

## 4.1 Rete packet-switched

Le slide considerano una rete a commutazione di pacchetto composta da:

- host sorgenti;
- router;
- link;
- host destinatari.

Un host può avere un link locale molto veloce, ma i suoi pacchetti possono incontrare più avanti un link più lento o condiviso da molti altri flussi.

Questo link diventa un **bottleneck**, cioè un collo di bottiglia.

Esempio:

```text
Host A ----\
            Router ---- link lento ---- Destinazione
Host B ----/
```

Anche se A e B hanno link locali veloci, il link in uscita dal router può saturarsi.

---

## 4.2 Connectionless Flows

Anche se IP è connectionless, nella pratica i pacchetti non sono sempre completamente indipendenti.

Un flusso di pacchetti tra due host tende spesso a seguire lo stesso percorso attraverso la rete.

Per questo si introduce il concetto di **flow**.

Un flow può essere definito a diverse granularità:

| Tipo di flow | Identificazione |
|---|---|
| Host-to-host | stesso IP sorgente e stesso IP destinazione |
| Process-to-process | stesso IP sorgente, IP destinazione, porta sorgente e porta destinazione |

Nel secondo caso il flow è molto simile al concetto di **canale** end-to-end.

La differenza importante è:

- il **canale** è un’astrazione end-to-end;
- il **flow** può essere visibile anche ai router intermedi.

---

## 4.3 Soft State

I router possono mantenere alcune informazioni sui flussi, per esempio:

- rate;
- dimensione media dei pacchetti;
- bitrate;
- quantità di traffico osservata.

Queste informazioni sono chiamate **soft state**.

### Soft state vs hard state

| Tipo di stato | Caratteristiche |
|---|---|
| Hard state | creato e rimosso esplicitamente tramite segnalazione |
| Soft state | inferito automaticamente osservando il traffico |

Il soft state non è necessario per il corretto funzionamento della rete.

Infatti, anche senza soft state, ogni pacchetto può comunque essere instradato.

Tuttavia, se il router possiede informazioni sul flusso, può gestirlo meglio.

---

# 5. Approcci all’allocazione delle risorse

## 5.1 Router-centric vs Host-centric

### Router-centric

Nel modello **router-centric**, i router hanno un ruolo attivo.

Decidono:

- quando inoltrare i pacchetti;
- quali pacchetti scartare;
- come informare gli host sulla quantità di traffico che possono inviare.

Esempio:

- un router rileva congestione;
- scarta pacchetti prima che il buffer sia pieno;
- oppure invia segnali espliciti agli host.

### Host-centric

Nel modello **host-centric**, sono gli host finali a osservare il comportamento della rete.

L’host mittente può dedurre la congestione osservando:

- perdite di pacchetti;
- timeout;
- ACK duplicati;
- aumento dell’RTT.

TCP classico è principalmente host-centric.

### Nota importante

I due approcci non sono mutuamente esclusivi.

Una rete può usare contemporaneamente:

- router intelligenti;
- host che regolano il proprio invio.

---

## 5.2 Reservation-based vs Feedback-based

### Reservation-based

Nel modello **reservation-based**, un flusso chiede alla rete una certa quantità di risorse prima di iniziare a trasmettere.

Il router può:

- accettare la richiesta, se ha risorse sufficienti;
- rifiutarla, se la rete sarebbe sovraccaricata.

Vantaggio:

- maggiore garanzia di qualità.

Svantaggio:

- più complesso;
- richiede segnalazione;
- meno flessibile.

### Feedback-based

Nel modello **feedback-based**, gli host iniziano a trasmettere senza riservare risorse.

Poi regolano la propria velocità in base al feedback ricevuto.

Il feedback può essere:

| Tipo di feedback | Esempio |
|---|---|
| Esplicito | il router comunica direttamente “rallenta” |
| Implicito | il mittente rileva perdite, timeout o ACK duplicati |

TCP usa soprattutto feedback implicito.

---

# 6. Criteri di valutazione

Un meccanismo di allocazione delle risorse si valuta principalmente tramite:

- **throughput**;
- **delay**.

## 6.1 Throughput

Il throughput misura quanti dati vengono trasferiti nell’unità di tempo.

Un throughput alto significa che la rete viene usata bene.

## 6.2 Delay

Il delay misura il tempo necessario affinché un pacchetto attraversi la rete.

Un delay basso significa che i pacchetti non restano troppo tempo in coda.

## 6.3 Trade-off throughput-delay

I due obiettivi sono in conflitto.

Per aumentare il throughput, si tende a inserire più pacchetti nella rete.

Ma più pacchetti significano:

- code più lunghe;
- maggiore ritardo;
- maggiore probabilità di perdita.

Viceversa, per ridurre il delay, bisogna mantenere le code quasi vuote.

Ma questo può ridurre l’utilizzazione dei link.

---

# 7. Modello M/M/1

Le slide usano un esempio di teoria delle code: il modello **M/M/1**.

È un sistema con:

- arrivi casuali;
- un solo server;
- tempo di servizio medio;
- coda potenzialmente infinita.

## 7.1 Parametri

| Simbolo | Significato |
|---|---|
| `λ` | tasso medio di arrivo nella coda |
| `S` | tempo medio di servizio |
| `ρ` | utilizzazione del server |
| `R` | tempo medio totale nel sistema |
| `Q` | lunghezza media della coda/sistema |
| `W` | tempo medio di attesa prima del servizio |

## 7.2 Formule principali

```math
\rho = \lambda S
```

```math
R = \frac{S}{1 - \lambda S}
```

```math
Q = \lambda R
```

```math
W = R - S
```

oppure:

```math
W = \frac{S\rho}{1 - \rho}
```

## 7.3 Interpretazione

Quando `λS` è piccolo:

- il sistema è poco carico;
- le code sono brevi;
- il delay è vicino al tempo di servizio `S`.

Quando `λS` si avvicina a 1:

- il server è quasi saturo;
- le code crescono rapidamente;
- il delay tende a infinito.

Quando:

```math
\lambda S \geq 1
```

il sistema non è stabile.

Significa che arrivano richieste più velocemente di quanto il server riesca a servirle.

---

## 7.4 Esempio della banca

Esempio delle slide:

- un solo sportello;
- tempo medio di servizio: `S = 10 min/client`;
- tasso di arrivo variabile.

Se arrivano pochi clienti, il tempo totale nel sistema è poco superiore a 10 minuti.

Se il tasso di arrivo si avvicina alla capacità massima dello sportello, il tempo medio esplode.

Questo mostra perché non conviene lavorare sempre al 100% di utilizzo.

Una rete apparentemente “molto efficiente” perché sempre piena può in realtà produrre ritardi enormi.

---

# 8. Power della rete

Per combinare throughput e delay, si può usare la metrica:

```math
Power = \frac{Throughput}{Delay}
```

L’obiettivo è:

- throughput alto;
- delay basso.

Quindi vogliamo massimizzare la **power**.

Nel caso M/M/1 visto nelle slide:

```math
Power = \frac{\lambda}{S} - \lambda^2
```

## Interpretazione grafica

La curva della power ha tipicamente questa forma:

1. a basso carico, la power cresce quasi linearmente;
2. a carico medio, raggiunge un massimo;
3. ad alto carico, il throughput può ancora crescere, ma il delay cresce molto di più;
4. quindi la power diminuisce.

Il punto ideale non è quello in cui la rete è satura.

È quello in cui il throughput è buono ma le code restano ancora corte.

---

# 9. Discipline di accodamento

Le discipline di accodamento decidono come i router gestiscono i pacchetti nelle code.

Bisogna distinguere due aspetti:

| Aspetto | Domanda |
|---|---|
| Scheduling discipline | Quale pacchetto viene trasmesso per primo? |
| Drop policy | Quale pacchetto viene scartato quando serve? |

---

# 10. FIFO con Tail Drop

## 10.1 FIFO

FIFO significa **First-In First-Out**.

Il primo pacchetto che arriva è il primo pacchetto trasmesso.

È anche chiamato:

```text
FCFS = First-Come First-Served
```

## 10.2 Tail Drop

I buffer dei router sono finiti.

Se arriva un pacchetto quando la coda è piena, il router lo scarta.

Questa politica si chiama **tail drop**, perché viene scartato il pacchetto che arriva in fondo alla coda.

## 10.3 Problemi di FIFO + Tail Drop

FIFO non distingue tra:

- flussi diversi;
- pacchetti importanti e non importanti;
- traffico sensibile al ritardo e traffico non sensibile al ritardo.

Quindi un flusso aggressivo può occupare molta coda e penalizzare gli altri.

Inoltre, con tail drop, molti pacchetti possono essere persi insieme quando la coda si riempie.

---

# 11. Priority Queuing

La **Priority Queuing** assegna una priorità ai pacchetti.

Il router mantiene più code FIFO:

```text
Coda alta priorità
Coda media priorità
Coda bassa priorità
```

Il router serve prima la coda con priorità più alta.

Solo quando questa è vuota passa alla successiva.

## 11.1 Come si indica la priorità?

La priorità può essere indicata:

- nel campo TOS/DSCP di IPv4;
- nel campo Traffic Class di IPv6;
- tramite regole interne del router;
- tramite classificazione del traffico.

## 11.2 Vantaggio

Permette di favorire traffico sensibile al ritardo, per esempio:

- VoIP;
- videoconferenze;
- streaming real-time;
- controllo industriale.

## 11.3 Problema

Se il traffico ad alta priorità è troppo, quello a bassa priorità può subire starvation.

Cioè può restare in coda per troppo tempo.

## 11.4 Weighted Round Robin

Una variante è il **Weighted Round Robin**.

A ogni coda viene assegnato un peso.

Esempio:

| Coda | Peso |
|---|---|
| Alta priorità | 3 |
| Media priorità | 2 |
| Bassa priorità | 1 |

Il router può servire:

- 3 pacchetti dalla coda alta;
- 2 pacchetti dalla coda media;
- 1 pacchetto dalla coda bassa.

In questo modo anche le code meno prioritarie ricevono una parte di servizio.

---

# 12. Fair Queuing

## 12.1 Problema che vuole risolvere

FIFO tratta tutti i pacchetti allo stesso modo, ma non tratta equamente i flussi.

Un flusso che invia moltissimi pacchetti può occupare molta banda e molta coda.

La **Fair Queuing** cerca di distribuire equamente la banda tra i flussi.

## 12.2 Idea generale

Il router mantiene una coda separata per ogni flow.

Esempio:

```text
Flow A -> coda A
Flow B -> coda B
Flow C -> coda C
Flow D -> coda D
```

Poi il router serve le code in modo simile al round-robin.

---

## 12.3 Perché il round-robin semplice non basta?

I pacchetti possono avere dimensioni diverse.

Esempio:

- Flow 1 invia pacchetti da 1000 byte;
- Flow 2, 3, 4 inviano pacchetti da 100 byte.

Se il router prende un pacchetto da ogni coda, allora dopo un giro trasmette:

```text
1000 + 100 + 100 + 100 = 1300 byte
```

La quota di banda del flow 1 è:

```math
\frac{1000}{1300} = 77\%
```

La quota di ciascun altro flow è:

```math
\frac{100}{1300} = 7.7\%
```

Questo non è equo.

---

## 12.4 Bit-by-bit round robin

L’ideale sarebbe fare round-robin bit per bit:

```text
1 bit da Flow A
1 bit da Flow B
1 bit da Flow C
1 bit da Flow D
...
```

Così ogni flusso riceverebbe la stessa quantità di banda.

Ma nella pratica non si può trasmettere mezzo pacchetto o interlecciare bit di pacchetti diversi.

Un pacchetto deve essere trasmesso interamente.

Fair Queuing approssima il bit-by-bit round robin usando dei timestamp.

---

# 13. Algoritmo di Fair Queuing

Per ogni pacchetto si calcola un tempo virtuale di fine trasmissione.

## 13.1 Variabili

| Simbolo | Significato |
|---|---|
| `A_i` | tempo di arrivo del pacchetto `i` |
| `P_i` | durata/lunghezza del pacchetto `i` |
| `S_i` | tempo di inizio trasmissione virtuale del pacchetto `i` |
| `F_i` | tempo di fine trasmissione virtuale del pacchetto `i` |

## 13.2 Formula

Per un pacchetto `i` dello stesso flusso:

```math
S_i = \max(F_{i-1}, A_i)
```

```math
F_i = S_i + P_i
```

quindi:

```math
F_i = \max(F_{i-1}, A_i) + P_i
```

## 13.3 Regola di scelta

Il router trasmette sempre il pacchetto con **timestamp finale più piccolo**.

Cioè:

> viene trasmesso per primo il pacchetto che, nel modello bit-by-bit virtuale, avrebbe finito prima.

## 13.4 Nota importante

Se un pacchetto è già in trasmissione, non viene interrotto.

La Fair Queuing decide quale pacchetto trasmettere dopo, ma non spezza la trasmissione di un pacchetto già iniziato.

---

## 13.5 Esempio concettuale

Supponiamo tre flussi:

```text
A: 100, 200, 100, 1000
B: 300, 200, 500
C: 400
```

Per ogni flusso calcolo i timestamp virtuali.

Per A:

| Pacchetto | Durata | Finish time virtuale |
|---|---:|---:|
| A1 | 100 | 100 |
| A2 | 200 | 300 |
| A3 | 100 | 400 |
| A4 | 1000 | 1400 |

Per B:

| Pacchetto | Durata | Finish time virtuale |
|---|---:|---:|
| B1 | 300 | 300 |
| B2 | 200 | 500 |
| B3 | 500 | 1000 |

Per C:

| Pacchetto | Durata | Finish time virtuale |
|---|---:|---:|
| C1 | 400 | 400 |

Ordine di trasmissione in base al finish time:

```text
A1, B1, A2, C1, A3, B2, B3, A4
```

Quando due pacchetti hanno lo stesso timestamp, si può usare un criterio di spareggio, per esempio l’ordine di arrivo o l’ordine delle code.

---

# 14. TCP Congestion Control

## 14.1 Perché nasce

TCP congestion control fu introdotto alla fine degli anni ’80 da Van Jacobson.

Prima, Internet soffriva di **congestion collapse**.

Il problema era:

1. gli host inviavano dati il più velocemente possibile;
2. i router congestionati scartavano pacchetti;
3. gli host andavano in timeout;
4. gli host ritrasmettevano;
5. le ritrasmissioni aumentavano ancora di più la congestione.

Risultato:

> la rete era piena di pacchetti ritrasmessi, ma il throughput utile crollava.

---

## 14.2 Idea generale

TCP deve stimare quanta capacità è disponibile nella rete.

Deve capire quanti dati può avere “in volo”, cioè inviati ma non ancora riscontrati.

L’idea è:

> quando arriva un ACK, significa che un pacchetto ha lasciato la rete; quindi il mittente può inserirne un altro senza aumentare il numero di pacchetti in transito.

Questo comportamento si chiama **self-clocking**.

Gli ACK scandiscono il ritmo di invio.

---

# 15. CongestionWindow

TCP introduce una variabile:

```text
CongestionWindow = cwnd
```

Questa variabile limita quanti byte il mittente può avere in transito.

È diversa da `AdvertisedWindow`.

## 15.1 AdvertisedWindow

`AdvertisedWindow` riguarda il controllo di flusso.

Indica quanto spazio libero ha il buffer del ricevente.

Serve a non sovraccaricare il destinatario.

## 15.2 CongestionWindow

`CongestionWindow` riguarda il controllo della congestione.

Indica quanto la rete sembra poter sopportare.

Serve a non sovraccaricare la rete.

---

# 16. Effective Window

TCP deve rispettare entrambi i limiti:

- il limite del destinatario;
- il limite della rete.

Quindi:

```math
MaxWindow = \min(CongestionWindow, AdvertisedWindow)
```

Poi:

```math
EffectiveWindow = MaxWindow - (LastByteSent - LastByteAcked)
```

Dove:

| Variabile | Significato |
|---|---|
| `LastByteSent` | ultimo byte inviato |
| `LastByteAcked` | ultimo byte confermato |
| `LastByteSent - LastByteAcked` | byte già in volo |
| `EffectiveWindow` | byte che posso ancora inviare |

Interpretazione:

> TCP può trasmettere solo quanto consentito dal componente più lento: rete o ricevitore.

---

# 17. AIMD

AIMD significa:

```text
Additive Increase Multiplicative Decrease
```

È il meccanismo base del congestion control classico.

## 17.1 Formula generale

Sia:

- `w(t)` la congestion window al tempo `t`;
- `a > 0` il parametro di incremento additivo;
- `0 < b < 1` il fattore di decremento moltiplicativo.

Allora:

```math
w(t+1) =
\begin{cases}
w(t) + a & \text{se non viene rilevata congestione} \\
w(t) \cdot b & \text{se viene rilevata congestione}
\end{cases}
```

Nel TCP classico:

```text
a = 1 MSS
b = 0.5
```

---

## 17.2 Multiplicative Decrease

Quando TCP rileva congestione, riduce la finestra.

Esempio:

```text
cwnd = 16 MSS
perdita rilevata
cwnd = 8 MSS
altra perdita
cwnd = 4 MSS
altra perdita
cwnd = 2 MSS
altra perdita
cwnd = 1 MSS
```

La congestion window non scende sotto 1 MSS.

## 17.3 Come TCP rileva la congestione?

Nel TCP classico, la congestione è dedotta soprattutto da:

- timeout;
- ACK duplicati;
- perdita di pacchetti.

L’assunzione classica è:

> se un pacchetto si perde, probabilmente è stato scartato da un router congestionato.

Questa assunzione è meno vera nelle reti wireless, dove le perdite possono essere dovute anche a errori radio.

---

## 17.4 Additive Increase

Quando non c’è congestione, TCP aumenta lentamente la congestion window.

La regola concettuale è:

> ogni RTT, se tutti i dati inviati sono stati riscontrati, aumenta `cwnd` di 1 MSS.

Quindi, in fase additiva:

```text
cwnd = 8 MSS
dopo 1 RTT -> 9 MSS
dopo 1 RTT -> 10 MSS
dopo 1 RTT -> 11 MSS
...
```

---

## 17.5 Incremento pratico per ACK

TCP non aspetta necessariamente tutto l’RTT per aggiornare `cwnd`.

Ogni volta che riceve un ACK per `k` nuovi byte, incrementa:

```math
Increment = MSS \cdot \frac{k}{CongestionWindow}
```

Poi:

```math
CongestionWindow = CongestionWindow + Increment
```

Se durante un RTT vengono riscontrati tutti i byte della congestion window, la somma degli incrementi produce circa `1 MSS`.

---

## 17.6 Andamento a dente di sega

AIMD produce il tipico andamento a **sawtooth**, cioè a dente di sega:

```text
cwnd cresce linearmente
cwnd cresce linearmente
cwnd cresce linearmente
perdita
cwnd si dimezza
cwnd cresce linearmente
perdita
cwnd si dimezza
...
```

Questo è il comportamento classico del TCP congestion control.

---

# 18. Slow Start

## 18.1 Perché serve

L’additive increase è troppo lenta quando una connessione parte da zero.

Se TCP partisse con `cwnd = 1 MSS` e aumentasse solo di `1 MSS` per RTT, impiegherebbe troppo tempo a raggiungere una buona velocità.

Per questo TCP usa la **slow start**.

Il nome è un po’ ingannevole: rispetto ad AIMD, slow start è veloce.

È “slow” solo rispetto all’idea di inviare subito tutta la finestra disponibile.

---

## 18.2 Funzionamento

All’inizio:

```text
cwnd = 1 MSS
```

Quando arriva l’ACK:

```text
cwnd = 2 MSS
```

Poi, se arrivano due ACK:

```text
cwnd = 4 MSS
```

Poi:

```text
cwnd = 8 MSS
```

Quindi la crescita è esponenziale.

In pratica:

```text
1, 2, 4, 8, 16, 32, ...
```

La congestion window raddoppia circa ogni RTT.

---

## 18.3 Quando viene usata Slow Start?

Slow start viene usata in due situazioni principali.

### Caso 1: inizio della connessione

All’inizio TCP non sa quanta capacità sia disponibile.

Quindi parte con una finestra piccola e cresce rapidamente finché non rileva congestione.

### Caso 2: dopo un timeout

Dopo un timeout, la connessione può essere rimasta “ferma”.

Non ci sono più ACK in arrivo per scandire l’invio di nuovi pacchetti.

Se TCP inviasse subito una grande finestra di dati, potrebbe creare una nuova congestione.

Quindi riparte con slow start.

---

# 19. ssthreshold

TCP usa una variabile chiamata:

```text
ssthreshold
```

oppure:

```text
CongestionThreshold
```

Questa variabile rappresenta la soglia tra:

- slow start;
- additive increase.

## 19.1 Dopo una perdita

Quando avviene una perdita, TCP imposta:

```text
ssthreshold = cwnd / 2
```

Poi, in caso di timeout:

```text
cwnd = 1 MSS
```

TCP riparte in slow start fino a raggiungere `ssthreshold`.

Dopo `ssthreshold`, passa alla crescita lineare AIMD.

## 19.2 Schema

```text
cwnd < ssthreshold
    -> Slow Start
    -> crescita esponenziale

cwnd >= ssthreshold
    -> Congestion Avoidance / Additive Increase
    -> crescita lineare
```

---

# 20. Fast Retransmit

## 20.1 Problema dei timeout

I timeout TCP possono essere lunghi.

Se TCP aspetta sempre il timeout prima di ritrasmettere, la connessione può rimanere inattiva troppo tempo.

Per questo è stato introdotto il **Fast Retransmit**.

## 20.2 ACK duplicati

TCP usa ACK cumulativi.

Se il ricevente riceve un pacchetto fuori ordine, non può avanzare l’ACK cumulativo.

Quindi ripete lo stesso ACK già inviato.

Questo si chiama **duplicate ACK**.

Esempio:

```text
Ricevuti byte fino a 999
manca il segmento 1000-1999
arriva il segmento 2000-2999
il ricevente manda ancora ACK=1000
arriva il segmento 3000-3999
il ricevente manda ancora ACK=1000
```

Il mittente vede più ACK uguali.

Questo suggerisce che il segmento mancante potrebbe essere stato perso.

---

## 20.3 Regola dei tre duplicate ACK

TCP non ritrasmette al primo duplicate ACK, perché un pacchetto potrebbe solo essere in ritardo.

Aspetta normalmente:

```text
3 duplicate ACK
```

cioè quattro ACK totali con lo stesso valore.

A quel punto ritrasmette il segmento mancante senza aspettare il timeout.

---

# 21. Tahoe

TCP Tahoe usa:

- slow start;
- AIMD;
- fast retransmit.

Quando riceve 3 duplicate ACK:

1. esegue fast retransmit;
2. imposta `ssthreshold = cwnd / 2`;
3. imposta `cwnd = 1 MSS`;
4. riparte in slow start.

Quindi Tahoe reagisce in modo abbastanza drastico.

---

# 22. Fast Recovery e Reno

TCP Reno aggiunge il **Fast Recovery**.

L’idea è:

> se sto ricevendo duplicate ACK, significa che alcuni pacchetti stanno comunque arrivando al destinatario. Quindi la rete non è completamente ferma.

Perciò non è sempre necessario tornare a `cwnd = 1 MSS`.

## 22.1 Comportamento di Reno

Quando Reno riceve 3 duplicate ACK:

1. esegue fast retransmit;
2. imposta:

```text
ssthreshold = cwnd / 2
```

3. imposta:

```text
cwnd = ssthreshold + 3 MSS
```

4. entra in fast recovery.

Se invece avviene un timeout:

```text
cwnd = 1 MSS
```

e TCP riparte in slow start.

## 22.2 Differenza Tahoe vs Reno

| Evento | Tahoe | Reno |
|---|---|---|
| 3 duplicate ACK | `cwnd = 1 MSS` | `cwnd = ssthreshold + 3 MSS` |
| Timeout | `cwnd = 1 MSS` | `cwnd = 1 MSS` |
| Recupero | Slow start | Fast recovery |

Quindi Reno è meno aggressivo nel ridurre la finestra quando la perdita è rilevata tramite ACK duplicati.

---

# 23. Esercizi tipici su TCP Congestion Control

## 23.1 Slow Start

Se parto con:

```text
cwnd = 2 MSS
```

e faccio 3 round completi in slow start:

```text
dopo 1 RTT: 4 MSS
dopo 2 RTT: 8 MSS
dopo 3 RTT: 16 MSS
```

Se nel terzo round mancano gli ACK per 2 segmenti, allora la finestra effettivamente raggiunta può essere:

```text
16 MSS - 2 MSS = 14 MSS
```

Se:

```text
MSS = 1400 byte
```

allora:

```text
14 MSS = 14 * 1400 = 19600 byte
```

---

## 23.2 Additive Increase con ACK

Formula:

```math
Increment = MSS \cdot \frac{k}{CongestionWindow}
```

Se:

```text
MSS = 1400
CongestionWindow = 10000
k = 1400
```

allora ogni ACK incrementa:

```math
1400 \cdot \frac{1400}{10000} = 196
```

Dopo 5 ACK:

```math
CongestionWindow = 10000 + 5 \cdot 196 = 10980
```

Se poi avviene un timeout:

```math
CongestionWindow = \frac{10980}{2} = 5490
```

---

# 24. Congestion Avoidance

TCP classico controlla la congestione dopo che ha osservato un segnale forte, come una perdita.

La congestion avoidance cerca invece di agire prima.

L’idea è:

> rilevare che una coda sta crescendo e ridurre il traffico prima che la coda si riempia.

---

# 25. RED — Random Early Detection

RED è un meccanismo di congestion avoidance introdotto da Sally Floyd e Van Jacobson.

È implementato nei router.

## 25.1 Idea generale

Il router osserva la lunghezza media della coda.

Quando la coda comincia a diventare troppo lunga, il router scarta alcuni pacchetti in anticipo.

Questo sembra controintuitivo, ma serve a segnalare la congestione ai mittenti TCP.

Infatti TCP interpreterà la perdita come congestione e ridurrà `cwnd`.

## 25.2 Perché “Early”?

Perché il router scarta pacchetti prima che il buffer sia completamente pieno.

Con tail drop, il router aspetta la saturazione del buffer.

Con RED, il router inizia a scartare prima, con bassa probabilità.

Obiettivo:

- evitare burst di perdite;
- evitare code troppo lunghe;
- segnalare prima la congestione.

---

# 26. RED: lunghezza media della coda

RED non usa semplicemente la lunghezza istantanea della coda.

Usa una media pesata:

```math
AvgLen = (1 - w) \cdot AvgLen + w \cdot SampleLen
```

Dove:

| Variabile | Significato |
|---|---|
| `AvgLen` | lunghezza media stimata della coda |
| `SampleLen` | lunghezza attuale misurata |
| `w` | peso della nuova misurazione |

Con `w` piccolo, la media cambia lentamente.

Con `w` grande, la media segue più rapidamente i cambiamenti.

---

# 27. RED: soglie

RED usa due soglie:

```text
MinThreshold
MaxThreshold
```

## 27.1 Regole

### Caso 1

```text
AvgLen <= MinThreshold
```

Il router accoda il pacchetto.

```text
P(drop) = 0
```

### Caso 2

```text
MinThreshold < AvgLen < MaxThreshold
```

Il router scarta il pacchetto con una certa probabilità.

### Caso 3

```text
AvgLen >= MaxThreshold
```

Il router scarta il pacchetto sicuramente.

```text
P(drop) = 1
```

---

# 28. RED: probabilità di drop

Nel caso intermedio:

```text
MinThreshold < AvgLen < MaxThreshold
```

la probabilità di scarto è:

```math
P(drop) = MaxP \cdot \frac{AvgLen - MinThreshold}{MaxThreshold - MinThreshold}
```

Dove `MaxP` è un parametro massimo configurabile.

Nelle versioni semplificate degli esercizi, spesso si assume:

```text
MaxP = 1
```

quindi:

```math
P(drop) = \frac{AvgLen - MinThreshold}{MaxThreshold - MinThreshold}
```

---

## 28.1 Interpretazione

Se la coda è appena sopra `MinThreshold`, la probabilità di scarto è bassa.

Se la coda si avvicina a `MaxThreshold`, la probabilità di scarto aumenta.

Quando raggiunge `MaxThreshold`, il pacchetto viene scartato sicuramente.

---

# 29. Esercizi tipici su RED

## 29.1 Calcolare la lunghezza della coda da P(drop)

Supponiamo:

```text
MinThreshold = 20 KB
MaxThreshold = 100 KB
P(drop) = 0.1
MaxP = 1
```

Formula:

```math
0.1 = \frac{x - 20}{100 - 20}
```

```math
0.1 = \frac{x - 20}{80}
```

```math
8 = x - 20
```

```math
x = 28 KB
```

Quindi la coda media è:

```text
28 KB
```

---

## 29.2 Probabilità che più pacchetti vengano accodati

Esempio:

```text
MinThreshold = 10 KB
MaxThreshold = 20 KB
Coda iniziale = 9 KB
Arrivano pacchetti da 2 KB, 3 KB, 2 KB
```

### Primo pacchetto

Coda iniziale:

```text
9 KB <= 10 KB
```

Il primo pacchetto viene accodato sicuramente.

```text
P1 = 1
```

Nuova coda:

```text
11 KB
```

### Secondo pacchetto

Probabilità di drop:

```math
P(drop) = \frac{11 - 10}{20 - 10} = \frac{1}{10} = 0.1
```

Probabilità di accodamento:

```math
P2 = 1 - 0.1 = 0.9
```

Se accodato, nuova coda:

```text
14 KB
```

### Terzo pacchetto

Probabilità di drop:

```math
P(drop) = \frac{14 - 10}{20 - 10} = \frac{4}{10} = 0.4
```

Probabilità di accodamento:

```math
P3 = 1 - 0.4 = 0.6
```

### Probabilità totale

```math
P = P1 \cdot P2 \cdot P3
```

```math
P = 1 \cdot 0.9 \cdot 0.6 = 0.54
```

Quindi:

```text
Probabilità = 54%
```

---

# 30. Source-based Congestion Avoidance

La congestion avoidance può essere fatta anche dal mittente.

In questo caso il mittente osserva segnali come:

- aumento dell’RTT;
- variazione del throughput;
- stima della banda del bottleneck.

## 30.1 Idea basata su RTT

Quando le code nei router crescono, i pacchetti passano più tempo in attesa.

Questo fa aumentare l’RTT.

Quindi il mittente può interpretare l’aumento dell’RTT come segnale precoce di congestione.

## 30.2 Algoritmo semplificato delle slide

L’algoritmo aumenta normalmente la congestion window.

Ogni due RTT controlla se:

```text
RTT corrente > media tra RTT minimo e RTT massimo osservati
```

Se sì, riduce la congestion window:

```math
CongestionWindow = CongestionWindow \cdot 0.875
```

cioè riduce la finestra di un ottavo.

---

# 31. QoS e informazioni nei pacchetti

Per implementare politiche di qualità del servizio, i router possono usare informazioni presenti negli header.

## 31.1 IPv4

In IPv4 si possono usare campi come:

```text
TOS / DSCP
```

per classificare il traffico.

## 31.2 IPv6

In IPv6 ci sono campi utili come:

```text
Traffic Class
Flow Label
```

### Traffic Class

Serve a indicare priorità o classe di servizio.

### Flow Label

Serve a identificare un flusso, così che i router possano riconoscere pacchetti appartenenti allo stesso flow.

---

# 32. Riepilogo concettuale

## Resource Allocation

Decide come distribuire le risorse tra flussi concorrenti.

Può essere:

- preventiva;
- router-centric;
- reservation-based.

## Congestion Control

Reagisce alla congestione dopo che viene rilevata.

TCP classico usa:

- perdite;
- timeout;
- ACK duplicati.

## Congestion Avoidance

Cerca di prevenire la congestione.

Esempi:

- RED;
- algoritmi basati su RTT;
- Vegas;
- BBR.

---

# 33. Tabelle di confronto

## 33.1 Congestion control vs congestion avoidance

| Aspetto | Congestion Control | Congestion Avoidance |
|---|---|---|
| Quando interviene | Dopo segnali di congestione | Prima che la congestione esploda |
| Segnale tipico | perdita, timeout, duplicate ACK | coda crescente, RTT crescente |
| Esempio | TCP Tahoe/Reno | RED, Vegas, BBR |
| Obiettivo | recuperare da congestione | prevenire congestione |

---

## 33.2 FIFO, Priority, Fair Queuing

| Disciplina | Idea | Vantaggio | Problema |
|---|---|---|---|
| FIFO | primo arrivato, primo servito | semplice | non distingue i flussi |
| Priority Queuing | serve prima pacchetti prioritari | utile per QoS | rischio starvation |
| Fair Queuing | coda separata per flow | equità tra flussi | più complessa |

---

## 33.3 Tahoe vs Reno

| Meccanismo | Tahoe | Reno |
|---|---|---|
| Slow Start | sì | sì |
| AIMD | sì | sì |
| Fast Retransmit | sì | sì |
| Fast Recovery | no | sì |
| Dopo 3 duplicate ACK | `cwnd = 1 MSS` | `cwnd = ssthresh + 3 MSS` |
| Dopo timeout | `cwnd = 1 MSS` | `cwnd = 1 MSS` |

---

# 34. Formule da ricordare

## M/M/1

```math
\rho = \lambda S
```

```math
R = \frac{S}{1 - \lambda S}
```

```math
Q = \lambda R
```

```math
W = R - S
```

```math
W = \frac{S\rho}{1 - \rho}
```

## Power

```math
Power = \frac{Throughput}{Delay}
```

Nel caso M/M/1:

```math
Power = \frac{\lambda}{S} - \lambda^2
```

## Fair Queuing

```math
S_i = \max(F_{i-1}, A_i)
```

```math
F_i = \max(F_{i-1}, A_i) + P_i
```

## TCP Effective Window

```math
MaxWindow = \min(CongestionWindow, AdvertisedWindow)
```

```math
EffectiveWindow = MaxWindow - (LastByteSent - LastByteAcked)
```

## AIMD

```math
w(t+1) =
\begin{cases}
w(t) + a & \text{se non c'è congestione} \\
w(t) \cdot b & \text{se c'è congestione}
\end{cases}
```

Nel TCP classico:

```text
a = 1 MSS
b = 0.5
```

## Additive increase per ACK

```math
Increment = MSS \cdot \frac{k}{CongestionWindow}
```

```math
CongestionWindow = CongestionWindow + Increment
```

## RED

```math
AvgLen = (1 - w) \cdot AvgLen + w \cdot SampleLen
```

```math
P(drop) = MaxP \cdot \frac{AvgLen - MinThreshold}{MaxThreshold - MinThreshold}
```

---

# 35. Domande tipiche da esame

## Domanda 1

Spiega la differenza tra congestion control e congestion avoidance.

Risposta sintetica:

- congestion control reagisce alla congestione dopo che viene rilevata;
- congestion avoidance cerca di prevenirla osservando segnali precoci.

---

## Domanda 2

Perché FIFO con tail drop può essere problematico?

Perché:

- non distingue tra flussi;
- non considera priorità;
- può penalizzare flussi meno aggressivi;
- scarta solo quando la coda è piena;
- può produrre perdite a raffica.

---

## Domanda 3

Perché Fair Queuing non può usare un semplice round-robin tra pacchetti?

Perché i pacchetti possono avere dimensioni diverse.

Un flusso con pacchetti grandi riceverebbe più banda rispetto a flussi con pacchetti piccoli.

Fair Queuing usa timestamp virtuali per approssimare un round-robin bit per bit.

---

## Domanda 4

Cos’è la CongestionWindow?

È la finestra usata da TCP per limitare il numero di byte non ancora riscontrati che possono essere presenti nella rete.

Serve a evitare che il mittente sovraccarichi la rete.

---

## Domanda 5

Qual è la differenza tra AdvertisedWindow e CongestionWindow?

| Finestra | Controlla |
|---|---|
| AdvertisedWindow | capacità del ricevitore |
| CongestionWindow | capacità stimata della rete |

TCP usa il minimo tra le due.

---

## Domanda 6

Cosa significa TCP self-clocking?

Significa che TCP usa l’arrivo degli ACK per regolare il ritmo di invio.

Quando arriva un ACK, il mittente deduce che un pacchetto ha lasciato la rete e può inserirne un altro.

---

## Domanda 7

Cosa succede in Slow Start?

La congestion window cresce esponenzialmente.

Indicativamente:

```text
1, 2, 4, 8, 16, ...
```

cioè raddoppia ogni RTT.

---

## Domanda 8

Cosa succede dopo un timeout TCP?

Nel TCP classico:

```text
ssthreshold = cwnd / 2
cwnd = 1 MSS
```

Poi TCP riparte in slow start.

---

## Domanda 9

Cosa succede dopo tre duplicate ACK?

Dipende dalla variante.

In Tahoe:

```text
ssthreshold = cwnd / 2
cwnd = 1 MSS
```

In Reno:

```text
ssthreshold = cwnd / 2
cwnd = ssthreshold + 3 MSS
```

---

## Domanda 10

Cos’è RED?

RED è una politica router-based di congestion avoidance.

Il router calcola la lunghezza media della coda e, se questa supera una soglia minima, inizia a scartare pacchetti con probabilità crescente.

Lo scarto anticipato segnala ai mittenti TCP di rallentare prima che il buffer sia completamente pieno.

---

# 36. Errori comuni da evitare

## Errore 1

Confondere `AdvertisedWindow` e `CongestionWindow`.

- `AdvertisedWindow` viene dal ricevente.
- `CongestionWindow` viene stimata dal mittente.

## Errore 2

Dire che Slow Start è lenta.

Slow Start è lenta solo rispetto all’invio immediato di una finestra enorme.

Rispetto all’additive increase, è veloce perché cresce esponenzialmente.

## Errore 3

Dire che RED evita sempre le perdite.

RED usa proprio alcune perdite anticipate per evitare perdite peggiori in futuro.

## Errore 4

Confondere FIFO e Tail Drop.

FIFO è una disciplina di scheduling.

Tail Drop è una politica di scarto.

Possono essere usate insieme, ma sono concetti diversi.

## Errore 5

Pensare che Fair Queuing faccia semplice round-robin tra pacchetti.

Fair Queuing cerca di approssimare un round-robin bit per bit, tenendo conto della dimensione dei pacchetti.

---

# 37. Schema finale mentale

```text
Problema:
    molte sorgenti condividono link e buffer

Se i pacchetti sono troppi:
    code crescono
    buffer pieni
    pacchetti persi
    congestione

Soluzioni:
    1. Resource Allocation
        - router-centric
        - reservation-based
        - QoS
        - scheduling

    2. Congestion Control
        - host-centric
        - TCP
        - AIMD
        - Slow Start
        - Fast Retransmit
        - Fast Recovery

    3. Congestion Avoidance
        - RED
        - RTT-based
        - source-based avoidance
```

---

# 38. Mini-riassunto orale

In questo capitolo si studia come una rete gestisce la competizione tra più flussi per risorse limitate come banda e buffer. Quando troppi pacchetti arrivano allo stesso router, si formano code; se i buffer si riempiono, i pacchetti vengono scartati e la rete entra in congestione.

Il problema può essere affrontato tramite allocazione preventiva delle risorse, controllo della congestione o prevenzione della congestione. Nei router si possono usare diverse discipline di accodamento, come FIFO, Priority Queuing e Fair Queuing. FIFO è semplice ma non equa; Priority Queuing permette di favorire traffico sensibile al ritardo; Fair Queuing cerca di distribuire equamente la banda tra i flussi usando timestamp virtuali.

TCP affronta la congestione tramite una variabile chiamata CongestionWindow, che limita quanti byte possono essere in transito. La finestra effettiva è il minimo tra CongestionWindow e AdvertisedWindow. TCP usa AIMD: aumenta lentamente la finestra quando non c’è congestione e la riduce moltiplicativamente quando rileva congestione. All’inizio della connessione usa Slow Start, che fa crescere la finestra esponenzialmente. Per recuperare più rapidamente le perdite usa Fast Retransmit, basato sugli ACK duplicati, e in Reno anche Fast Recovery.

Infine, la congestion avoidance cerca di anticipare la congestione. RED, per esempio, fa scartare anticipatamente alcuni pacchetti quando la lunghezza media della coda supera certe soglie. In questo modo segnala ai mittenti TCP di rallentare prima che il buffer sia completamente pieno.