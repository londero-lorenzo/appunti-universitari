---
title: "Guida Esercizi Esame"
aliases: ["Guida Esercizi Esame"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "guida-esercizi-esame"]
created: 2026-06-09
---
# Guida agli esercizi d’esame di Reti di Calcolatori

Questa guida raggruppa le principali tipologie di esercizi d’esame per argomento, indicando **quando usare una formula/metodo** e **come procedere nella risoluzione**.

---

## 1. Livello fisico e teoria dell’informazione

Questi esercizi riguardano la **capacità dei canali**, la **codifica dei segnali** e il calcolo del **bitrate massimo**.

---

### 1.1 Teorema di Shannon-Hartley

> [!formula] Formula  
> $$  
> C = B \log\_2(1 + SNR)  
> $$
> 
> dove:
> 
> - $C$ = capacità massima del canale;
>     
> - $B$ = larghezza di banda;
>     
> - $SNR$ = rapporto segnale/rumore in forma lineare.
>     

#### Quando si usa

Si usa per calcolare la **capacità massima di un canale rumoroso**.

#### Procedura

1. Individua la larghezza di banda $B$.
    
2. Se il rapporto segnale/rumore è espresso in decibel, trasformalo in valore lineare:
    

$$  
SNR = 10^{\frac{dB}{10}}  
$$

3. Applica la formula di Shannon-Hartley:
    

$$  
C = B \log\_2(1 + SNR)  
$$

4. Se viene richiesta la capacità netta con una codifica, moltiplica per l’efficienza della codifica.
    

Esempio:

$$  
\text{Efficienza 4B/5B} = \frac{4}{5}  
$$

quindi:

$$  
C\_{\text{netta}} = C \cdot \frac{4}{5}  
$$

---

### 1.2 Teorema di Nyquist

> [!formula] Formula  
> $$  
> R\_{\max} = 2B \log\_2 L  
> $$
> 
> dove:
> 
> - $B$ = banda del canale;
>     
> - $L$ = numero di livelli o simboli del segnale.
>     

#### Quando si usa

Si usa per canali **senza rumore**, quando si conosce il numero di livelli del segnale.

#### Procedura

1. Individua la banda $B$.
    
2. Individua il numero di livelli $L$.
    
3. Calcola:
    

$$  
R\_{\max} = 2 \cdot B \cdot \log\_2 L  
$$

---

### 1.3 Modulazione e bitrate

#### Quando si usa

Si usa quando l’esercizio chiede di calcolare il **numero di bit per simbolo** oppure il **bitrate** a partire da una modulazione.

#### Procedura

1. Calcola i bit per simbolo:
    

$$  
\text{bit per simbolo} = \log\_2(\text{numero di simboli})  
$$

2. Calcola il bitrate:
    

$$  
\text{bitrate} = \text{simboli al secondo} \cdot \text{bit per simbolo}  
$$

---

## 2. Livello datalink

Questa categoria comprende:

- controllo degli errori;
    
- CRC;
    
- probabilità di errore;
    
- efficienza del mezzo;
    
- protocolli MAC;
    
- Ethernet;
    
- Wi-Fi;
    
- Bluetooth;
    
- sliding window;
    
- stop-and-wait.
    

---

### 2.1 Controllo degli errori: CRC

#### Quando si usa

Si usa per verificare l’integrità dei dati tramite un **polinomio generatore**.

#### Verifica di un frame ricevuto

1. Prendi la sequenza di bit ricevuta.
    
2. Dividila per il polinomio generatore usando la divisione binaria modulo 2.
    
3. Controlla il resto.
    

> [!important] Regola  
> Se il resto è zero, il frame è considerato corretto.
> 
> Se il resto è diverso da zero, il frame contiene un errore rilevato.

#### Generazione del CRC da trasmettere

1. Prendi i dati originali.
    
2. Aggiungi $n$ zeri, dove $n$ è il grado del polinomio generatore.
    
3. Dividi la nuova sequenza per il polinomio.
    
4. Usa il resto come bit di controllo.
    
5. Trasmetti:
    

$$  
\text{dati originali} + \text{CRC}  
$$

---

### 2.2 Probabilità di errore

#### Quando si usa

Si usa per calcolare la probabilità che un frame arrivi integro.

#### Formula

Se la probabilità di errore di un bit è $p$, allora la probabilità che un bit sia corretto è:

$$  
1 - p  
$$

Per un frame di $L$ bit:

$$  
P(\text{frame corretto}) = (1-p)^L  
$$

#### Procedura

1. Individua la probabilità di errore per bit $p$.
    
2. Individua la lunghezza del frame $L$.
    
3. Applica:
    

$$  
(1-p)^L  
$$

---

### 2.3 Efficienza e banda netta

#### Quando si usa

Si usa quando l’esercizio chiede il **throughput reale** o l’**efficienza del canale**, considerando overhead, intestazioni, CRC, preambolo, spazi inter-frame ecc.

#### Procedura

1. Somma tutti i bit trasmessi in un ciclo:
    
    - preambolo;
        
    - header;
        
    - payload;
        
    - CRC;
        
    - IPG / inter-frame gap;
        
    - eventuali ACK;
        
    - eventuali pause.
        
2. Calcola il tempo totale del ciclo.
    
3. Calcola il tempo utile, cioè quello dedicato al payload.
    
4. Calcola l’efficienza:
    

$$  
\eta = \frac{\text{tempo di trasmissione del payload}}{\text{tempo totale del ciclo}}  
$$

Oppure, in termini di bit:

$$  
\eta = \frac{\text{bit utili}}{\text{bit totali trasmessi}}  
$$

5. Calcola la banda netta:
    

$$  
\text{banda netta} = \text{banda lorda} \cdot \eta  
$$

---

### 2.4 Collisioni Ethernet: CSMA/CD

#### Quando si usa

Si usa per esercizi su Ethernet condivisa, collisioni e backoff.

#### Idea principale

Dopo una collisione, la stazione non ritrasmette subito, ma attende un tempo casuale calcolato con il **binary exponential backoff**.

#### Procedura

Dopo l’$n$-esima collisione:

1. Si sceglie un valore casuale $k$ nell’intervallo:
    

$$  
0 \leq k \leq 2^n - 1  
$$

2. Il tempo di attesa è:
    

$$  
T\_{\text{attesa}} = k \cdot \text{slot time}  
$$

3. Se viene richiesto il tempo medio, usa il valore medio di $k$:
    

$$  
k\_{\text{medio}} = \frac{2^n - 1}{2}  
$$

4. Quindi:
    

$$  
T\_{\text{medio}} = k\_{\text{medio}} \cdot \text{slot time}  
$$

In alcuni esercizi può essere richiesto di aggiungere anche l’IPG:

$$  
T\_{\text{totale}} = IPG + T\_{\text{medio}}  
$$

---

### 2.5 Wi-Fi: CSMA/CA, RTS e CTS

#### Quando si usa

Si usa per esercizi su Wi-Fi, terminale nascosto, RTS/CTS e accesso al mezzo.

#### Concetto fondamentale

In Wi-Fi non si rilevano collisioni come in Ethernet classica. Si cerca quindi di **evitarle** usando meccanismi di attesa e, se previsto, RTS/CTS.

#### Regola RTS/CTS

- Una stazione invia un RTS.
    
- Il destinatario risponde con un CTS.
    
- Le altre stazioni che sentono il CTS capiscono che il mezzo sarà occupato.
    
- Una stazione che riceve un CTS non indirizzato a lei evita di trasmettere.
    

> [!important] Da ricordare  
> Una stazione non trasmette se riceve un CTS destinato a un’altra stazione, perché deve evitare interferenze.

---

### 2.6 Bluetooth e occupazione degli slot

#### Quando si usa

Si usa quando l’esercizio chiede il throughput utile in Bluetooth, considerando slot master/slave e overhead.

#### Procedura

1. Individua la durata di uno slot.
    
2. Capisci quanti slot compongono un ciclo.
    

Esempio:

$$  
3 \text{ slot master} + 1 \text{ slot slave}  
$$

3. Calcola la durata totale del ciclo.
    
4. Sottrai gli overhead:
    
    - header;
        
    - pause;
        
    - eventuali bit non utili.
        
5. Calcola i bit utili trasmessi nel ciclo.
    
6. Calcola il throughput:
    

$$  
\text{throughput} = \frac{\text{bit utili}}{\text{tempo del ciclo}}  
$$

---

### 2.7 Sliding Window e Stop-and-Wait

#### Quando si usa

Si usa per esercizi su numeri di sequenza, finestre di trasmissione e ACK.

#### Stop-and-Wait

Nel protocollo stop-and-wait:

- il mittente invia un frame;
    
- attende l’ACK;
    
- solo dopo l’ACK può inviare il frame successivo.
    

Serve un numero di sequenza minimo per distinguere frame nuovi da ritrasmissioni.

---

#### Sliding Window

In una sliding window, il mittente può inviare più frame senza attendere subito gli ACK.

#### Regola importante

Se si usano $n$ bit per i numeri di sequenza, i numeri disponibili sono:

$$  
2^n  
$$

Per evitare ambiguità, la finestra non deve superare:

$$  
\frac{2^n}{2}  
$$

Quindi:

$$  
W\_{\max} = 2^{n-1}  
$$

---

## 3. Livello rete: IP

Questi esercizi riguardano:

- indirizzamento IP;
    
- subnetting;
    
- CIDR;
    
- routing;
    
- tabelle di inoltro;
    
- frammentazione;
    
- ARP;
    
- DHCP;
    
- NAT.
    

---

### 3.1 Subnetting e CIDR

#### Quando si usa

Si usa per:

- dividere una rete in sottoreti;
    
- trovare la rete minima che contiene più indirizzi;
    
- determinare maschera, prefisso e numero di host.
    

---

### 3.2 Trovare la rete minima

#### Procedura

1. Scrivi gli indirizzi IP in binario.
    
2. Confronta i bit da sinistra verso destra.
    
3. Trova il prefisso comune più lungo.
    
4. Il prefisso comune determina la rete minima.
    

Esempio concettuale:

```text
IP1: 11000000.10101000.00000001.xxxxxxxx
IP2: 11000000.10101000.00000001.yyyyyyyy
```

La parte comune diventa il prefisso della rete.

---

### 3.3 Creare sottoreti

#### Procedura

1. Individua il numero di host richiesti.
    
2. Trova la potenza di 2 successiva.
    

Esempio:

Se servono 50 host:

$$  
2^5 = 32 \quad \text{non basta}  
$$

$$  
2^6 = 64 \quad \text{basta}  
$$

3. Ricorda che, nelle reti tradizionali, due indirizzi sono riservati:
    
    - indirizzo di rete;
        
    - indirizzo di broadcast.
        

Quindi gli host effettivi sono:

$$  
2^h - 2  
$$

4. Determina il numero di bit host $h$.
    
5. Il prefisso sarà:
    

$$  
/(32-h)  
$$

---

### 3.4 Tabelle di inoltro: routing tables

#### Quando si usa

Si usa quando bisogna costruire la tabella di routing di un router.

#### Procedura

Per ogni rete di destinazione:

1. Verifica se la rete è direttamente connessa.
    
2. Se è direttamente connessa, indica l’interfaccia di uscita.
    
3. Se non è direttamente connessa, indica il next hop.
    
4. Aggiungi, se necessario, una rotta di default.
    

La rotta di default è:

$$  
0.0.0.0/0  
$$

oppure semplicemente:

$$  
/0  
$$

#### Struttura tipica della tabella

|Destinazione|Maschera / prefisso|Next hop|Interfaccia|
|---|--:|---|---|
|Rete direttamente connessa|`/x`|—|interfaccia locale|
|Rete remota|`/x`|IP router successivo|interfaccia di uscita|
|Default|`/0`|gateway|interfaccia di uscita|

---

### 3.5 Algoritmi di routing

---

#### Distance Vector

##### Quando si usa

Si usa per esercizi in cui i router aggiornano le proprie tabelle scambiandosi vettori di distanza con i vicini.

##### Procedura

1. Ogni router riceve dal vicino una tabella delle distanze.
    
2. Per ogni destinazione, somma:
    

$$  
\text{costo verso vicino} + \text{costo dichiarato dal vicino}  
$$

3. Se il nuovo costo è minore di quello attuale, aggiorna la tabella.
    

Formula generale:

$$  
D\_x(y) = \min\_v { c(x,v) + D\_v(y) }  
$$

dove:

- $D\_x(y)$ = distanza stimata da $x$ a $y$;
    
- $c(x,v)$ = costo del link tra $x$ e il vicino $v$;
    
- $D\_v(y)$ = distanza dichiarata dal vicino $v$ verso $y$.
    

---

#### Link State

##### Quando si usa

Si usa per esercizi su flooding, LSP e costruzione della mappa della rete.

##### Procedura

1. Ogni router genera un Link State Packet.
    
2. Il pacchetto contiene informazioni sui collegamenti del router.
    
3. Gli LSP vengono diffusi tramite flooding.
    
4. Se un router riceve più versioni dello stesso LSP, tiene quella con numero di sequenza più alto.
    
5. Dopo aver costruito la mappa completa, calcola i cammini minimi.
    

---

### 3.6 Frammentazione IP

#### Quando si usa

Si usa quando un pacchetto IP deve attraversare un link con MTU più piccola della dimensione del pacchetto.

#### Procedura

1. Individua la MTU.
    
2. Sottrai l’header IP, di solito 20 byte:
    

$$  
\text{payload massimo} = MTU - 20  
$$

3. Il payload di ogni frammento, tranne l’ultimo, deve essere multiplo di 8 byte.
    
4. Dividi il payload originario in frammenti.
    
5. Calcola l’offset di ogni frammento:
    

$$  
\text{offset} = \frac{\text{byte iniziale del frammento}}{8}  
$$

6. Imposta il flag MF:
    
    - MF = 1 per tutti i frammenti tranne l’ultimo;
        
    - MF = 0 per l’ultimo frammento.
        

#### Schema utile

|Frammento|Payload|Offset|MF|
|--:|--:|--:|--:|
|1|multiplo di 8|0|1|
|2|multiplo di 8|offset calcolato|1|
|ultimo|anche non multiplo di 8|offset calcolato|0|

---

### 3.7 ARP

#### Quando si usa

Si usa quando bisogna associare un indirizzo IP a un indirizzo MAC nella rete locale.

#### Regola

Una risposta ARP contiene il MAC address dell’host richiesto.

Esempio:

```text
Chi ha IP 192.168.1.10?
Risposta: 192.168.1.10 ha MAC AA:BB:CC:DD:EE:FF
```

---

### 3.8 DHCP

#### Quando si usa

Si usa per esercizi sulla configurazione automatica degli host.

#### Concetto

DHCP assegna automaticamente:

- indirizzo IP;
    
- maschera;
    
- gateway;
    
- DNS;
    
- durata del lease.
    

#### Nota importante

Più server DHCP possono coesistere nella stessa LAN solo se i range di IP assegnati non si sovrappongono.

---

### 3.9 NAT

#### Quando si usa

Si usa per esercizi in cui un router modifica indirizzi IP e porte tra rete privata e rete pubblica.

#### Concetto

Un router NAT modifica l’IP sorgente dei pacchetti in uscita, sostituendolo con il proprio IP pubblico.

#### Caso importante

Se l’IP pubblico del NAT cambia durante una connessione TCP, la connessione cade.

Motivo:

- TCP identifica la connessione anche tramite indirizzi IP e porte;
    
- se l’IP cambia, l’altro host riceve pacchetti da un indirizzo inatteso;
    
- i pacchetti vengono scartati.
    

---

## 4. Livello trasporto: TCP e UDP

Questi esercizi riguardano:

- stati TCP;
    
- gestione delle socket;
    
- buffer;
    
- finestre;
    
- controllo della congestione;
    
- algoritmo di Nagle;
    
- fair queueing.
    

---

### 4.1 Stati delle socket TCP

#### Quando si usa

Si usa quando bisogna ricostruire le transizioni di stato di una connessione TCP.

#### Stati comuni

|Stato|Significato|
|---|---|
|`ESTABLISHED`|Connessione attiva|
|`FIN_WAIT_1`|È stata chiamata `close()` e inviato FIN|
|`FIN_WAIT_2`|Il FIN è stato riscontrato con ACK|
|`CLOSE_WAIT`|È stato ricevuto FIN dall’altro lato|
|`LAST_ACK`|È stato inviato FIN dopo aver ricevuto FIN|
|`TIME_WAIT`|Attesa finale prima di chiudere definitivamente|
|`CLOSED`|Connessione chiusa|

#### Regole importanti

- Una `close()` attiva porta in `FIN_WAIT_1`.
    
- Lo stato `TIME_WAIT` dura solitamente $2 \cdot MSL$.
    
- `TIME_WAIT` serve a evitare che vecchi segmenti interferiscano con nuove connessioni.
    

---

### 4.2 Gestione buffer e finestre TCP

#### Quando si usa

Si usa quando l’esercizio chiede:

- quanti byte possono ancora essere inviati;
    
- quanto spazio libero c’è nel buffer;
    
- qual è la finestra effettiva.
    

---

#### Effective Window

> [!formula] Formula  
> $$  
> \text{EffectiveWindow} =  
> \text{AdvertisedWindow} -  
> (\text{LastByteSent} - \text{LastByteAcked})  
> $$

#### Significato

La Effective Window indica quanti byte il mittente può ancora inviare senza superare la finestra annunciata dal destinatario.

---

#### Spazio libero nel buffer

> [!formula] Formula  
> $$  
> \text{SpazioLibero} =  
> \text{MaxBufferSize} -  
> (\text{LastByteWritten} - \text{LastByteAcked})  
> $$

#### Procedura

1. Individua `LastByteSent`.
    
2. Individua `LastByteAcked`.
    
3. Individua `AdvertisedWindow`.
    
4. Calcola i byte già inviati ma non ancora confermati:
    

$$  
\text{byte in volo} = \text{LastByteSent} - \text{LastByteAcked}  
$$

5. Sottrai questi byte dalla finestra annunciata.
    

---

### 4.3 Controllo della congestione TCP

#### Quando si usa

Si usa per esercizi su:

- slow start;
    
- congestion avoidance;
    
- crescita della congestion window;
    
- timeout;
    
- perdita di pacchetti.
    

---

#### Slow Start

In slow start, la congestion window cresce rapidamente.

Di solito, per ogni RTT:

$$  
cwnd \leftarrow 2 \cdot cwnd  
$$

finché non viene raggiunta la soglia `ssthresh`.

---

#### Congestion Avoidance

In fase additiva, la congestion window cresce più lentamente.

Indicativamente:

$$  
cwnd \leftarrow cwnd + 1 MSS  
$$

per ogni RTT.

---

#### Timeout

In caso di timeout, tipicamente:

- `ssthresh` viene aggiornata;
    
- `cwnd` viene ridotta.
    

Spesso:

$$  
ssthresh = \frac{cwnd}{2}  
$$

e:

$$  
cwnd = 1 MSS  
$$

A seconda dell’algoritmo specifico, il comportamento può cambiare.

---

### 4.4 Algoritmo di Nagle

#### Quando si usa

Si usa per esercizi in cui l’applicazione produce piccoli segmenti TCP e bisogna capire quando vengono inviati.

#### Idea principale

L’algoritmo di Nagle evita di inviare tanti piccoli segmenti se ci sono dati non ancora riscontrati.

#### Procedura

1. Calcola quanti dati produce l’applicazione in un RTT.
    
2. Confronta questa quantità con MSS.
    
3. Se i dati accumulati raggiungono MSS, viene inviato un segmento pieno.
    
4. Se ci sono dati non confermati, i piccoli segmenti possono essere trattenuti.
    

> [!important] Regola pratica  
> Se l’applicazione produce più di un MSS per RTT, verrà inviato un segmento ogni volta che si raggiunge MSS.

---

### 4.5 Fair Queueing

#### Quando si usa

Si usa quando bisogna determinare l’ordine di trasmissione dei pacchetti appartenenti a flussi diversi.

#### Procedura

1. Dividi i pacchetti per flusso.
    
2. Per ogni pacchetto, calcola il tempo di fine trasmissione virtuale.
    
3. Trasmetti i pacchetti in ordine crescente di tempo di fine virtuale.
    

#### Idea

Il fair queueing cerca di distribuire equamente la capacità del link tra i flussi attivi.

---

## 5. Sicurezza

Questa sezione riguarda:

- crittografia;
    
- cifrari a blocchi;
    
- modalità operative;
    
- autenticazione;
    
- challenge-response;
    
- CIA;
    
- certificati;
    
- firme digitali;
    
- RSA;
    
- X.509.
    

---

### 5.1 Crittografia e modalità operative

#### CBC

In CBC, ogni blocco dipende dal blocco precedente.

Caratteristiche:

- richiede IV;
    
- non permette accesso casuale efficiente;
    
- un errore può propagarsi parzialmente.
    

---

#### CTR / OFB

CTR e OFB generano uno stream di bit da combinare con il testo in chiaro.

Caratteristiche:

- funzionano in modo simile a stream cipher;
    
- CTR è adatto all’accesso casuale;
    
- non bisogna mai riutilizzare la stessa coppia chiave + IV/nonce.
    

> [!danger] Attenzione  
> Usare la stessa chiave e lo stesso IV/nonce in modalità stream espone all’attacco del keystream uguale.

---

### 5.2 Attacco del keystream uguale

Se due messaggi sono cifrati con lo stesso keystream:

$$  
C\_1 = P\_1 \oplus K  
$$

$$  
C\_2 = P\_2 \oplus K  
$$

allora:

$$  
C\_1 \oplus C\_2 = P\_1 \oplus P\_2  
$$

Il keystream si cancella, permettendo all’attaccante di ricavare informazioni sui testi in chiaro.

---

### 5.3 Protocolli di autenticazione e challenge-response

#### Quando si usa

Si usa quando bisogna stabilire se un host o un utente è davvero autenticato.

#### Concetto

Un’entità è autenticata se dimostra di conoscere un segreto, per esempio:

- una chiave simmetrica;
    
- una chiave privata;
    
- una password;
    
- un token segreto.
    

#### Challenge-response

1. Il verificatore invia una sfida, detta nonce.
    
2. L’entità da autenticare calcola una risposta usando il proprio segreto.
    
3. Il verificatore controlla la risposta.
    
4. Se la risposta è corretta, l’entità è autenticata.
    

#### Perché serve il nonce?

Il nonce impedisce il replay attack.

> [!important] Regola  
> Una risposta vecchia non deve poter essere riutilizzata in una nuova sessione.

---

### 5.4 Attacchi Man-in-the-Middle

#### Quando controllare la possibilità di MITM

Bisogna sospettare un attacco Man-in-the-Middle quando:

- manca autenticazione reciproca;
    
- le chiavi pubbliche non sono certificate;
    
- non ci sono firme;
    
- il protocollo non lega l’identità alla chiave;
    
- un nonce può essere riutilizzato;
    
- un messaggio può essere inoltrato senza essere modificato.
    

#### Domande da farsi

- Chi sta autenticando chi?
    
- La chiave pubblica è davvero dell’entità corretta?
    
- Il messaggio è firmato?
    
- Il nonce è fresco?
    
- Un attaccante può fare da ponte tra due parti?
    

---

### 5.5 Aspetti CIA

CIA significa:

- Confidenzialità;
    
- Integrità;
    
- Disponibilità.
    

---

#### Confidenzialità

Protegge i dati dalla lettura non autorizzata.

Esempio di attacco:

```text
sniffing
```

Tipo di attacco:

```text
passivo
```

---

#### Integrità

Protegge i dati dalla modifica non autorizzata.

Esempio di attacco:

```text
modifica dei pacchetti
```

Tipo di attacco:

```text
attivo
```

---

#### Disponibilità

Protegge il servizio dall’interruzione.

Esempio di attacco:

```text
DoS / Denial of Service
```

Tipo di attacco:

```text
attivo
```

---

### 5.6 Certificati, firme digitali e RSA

---

#### Firma digitale RSA

#### Procedura concettuale

1. Si calcola l’hash del messaggio.
    
2. L’hash viene cifrato con la chiave privata del firmatario.
    
3. Il destinatario verifica la firma usando la chiave pubblica del firmatario.
    

Schema:

$$  
\text{firma} = E\_{\text{privata}}(H(M))  
$$

Verifica:

$$  
H(M) \stackrel{?}{=} D\_{\text{pubblica}}(\text{firma})  
$$

---

### 5.7 Certificati X.509

#### Quando si usa

Si usa per esercizi su PKI, certificati, CA e autenticazione delle chiavi pubbliche.

#### Concetto

Un certificato X.509 lega una chiave pubblica a un soggetto.

Contiene tipicamente:

- subject;
    
- chiave pubblica del subject;
    
- issuer;
    
- periodo di validità;
    
- firma della CA;
    
- algoritmo di firma.
    

> [!important] Regola fondamentale  
> La chiave privata è generata e posseduta solo dal subject, cioè dal proprietario del certificato.
> 
> La CA non possiede la chiave privata del subject.

#### Ruolo della CA

La CA:

- verifica l’identità del subject;
    
- firma il certificato;
    
- garantisce che quella chiave pubblica appartiene a quel subject.
    

---

## Schema di ripasso rapido

|Argomento|Formula / metodo chiave|Quando usarlo|
|---|---|---|
|Shannon-Hartley|$C = B \log\_2(1+SNR)$|Canale rumoroso|
|Nyquist|$2B \log\_2 L$|Canale senza rumore|
|Bit per simbolo|$\log\_2 L$|Modulazione|
|CRC|Divisione modulo 2|Controllo errori|
|Frame corretto|$(1-p)^L$|Probabilità di integrità|
|Efficienza|$\frac{\text{bit utili}}{\text{bit totali}}$|Throughput netto|
|CSMA/CD|Backoff esponenziale|Collisioni Ethernet|
|Sliding window|$W\_{\max}=2^{n-1}$|Numeri di sequenza|
|Subnetting|Potenze di 2|Host e sottoreti|
|Frammentazione IP|MTU - header|Pacchetti troppo grandi|
|TCP Effective Window|$AW - (LBS-LBA)$|Dati ancora inviabili|
|Congestion control|`cwnd`, `ssthresh`|Perdita e congestione|
|Challenge-response|Nonce + segreto|Autenticazione|
|CIA|C / I / A|Classificazione attacchi|
|X.509|CA firma certificato|Identità e chiavi pubbliche|

---

## Checklist per affrontare un esercizio

-  Individuare il livello coinvolto: fisico, datalink, rete, trasporto o sicurezza.
    
-  Capire se l’esercizio è numerico, teorico o misto.
    
-  Scrivere i dati noti.
    
-  Scrivere la formula o il protocollo da usare.
    
-  Controllare le unità di misura.
    
-  Convertire eventuali valori in dB.
    
-  Verificare se ci sono overhead.
    
-  Disegnare uno schema se ci sono router, link o finestre TCP.
    
-  Controllare casi particolari: ultimo frammento, rotta default, ACK mancanti, nonce riutilizzati.
    
-  Scrivere una conclusione esplicita.
    

---

## Collegamenti consigliati

- [[Livello fisico]]
    
- [[Livello datalink]]
    
- [[Livello rete]]
    
- [[TCP]]
    
- [[UDP]]
    
- [[Subnetting]]
    
- [[Routing]]
    
- [[Sicurezza informatica]]
    
- [[Crittografia]]
    
- [[Certificati digitali]]