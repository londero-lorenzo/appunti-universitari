---
title: "Capitolo 8"
aliases: ["Capitolo 8"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-8"]
created: 2026-05-05
---
Di seguito trovi appunti in formato Markdown/Obsidian basati sulle slide _Reti - Chapter 8: Network Security_.

---

# Reti di Calcolatori — Capitolo 8: Network Security

#reti #sicurezza #crittografia #tls #network-security

## 1. Perché serve la sicurezza nelle reti

Nelle reti moderne l’informazione non è più concentrata fisicamente in un solo luogo. Gli utenti autorizzati possono inviare, recuperare e modificare informazioni a distanza. Questo significa che non basta più proteggere soltanto il computer dove i dati sono memorizzati: bisogna proteggere anche i canali di comunicazione.

In una rete, un attaccante può:

- intercettare dati durante la trasmissione;
    
- modificare messaggi;
    
- impersonare altri utenti;
    
- bloccare o rallentare servizi;
    
- analizzare il traffico anche senza leggere il contenuto dei messaggi.
    

La sicurezza di rete nasce quindi per proteggere **informazioni**, **sistemi** e **comunicazioni** in un ambiente distribuito.

---

## 2. Strategia generale per affrontare un problema di sicurezza

Una strategia generale per progettare la sicurezza consiste in questi passi:

1. **Identificare gli asset da proteggere**
    
    - dati;
        
    - servizi;
        
    - credenziali;
        
    - infrastruttura;
        
    - reputazione;
        
    - disponibilità del sistema.
        
2. **Definire gli obiettivi di sicurezza**
    
    - confidenzialità;
        
    - integrità;
        
    - disponibilità;
        
    - autenticazione;
        
    - non ripudio;
        
    - controllo degli accessi.
        
3. **Stabilire una security policy**
    
    - chi può fare cosa;
        
    - quali risorse sono accessibili;
        
    - quali comportamenti sono vietati;
        
    - quali livelli di rischio sono accettabili.
        
4. **Identificare le minacce**
    
    - intercettazione;
        
    - modifica;
        
    - spoofing;
        
    - replay;
        
    - DoS;
        
    - furto di chiavi;
        
    - compromissione di dispositivi.
        
5. **Sviluppare servizi e meccanismi di sicurezza**
    
    - cifratura;
        
    - firme digitali;
        
    - MAC;
        
    - hash;
        
    - autenticazione;
        
    - certificati;
        
    - protocolli sicuri;
        
    - piani di recovery.
        

---

## 3. Sicurezza come compromesso

La sicurezza ha sempre un costo:

- costo economico;
    
- costo computazionale;
    
- costo umano di configurazione e gestione;
    
- aumento della complessità software;
    
- peggioramento dell’usabilità;
    
- possibili fastidi per gli utenti.
    

Tuttavia, l’assenza di sicurezza può costare molto di più:

- perdita di dati importanti;
    
- danni economici;
    
- danni reputazionali;
    
- conseguenze legali o penali.
    

Una formula utile è:

$$  
Cost\ of\ Security\ Services \leq Cost\ from\ asset\ loss \cdot Loss\ probability  
$$

dove:

$$  
Loss\ probability = Vulnerability\ probability \cdot Attack\ probability  
$$

Quindi la sicurezza è conveniente quando il costo delle contromisure è inferiore al danno atteso.

> [!IMPORTANT]  
> Non si può massimizzare contemporaneamente sicurezza, funzionalità e semplicità d’uso. Aumentare molto la sicurezza spesso riduce l’usabilità o aumenta la complessità.

---

## 4. Obiettivi fondamentali: triade CIA

Il modello più comune per descrivere gli obiettivi di sicurezza è la **CIA triad**:

```text
Confidentiality
Integrity
Availability
```

### 4.1 Confidentiality — Confidenzialità

La confidenzialità significa che le informazioni devono essere accessibili solo a entità autorizzate.

Esempi:

- impedire che qualcuno legga una password;
    
- impedire che un attaccante intercetti dati bancari;
    
- proteggere il contenuto di una comunicazione.
    

Il meccanismo principale è la **cifratura**, ma non basta sempre: anche il traffico cifrato può rivelare metadati, per esempio chi comunica con chi e quando.

---

### 4.2 Integrity — Integrità

L’integrità significa che le informazioni non devono essere modificate in modo non autorizzato.

Serve a garantire che:

- il messaggio ricevuto sia uguale a quello inviato;
    
- eventuali modifiche siano rilevate;
    
- solo soggetti autorizzati possano cambiare dati.
    

Esempi:

- un bonifico non deve poter essere modificato durante la trasmissione;
    
- un file scaricato non deve essere alterato da un attaccante;
    
- una configurazione di rete non deve essere manipolata.
    

---

### 4.3 Availability — Disponibilità

La disponibilità significa che le risorse devono essere accessibili agli utenti autorizzati quando servono.

Esempi:

- un sito web deve rimanere raggiungibile;
    
- un server DNS deve continuare a rispondere;
    
- una rete aziendale deve rimanere operativa.
    

Gli attacchi tipici contro la disponibilità sono i **DoS** e **DDoS**.

---

## 5. Concetti base: threat, attack, service, mechanism

|Concetto|Significato|
|---|---|
|**Asset**|Risorsa da proteggere|
|**Threat**|Minaccia potenziale|
|**Vulnerability**|Debolezza che può essere sfruttata|
|**Attack**|Azione concreta che compromette la sicurezza|
|**Security service**|Servizio che aumenta la sicurezza|
|**Security mechanism**|Meccanismo tecnico usato per realizzare un servizio|

Esempio:

- asset: testi degli esami sul computer del professore;
    
- threat: studenti interessati a leggerli;
    
- vulnerability: il computer viene lasciato incustodito;
    
- attack: qualcuno usa il computer senza permesso;
    
- service: autenticazione;
    
- mechanisms: password, smart card, impronta digitale, guardia, riconoscimento vocale.
    

---

## 6. Tipi di attacchi nelle comunicazioni di rete

Gli attacchi si possono classificare in base all’obiettivo colpito:

```text
Confidentiality → snooping, traffic analysis
Integrity → modification, masquerading, replaying, repudiation
Availability → denial of service
```

---

## 7. Attacchi alla confidenzialità

### 7.1 Snooping

Lo **snooping** è l’accesso non autorizzato ai dati.

Può avvenire tramite:

- accesso abusivo a un computer;
    
- furto di password;
    
- malware;
    
- social engineering;
    
- sniffing del traffico di rete.
    

Contromisura principale:

```text
cifratura dei dati
```

---

### 7.2 Traffic analysis

La **traffic analysis** consiste nel ricavare informazioni osservando il traffico, anche senza leggerne il contenuto.

Esempio:

- non so cosa Alice e Bob si stanno dicendo;
    
- però vedo che comunicano spesso;
    
- vedo a che ora comunicano;
    
- vedo quanto traffico scambiano;
    
- posso dedurre relazioni o attività.
    

> [!WARNING]  
> La cifratura protegge il contenuto, ma non necessariamente i metadati.

---

## 8. Attacchi all’integrità

### 8.1 Modification

L’attaccante intercetta un messaggio e lo modifica.

Esempio:

```text
Alice invia: "Paga 100€ a Bob"
Attaccante modifica: "Paga 1000€ a Eve"
```

A volte l’attaccante non modifica il contenuto, ma:

- cancella il messaggio;
    
- lo ritarda;
    
- cambia l’ordine dei messaggi.
    

---

### 8.2 Masquerading / spoofing

L’attaccante finge di essere qualcun altro.

Può impersonare:

- il mittente;
    
- il destinatario;
    
- entrambi.
    

Caso tipico:

```text
Man-in-the-middle
```

L’attaccante si mette tra due parti e fa credere a ciascuna di parlare direttamente con l’altra.

---

### 8.3 Replay attack

Nel **replay attack**, l’attaccante registra un messaggio valido e lo reinvia in seguito.

Esempio:

```text
Alice invia a banca: "Trasferisci 100€"
Eve registra il messaggio
Eve lo reinvia più tardi
La banca esegue di nuovo l’operazione
```

Contromisure:

- nonce;
    
- timestamp;
    
- numeri di sequenza;
    
- chiavi di sessione fresche.
    

---

### 8.4 Repudiation

Il **ripudio** avviene quando una delle due parti nega di aver partecipato a una comunicazione.

Due casi:

- il mittente nega di aver inviato il messaggio;
    
- il destinatario nega di averlo ricevuto.
    

La particolarità è che l’attacco non è fatto da un terzo esterno, ma da una delle parti legittime.

Contromisure:

- firme digitali;
    
- ricevute firmate;
    
- notarizzazione;
    
- PEC.
    

---

## 9. Attacchi alla disponibilità

### 9.1 Denial of Service — DoS

Un attacco DoS mira a rallentare o interrompere un servizio.

Strategie:

- inviare richieste false in grande quantità;
    
- cancellare le risposte del server;
    
- cancellare le richieste del client;
    
- costringere il client a ripetere continuamente richieste.
    

### 9.2 Distributed DoS — DDoS

Nel DDoS l’attacco è coordinato da molti dispositivi.

```text
Molti host compromessi → traffico verso un server → saturazione
```

Contromisure generali:

- filtrare traffico illecito;
    
- distribuire il carico;
    
- rendere il costo per l’attaccante non inferiore al costo per il bersaglio;
    
- usare sistemi di mitigazione DDoS.
    

---

## 10. Attacchi passivi e attivi

|Tipo|Descrizione|Esempi|
|---|---|---|
|**Passivo**|L’attaccante osserva senza modificare|snooping, traffic analysis|
|**Attivo**|L’attaccante modifica o influenza il sistema|modification, spoofing, replay, DoS|

Gli attacchi passivi sono difficili da rilevare perché non alterano il sistema. Per questo si punta soprattutto sulla prevenzione.

Gli attacchi attivi sono più difficili da prevenire completamente, ma spesso sono più facili da rilevare perché lasciano effetti osservabili.

---

# 11. Servizi di sicurezza secondo ITU X.800

I principali servizi di sicurezza sono:

1. data confidentiality;
    
2. data integrity;
    
3. authentication;
    
4. non-repudiation;
    
5. access control.
    

La disponibilità è vista più come una proprietà generale dei servizi che come un servizio autonomo.

---

## 11.1 Authentication

L’autenticazione garantisce che un’entità sia davvero chi dice di essere.

Due forme:

|Tipo|Significato|
|---|---|
|**Data origin authentication**|garantisce l’origine di un singolo messaggio|
|**Peer entity authentication**|autentica un’entità durante una connessione/sessione|

Esempio:

- data origin authentication: verifico che una mail venga da Alice;
    
- peer entity authentication: verifico che sto parlando con Alice per tutta la sessione TLS.
    

---

## 11.2 Access control

Il controllo degli accessi impedisce l’uso non autorizzato di una risorsa.

Può riguardare:

- lettura;
    
- scrittura;
    
- modifica;
    
- esecuzione;
    
- cancellazione.
    

Esempio:

```text
Solo gli amministratori possono modificare la configurazione del router.
```

---

## 11.3 Data confidentiality

Protegge dati e metadati dalla divulgazione non autorizzata.

Esempi di meccanismi:

- cifratura;
    
- padding del traffico;
    
- routing control;
    
- VPN.
    

---

## 11.4 Data integrity

Garantisce che i dati ricevuti siano quelli inviati da un’entità autorizzata.

Può includere:

- protezione contro modifiche;
    
- protezione contro replay;
    
- rilevamento di errori o manipolazioni.
    

---

## 11.5 Non-repudiation

Protegge contro la negazione di una comunicazione.

Due tipi:

|Tipo|Significato|
|---|---|
|**Proof of origin**|prova che il mittente ha inviato il messaggio|
|**Proof of delivery**|prova che il destinatario ha ricevuto il messaggio|

Esempio pratico:

```text
La PEC fornisce prova dell’invio e della consegna nella casella del destinatario.
```

---

# 12. Meccanismi di sicurezza

Un meccanismo di sicurezza è una tecnica usata per realizzare servizi di sicurezza.

## 12.1 Encipherment

Consiste nel nascondere i dati tramite cifratura.

Può fornire:

- confidenzialità;
    
- in alcuni casi anche supporto a integrità e autenticazione.
    

Comprende:

- crittografia;
    
- steganografia.
    

---

## 12.2 Data integrity mechanisms

Servono a rilevare modifiche dei dati.

Esempi:

- checksum;
    
- hash;
    
- MAC;
    
- firme digitali.
    

---

## 12.3 Digital signatures

Le firme digitali permettono di garantire:

- origine del messaggio;
    
- integrità;
    
- non ripudio.
    

---

## 12.4 Authentication exchange

Protocollo con cui due parti provano reciprocamente la propria identità.

Esempi:

- challenge-response;
    
- TLS handshake;
    
- Kerberos;
    
- protocolli con nonce.
    

---

## 12.5 Traffic padding

Consiste nell’inserire traffico fittizio per rendere più difficile la traffic analysis.

Esempio:

```text
Anche quando non sto inviando dati reali, genero pacchetti finti.
```

Così l’attaccante fatica a capire quando sto comunicando davvero.

---

## 12.6 Routing control

Consiste nel scegliere o cambiare percorso per evitare link insicuri o intercettabili.

---

## 12.7 Notarization

Una terza parte fidata controlla o certifica una comunicazione.

Serve soprattutto per:

- non ripudio;
    
- validazione temporale;
    
- prova di consegna.
    

---

# 13. Modello del canale insicuro

Il modello del canale insicuro, spesso associato all’impostazione **Dolev-Yao**, assume che la rete non sia affidabile.

L’attaccante può idealmente:

- leggere messaggi;
    
- intercettarli;
    
- modificarli;
    
- cancellarli;
    
- reinviarli;
    
- crearne di nuovi;
    
- impersonare entità.
    

Per progettare sicurezza in questo modello bisogna:

1. progettare una trasformazione sicura, per esempio cifratura;
    
2. generare le informazioni segrete, cioè le chiavi;
    
3. distribuire o condividere le chiavi;
    
4. definire un protocollo che usi algoritmo e chiavi per ottenere il servizio desiderato.
    

---

# 14. Dove implementare la sicurezza

La sicurezza può essere implementata a diversi livelli dello stack.

## 14.1 Link security

La trasformazione di sicurezza avviene su ogni singolo link.

Vantaggi:

- protegge anche header e traffico locale;
    
- può essere trasparente agli utenti.
    

Svantaggi:

- ogni link deve essere protetto separatamente;
    
- i dati devono essere decifrati nei nodi intermedi;
    
- richiede molte chiavi;
    
- vulnerabile nei punti di passaggio, come router o bridge.
    

---

## 14.2 End-to-end security

La protezione avviene tra sorgente iniziale e destinazione finale.

Vantaggi:

- il contenuto resta protetto lungo tutto il percorso;
    
- utile per autenticazione end-to-end;
    
- non richiede fiducia nei nodi intermedi.
    

Svantaggi:

- gli header devono rimanere in chiaro per permettere il routing;
    
- i pattern di traffico possono restare visibili;
    
- maggiore complessità nella gestione delle chiavi.
    

---

## 14.3 Sicurezza ai diversi livelli

|Livello|Sicurezza|Esempi|
|---|---|---|
|Fisico|protezione fisica del mezzo|sensori, sigilli, barriere|
|Data link|protezione del link locale|WEP, WPA, 802.1X|
|Rete|protezione IP|IPsec, VPN|
|Trasporto/sessione|canale end-to-end sicuro|SSL/TLS|
|Applicazione|sicurezza specifica dell’app|SSH, PGP, S/MIME, PEC, Signal|

> [!NOTE]  
> Più si sale di livello, meno informazioni vengono protette, ma la protezione può essere più specifica e più adatta all’applicazione. Più si scende di livello, più la protezione è trasparente, ma diventa più complessa da implementare e gestire.

---

# 15. Cifratura

La cifratura è uno dei meccanismi fondamentali della sicurezza.

Esistono due grandi famiglie:

|Tipo|Nome alternativo|Chiavi|
|---|---|---|
|**Simmetrica**|private key / single key|stessa chiave per cifrare e decifrare|
|**Asimmetrica**|public key|coppia chiave pubblica / chiave privata|

Non sono alternative: vengono spesso usate insieme.

Esempio:

```text
TLS usa crittografia asimmetrica per autenticazione/scambio chiavi
e crittografia simmetrica per cifrare i dati della sessione.
```

---

## 15.1 Terminologia

|Termine|Significato|
|---|---|
|Plaintext|messaggio originale|
|Ciphertext|messaggio cifrato|
|Cipher|algoritmo di cifratura|
|Key|informazione segreta usata dal cipher|
|Encryption|trasformazione plaintext → ciphertext|
|Decryption|trasformazione ciphertext → plaintext|
|Cryptography|studio dei metodi di cifratura|
|Cryptanalysis|studio degli attacchi alla cifratura|
|Cryptology|crittografia + crittoanalisi|

---

# 16. Crittografia simmetrica

Nella crittografia simmetrica mittente e destinatario condividono una stessa chiave segreta.

```text
Alice e Bob condividono K.
Alice cifra con K.
Bob decifra con K.
```

Formalmente:

$$  
Y = E\_K(X)  
$$

$$  
X = D\_K(Y)  
$$

e deve valere:

$$  
D\_K(E\_K(X)) = X  
$$

Se si usa una chiave sbagliata:

$$  
D\_H(E\_K(X)) = error \quad se \quad H \neq K  
$$

---

## 16.1 Requisiti

Per usare in modo sicuro la cifratura simmetrica servono:

1. un algoritmo forte;
    
2. una chiave segreta nota solo a mittente e destinatario.
    

Il problema principale è:

```text
Come distribuisco la chiave segreta in modo sicuro?
```

---

## 16.2 Principio di Kerckhoffs

Il principio di Kerckhoffs dice che la sicurezza non deve dipendere dalla segretezza dell’algoritmo, ma solo dalla segretezza della chiave.

In altre parole:

```text
L’attaccante conosce il sistema.
L’unica cosa che non conosce è la chiave.
```

Questo principio è importante perché un algoritmo segreto può essere scoperto, copiato o analizzato. Un sistema sicuro deve restare sicuro anche se l’algoritmo è pubblico.

---

# 17. Crittoanalisi

La crittoanalisi cerca di ricavare il plaintext o la chiave senza conoscere la chiave.

## 17.1 Tipi di attacco crittoanalitico

|Attacco|Cosa conosce l’attaccante|
|---|---|
|Ciphertext-only|solo ciphertext e algoritmo|
|Known-plaintext|alcune coppie plaintext/ciphertext|
|Chosen-plaintext|può scegliere plaintext e ottenere ciphertext|
|Chosen-ciphertext|può scegliere ciphertext e ottenere plaintext|
|Chosen-text|può scegliere plaintext o ciphertext|

Un buon algoritmo deve resistere almeno agli attacchi **known-plaintext**.

---

## 17.2 Sicurezza incondizionata e computazionale

### Sicurezza incondizionata

Un cifrario ha sicurezza incondizionata se non può essere rotto neanche con potenza computazionale illimitata.

Esempio:

```text
One-Time Pad usato correttamente
```

### Sicurezza computazionale

Un cifrario ha sicurezza computazionale se romperlo è teoricamente possibile, ma praticamente impraticabile.

Questo accade quando:

- il costo dell’attacco supera il valore dell’informazione;
    
- il tempo richiesto è troppo grande;
    
- le risorse necessarie sono irrealistiche.
    

---

## 17.3 Brute force

Il brute force consiste nel provare tutte le chiavi possibili.

È sempre possibile in teoria, ma diventa rapidamente impraticabile se lo spazio delle chiavi è grande.

Esempio concettuale:

```text
Chiave di 32 bit → circa 2^32 possibilità
Chiave di 56 bit → circa 2^56 possibilità
Chiave di 128 bit → circa 2^128 possibilità
```

> [!IMPORTANT]  
> Aumentare la dimensione della chiave aumenta esponenzialmente il costo del brute force.

---

# 18. Stream cipher

Uno stream cipher cifra il messaggio bit per bit o byte per byte.

Funzionamento:

```text
plaintext XOR keystream = ciphertext
ciphertext XOR keystream = plaintext
```

Formula:

$$  
C\_i = M\_i \oplus KS\_i  
$$

dove:

- $C\_i$ è il bit/byte cifrato;
    
- $M\_i$ è il bit/byte del messaggio;
    
- $KS\_i$ è il bit/byte del keystream.
    

---

## 18.1 Proprietà degli stream cipher

Il keystream deve essere:

- pseudocasuale;
    
- con periodo lungo;
    
- non ripetuto;
    
- dipendente da una chiave sufficientemente grande.
    

Regola fondamentale:

> [!DANGER]  
> Non bisogna mai riutilizzare lo stesso keystream.

Se si riusa il keystream:

$$  
C \oplus C' = (M \oplus KS) \oplus (M' \oplus KS) = M \oplus M'  
$$

Il keystream si cancella e rimane una relazione tra i due plaintext.

---

## 18.2 RC4

RC4 è uno stream cipher:

- progettato da Ron Rivest;
    
- orientato ai byte;
    
- molto veloce;
    
- usato storicamente in SSL/TLS, WEP e WPA;
    
- basato su una permutazione interna di valori da 0 a 255.
    

L’idea è:

1. inizializzare un array `S`;
    
2. mischiarlo usando la chiave;
    
3. generare un keystream;
    
4. fare XOR con il messaggio.
    

---

## 18.3 One-Time Pad

Il One-Time Pad usa una chiave:

- veramente casuale;
    
- lunga quanto il messaggio;
    
- usata una sola volta.
    

Se queste condizioni sono rispettate, è incondizionatamente sicuro.

Problemi pratici:

- generare chiavi veramente casuali;
    
- distribuire chiavi lunghe quanto i messaggi;
    
- garantire che la chiave non venga mai riutilizzata.
    

Per questo ha utilità limitata, soprattutto in canali a bassa banda ma ad altissima sicurezza.

---

# 19. Block cipher

Un block cipher cifra blocchi di dimensione fissa.

Esempi:

- DES: blocchi da 64 bit;
    
- AES: blocchi da 128 bit.
    

L’idea è simile a una grande sostituzione:

```text
blocco plaintext → blocco ciphertext
```

Il problema è che una tabella completa di sostituzione sarebbe enorme, quindi i cifrari moderni usano strutture interne più efficienti.

---

## 19.1 AES

AES, Advanced Encryption Standard, è basato sul cifrario Rijndael.

Caratteristiche:

- cifrario simmetrico a blocchi;
    
- blocco dati da 128 bit;
    
- chiavi da 128, 192 o 256 bit;
    
- non è una rete di Feistel;
    
- lavora su una matrice di 4x4 byte;
    
- è iterativo, cioè usa più round.
    

Obiettivi di progetto:

- resistenza agli attacchi noti;
    
- velocità;
    
- compattezza;
    
- semplicità.
    

---

# 20. Modi di funzionamento dei block cipher

Un block cipher cifra blocchi di dimensione fissa, ma nella pratica i messaggi possono avere dimensione arbitraria.

Servono quindi modi di funzionamento:

- ECB;
    
- CBC;
    
- OFB;
    
- CTR.
    

---

## 20.1 ECB — Electronic Codebook

In ECB ogni blocco viene cifrato indipendentemente.

$$  
C\_i = E\_K(P\_i)  
$$

Vantaggio:

- semplice.
    

Svantaggi:

- blocchi plaintext uguali producono blocchi ciphertext uguali;
    
- le ripetizioni restano visibili;
    
- non adatto a dati strutturati o immagini;
    
- debole per messaggi lunghi.
    

Uso tipico:

```text
solo pochi blocchi, spesso un singolo valore
```

---

## 20.2 CBC — Cipher Block Chaining

In CBC ogni blocco plaintext viene combinato con il blocco ciphertext precedente.

$$  
C\_i = E\_K(P\_i \oplus C\_{i-1})  
$$

con:

$$  
C\_0 = IV  
$$

dove `IV` è l’Initialization Vector.

Vantaggi:

- blocchi uguali non producono necessariamente ciphertext uguali;
    
- ogni blocco dipende dai precedenti.
    

Svantaggi:

- serve un IV;
    
- errori o modifiche possono propagarsi;
    
- l’IV deve essere gestito correttamente;
    
- se l’IV è manipolabile, può influenzare il primo blocco.
    

Uso:

- cifratura di file;
    
- email;
    
- traffico web in versioni storiche;
    
- autenticazione in alcuni schemi.
    

---

## 20.3 OFB — Output Feedback

OFB trasforma un block cipher in qualcosa di simile a uno stream cipher.

$$  
O\_i = E\_K(O\_{i-1})  
$$

$$  
C\_i = P\_i \oplus O\_i  
$$

con:

$$  
O\_0 = IV  
$$

Vantaggi:

- gli errori di bit non si propagano;
    
- il keystream può essere calcolato in anticipo.
    

Svantaggi:

- non bisogna mai riutilizzare la stessa sequenza key + IV;
    
- mittente e destinatario devono restare sincronizzati;
    
- più vulnerabile a modifiche del flusso.
    

---

## 20.4 CTR — Counter Mode

CTR cifra un contatore e poi fa XOR con il plaintext.

$$  
O\_i = E\_K(i)  
$$

$$  
C\_i = P\_i \oplus O\_i  
$$

Vantaggi:

- molto efficiente;
    
- parallelizzabile;
    
- adatto ad alte velocità;
    
- consente accesso casuale a blocchi cifrati;
    
- utile per file system cifrati e reti veloci.
    

Svantaggio principale:

> [!DANGER]  
> Non bisogna mai riutilizzare la stessa coppia chiave/contatore.

---

# 21. Integrità e autenticazione dei messaggi

La protezione dei messaggi riguarda:

- integrità del contenuto;
    
- autenticazione del mittente;
    
- protezione contro modifiche;
    
- protezione contro replay;
    
- protezione contro ripudio.
    

Tre strumenti principali:

1. cifratura del messaggio;
    
2. MAC;
    
3. hash.
    

---

## 21.1 Autenticazione tramite cifratura simmetrica

Se Alice e Bob condividono una chiave segreta, e Bob riceve un messaggio cifrato correttamente con quella chiave, Bob può dedurre che il messaggio provenga da qualcuno che conosce la chiave.

Questo fornisce:

- una forma di autenticazione;
    
- una forma di integrità, se il messaggio ha ridondanza o checksum.
    

Limite:

```text
Non impedisce il ripudio.
```

Perché sia Alice sia Bob conoscono la stessa chiave: Bob potrebbe falsificare un messaggio e dire che lo ha inviato Alice.

---

## 21.2 MAC — Message Authentication Code

Un MAC è un piccolo blocco di lunghezza fissa calcolato a partire da:

- messaggio;
    
- chiave segreta.
    

Formula:

$$  
MAC = C\_K(M)  
$$

Il mittente invia:

```text
M || MAC
```

Il destinatario ricalcola il MAC sul messaggio ricevuto e verifica che coincida.

Il MAC garantisce:

- integrità;
    
- autenticazione del mittente rispetto al destinatario.
    

Non garantisce:

- non ripudio.
    

Perché mittente e destinatario condividono la stessa chiave.

---

## 21.3 Hash function

Una funzione hash prende un messaggio di lunghezza arbitraria e produce un digest di lunghezza fissa.

$$  
h = H(M)  
$$

Caratteristiche:

- input di qualsiasi dimensione;
    
- output fisso;
    
- facile da calcolare;
    
- pubblica;
    
- non usa chiave.
    

Un hash da solo rileva modifiche, ma non autentica il mittente.

---

## 21.4 Proprietà di sicurezza degli hash

Una funzione hash sicura deve avere:

|Proprietà|Significato|
|---|---|
|Preimage resistance|dato `h`, è difficile trovare `x` tale che `H(x)=h`|
|Second preimage resistance|dato `x`, è difficile trovare `y` diverso con stesso hash|
|Collision resistance|è difficile trovare due messaggi qualsiasi con stesso hash|

Differenza importante:

```text
Second preimage: parto da un messaggio specifico.
Collision: cerco due messaggi qualsiasi.
```

---

## 21.5 Birthday attack

Il birthday paradox mostra che trovare collisioni è più facile di quanto sembri.

Per un hash di `m` bit, la complessità per trovare una collisione è circa:

$$  
2^{m/2}  
$$

Quindi un hash da 64 bit non offre 64 bit di sicurezza contro collisioni, ma circa 32 bit.

> [!IMPORTANT]  
> Per proteggersi dagli attacchi birthday servono hash sufficientemente lunghi.

---

## 21.6 SHA

SHA è una famiglia di funzioni hash.

Versioni citate:

- SHA-1: output da 160 bit;
    
- SHA-256;
    
- SHA-384;
    
- SHA-512.
    

SHA-1 è stato storicamente importante, ma le slide indicano già che dal 2005 erano emerse preoccupazioni sulla sua sicurezza.

---

## 21.7 HMAC

HMAC è un MAC costruito usando una funzione hash e una chiave.

Schema:

$$  
HMAC\_K(M) = Hash[(K^+ \oplus opad) || Hash[(K^+ \oplus ipad)||M]]  
$$

Dove:

- `K+` è la chiave adattata alla dimensione del blocco;
    
- `opad` e `ipad` sono costanti;
    
- `M` è il messaggio.
    

HMAC è usato perché:

- è efficiente;
    
- può usare diverse funzioni hash;
    
- la sicurezza dipende dalla funzione hash sottostante e dalla segretezza della chiave.
    

---

# 22. WEP, WPA e sicurezza Wi-Fi

## 22.1 WEP

WEP, Wired Equivalent Privacy, era lo schema di sicurezza di 802.11.

Obiettivi:

- offrire confidenzialità simile a una rete cablata;
    
- limitare l’accesso alla rete agli host autorizzati.
    

Caratteristiche:

- usa RC4;
    
- chiave condivisa tra host e access point;
    
- spesso la stessa chiave per tutti;
    
- IV di 24 bit;
    
- IV inviato insieme al ciphertext;
    
- la gestione della chiave non è specificata bene.
    

---

## 22.2 Problema del riuso del keystream in WEP

In WEP il keystream è determinato da:

```text
chiave + IV
```

Se la chiave resta uguale a lungo e l’IV si ripete, due pacchetti possono essere cifrati con lo stesso keystream.

Allora:

$$  
C\_1 \oplus C\_2 = (P\_1 \oplus KS) \oplus (P\_2 \oplus KS) = P\_1 \oplus P\_2  
$$

Questo permette attacchi statistici e può portare al recupero del plaintext o del keystream.

---

## 22.3 Birthday attack a WEP

Con IV da 24 bit, lo spazio degli IV è relativamente piccolo.

Se gli IV sono pseudocasuali, per il paradosso del compleanno bastano molti meno pacchetti di quanto ci si aspetterebbe per trovare una collisione.

Una volta trovati due pacchetti con stesso keystream:

- si può ottenere relazione tra i plaintext;
    
- con abbastanza dati si può recuperare keystream;
    
- con abbastanza keystream si possono forgiare pacchetti.
    

---

## 22.4 Attacco crittografico a WEP

Alcuni IV sono deboli per RC4.

In WEP:

- certi IV permettono di ricavare informazioni sulla chiave;
    
- il primo byte del traffico è spesso prevedibile;
    
- con molti pacchetti si può recuperare statisticamente la chiave.
    

Conclusione:

```text
WEP è insicuro.
```

---

## 22.5 WPA e WPA2

WPA/WPA2 nascono per correggere WEP.

L’emendamento 802.11i introduce:

- 4-way handshake;
    
- autenticazione mutua;
    
- PMK, Pairwise Master Key;
    
- PTK, Pairwise Transient Key;
    
- protocolli per confidenzialità e integrità.
    

Due protocolli importanti:

|Protocollo|Caratteristiche|
|---|---|
|TKIP|usa ancora RC4, disciplina IV, compatibile con hardware vecchio|
|CCMP|usa AES in CTR + CBC-MAC, più robusto|

TKIP è una soluzione transitoria, mentre CCMP è la soluzione più robusta.

---

## 22.6 KRACK

KRACK è un attacco al 4-way handshake.

L’idea è sfruttare la ritrasmissione di messaggi per reinstallare una chiave di sessione.

Effetti indicati dalle slide:

- in CCMP: replay e decryption, ma non forging;
    
- in TKIP/GCMP: replay, decryption e forging.
    

Punto importante:

> [!IMPORTANT]  
> KRACK non è un attacco matematico ad AES, ma un attacco al protocollo di handshake.

---

# 23. Crittografia a chiave pubblica

La crittografia simmetrica usa una chiave condivisa. Questo crea problemi:

- come distribuire la chiave?
    
- cosa succede se la chiave viene rubata?
    
- come impedire che il destinatario falsifichi messaggi del mittente?
    

La crittografia a chiave pubblica usa due chiavi:

|Chiave|Uso|
|---|---|
|Public key|può essere conosciuta da tutti|
|Private key|conosciuta solo dal proprietario|

La chiave pubblica può servire a:

- cifrare messaggi destinati al proprietario;
    
- verificare firme prodotte dal proprietario.
    

La chiave privata può servire a:

- decifrare messaggi ricevuti;
    
- firmare messaggi.
    

---

## 23.1 Applicazioni della crittografia pubblica

Tre usi principali:

1. **Encryption/decryption**
    
    - il mittente cifra con la chiave pubblica del destinatario;
        
    - solo il destinatario decifra con la propria chiave privata.
        
2. **Digital signatures**
    
    - il mittente firma con la propria chiave privata;
        
    - chiunque verifica con la chiave pubblica del mittente.
        
3. **Key exchange**
    
    - la crittografia pubblica serve a creare o scambiare chiavi di sessione simmetriche.
        

---

## 23.2 Perché non sostituisce la crittografia simmetrica

La crittografia asimmetrica è più lenta.

Per questo, nella pratica:

```text
asimmetrica → autenticazione/scambio chiavi
simmetrica → cifratura dei dati
```

Esempio:

```text
TLS usa meccanismi asimmetrici nel handshake,
poi cifra il traffico con chiavi simmetriche.
```

---

# 24. RSA

RSA è uno dei più noti algoritmi a chiave pubblica.

È basato sulla difficoltà di fattorizzare grandi numeri.

## 24.1 Funzione φ di Eulero

Per un numero `n`, `φ(n)` indica quanti numeri minori di `n` sono coprimi con `n`.

Se `p` è primo:

$$  
\phi(p) = p - 1  
$$

Se:

$$  
n = p \cdot q  
$$

con `p` e `q` primi, allora:

$$  
\phi(n) = (p-1)(q-1)  
$$

---

## 24.2 Generazione delle chiavi RSA

Passi:

1. scegliere due primi grandi `p` e `q`;
    
2. calcolare:
    

$$  
n = p \cdot q  
$$

3. calcolare:
    

$$  
\phi(n) = (p-1)(q-1)  
$$

4. scegliere `e` tale che:
    

$$  
1 < e < \phi(n)  
$$

e:

$$  
gcd(e,\phi(n)) = 1  
$$

5. trovare `d` tale che:
    

$$  
e \cdot d = 1 \mod \phi(n)  
$$

6. pubblicare:
    

```text
PU = {e, n}
```

7. mantenere segreto:
    

```text
PR = {d, n}
```

---

## 24.3 Cifratura RSA

Per cifrare un messaggio `M`:

$$  
C = M^e \mod n  
$$

dove `{e,n}` è la chiave pubblica del destinatario.

---

## 24.4 Decifratura RSA

Per decifrare:

$$  
M = C^d \mod n  
$$

dove `{d,n}` è la chiave privata del destinatario.

---

## 24.5 Perché RSA funziona

Poiché `e` e `d` sono inversi modulo `φ(n)`:

$$  
ed = 1 + k\phi(n)  
$$

Allora:

$$  
C^d = (M^e)^d = M^{ed} = M^{1+k\phi(n)}  
$$

Usando il teorema di Eulero, si ottiene di nuovo `M`.

---

## 24.6 Esempio RSA delle slide

Dati:

```text
p = 17
q = 29
n = 17 * 29 = 493
φ(n) = 16 * 28 = 448
e = 11
d = 163
```

Perché:

$$  
11 \cdot 163 = 1793 = 4 \cdot 448 + 1  
$$

Chiave pubblica:

```text
PU = (11, 493)
```

Chiave privata:

```text
PR = (163, 493)
```

Messaggio:

```text
M = 'A' = 65
```

Cifratura:

$$  
C = 65^{11} \mod 493 = 197  
$$

Decifratura:

$$  
M = 197^{163} \mod 493 = 65  
$$

---

## 24.7 Sicurezza di RSA

Attacchi possibili:

- brute force;
    
- fattorizzazione di `n`;
    
- timing attacks;
    
- chosen ciphertext attacks.
    

La sicurezza dipende dal fatto che:

```text
moltiplicare p*q è facile,
fattorizzare n per ricavare p e q è difficile.
```

---

# 25. Altri sistemi a chiave pubblica

## 25.1 ElGamal

Basato sul problema del logaritmo discreto.

È facile calcolare:

$$  
e\_2 = e\_1^d \mod p  
$$

ma è difficile ricavare `d` conoscendo `e1`, `e2` e `p`.

---

## 25.2 Crittografia su curve ellittiche

Basata su operazioni su punti di una curva ellittica su campo finito.

L’idea è:

- la moltiplicazione scalare è facile;
    
- il logaritmo discreto su curve ellittiche è difficile.
    

Vantaggio:

```text
chiavi più corte a parità di sicurezza
```

Esempio indicato:

```text
256-bit ECC ≈ 3072-bit RSA
```

---

# 26. Firme digitali

Una firma digitale deve permettere di:

- verificare l’autore;
    
- verificare data e ora della firma;
    
- autenticare il contenuto;
    
- essere verificabile da terzi;
    
- risolvere dispute.
    

Proprietà richieste:

- dipendere dal messaggio firmato;
    
- usare informazione unica del mittente;
    
- essere facile da produrre per il legittimo firmatario;
    
- essere facile da verificare;
    
- essere computazionalmente impossibile da falsificare;
    
- essere conservabile.
    

---

## 26.1 Firma con chiave asimmetrica

Il firmatario usa la propria chiave privata.

Il verificatore usa la chiave pubblica del firmatario.

```text
Alice firma con PR_A.
Bob verifica con PU_A.
```

Questo fornisce:

- autenticazione;
    
- integrità;
    
- non ripudio.
    

---

## 26.2 Le firme digitali non danno confidenzialità

Firmare un messaggio non significa nasconderlo.

La firma garantisce:

```text
chi lo ha firmato
se è stato modificato
```

ma non impedisce ad altri di leggerlo.

Per avere anche confidenzialità serve cifrare.

---

## 26.3 Firma del digest

Poiché la crittografia asimmetrica è lenta, normalmente non si firma tutto il messaggio.

Si fa così:

1. si calcola l’hash del messaggio;
    
2. si firma l’hash;
    
3. il destinatario ricalcola l’hash e verifica la firma.
    

```text
M → H(M) → firma di H(M)
```

La sicurezza dipende anche dalla sicurezza della funzione hash.

---

# 27. Certificati e PKI

## 27.1 Problema della distribuzione delle chiavi pubbliche

Se ricevo una chiave pubblica, come so che appartiene davvero ad Alice?

Un attaccante potrebbe sostituire la chiave pubblica di Alice con la propria.

Soluzione:

```text
certificati digitali
```

---

## 27.2 Certificato digitale

Un certificato lega un’identità a una chiave pubblica.

Contiene:

- identità del soggetto;
    
- chiave pubblica;
    
- periodo di validità;
    
- informazioni sull’emittente;
    
- algoritmo di firma;
    
- firma della Certification Authority.
    

La CA firma il certificato.

Chi conosce la chiave pubblica della CA può verificare il certificato.

---

## 27.3 Certification Authority — CA

Una CA è una terza parte fidata che certifica l’associazione:

```text
identità → chiave pubblica
```

Il processo tipico:

1. l’utente genera coppia chiave pubblica/privata;
    
2. invia una richiesta alla CA;
    
3. la CA verifica l’identità;
    
4. la CA firma il certificato;
    
5. l’utente conserva e distribuisce il certificato.
    

---

## 27.4 X.509

X.509 è uno standard per certificati digitali.

Un certificato X.509 contiene:

- versione;
    
- numero seriale;
    
- algoritmo di firma;
    
- issuer;
    
- periodo di validità;
    
- subject;
    
- subject public key info;
    
- eventuali estensioni;
    
- firma della CA.
    

Notazione:

```text
CA<<A>>
```

significa:

```text
certificato di A firmato dalla CA
```

---

## 27.5 Revoca dei certificati

Un certificato può dover essere revocato prima della scadenza.

Motivi:

- chiave privata compromessa;
    
- utente non più certificato;
    
- CA compromessa;
    
- errore nel certificato.
    

Meccanismi:

|Meccanismo|Significato|
|---|---|
|CRL|Certificate Revocation List|
|OCSP|Online Certificate Status Protocol|

---

## 27.6 Gerarchia delle CA

Se due utenti non condividono la stessa CA, serve una gerarchia.

Esempio:

```text
Root CA
 └── Intermediate CA
      └── Certificato utente/server
```

Il client verifica una catena di certificati fino a una root CA fidata.

---

## 27.7 Root CA

Le Root CA sono auto-certificate.

Il loro certificato è distribuito in modo sicuro, per esempio:

- con il sistema operativo;
    
- con il browser;
    
- con un’applicazione.
    

> [!IMPORTANT]  
> Se ti fidi del sistema operativo o del browser, implicitamente ti fidi anche delle Root CA che include.

---

## 27.8 PKI

PKI significa Public Key Infrastructure.

Comprende:

- hardware;
    
- software;
    
- persone;
    
- policy;
    
- procedure;
    
- creazione certificati;
    
- gestione certificati;
    
- distribuzione;
    
- revoca.
    

Non è solo crittografia: è un’intera infrastruttura organizzativa e tecnica.

---

# 28. Sicurezza della posta elettronica

## 28.1 Problemi dell’email tradizionale

L’email normale è simile a una cartolina:

- può essere letta;
    
- può essere modificata;
    
- il mittente può essere falsificato;
    
- può passare attraverso sistemi intermedi;
    
- non garantisce non ripudio.
    

Servizi desiderati:

- confidenzialità;
    
- autenticazione del mittente;
    
- integrità;
    
- non ripudio di origine;
    
- non ripudio di destinazione.
    

---

## 28.2 Struttura base della sicurezza email

L’email non è una sessione interattiva.

Quindi il messaggio deve includere:

- algoritmi usati;
    
- eventuale chiave simmetrica cifrata;
    
- firma;
    
- certificati o identificatori.
    

Schema tipico:

1. si genera una chiave simmetrica per il messaggio;
    
2. si cifra il contenuto con la chiave simmetrica;
    
3. si cifra la chiave simmetrica con la chiave pubblica del destinatario;
    
4. si allegano le informazioni necessarie alla decifratura;
    
5. eventualmente si firma il messaggio o il digest.
    

---

## 28.3 PGP

PGP, Pretty Good Privacy, è uno standard de facto per email sicura.

Può fornire:

- confidenzialità;
    
- firma digitale;
    
- entrambe.
    

PGP usa:

- crittografia simmetrica per il contenuto;
    
- crittografia asimmetrica per proteggere la chiave di sessione;
    
- firme digitali;
    
- compressione;
    
- codifica per email.
    

---

## 28.4 Key rings PGP

Ogni utente PGP ha:

|Key ring|Contenuto|
|---|---|
|Public-key ring|chiavi pubbliche di altri utenti|
|Private-key ring|proprie chiavi private, cifrate con passphrase|

La sicurezza della chiave privata dipende anche dalla robustezza della passphrase.

---

## 28.5 Web of trust

In PGP ogni utente può firmare le chiavi di altri utenti.

Non c’è necessariamente una CA gerarchica.

La fiducia è distribuita:

```text
Mi fido della chiave di Bob
Bob ha firmato la chiave di Carol
Allora posso decidere di fidarmi anche di Carol
```

Questo modello si chiama:

```text
web of trust
```

---

## 28.6 S/MIME

S/MIME aggiunge sicurezza a MIME.

È uno standard de jure per email sicura.

Usa principi simili a PGP, ma con una gestione diversa, basata su certificati X.509 e CA.

È supportato da molti client email.

---

## 28.7 PEC

La PEC è un’estensione della posta elettronica con valore legale.

Aggiunge:

- non ripudio della consegna;
    
- timestamp certificato;
    
- ricevute firmate dal server;
    
- valore legale se i server sono riconosciuti ufficialmente.
    

Punto importante:

```text
La PEC prova la consegna nella casella,
non prova necessariamente che il destinatario abbia letto il messaggio.
```

---

# 29. Entity authentication

## 29.1 Differenza tra message authentication ed entity authentication

|Tipo|Significato|
|---|---|
|Message authentication|autentica un singolo messaggio|
|Entity authentication|autentica un’entità per una sessione|

La message authentication può anche non essere in tempo reale.

L’entity authentication invece cambia lo stato interno dei partecipanti:

```text
Prima: non so se sto parlando con Alice.
Dopo: considero Alice autenticata per questa sessione.
```

Spesso l’entity authentication porta alla creazione di una chiave di sessione condivisa.

---

## 29.2 Claimant e verifier

|Ruolo|Significato|
|---|---|
|Claimant|entità che dichiara la propria identità|
|Verifier|entità che verifica l’identità del claimant|

Esempio:

```text
Alice dice: "Sono Alice"
Bob verifica
```

Alice è claimant, Bob è verifier.

---

## 29.3 Challenge-response con chiave asimmetrica

Protocollo monodirezionale:

```text
1. A → B: A
2. B → A: E_KA(B, RB)
3. A → B: RB
```

Dove:

- `RB` è un nonce generato da Bob;
    
- Bob cifra la sfida con la chiave pubblica di Alice;
    
- solo Alice può decifrare e restituire `RB`.
    

Questo autentica Alice per Bob, ma non Bob per Alice.

---

## 29.4 Autenticazione bidirezionale

Protocollo:

```text
1. A → B: E_KB(A, RA)
2. B → A: E_KA(B, RA, RB)
3. A → B: RB
```

Dove:

- `RA` è nonce di Alice;
    
- `RB` è nonce di Bob.
    

Risultato:

- Bob è autenticato per Alice;
    
- Alice è autenticata per Bob.
    

---

## 29.5 Procedure X.509

X.509 definisce tre procedure:

|Procedura|Uso|
|---|---|
|One-way authentication|messaggi unidirezionali|
|Two-way authentication|sessioni interattive con timestamp|
|Three-way authentication|sessioni interattive con nonce, senza dipendere dai timestamp|

---

## 29.6 Problemi dei timestamp

Per evitare replay, un messaggio può includere un timestamp.

Il destinatario accetta il messaggio se:

$$  
|t\_B - t\_A| < \Delta  
$$

Problemi:

- scegliere `Δ`;
    
- se `Δ` è troppo grande, aumenta il rischio replay;
    
- se `Δ` è troppo piccolo, messaggi validi possono essere rifiutati;
    
- gli orologi devono essere sincronizzati;
    
- NTP può avere errori ed essere attaccato.
    

---

# 30. Diffie-Hellman

Diffie-Hellman permette a due parti di creare una chiave simmetrica condivisa su un canale insicuro.

Non serve per cifrare messaggi arbitrari, ma per stabilire una chiave.

---

## 30.1 Parametri globali

Alice e Bob concordano:

- un grande primo `p`;
    
- un generatore `g`.
    

Alice sceglie un segreto:

$$  
x < p  
$$

e pubblica:

$$  
R\_A = g^x \mod p  
$$

Bob sceglie un segreto:

$$  
y < p  
$$

e pubblica:

$$  
R\_B = g^y \mod p  
$$

---

## 30.2 Calcolo della chiave condivisa

Alice calcola:

$$  
K = R\_B^x \mod p  
$$

Bob calcola:

$$  
K = R\_A^y \mod p  
$$

Poiché:

$$  
R\_B^x = (g^y)^x = g^{xy}  
$$

e:

$$  
R\_A^y = (g^x)^y = g^{xy}  
$$

entrambi ottengono la stessa chiave.

---

## 30.3 Sicurezza

Un attaccante vede:

```text
p, g, R_A, R_B
```

ma per calcolare `K` dovrebbe ricavare `x` o `y`, cioè risolvere il problema del logaritmo discreto.

---

## 30.4 Esempio delle slide

Parametri:

```text
p = 353
g = 3
```

Alice sceglie:

```text
xA = 97
```

Bob sceglie:

```text
xB = 233
```

Chiavi pubbliche:

```text
RA = 3^97 mod 353 = 40
RB = 3^233 mod 353 = 248
```

Chiave condivisa:

```text
Alice: K = 248^97 mod 353 = 160
Bob:   K = 40^233 mod 353 = 160
```

---

## 30.5 Man-in-the-middle su Diffie-Hellman

Diffie-Hellman puro non autentica le parti.

Eve può fare:

```text
Alice ↔ Eve
Eve ↔ Bob
```

Eve stabilisce una chiave con Alice e una diversa con Bob.

Poi può:

- leggere;
    
- modificare;
    
- decifrare;
    
- ricifrare;
    
- inoltrare.
    

Contromisura:

```text
autenticare i valori Diffie-Hellman, per esempio firmandoli con certificati
```

Questo è il principio di protocolli come TLS e IPsec.

---

# 31. Web security e TLS

## 31.1 Problemi del Web

Il Web è vulnerabile a:

- perdita di confidenzialità;
    
- modifica dei dati;
    
- impersonificazione;
    
- DoS;
    
- furto di credenziali;
    
- man-in-the-middle.
    

Servono meccanismi aggiuntivi di sicurezza.

---

## 31.2 Approcci alla sicurezza Web

Tre possibilità:

1. sicurezza a livello rete;
    
2. sicurezza a livello trasporto;
    
3. sicurezza specifica dell’applicazione.
    

La sicurezza a livello trasporto è molto usata perché:

- è abbastanza generale;
    
- non richiede modifiche allo stack TCP/IP;
    
- può essere implementata in user-space;
    
- può proteggere protocolli diversi.
    

---

# 32. SSL/TLS

TLS fornisce sicurezza a livello trasporto/sessione.

Servizi principali:

- confidenzialità;
    
- integrità;
    
- autenticazione;
    
- protezione contro replay;
    
- negoziazione di algoritmi;
    
- generazione di chiavi di sessione.
    

TLS usa TCP come trasporto affidabile.

---

## 32.1 Evoluzione SSL/TLS

|Protocollo|Stato nelle slide|
|---|---|
|SSL 1.0|non pubblicato|
|SSL 2.0|deprecato|
|SSL 3.0|deprecato|
|TLS 1.0|deprecato|
|TLS 1.1|deprecato|
|TLS 1.2|ancora rilevante|
|TLS 1.3|versione moderna semplificata|

---

## 32.2 Architettura TLS

TLS ha due livelli principali:

```text
Handshake / ChangeCipherSpec / Alert
Record Protocol
TCP
IP
```

### Record Protocol

Esegue le trasformazioni di sicurezza sui dati applicativi:

- frammentazione;
    
- compressione, nelle vecchie versioni;
    
- MAC;
    
- cifratura;
    
- trasmissione su TCP.
    

### Handshake Protocol

Serve a:

- autenticare server e, opzionalmente, client;
    
- negoziare versione TLS;
    
- negoziare algoritmi;
    
- stabilire chiavi;
    
- creare il master secret.
    

---

## 32.3 Sessione TLS e connessione TLS

|Concetto|Significato|
|---|---|
|TLS session|associazione logica creata dal handshake|
|TLS connection|collegamento transitorio peer-to-peer|

Una sessione può essere condivisa da più connessioni.

---

## 32.4 Stato di sessione

Contiene:

- session identifier;
    
- certificato del peer, se presente;
    
- metodo di compressione;
    
- cipher spec;
    
- master secret da 48 byte.
    

---

## 32.5 Stato di connessione

Contiene:

- client random;
    
- server random;
    
- client write MAC secret;
    
- server write MAC secret;
    
- client write key;
    
- server write key;
    
- IV per CBC;
    
- sequence number.
    

Il sequence number è importante per evitare replay.

---

# 33. Cipher suite TLS

Una cipher suite definisce la combinazione di algoritmi usati.

Esempio:

```text
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
```

Significa:

- key agreement: ECDHE;
    
- autenticazione: RSA;
    
- cifratura: AES 128 in CBC;
    
- hash/MAC: SHA-256.
    

Una cipher suite specifica quindi:

1. come stabilire la chiave;
    
2. come autenticare;
    
3. come cifrare;
    
4. come proteggere l’integrità.
    

---

# 34. TLS Handshake

Il TLS handshake ha quattro fasi principali.

## 34.1 Fase 1 — Establish Security Capabilities

Client e server decidono:

- versione TLS;
    
- algoritmi;
    
- cipher suite;
    
- compressione;
    
- random number del client;
    
- random number del server.
    

---

## 34.2 Fase 2 — Server Authentication and Key Exchange

Il server viene autenticato al client.

Il client ottiene la chiave pubblica del server, di solito tramite certificato X.509.

---

## 34.3 Fase 3 — Client Authentication and Key Exchange

Il client può essere autenticato al server.

In molti casi l’autenticazione del client è opzionale.

Alla fine client e server conoscono il pre-master secret.

---

## 34.4 Fase 4 — Finish / ChangeCipherSpec

Le parti attivano i parametri negoziati.

Dopo questa fase possono scambiarsi dati protetti.

---

# 35. Varianti di key exchange in TLS

## 35.1 RSA

Nel caso RSA:

- il client genera il pre-master secret;
    
- lo cifra con la chiave pubblica RSA del server;
    
- il server lo decifra con la propria chiave privata.
    

Richiede certificato del server.

È stata una situazione molto comune nelle versioni precedenti di TLS.

---

## 35.2 Anonymous Diffie-Hellman

Diffie-Hellman anonimo non autentica le parti.

Problema:

```text
vulnerabile a man-in-the-middle
```

Per questo non è una soluzione sicura in scenari reali.

---

## 35.3 Fixed Diffie-Hellman

I valori pubblici DH sono contenuti nei certificati.

Problema:

- genera chiavi fisse per coppie di peer;
    
- meno flessibile;
    
- meno robusto rispetto a DH effimero.
    

---

## 35.4 Ephemeral Diffie-Hellman

Usa valori DH temporanei generati per la sessione.

I valori sono firmati, per esempio con RSA o DSS.

Vantaggi:

- più robusto;
    
- fornisce chiavi fresche;
    
- riduce l’impatto della compromissione di una chiave a lungo termine.
    

È la scelta migliore quando disponibile.

---

# 36. Master secret e segreti di connessione

TLS genera il master secret a partire da:

```text
pre-master secret
client random
server random
```

Poi, per ogni connessione, deriva:

- chiavi di cifratura;
    
- segreti MAC;
    
- IV;
    
- altri parametri.
    

Questo avviene tramite una PRF, cioè Pseudo Random Function, basata su HMAC.

---

# 37. TLS Record Protocol

Il Record Protocol applica la sicurezza ai dati applicativi.

Servizi:

1. **Integrità**
    
    - MAC con chiave condivisa;
        
    - sequence number contro replay.
        
2. **Confidenzialità**
    
    - cifratura simmetrica;
        
    - uso delle chiavi negoziate nel handshake.
        

Il messaggio viene:

```text
frammentato → eventualmente compresso → autenticato → cifrato → trasmesso
```

La dimensione massima del frammento indicata è:

$$  
2^{14} = 16384 \text{ byte}  
$$

---

# 38. TLS 1.3

TLS 1.3 semplifica molto TLS.

Cambiamenti principali:

- usa AEAD, cioè authenticated encryption with associated data;
    
- usa HKDF per derivare chiavi;
    
- richiede key exchange effimero;
    
- riduce il handshake a 1 RTT;
    
- rimuove molti algoritmi vecchi.
    

---

## 38.1 Cosa rimuove TLS 1.3

TLS 1.3 rimuove:

- RSA key exchange;
    
- RC4;
    
- DES;
    
- 3DES;
    
- Camellia;
    
- MD5;
    
- SHA-1;
    
- AES-CBC;
    
- compressione TLS;
    
- renegotiation;
    
- DSA signatures;
    
- ChangeCipherSpec come meccanismo reale;
    
- export ciphers;
    
- gruppi/curve arbitrari.
    

---

## 38.2 Cipher suite TLS 1.3

TLS 1.3 supporta poche cipher suite, per esempio:

```text
TLS_AES_128_GCM_SHA256
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_CCM_SHA256
TLS_AES_128_CCM_8_SHA256
```

La struttura è più semplice:

```text
Protocollo + AEAD cipher mode + HKDF hash algorithm
```

---

# 39. Schema di ripasso rapido

## 39.1 Concetti da sapere benissimo

- CIA triad;
    
- differenza tra threat, vulnerability, attack, service, mechanism;
    
- attacchi passivi vs attivi;
    
- snooping vs traffic analysis;
    
- modification, spoofing, replay, repudiation;
    
- DoS/DDoS;
    
- servizi X.800;
    
- differenza tra cifratura simmetrica e asimmetrica;
    
- principio di Kerckhoffs;
    
- brute force e crittoanalisi;
    
- stream cipher e pericolo del riuso del keystream;
    
- block cipher e modi ECB/CBC/OFB/CTR;
    
- MAC vs hash vs firma digitale;
    
- birthday attack;
    
- WEP e perché è insicuro;
    
- WPA/WPA2, TKIP, CCMP;
    
- RSA;
    
- Diffie-Hellman e MITM;
    
- certificati X.509 e PKI;
    
- PGP, S/MIME, PEC;
    
- TLS handshake;
    
- TLS record;
    
- TLS 1.3.
    

---

## 39.2 Domande probabili d’esame

### Domanda: Qual è la differenza tra attacco passivo e attacco attivo?

Risposta:

```text
Un attacco passivo osserva o usa informazioni senza modificare il sistema, come snooping e traffic analysis. Un attacco attivo modifica dati o operazioni del sistema, come modification, spoofing, replay o DoS.
```

---

### Domanda: Perché la cifratura non impedisce sempre la traffic analysis?

Risposta:

```text
Perché la cifratura protegge il contenuto dei messaggi, ma non necessariamente i metadati: chi comunica, quando, con quale frequenza e con quale volume di traffico.
```

---

### Domanda: Perché il riuso del keystream è pericoloso?

Risposta:

```text
Perché se due messaggi sono cifrati con lo stesso keystream, facendo XOR dei ciphertext il keystream si cancella e si ottiene lo XOR dei plaintext. Questo può permettere di recuperare informazioni sui messaggi originali.
```

---

### Domanda: Differenza tra MAC e firma digitale?

Risposta:

```text
Un MAC usa una chiave segreta condivisa tra mittente e destinatario, quindi garantisce integrità e autenticazione tra loro, ma non il non ripudio. Una firma digitale usa la chiave privata del mittente e può essere verificata con la chiave pubblica, quindi fornisce anche non ripudio.
```

---

### Domanda: Perché Diffie-Hellman puro è vulnerabile al MITM?

Risposta:

```text
Perché i valori pubblici scambiati non sono autenticati. Un attaccante può intercettare lo scambio e stabilire due chiavi diverse: una con Alice e una con Bob, fingendo di essere Bob con Alice e Alice con Bob.
```

---

### Domanda: A cosa serve un certificato digitale?

Risposta:

```text
Serve a legare una chiave pubblica a un’identità. La Certification Authority firma il certificato, così chi si fida della CA può fidarsi dell’associazione tra identità e chiave pubblica.
```

---

### Domanda: Perché TLS usa sia crittografia asimmetrica sia simmetrica?

Risposta:

```text
La crittografia asimmetrica serve per autenticare e stabilire in modo sicuro le chiavi di sessione. La crittografia simmetrica viene poi usata per cifrare i dati perché è molto più veloce.
```

---

### Domanda: Qual è il ruolo del TLS Record Protocol?

Risposta:

```text
Il TLS Record Protocol applica concretamente la sicurezza ai dati applicativi: frammenta i dati, calcola il MAC o usa AEAD, cifra il contenuto e lo invia su TCP usando le chiavi negoziate dal handshake.
```

---

## 39.3 Mappa mentale sintetica

```text
Network Security
├── Obiettivi
│   ├── Confidenzialità
│   ├── Integrità
│   └── Disponibilità
├── Attacchi
│   ├── Passivi
│   │   ├── Snooping
│   │   └── Traffic analysis
│   └── Attivi
│       ├── Modification
│       ├── Spoofing / MITM
│       ├── Replay
│       ├── Repudiation
│       └── DoS / DDoS
├── Servizi
│   ├── Authentication
│   ├── Access control
│   ├── Confidentiality
│   ├── Integrity
│   └── Non-repudiation
├── Meccanismi
│   ├── Cifratura
│   ├── Hash
│   ├── MAC
│   ├── Firma digitale
│   ├── Certificati
│   └── Protocolli di autenticazione
├── Crittografia
│   ├── Simmetrica
│   │   ├── Stream cipher
│   │   ├── Block cipher
│   │   └── AES
│   └── Asimmetrica
│       ├── RSA
│       ├── Diffie-Hellman
│       └── ECC
├── Applicazioni
│   ├── WEP / WPA / WPA2
│   ├── PGP
│   ├── S/MIME
│   ├── PEC
│   └── TLS
└── TLS
    ├── Handshake
    ├── Record Protocol
    ├── Cipher suites
    ├── Session state
    ├── Connection state
    └── TLS 1.3
```

---

## 39.4 Frasi chiave da ricordare

- La sicurezza non è assoluta: è sempre un compromesso tra costo, rischio, funzionalità e usabilità.
    
- La confidenzialità protegge dalla lettura non autorizzata.
    
- L’integrità protegge dalla modifica non autorizzata.
    
- La disponibilità protegge dall’interruzione del servizio.
    
- Gli attacchi passivi sono difficili da rilevare, quindi si prevengono.
    
- Gli attacchi attivi sono difficili da prevenire completamente, ma più facili da rilevare.
    
- La sicurezza di un cifrario deve dipendere dalla chiave, non dall’algoritmo.
    
- Non bisogna mai riutilizzare uno stesso keystream.
    
- Un hash non autentica il mittente.
    
- Un MAC autentica ma non dà non ripudio.
    
- Una firma digitale fornisce autenticazione, integrità e non ripudio.
    
- Diffie-Hellman crea una chiave condivisa, ma deve essere autenticato.
    
- Un certificato lega una chiave pubblica a un’identità.
    
- TLS usa handshake per negoziare chiavi e Record Protocol per proteggere i dati.
    
- TLS 1.3 semplifica e rimuove algoritmi vecchi o problematici.