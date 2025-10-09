---
title: Esercizi
aliases:
  - Esercizi
tags:
  - università
  - Esercizi
  - materie
  - anno-2025-2026
  - reti-di-calcolatori
created: 2025-10-09
---

## Esercizi su connessione ed encoding dalle slide

### **Es 1:**

Testo:
+  Un certo canale ha SNR = −8 dB, con una larghezza di banda pari a 20MHz. (a) Qual è la massima capacità ottenibile (in Mbps)? (b) Se il baud rate è di 3 Mbaud, quanti bit devono essere codificati in ogni simbolo per avere tale capacità di canale?

Svolgimento:
+ $S/N = 10^{-8/10} = 10^{-0,8} = 0,1585$    --> siccome il valore è inferiore a 1 vuol dire che c'è più rumore che segnale informativo
+ La capacità massima è: $B\*log\_2(1+S/N) = 20Hz\*log\_2(1+0,1585) = 4,24Mbit/s$
+ $\frac{4,24Mbit/s}{3Msimboli/s} = 1,41bit/simbolo$
___
### **Es 2**:

Testo:
+ La lingua italiana conta 46 simboli sonori, chiamati fonemi, e in un normale eloquio vengono pronunciati circa 15 fonemi al secondo. a) A quanto equivale il bit rate di tale trasmissione? b) Se il canale usato per la trasmissione ha un SNR di 10dB, quale ampiezza di banda è necessaria?

Svolgimento:
+ Ogni simbolo codifica $log\_2(45) = 5,49 bit$  il che vuol dire che il bitrate è: $5,49 \* 15 = 82,3bps$ 
+ Avendo un SNR di 10dB,    $S/R = 10^{10/10} = 10$
+ $82,3 = B\*log\_2(11)$  da cui viene l'ampiezza di banda $B = 82,3/3,459 = 23,8Hz$

>[!tip] Conoscenza bonus
>Con 5,49 bit la potenza di 2 rappresentabile è 32 simboli diversi, il che vuol dire che 46-32 = 14 simboli rimangono inutilizzati.
>Se però al posto di utilizzare solo la parte intera del bit ma anche la metà e ad esempio i simboli vengono presi a coppie -->  $5,49+5,49 = 11bit$ che mi permettono di mappare $2^{11}$ combinazioni a tutte le coppie possibili di simboli (aa, ab, ac,....).
>Le combinazioni dei simboli saranno quindi $46\*46=2116$ in cui mappare $2^{11}=2048$ combinazioni, avendo così uno spreco molto più contenuto rispetto a prima, utilizzando anche i mezzi bit.

___

## Esercizi sulle connessioni dalle esercitazioni in aula

### Es 2:

Testo:
+ Si supponga di realizzare una rete a commutazione di pacchetti usando una tecnologia di collegamento punto-punto che garantisce la consegna affidabile a livello datalink, a meno di guasti completi del collegamento. a) Cosa può fare un nodo se si accorge che un collegamento è guasto? b) è necessario implementare altri meccanismi di gestione errori ai livelli superiori (es. trasporto)?

Risposta:
+ a) il nodo rileva il guasto, informa gli altri nodi e aggiorna la topologia per evitare di instradare pacchetti su quel collegamento.
+ b) serve comunque un protocollo di trasporto affidabile per garantire la **corretta consegna da host a host**.

___
### Es 3:

Testo:
+ La lingua italiana conta 45 simboli sonori, chiamati fonemi, e in un normale eloquio vengono pronunciati circa 15 fonemi al secondo. a) A quanto equivale il bitrate di tale trasmissione? b)Se il canale usato per la trasmissione ha un SNR di 10dB, quale ampiezza di banda è necessaria?

Risposta:
+ a) Ogni fonema presenta $log\_2(45) = 5,49$ bit a fonema, quindi il bitrate è $15\*5,49=82,35bit/s$
+ b) SNR da 10 dB corrisponde a S/N = 10 (rapporto lineare)
	+ $C=B\*log\_2(11)$, quindi $B=23,8Hz$

>[!tip]
>Per convertire da SNR a S/R, la formula è la seguente:
>$$SNR=10\*log\_10(S/N)$$

___
### Es 4:

Testo:
+ Nei sistemi radio DAB e DAB+, i dati sono codificati mediante simboli (OFDM); ogni simbolo porta 3072 bit e dura 1,246 ms. Ogni frame contiene 76 simboli, e i frame sono separati da una pausa di 1,304ms. a) A quanto equivale il bitrate grezzo di tale trasmissione? b) Se il canale usato ha una larghezza di banda di 1536 kHz, quanto dev'essere il rapporto S/N minimo per una trasmissione senza errori?

Risposta:
+ a) Durata totale di un frame --> $T=76\*0,001246 + 0,001304 = 0,0983s$
	+ Bit per frame = $76\*3072=233472$ bit
	+ Bitrate: $\frac{233472}{0,0983}=2374000bit/s=2,37Mbit/s$

+ b) $C=2,374Mbit/s$ e $B=1,536MHz$, quindi $log\_2(1+SNR) = \frac{C}{B}=2,374/1,536=1,547$ e di conseguenza $(1+SNR)=2^1,547 = 2,92$  --> SNR = 1,92
  In decibel $10\*log\_{10}(1,92) = 2,8$

___
### Es 5:

Testo:
+ Un canale di trasmissione ha una larghezza di banda di 10 MHz e un rapporto segnale/rumore in potenza di -20dB. a) Determinare il massimo bit rate grezzo di tale canale. b) Se si usa una codifica con un alfabeto di 8 simboli, qual è il baud rate massimo corrispondente.

Risposta:
+ a) SNR = $10^{-20/10} = 10^{-2} = 0,01$
	+ Bitrate grezzo= $C=10^7 \* log\_2(1,01) = 143,6kbit/s$

+ b) Ogni simbolo avrà --> $log\_2(8)=3$ bit/simbolo
	+ Baud rate= C/3 = $\frac{143,6\*10^3}{3}=47,9kbaud$
	+ 

___
### Es 6:

Testo:
+ Il Controllo Missione della NASA sta comunicando con un rover su Marte, che dista circa 60 milioni di km dalla Terra, su un canale con una capacità di 250kbps. a) Ricordando che c = 3x10^8m/s, quant'è il RTT? b) Periodicamente il rover scatta una foto, che pesa 5MB, e la trasmette su tale canale. Dopo quanto tempo, dal momento dello scatto, tale foto è disponibile presso il Controllo Missione?

Risposta:
+ a)  Tempo di propagazione --> d/c = $\frac{6\*10^{10}}{3\*10^8}= 200s$
	+ RTT(Round Trip Time) --> $2\*200=400s$

+ b) tempo di trasmissione --> $\frac{40\*10^6}{2,5\*10^5}=160s$
	+ Tempo totale --> $t=200+160=360s$

___
### Es 7:

Testo:
+ Il sistema DVB-T2 prevede diversi "profili" a livello fisico. Uno di questi definisce una modulazione 64-QAM (quindi un alfabeto di 64 simboli), con una FEC 3/5, su un canale largo 8MHz; si codifica un simbolo per ciclo. Sapendo che circa l'8% della banda viene consumato da traffico di servizio, quant'è il bitrate utile per ogni canale?

Risposta:
+ Bitrate lordo (senza FEC): R= $8\*10^6\*6=48Mbit/s$
	+ dopo FEC(solo il 60% dei bit sono utili): $R\*3/5=28,8Mbit/s$
	+ dopo overhead dell'8% (solo il 92% è utile): R_utile = $28,8\*0,92 = 26,5Mbit/s$

___
### Es 8:

Testo:
+ Su una certa linea di trasmissione, i dati vengono inviati in frame composti da una intestazione di 10 byte, comprensiva di CRC, e un payload di 1000 byte. Se un frame è errato, viene scartato e ritrasmesso. La probabilità di errore per ogni bit è p=10^-5. Se questi frame vengono usati per trasferire un file da 10KB, qual è la probabilità che si debba effettuare almeno una ritrasmissione?

Risposta:
+ File: 10KB = 10240 B--> $\frac{10240}{1000}=10,24$ == 11 bit 
+ totale bit per frame: 1000 B(payload) + 10 B(header) = $1010\*8=8080bit$
+ Probabilità che un frame sia ricevuto correttamente: P1 = $(1-p)^8080=0,9224$
+ Probabilità che nessun frame sia errato: P2 = $(P1)^{11} = 0,420$
+ Probabilità di almeno una ritrasmissione: P3 = 1-P2 = 0,58

___
### Es 11:

Testo:
+ Su una linea con una probabilità di errore per bit di 10^-4, si trasmettono due frame, ognuno di 500 byte. Qual è la probabilità che almeno uno arrivi a destinazione senza errori?

Risposta:
+ bit totali per frame: 500byte x 8 = 4000 bit
+ Probabilità di un frame senza errori: $P1=(1-p)^{4000}=0,6703$
+ Probabilità di un frame errato:$P\_{err}=1-P1 = 0,3297$
+ Probabilità di due frame senza errori: $1-(P\_{err})^2=0,8913$

___
