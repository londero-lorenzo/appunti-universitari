---
title: "Capitolo 2"
aliases: ["Capitolo 2"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-2"]
created: 2025-10-16
---

# Capitolo 2
>[!question]
>Nel primo abbiamo visto che la rete è composta da più nodi connessi tra loro, ma come si connettono diversi nodi?

Le connessioni tra due nodi possono essere di diverso tipo e dipendono dal **mezzo** di connessione, che si basano comunque sulla propagazione delle **onde elettromagnetiche:**
+ Fibra ottica
+ Cavi in doppino / cavi coassiali
+ Aria/ spazio libero

### Caratteristiche importanti dei collegamenti:
**Frequenza**: numero di oscillazioni al secondo, misurata in hertz.
**Lunghezza d'onda**: distanza fra due punti di massimo o minimo
>[!definition]
>Lunghezza d'onda
>>Distanza tra una coppia di massimi o minimi d'onda adiacenti, tipicamente misurata in metri

>[!example]
>La frequenza del telefono va tipicamente dai 30 ai 3300Hz e la lunghezza d'onda sarà: velocità della luce nel coppino / frequenza = $2.3 x 10^8 / 300 = 766km$ 
>>(L'udito umano sente dai 20 ai 20000 Hz, il telefono porta a limitare queste frequenze in quanto non le riproduce.)

## Onde elettromagnetiche
Più in generale le onde elettromagnetiche spaziano su un intervallo di frequenzemolto più ampio: dai $10^4Hz$  ai  $10^{16}Hz$ , dalle onde radio alle onde UV. Questo perché frequenze maggiori (X-Ray, Gama Ray) sono considerate pericolose.
Queste frquenze sono usate da tutta la gamma di dispositivi che inviano segnali elettromagnetici, quali radio, telefoni, fibre ottiche....

![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-08 180754.png]]

# Encoding

>[!definition]
>Encoding (codifica)
>> Trasformare l'informazione (dati: bit) in un segnale

L'encoding è definito dalla **modulazione** ed è definito da:
+ Ampiezza 'A' (ASK)
+ Frequenza 'f' (FSK)
+ Fase $\phi$ (PSK)
Formula del segnale:
$$x(t)= A\*sin(2\pi ft + \phi)$$

>[!tip]
>Demodulazione è l'opposto: estrarre i bit da un segnale modulare

>[!definition]
>Modem
>>Device che si occupa appunto della modulazione e demodulazione di un segnale

>[!tip]
>Il 'modem' del Wi-fi che abbiamo a casa non è veramente un modem ma un router, che non c'entra niente

Ci sono tre modi per modulare un segnale, una per ogni parametro:
+ cambiando la ampiezza:
	+ quando il bit che voglio trasmettere è 0 l'ampiezza sarà più debole, quando è 1 sarà più pronunciata
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-08 182950.png|350]]
+ cambiando la frequenza:
	+ frequenza pari a 0 per il bit 0 e pari a 1 per il bit 1
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-08 183009.png|350]]
+ cambiando la fase:
	+ anche qua come la frequenza, cambio la fase (ovvero sposto la sinusoide di un tot avanti o indietro (ad esempio $\pi$)) in base al bit mantenendo uguali ampiezza e frequenza.
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-08 183050.png|350]]

>[!tip]
>I 3 metodi possono anche essere usati insieme e si possono anche ad esempio usare più di due frequenze e più ampiezze e più frazioni di $\pi$ per la fase, potendo così idealmente pompare tutti i bit che vogliamo nel canale, anche se vedremo ci sono delle limitazioni
>

>[!question] Quanti dati possiamo codificare e trasmettere sul canale?
>Due aspetti da considerare:
>- Quanti bit possiamo condensare in un **simbolo**?
>- Quanti simboli possiamo trasmettere in un secondo?

>[!definition]
>Stati
>>I diversi valori acquisibili dalle variabili f, A, $\phi$

>[!definition]
>Simbolo
>>Ogni stato in cui il canale può essere settato dal trasmettitore e osservato dal ricevente.

>[!example]
>In un libro le lettere sono i simboli e la carta il mezzo.
>In un messaggio ad esempio sono i caratteri ASCII.
>Nella voce i simboli sono decodificati nei fonemi

Simboli sono quello che viene effettivamente trasmesso sul canale:
+ Livelli di tensione
+ Modulazione di ampiezza
+ Modulazione di frequenza
+ Modulazione di fase
+ On/Off light
+ Lettere stampate su un libro. Lettere = simbolo, carta = mezzo
+ ecc...

>[!definition]
>Baud rate
>> Simboli che riesco a mandare in un secondo


La limitazione nella quantità di simboli che percorrono un canale al secondo è definita dal teorema di Nyquist-Shannon:
>[!definition]
>Teorema Nyquist-Shannon
>>In un canale con larghezza di banda B [Hz] possiamo trsmettere un massimo di simboli pari al doppio della banda $2\*B$.
>>

>[!tip]
>Potrei effettivamente trasmettere più simboli, ma dall'altra parte del collegamento il decodificatore avrà più ricostruzioni tutte lecite senza sapere qual è quella effettivamente corretta, rendendo il teorema solo una limitazione per la corretta decodificazione dei simboli

Se ho un segnale $x(t)$ non modulato la larghezza di banda è 0 e che utilizza un altro segnale modulante $x\_m(t)$:

$x(t)=x\_{m}(t)\*\sin(2\pi f\_{0} t)$
$f\_0$ = frequenza iniziale utilizzata come frequenza iniziale (grazie al cazzo dirai)
$x\_{m}(t)=\sin(2\pi f\_{m} t)$
$x(t)= \sin(2\pi f\_{0} t)\*\sin(2\pi f\_{0} t)=-\frac{1}{2}(\cos(2\pi f\_{m}t+2\pi f\_{0}t)-\cos(2\pi f\_{m}t-2\pi f\_{0}t))$

Si avrà quindi un segnale $x(t)$, che cambia in base ai bit tra due frequenze che però non corrispondono a quella fondamentale $f\_0$.

## Codifica dei segnali

>[!tip]
>Quanti bit riusciamo a inserire in un simbolo dipende da quanti simboli abbiamo a disposizione.

Il primo livello dello stack dell'encoder prende in entrata i bit e li trasforma in segnale.
L'associazione tra simbolo e bit corrispondente/i è detta **codifica dei simboli**

>[!warning]
>In un alfabeto di M simboli, il numero di bit che ogni simbolo può rappresentare è $\log\_2(M)$


>[!example]
>Se codifichiamo bit con tensione elettrica su un cavo con un dato range di tensione possiamo dividere questo range in:
>- 2 livelli: 2 simboli = 1 bit per simbolo
>- 4 livelli: 4 simboli = 2 bit per simbolo
>- 128 livelli: 128 simboli = 7 bit per simbolo
>	- Il codice ASCII ha 128caratteri, il che vuol dire che ogni carattere è rappresentato da 7 bit


## Rumore

>[!definition]
>Rumore
>>Segnale (derivante da onde magnetiche e dipendente dal tipo di mezzo) che si sovrappone a quello informativo durante la trasmissione.
>>Ciò può provocare un errore nella decodifica.

>[!tip]
>Spesso il noise nei canali di comunicazione è un **rumore bianco**, ovvero rumore che viene 'disperso' in tutte le frequenze in modo uniforme

>[!example]
>se il noise è troppo forte un simbolo può cambiare nel canale ed essere quindi interpretato male dal decoder:
>101(codifica) -->2,4V(originale) + 0.3(rumore) = 2,7V --> 110 (decodifica errata)

Un importante fattore per la stima del noise è il **signal-to-noise ratio**: S/N
>[!definition]
>S/N
>>il rapporto tra la potenza media del segnale S e la potenza media del rumore N

>[!tip]
>S e N si misurano in Watt, quindi S/N è un numero puro.

Spesso questo rapporto è espresso in decibel (dB) ed è nominata in questo caso **SNR**:
$$SNR = 10\*log\_{10}(S/N)$$
___
>[!definition]
>Teorema di Shannon-Hartley
>> Definisce la capacità massima di un canale
>> $$C = B\*log\_2(1+S/N)$$     
>> Dove B rappresenta la larghezza di banda.
>> Espresso in [b/s].

>[!tip]
>- Per avere una capacità maggiore bisognerà quindi aumentare la larghezza di banda B o aumentare il rapporto S/N ovvero diminuendo il rumore.
>- Il logaritmo è in base due perché stiamo calcolando in termini di bit. Se volessimo mandare segnali da 10 diverse codifiche il logaritmo sarebbe in base 10 

>[!example]
>Se S/N = 7, vuol dire che N = S/7, il che vuol dire che ci sono 8 livelli (4 positivi e 4 negativi) che possono essere correttamente letti dal decoder senza che il rumore aggiunto faccia interferenza, ovvero senza che il segnale sommato al rumore scivoli in un altro valore.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-08 203011.png|300]]

___

#### Adattatore hardware
La maggior parte delle funzioni di questo capitolo sono svolte da un adattatore di rete, hardware che collega un nodo ad una linea di connessione e che svolge la codifica e decodifica dei bit trasformati in segnali grazie ad una componente di segnalazione al suo interno.
I **segnali quindi viaggiano tra due componenti di segnalazione** e i **bit fluiscono tra i due adattatori**.

# Diverse tecniche di encoding

### NRZ (non-return-to-zero)
La cosa più naturale da fare è stabilire una corrispondenza tra i dati di valore 1 ed il segnale alto e i dati di valore 0 e il segnale basso, e in questo consiste la tecnica NRZ:

![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-09 145250.png|500]]

Il ricevente tiene presente il valore medio dei segnali che ha analizzato fino a quel punto e se il nuovo segnale è inferiore gli assegnerà 0, mentre se il nuovo segnale è superiore gli assegnerà 1.

>[!problem]
>- Il primo problema di questa tecnica di codifica è che per questo motivo troppi zeri o troppi uno consecutivi comportano un cambiamento della media, aumentando la difficoltà nel codificare correttamente i segnali.
>- Il secondo problema è dovuto al fatto che affinché la codifica e decodifica funzioni il processo di codifica e decodifica devono avere lo stesso ciclo di clock (quindi ad ogni ciclo corrisponde un bit codificato da una parte e decodificato dall'altra), e sincronizzare il clock il processo ricevente attua una tecnica di *ricostruzione del segnale di sincronismo* (clock recovery), ovvero ad ogni cambiamento di stato (da 0 a 1 o viceversa) il processo riconosce il ciclo di clock e si sincronizza. Il problema è che molti bit uguali comportano la deriva del clock e la perdita di sincronizzazione.

### NRZI (non-return-to-zero-inverted)
Consiste nel cambiare stato del segnale in presenza di un bit 1 e di mantenerlo in presenza di un bit 0.

>[!problem]
>In questo modo si risolve la presenza di bit a 1 contigui, ma ovviamente non la presenza di bit contigui a 0.

### Manchester
Consiste nel trasmettere lo XOR del clock e dei dati codificati con NRZ, provocando un cambiamento del segnale dal basso verso l'alto per lo 0 e dall'alto verso il basso per l'1.

>[!problem]
>Il problema della codifica Manchester è che si raddoppia la velocità a cui avvengono le transizioni di segnale lungo una linea di connessione e di conseguenza il ricevitore ha a disposizione la metà del tempo per identificare ciascun impulso di segnale. La velocità di bit (bit rate) è quindi la metà della **velocità di baud** (velocità di transizione di un segnale), ovvero 2 stati equivalgono ad 1 bit

### MLT-3
Diversamente dalle altre codifiche, usa 3 livelli anziché 2 (-1, 0, +1), ma per il resto ha lo stesso funzionamento di NZI: cambiare stato quando il bit è diverso dal precedente. Con NZI condivide anche i problemi di sincronizzazione. (inutile alla merda insomma)
L'unica roba è che avendo tre livelli il segnale apparirà più simile ad una sinusoide che è molto bella molto fancy.

### 4B/5B
L'idea di questa tecnica è di risolvere i problemi di Manchester introducendo dei bit extra che vanno a interrompere eventuali lunghe sequenze di 0 o 1. Nello specifico ogni sequenza di 4 bit di dati viene codificata con 5 bit che si trasmettono al ricevitore; tale codice non potrà avere più di uno 0 iniziale e 2 0 finali, quindi ogni 5 bit non ci saranno mai più di 3 bit uguali a 0. Le parole così organizzate vengono trasmesse poi con la codifica NRZI (infatti 4B/5B si preoccupa solo del problema degli 0, essendosi NRZI già occupata degli 1 rispetto a NRZ).
Può essere usato anche insieme a MLT-3.

>[!problems]
>L'efficienza sarà all'80% in quanto si utilizzano 5 bit per decodificarne 4, e per lo stesso motivo il delay sarà di 5 bit

### Schemi dei segnali delle diverse codifiche
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-09 154857.png|500]]
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-09 154919.png|500]]

# Framing

Avvalendosi la connessione tra i due adattatori di una commutazione a pacchetto, nel secondo livello dello stack tale pacchetto viene chiamato **frame**. 

>[!question]
>L'adattatore del nodo ricevente riceve la sequenza di bit in arrivo dalla linea ma il compito primario è: come identificare esattamente quale insieme di bit costituisca il frame?
>Questo è il problema del *framing*

## Byte-oriented Protocols
Ci sono diversi modi per risolvere il problema del framing e uno di essi è attraverso un *approccio orientato ai byte*, ovvero trattando ciascun frame come un insieme di byte piuttosto che come un insieme di bit.
Esempi di questi protocolli sono BYSINC (con **approccio con sentinella**) e DDCMP (con **approccio a conteggio di byte**).

### BYSINC (approccio con sentinella)
Il frame con questo approccio è formato nel seguente modo:
+ invio del carattere speciale SYN (synchronization)
+ i dati del frame (Body) sono poi racchiusi tra i caratteri sentinella: STX (start of text) e ETX (end of text)
+ Il campo SOH (start of header) è il corrispettivo di STX per il campo Header
+ Alla fine un campo CRC (codice per il controllo di errori di trasmissione)

>[!tip]
>Per non far comparire il carattere ETX nei dati, BISYNC lo fa precedere da un carattere DLE ("escape"), e allo stesso modo anche un carattere DLE deve essere preceduto da un DLE (è praticamente la '/ rovesciata' in C )

>[!problem]
>La memorizzazione di dati aggiuntivi come STX e ETX .... comportano byte in più che portano ad una perdita di performance fino al 50%, quindi le funzionalità aggiuntive devono essere importanti per valerne la pena
#### Formato dei frame BISYNC
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-09 164240.png]]

### DDCMP (approccio a conteggio di byte)
L'alternativa alla rilevazione della fine di un file mediante sentinella è l'inserimento della dimensione del file all'inizio del file stesso.
Questo è quello che fa l'approccio a conteggio di byte con in campo Count che specifica quanti bit sono contenuti nel corpo del frame.

>[!problem]
>Se il campo Count viene corrotto, la fine del frame non verrebbe identificata correttamente.
>In quel caso comunque il ricevitore immagazzinerebbe quanti byte affermati dal campo Count errato e successivamente il campo CRC riconoscerebbe il frame errato e darebbe *errore di framing* (framing error).
>In seguito il ricevitore aspetterà di osservare il successivo carattere SYN prima di riiniziare a memorizzare i byte del nuovo frame.
#### Formato dei frame DDCMP
![[materie/anno_2025-2026/reti_di_calcolatori/assets/Immagine 2025-10-09 164304.png]]

### HDLC (protocolli orientati ai bit)
>[!definition]
>>Un protocollo orientato ai bit considera il frame come una **sequenza di bit**.

Contrassegna inizio e fine del frame con la sequenza 01111110:
+ viene trasmessa durante tutto il tempo in cui la connessione è inattiva
+ per mantenere sorgente e ricevitore sincronizzati
+ può comparire **ovunque** all'interno del frame

>[!tip]
I protocolli orientati ai bit usano  l'**interposizione di bit (bit stuffing)** analoga al carattere DLE.

#### Interposizione di bit in HDLC
+ **Sorgente:** quando invia cinque valori **1** consecutivi nel corpo del messaggio inserisce un valore **0** prima di trasmettere il bit successivo
+ **Ricevitore**: se arrivano cinque valori **1** consecutivi si comporterà in base al bit successivo:
	+ Se **0**: deriva dall'interposizione e viene eliminato
	+ Se **1**: si tratta del marcatore **fine** frame oppure è stato introdotto un **errore**

+ Osservando il bit ancora successivo:
	+ Se **0**: (gli ultimi 8 bit ricevuti sono stati 01111110) allora è marcatore di fine frame
	+ Se **1**: (gli ultimi 8 bit ricevuti sono stati 01111111) allora deve essersi verificato un errore e il frame viene eliminato.
		+ Il ricevitore dovrà attendere il successivo 01111110 prima di poter iniziare a ricevere di nuovo.

#### Caratteristica dell'interposizione di bit
>[!tip]
>La dimensione del frame dipende dai dati che vengono inviati come carico utile del frame stesso: infatti non è possibile che tutti i frame abbiano la stessa dimensione, poiché i dati che si possono trovare in ciascun frame sono arbitrari.

### PPP (Point-to-Point Protocol)
![[materie/anno_2025-2026/reti_di_calcolatori/assets/pppFrame.jpg]]

+ **Flag**: 01111110
+ **Address** e **Control**: contengono valori predefiniti (poco interessanti)
+ **Protocol**: usato per **demultiplexing** in quanto identifica il protocollo di livello superiore
+ **Payload**: dimensione può essere negoziata altrimenti è 1500 byte
+ **Checksum**: lungo 2 o 4 byte

>[!tip]
>Dimensioni dei campi negoziate tramite **LCP** (Link Control Protocol).

# Error Detection

>[!definition]
>>A volte nei frame vengono introdotti bit errati a causa di interferenza elettrica o rumore termico.

+ **Rilevamento** di errori è una funzione fondamentale del livello di collegamento

Quando il destinatario di un messaggio individua un errore:
+ avverte il mittente che il messaggio è stato corrotto in modo che ritrasmetta una copia
+ **ricostruire il messaggio corretto** usando degli algoritmi di rilevazione d'errore:
	+ si basano su **codici a correzione d'errore**.

## Esempi di errori nei bit

### Almeno un errore in un pacchetto
- Lunghezza pacchetto: $n=10,000$ bit (10 kb).
- Probabilità di errore per **singolo bit**: $p\_{E}=10^{−7}$.
- Indipendenza tra bit.
#### Probabilità di nessun errore in 10Kb
$P=(1-p\_{E})^{10,000}$
#### Probabilità che ci sia almeno un errore
$P(\geq1\textrm{ errore})=1-P(\textrm{nessun errore})=1-(1-p\_{E})^{10,000}=1-(1-10^{-7})^{10,000}\approx0.0009995$
Approssimazione (Poisson)
$(1-p)^{n}\approx1-np\Rightarrow P(\geq1)\approx np=10^{4}\cdot10^{-7}=10^{-3}=0.001$
Il valore approssimato si avvicina circa al valore esatto quindi la probabilità di avere **almeno un errore** in un pacchetto da 10Kb è circa **0.001** ovvero **1 errore ogni 1000 pacchetti**.

### Esattamente due errori in un pacchetto

Binomiale:
$P(X=2)=\binom{n}{2}p^{2}\_{E}(1-p\_{E})^{n-2}$

$\binom{10^{4}}{2}(10^{-7})^{2}(1-10^{-7})^{9998}\approx\frac{10^{4}\cdot(10^{4}-1)}{2}\cdot10^{-14}\cdot1\approx\frac{10^{8}}{2}\cdot10^{-14}\approx5\cdot10^{-7}$

Quindi $P(2\textrm{ errori})\approx5\cdot10^{-7}=5p\_{E}$

### BER (Bit Error Rate)
>[!definition]
>>Frequenza dei bit errati: è proprio $p\_{E}$ probabilità che un singolo bit sia sbagliato

## Idea alla base del rilevamento di errori
>[!definition]
>>Aggiungere informazioni ridondanti al frame che possono essere usate per determinare se sono stati introdotti errori.

+ Immaginiamo di trasmettere due copie complete di dati se le due copie giunte a destinazione sono:
	+ **identiche**: sono entrambe corrette
	+ **diverse**: un errore è stato introdotto in una o entrambe (**eliminate**)
+ Schema di rilevazione **inefficiente**:
	+ vengono inviati $n$ bit ridondanti per un messaggio di $n$ bit
	+ sfuggono alla rilevazione di molti errori

### Schemi migliori
>[!tip]
>Siamo in grado di garantire una forte capacità di rilevazione d'errore:
> - inviando solo $k$ bit ridondanti per un messaggio di $n$ bit 
> - con $k$ molto minore di $n$

>[!example]
>In una linea Ethernet un frame contente fino a **12000** bit (1500 byte) di dati richiede soltanto un codice CRC di 32 bit.

Bit aggiuntivi inviati sono detti ridondanti perché non aggiungono alcuna informazione al messaggio:
+ calcolati elaborando direttamente il messaggio ordinario mediante **algoritmi**
+ algoritmi conosciuti sia da **mittente** che **destinatario**
+ mittente applica l'algoritmo per generare **bit ridondanti**
+ destinatario applica lo stesso algoritmo e in assenza di errori dovrebbe ottenere lo stesso risultato del mittente.

## Parità unidimensionale
>[!definition]
>>Comporta l'aggiunta di un **bit extra** ad un codice a 7 bit per rendere bilanciato il numero di valori **1** nel byte.

### Odd parity (Parità dispari)
Imposta a 1 l'**ottavo bit** se ciò è necessario per rendere dispari il numero di valori **1** nel byte.
### Even parity (Parità pari)
Imposta a 1 l'**ottavo bit** se ciò è necessario per rendere pari il numero di valori **1** nel byte.

## Parità bidimensionale
>[!definition]
>>Effettua un calcolo simile alla unidimensionale per ciascuna posizione di bit in tutti i byte contenuti nel frame.
>>Viene prodotto un byte aggiuntivo di parità per l'intero frame, in aggiunta al bit di parità presente in ciascun byte.

### Parità bidimensionale pari
+ Frame di 6 byte di dati
+ il terzo bit del byte di parità = 1 perché c'è un numero dispari di valori 1 nei terzi bit dei 6 byte del frame
>[!tip]
>Si può dimostrare che la parità bidimensionale rileva **tutti gli errori** che coinvolgono uno, due, tre e la maggioranza degli errori di 4 bit.

>[!warning] Errori di 4 bit
>Non sono individuabili se sono allineati sulla stessa riga e stessa colonna

In questo esempio abbiamo aggiunto 14 bit di informazioni ridondanti ad un messaggio di 42 bit.

**Schema esplicativo dell'esempio**:

![esempio_bit_parita_bidimensionale|700](/materie/anno_2025-2026/reti_di_calcolatori/assets/esempio_bit_parita_bidimensionale.svg)


## Algoritmo di checksum di Internet

Sommare tutte le parole che trasmettiamo:
- il risultato della somma è la **somma di controllo** (*checksum*)
Ricevente esegue lo stesso calcolo sui dati ricevuti
- confronta il risultato con il checksum ricevuto
- se qualsiasi dato trasmesso è stato corrotto il risultato non coinciderà quindi si è verificato un **errore**

### Esempio di uno schema
+ I dati da controllare: sequenza di **16 bit**
	+ sommarli usando l'aritmetica in complemento a uno a 16 bit
	+ infine si prende il complemento a uno del risultato: il **checksum a 16 bit**

Addizione $-5$ e $-2$:
+ numeri interi di 4 bit:
	+ $+5=0101$ quindi $-5=1010$
	+ $+2=0010$ quindi $-2=1101$
+ Se sommiamo $1010$ e $1101$ ignorando il riporto: $0111$
	+ è stato generato un riporto sul bit più significativo
	+ incrementiamo il risultato di un'unità
	+ otteniamo $1000$
	+ è la rappresentazione in complemento a uno di $-7$
	+ invertendo otteniamo $0111$ come ci aspetteremmo

```
u_short cksum(u_short *buf, int count) {
	register u_long sum = 0; \\ 16-bit checksum
	while (count--) { \\ count 16-bit units
		sum += *buf++; \\ 16-bit buffer units
		if (sum & 0xFFFF0000) { \\ if carry
			sum &= 0xFFFF; \\ erase carry
			sum++; \\ increment
		}
	}
	return ~(sum & 0xFFFF); \\ erase last carry
} \\ and complement
```

## CRC (Cyclic Redundancy Check)
>[!tip]
>Rilevare gli errori usando soltanto pochi bit ridondanti.

Un codice CRC a 32 bit fornisce una protezione robusta contro i più comuni errori di bit che si verifichino in messaggi con lunghezza di migliaia di byte.

+ Un messaggio di $(n+1)$ bit rappresentandolo con un polinomio di grado $n$.
+ valore di ciascun bit del messaggio come **coefficiente** di ciascun termine del polinomio (iniziando dal bit più significativo)

Messaggio di 8 bit: $10011010$
Polinomio: $M(x)=1\times x^{7}+0\times x^{6}+0\times x^{5}+1\times x^{4}+1\times x^{3}+0\times x^{2}+1\times x^{1}+0\times x^{0}$
+ Mittente e destinatario si scambiano i polinomi
+ Per calcolare un CRC mittente e destinatario si accordano su un **polinomio divisore** $C(x)$ di grado $k$
+ $C(x)=x^{3}+x^{2}+1$ $k=3$
>[!question] Come si sceglie $C(x)$ ?
>La scelta di $C(x)$ ha un impatto decisivo sul tipo di errori che vengono rilevati con una certa affidabilità.
>Esistono polinomi divisori che si dimostrano scelte valide per diverse situazioni.
>La scelta precisa fa parte del progetto del protocollo.

>[!example]
>Lo standard Ethernet usa un polinomio ben noto di grado 32.

- Mittente vuole trasmettere messaggio $M(x)$ lungo $n+1$ bit
	- viene inviato il messaggio di $n+1$ bit con $k$ bit aggiuntivi
	- $P(x)$: messaggio trasmesso con i bit ridondanti
	- rendere $P(x)$ divisibile per $C(x)$
- **No errori**: il ricevente dividendo $P(x)$ per $C(x)$ ha resto **0**;
- **Errori**: il polinomio ricevuto non sarà divisibile per $C(x)$ quindi **resto $\neq 0$**

I coefficienti possono assumere soltanto i valori 0 o 1 e operazioni sui coefficienti vengono eseguite con l'**aritmetica modulo 2**.

+ Qualsiasi polinomio $B(x)$ è divisibile dal polinomio divisore $C(x)$ se $B(x)$ è di grado superiore di $C(x)$
+ Qualsiasi polinomio $B(x)$ è divisibile una volta dal polinomio divisore $C(x)$ se $B(x)$ ha lo stesso grado di $C(x)$
+ Il resto ottenuto dividendo $B(x)$ per $C(x)$ si ottiene sottraendo $C(x)$ da $B(x)$
+ Per sottrarre $C(x)$ da $B(x)$ eseguiamo semplicemente l'operazione XOR su ciascuna coppia di coefficienti corrispondenti

Polinomio $x^{3}+1$ può essere diviso per $x^{3}+x^{2}+1$
+ Il resto della divisione: $0\times x^{3}+1\times x^{2}+0\times x^{1}+0\times x^{0} = x^{2}$
+ Possiamo dire che: $1001$ è divisibile per $1101$ con resto $0100$

### Esempio

Obiettivo di creare un polinomio da trasmettere derivato dal messaggio originale $M(x)$ che sia $k$ bit più lungo di $M(x)$ e che sia divisibile per $C(x)$:

1. Moltiplichiamo $M(x)$ per $x^{k}$ cioè aggiungiamo $k$ zeri alla fine del messaggio. Chiamiamo $P(x)$ questo messaggio.
2. Dividiamo $P(x)$ per $C(x)$ e calcoliamo il resto
3. Sottraiamo il resto da $P(x)$

Messaggio $x^{7}+x^{4}+x^{3}+x^{1}\Rightarrow 10011010$
+ moltiplichiamolo per $x^{3}$ perché il polinomio divisore è di grado 3
+ operazione ha come risultato $10011010000$
+ dividiamo per $C(x)=1101$
![[materie/anno_2025-2026/reti_di_calcolatori/assets/divisioneCRC.jpg]]
+ Il resto è $101$ quindi
	+ $10011010000$ meno $101$ sarebbe esattamente divisibile per $C(x)$ e questo è quello che **inviamo**
>[!tip]
>Nell'aritmetica dei polinomi, l'operazione di sottrazione è l'operazione di XOR logico per cui ciò che inviamo realmente è $10011010101$.

+ $10011010101$ è il messaggio originale con il **resto** accodato ad esso
+ il ricevitore divide il polinomio per $C(x)$ e se il risultato è 0 non ci sono stati errori
+ se il risultato $\neq 0$ potrebbe essere necessario eliminare il messaggio errato
+ ma con alcuni codici è possibile **correggere** un piccolo errore

>[!definition]
>Codice a correzione d'errore ECC
>>Codice che consente la correzione di errori.

### Trovare polinomio $C(x)$

Selezionare tale polinomio in modo che sia molto improbabile che sia un divisore con resto zero di un messaggio con errori.

+ Se il messaggio trasmesso è $P(x)$ 
+ introduciamo errori con l'aggiunta del polinomio $E(x)$ in modo che il ricevente veda il polinomio $P(x)+E(x)$
>[!warning]
>Un errore può sfuggire solo se il messaggio ricevuto è divisibile esattamente per $C(x)$ e poiché sappiamo che $P(x)$ può essere diviso esattamente per $C(x)$, può accadere solo se $E(x)$ può essere diviso esattamente per $C(x)$.

Prendere $C(x)$ in modo tale che ciò accada molto raramente per i tipi di errori più comuni.

#### Errore su un singolo bit
Si può esprimere come $E(x)=x^{1}$ nel caso in cui colpisca il bit in posizione $i$. 
+ scegliamo $C(x)$ in modo che il primo e l'ultimo termine siano diversi da zero
+ abbiamo un polinomio di due termini che non può essere divisore esatto dell'unico termine $E(x)$
+ $C(x)$ può rilevare tutti gli errori che colpiscono un singolo bit

È possibile dimostrare che i seguenti tipi di errori sono rilevabili da un polinomio $C(x)$ che abbia le caratteristiche enunciate:
+ Errori che colpiscono un singolo bit, se $C(x)$ ha i termini $x^{k}$ e $x^{0}$ con coefficienti $\neq 0$
+ Errori che colpiscono due bit, se $C(x)$ ha un fattore con almeno tre termini
+ Qualsiasi numero dispari di errori, se $C(x)$ contiene il fattore $(x+1)$
+ Errore a **burst**, se la lunghezza del burst è minore di $k$ bit

### Implementare algoritmo CRC nell'hardware
Si può realizzare usando un registro a scorrimento a $k$ bit e porte logiche XOR. 
Il numero di bit del registro a scorrimento è uguale al grado del polinomio generatore ($k$).

Esempio hardware per il generatore $x^{3}+x^{2}+1$

+ Messaggio viene fatto scorrere introducendolo da sinistra:
	+ iniziando con il bit più significativo e terminando con la stringa di $k$ zeri accodata al messaggio (come nella divisione in colonna)
+ quando i bit sono stati inseriti e le operazioni di XOR sono state eseguite
+ il registro contiene il resto cioè il CRC (con il bit più significativo a destra)
+ la posizione delle porte XOR si determina così:
	+ se i bit del registro a scorrimento vengono etichettati con i numeri interi da 0 a $k-1$ da sinistra a destra
	+ se il polinomio generatore è presente il termine $x^{n}$ si inserisce una porta logica XOR davanti al bit $n$
### Versioni di $C(x)$
- CRC-8: $x^{8}+x^{2}+x+1$
- CRC-10: $x^{10}+x^{9}+x^{5}+x^{4}+x+1$
- CRC-12: $x^{12}+x^{11}+x^{3}+x^{2}+x+1$
- CRC-16: $x^{16}+x^{15}+x^{2}+1$
- CRC-CCITT: $x^{16}+x^{12}+x^{5}+1$
- CRC-32: $x^{32}+x^{26}+x^{23}+x^{22}+x^{16}+x^{12}+x^{11}+x^{10}+x^{8}+x^{7}+x^{5}+x^{4}+x^{2}+x+1$

# Reliable Transmission (Trasmissione affidabile)
Un protocollo del livello di linea di connessione che voglia consegnare frame in maniera affidabile deve gestire queste situazioni in cui ci sono frame scartati o perduti.

>[!definition]
>Acknowledgement
>>È un piccolo **frame di controllo** restituito da un protocollo alla sua entità di pari livello per segnalare la ricezione di un frame precedente.
>>Frame di controllo si intende un'**intestazione** senza dati.

Il ricevimento di una conferma segnala al mittente del frame che tale frame è stato consegnato correttamente.

>[!definition]
>Timeout
>>Se il mittente non riceve conferma entro **un intervallo di tempo ragionevole** il frame viene ritrasmesso.

>[!definition]
>ARQ (Automatic Repeat Request)
>>Strategia che usa *acknowledgement* e *timeout* per realizzare la consegna affidabile.

## Stop-and-wait

>[!definition]
>>Dopo aver trasmesso un frame il mittente aspetta un acknowledgement prima di trasmettere il frame successivo.

Se l'acknowledgement non arriva entro un certo periodo di tempo, il mittente dichiara *timeout* e ritrasmette il frame.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/stop-and-wait.jpg]]
+ a) frame ACK viene ricevuto prima che scada il tempo
+ b) e c) vengono perduti il frame originale e il frame ACK
+ d) il tempo scade troppo presto
>[!warning]
>Supponiamo che il mittente invii un frame e il ricevitore ne dia conferma.
>La conferma va perduta o arriva in ritardo.
>Come illustrato in **(c)** e **(d)** il mittente dichiara timeout e ritrasmette il frame ma il ricevente penserà che si tratti del frame successivo perché aveva ricevuto correttamente il primo frame: questo può provocare la consegna di due copie di uno stesso frame.

Per ovviare al problema di copie di uno stesso frame in un protocollo stop-and-wait:
+ l'intestazione contiene un numero di sequenza di **un solo bit**
+ numero di sequenza può assumere soltanto i valori 0 e 1
+ 0 e 1 usati alternativamente per ciascun frame
+ il mittente ritrasmette il frame 0
+ il ricevitore è in grado di determinare se:
	+ è una seconda copia del frame 0 (nel caso ignora il frame)
	+ piuttosto che la prima copia del frame 1

>[!warning] Difetto dell'algoritmo
>Consente al mittente di avere un solo frame per volta sulla linea, in attesa di conferma, e ciò può essere molto meno di quanto consentito dalla capacità di collegamento.

>[!example]
>Una linea di collegamento a 1.5 Mbps con RTT 45 ms.
>Ritardo x ampiezza = 67.5 Kb cioè circa 8 KB.
>Dato che il mittente può inviare un solo frame per ciascun intervallo di tempo di durata RTT, ipotizzando una dimensione di frame di 1 KB ciò implica una **velocità massima** di invio di BitPerFrame/TempoPerFrame = $1024 \times 8/0.045= 182\textrm{ Kbps}$
>ovvero un ottavo della capacità della linea.
>Per sfruttare a pieno la linea dovremmo consentire al mittente di trasmettere fino a otto frame prima di metterlo in attesa di un acknowledgement.

## Sliding window
Tenendo a mente l'esempio di prima, vorremmo che il mittente fosse pronto per **trasmettere** il nono frame proprio nello **stesso momento** in cui arriva la conferma del **primo frame**.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/slidingWindowProtocol.jpg]]
### Mittente
+ assegna a ciascun frame un **numero di sequenza** (SeqNum):
	+ SeqNum: realizzato con un campo d'intestazione di dimensioni finite (ipotizziamo che possa diventare arbitrariamente grande)
	+ gestisce **tre variabili**:
		+ **dimensione della finestra di invio** SWS: il limite superiore per il numero di frame che il mittente può trasmettere sulla linea senza che questi siano confermati
		+ **LAR** (last acknowledgement received): indica il numero di sequenza dell'**ultima conferma ricevuta**
		+ **LFS** (last frame sent): indica il numero di sequenza dell'**ultimo frame inviato**
		+ invariante LFS - LAR $\leq$ SWS
	+ quando arriva una conferma sposta LAR verso **destra**
	+ così consente l'invio di un altro frame
	+ associa un conto alla rovescia a ciascun frame che trasmette con conseguente **ritrasmissione** se il tempo scade prima di aver ricevuto l'**ACK**

### Ricevitore
+ gestisce le variabili:
	+ **dimensione della finestra di ricezione** RWS: limite superiore per il numero di frame fuori sequenza che può accettare
	+ **LAF** (largest acceptable frame): il numero di sequenza del **frame accettabile più elevato**
	+ **LFR** (last frame received): il numero di sequenza dell'**ultimo frame ricevuto**
+ invariante LAF - LFR $\leq$ RWS
 
+ Se SeqNum $\leq$ LFP o SeqNum > LAF il frame si trova al di fuori della RWS viene **scartato**
+ Se LFR $<$ SeqNum $\leq$ LAF il frame si trova all'interno della RWS e viene **accettato**

+ SeqNumToAck: il più elevato numero di sequenza non ancora confermato in modo che tutti i frame con numeri di sequenza $\leq$ SeqNumToAck siano già stati ricevuti.

+ **Conferma cumulativa** la ricezione di SeqNumToAck anche se sono stati ricevuti pacchetti con numero più elevato 
+ LFR = SeqNumToAck
+ LAF = LFR + RWS

>[!example]
>LFR = 5 (l'ultimo ACK inviato dal ricevitore era relativo al numero di sequenza 5)
>RWS = 4
>Implica LAF = 9
>- Se dovessero arrivare i frame 7 e 8 (che sono dentro RWS) verrebbero memorizzati ma senza inviare alcun ACK
>- Perché il frame 6 non è ancora arrivato
>- Frame 7 e 8 sono arrivati **fuori sequenza**
>- Se dovesse arrivare il frame 6 in ritardo perché è stato perso
>- Ora il ricevitore
>	- confermerà il frame 8
>	- sposta LFR a 8
>	- sposta LAF a 12

### Problemi con lo Sliding Window Protocol
+ Quando avviene un timeout:
	+ quantità di dati in transito sulla linea diminuisce
	+ il mittente non è in grado di far avanzare la propria finestra

>[!tip]
>Quando si verificano perdite di pacchetti questo schema non è più in grado di mantenere la conduttura piena.
>Più tempo occorre per accorgersi che un pacchetto è andato perduto più grave diventa questo problema.

#### Migliorare inviando una delle seguenti conferme:
##### Conferma negativa (negative acknowledgement):
+ Per il frame 6 non appena fosse giunto il frame 7
+ non sarebbe necessario perché il meccanismo di **timeout** del mittente è **sufficiente** per gestire questa situazione e l'invio di conferme negative **aggiunge complessità** al ricevitore
##### Conferme aggiuntive
+ per il frame 5 quando sono stati ricevuti i frame 7 e 8
+ in alcuni casi il mittente può utilizzare le conferme duplicate come un segnale che un frame è andato perduto
+ Usato nel TCP
##### Conferme selettive
Il ricevitore potrebbe confermare i singoli pacchetti ricevuti, invece di segnalare il numero di sequenza più elevato dei frame ricevuti in ordine
+ Nell'esempio di prima il ricevitore potrebbe confermare la ricezione dei frame 7 e 8
+ Mittente sa che il frame 6 è perso
+ Mittente può mantenere il canale occupato (al prezzo di una complessità maggiore)
### Dimensione della finestra del mittente
Scelta in base al numero di frame che vogliamo avere in transito sulla linea in un determinato istante.

>[!tip]
>Facile calcolare SWS una volta assegnato il prodotto ritardo x ampiezza di banda.

+ Il ricevitore può usare il valore RWS che desidera
	+ RWS = 1: il ricevitore non memorizza alcun frame che arrivi **fuori sequenza**
	+ RWS = SWS: il ricevitore memorizza tanti frame quanti ne può trasmettere il mittente
+ Usare un valore **RWS > SWS** non ha senso, perché è impossibile che arrivino fuori sequenza frame in **numero maggiore di SWS**.
+ Se **RWS** **> SWS** il mittente potrebbe inviare i frame che il ricevitore non riesce a mettere in buffer e quindi devono essere scartati e ritrasmessi in seguito.

### Numeri di sequenza finiti
Numero di sequenza di un frame è specificato all'interno di un **campo dell'intestazione** (dimensione finita).

>[!example]
>Un campo di 3 bit: otto possibili numeri di sequenza da 0 a 7.

+ riutilizzare i numeri di sequenza
+ numeri di sequenza devono tornare al loro valore iniziale
+ distinguere fra diverse **incarnazioni** degli stessi numeri di sequenza
>[!tip]
>I numeri di sequenza **possibili** devono essere **più del numero di frame non confermati** a cui è consentito di essere in transito sulla linea.

#### Stop-and-wait
>[!example]
>L'algoritmo stop-and-wait consente solo un frame non confermato e ha quindi **due** numeri di sequenza (0 e 1).

#### Sliding window
+ Numeri disponibili come numero di sequenza sono uno in più del numero di frame in **transito**
+ SWS $\leq$ MaxSeqNum - 1
+ MaxSeqNum: **quantità di numeri di sequenza disponibili**
>[!question] È sufficiente?
>Dipende da RWS:
>- RWS = 1: MaxSeqNum $\geq$ SWS+1 **è sufficiente**
>- RWS = SWS: MaxSeqNum maggiore della dimensione della finestra di invio soltanto per un'unità **non è sufficiente**
>	- se abbiamo 8 numeri di sequenza 0-7
>	- SWS = RWS = /
>	- il mittente trasmette i frame da 0-6 
>	- ricevuti con successo ma **perdute** le conferme
>	- ricevitore aspetta il frame 7 seguito da frame numerati di nuovo da 0 a 5
>	- il mittente vede scadere le temporizzazioni e invia di nuovo i frame da 0 a 6
>	- ricevitore sta aspettando la **seconda incarnazione** dei frame da 0 a 5 ma riceve **una copi dei precedenti**
>	- **situazione che vogliamo evitare**

Nel caso RWS = SWS: la dimensione della finestra di invio non può essere maggiore della metà del numero di numeri di sequenza disponibili.

$\textrm{SWS}<\frac{(\textrm{MaxSeqNum}+1)}{2}=2^{n-1}$
$n$: sono i bit per il numero di sequenza.

+ solo **metà** dei numeri di sequenza possono essere sospesi in qualsiasi momento
>[!example]
>Dall'esempio sopra settiamo RWS = SWS = 4
>- mittente invia i frame da 0 a 3 e aspetta per gli ACK
>- ricevitore riceve i frame da 0 a 3 e manda i corrispettivi ACK e aspetta per i frame da 4 a 7
>- tutti gli ACK vanno persi
>- mittente **ritrasmette** da 0 a 3
>- ricevitore stava aspettando da 4 a 7 ma riconosce che i frame da 0 a 3 sono copie di quelli già ricevuti quindi non li accetta e manda gli ACK di nuovo

# ETHERNET (IEEE 802.3)

Usa il protocollo **CSMA/CD** (Carrier Sense Multiple Access with Collision Detect, accesso multiplo a sensore di portante con rilevazione di collisione).

>[!definition]
>>Rete ad accesso multiplo: insieme di nodi inviano e ricevono frame tramite una linea di connessione condivisa.
>Ethernet è come un **autobus** con più fermate lungo la sua linea.

>[!definition]
>Carrier sense
>>Tutti i nodi sono in grado di distinguere una linea **inattiva** da una linea **occupata**.

>[!definition]
>Collision Detect
>>Un nodo rimane in ascolto mentre trasmette e può quindi capire quando un frame che sta trasmettendo subisce interferenza da un frame trasmesso da un altro nodo.

>[!question] Come mediare l'accesso ad un mezzo condiviso in modo equo ed efficiente?
>Algoritmo che controlla il momento in cui ciascun nodo può trasmettere.

## Proprietà fisiche - 10Base5

Ethernet si realizza con cavo coassiale di lunghezza fino a 500 m.

+ Possono connettersi fino a **100 host** mediante prese *tap*
+ prese devono essere distanti una dall'altra almeno 2.5 m
>[!definition]
>Transceiver
>>Piccolo dispositivo elettronico che rileva i momenti in cui la **linea è inattiva** e **pilota il segnale** quando l'host trasmette.
>>Riceve i segnali in ingresso.
>>Collegato a un **adattatore** Ethernet nell'host.

![[materie/anno_2025-2026/reti_di_calcolatori/assets/ethernet10base5.jpg]]

![[materie/anno_2025-2026/reti_di_calcolatori/assets/transceiveradaptor.jpg]]

+ Qualsiasi segnale inserito sulla Ethernet da un host viene pervenuto dall'intera rete
	+ segnale si propaga in **entrambe** le direzioni
	+ ripetitori **inoltrano** il segnale su tutti i **segmenti**
	+ **terminatori** alla fine di ciascun segmento **assorbono** il segnale ed impediscono che rimbalzi

10base5 Ethernet usa lo schema di codifica **Manchester**:
+ 0V quando non trasmette
+ $\pm0.85V$ quando trasmette

+ Più segmenti ethernet possono essere uniti mediante **ripetitori**

>[!definition]
>Ripetitori
>>Dispositivi che inoltrano segnali digitali più o meno come un amplificatore è in grado di inoltrare segnali analogici.


>[!warning]
>Tra una coppia di Host non si possono inserire più di quattro ripetitori.
>Una rete Ethernet ha una estensione massima di 2500 m.

+ segmenti possono essere connessi in ogni modo a patto che
	+ non ci siano loop
	+ non ci siano più di 4 ripetitori tra gli host
+ tipico collegamento era un segmento che collegasse solo i ripetitori (**backbone**)
	+ tutte le stazioni sono su connesse ad ogni segmento

![[materie/anno_2025-2026/reti_di_calcolatori/assets/connessioneripetitori.jpg]]

## 10Base2, 10BaseT

### 10Base2
+ Cavo più sottile
+ rete opera a 10Mbps
+ Base: il cavo viene usato come sistema in **banda base**
+ 2: un segmento non può essere lungo più di 200 m
### 10BaseT
+ T: **twisted pair** cavo doppino intrecciato
+ lunghezza massima 100 m
+ usa la decodifica 4B/5B e MLT-3 invece della Manchester

## Fattori velocità minima per cavi di rete
+ Fattore velocità = velocità della luce in media / velocità della luce nel vuoto
+ più lenta è il fattore velocità, più lentamente il segnale si propaga, più grande sarà il **delay** introdotto dalla propagazione di segnale
+ Il fattore velocità è molto diverso a seconda del mezzo
![[materie/anno_2025-2026/reti_di_calcolatori/assets/velocityfactor.jpg]]

## Ethernet 10BaseT
+ Configurazione: segmenti **punto-punto** connessi ad un ripetitore a molte vie (**hub**)
	+ riceve un frame su una porta
	+ lo inoltra a tutte le altre porte (store-and-forward of frames, CRC check, non bit-by-bit like repeaters)
	+ da **non** confondere con gli switch
+ ogni doppino intrecciato può essere considerato come un **singolo segmento Ethernet** (un host trasmettitore e un host ricevitore)
	+ un paio da hub all'host e un paio dall'host all'hub
	+ le due coppie sono indipendenti: entrambe le parti possono trasmettere allo stesso tempo (**full duplex**)

## Mixed networks
>[!definition]
>>Gli host sono connessi agli hub, che sono connessi tra di loro da un cavo 10base-5 o 2 (**backbone**).

+ La rete deve essere intesa come una **singola**: un frame inviato da un host è inviato a ogni segmento e a tutti gli host.
## Formato del frame
![[materie/anno_2025-2026/reti_di_calcolatori/assets/frameformat.jpg]]
+ **Preambolo** (7 byte 10101010): su 10Base5 e 10Base2 genera un onda quadra di 10 MHz che permette al ricevitore di sincronizzarsi con il segnale
+ **Start of Frame Delimiter** (8 bit 10101011): sentinella che indica l'inizio del frame
+ **Host sorgente e destinazione**: identificati da un indirizzo a 48 bit
+ **VLAN** tag (optional, 4 byte): indica a quale Virtual LAN appartiene questo frame
+ **Packet type** (16 bit): agisce come **chiave di demux** per identificare un protocollo di livello più alto
+ **Data** (minimo 64 byte, massimo 1500 byte):
	+ devono essere aggiunti dei byte riempitivi prima della trasmissione
	+ esiste una dimensione minima perché deve essere sufficientemente lungo da consentire la rilevazione di una **collisione**
+ **CRC-32** (32 bit)
+ **Overall**: un 14(+4) byte in testa e 4-byte nella coda
	+ 8 byte di preambolo e SFD che non sono parte del frame

## Indirizzi
Ogni hot ha un indirizzo Ethernet univoco composto da 48 bit.
Limite teorico di $2^{48}=2.8\*10^{14}$

+ L'indirizzo è relativo all'**adattatore** non all'host:
	+ solitamente era scritto in una ROM, ora nella **flash memory** dell'adattatore
	+ a ciascun produttore di dispositivi Ethernet viene assegnato un diverso prefisso (**primi 3 byte**) che costruisce la parte iniziale dell'indirizzo
+ L'indirizzo è una sequenza di sei numeri separati dal carattere ":"
	+ ciascun numero corrisponde ad uno dei **6 byte** ed è scritto come coppia di cifre esadecimali una per ciascuna delle due parti di **4 byte** eliminando eventuali zeri iniziali
>[!example]
>8:0:2b:e4:b1:2 corrisponde a:
>00001000 00000000 00101011 11100100 10110001 00000010
## Algoritmo del ricevitore
Ciascun frame trasmesso in una rete Ethernet viene ricevuto da **tutti** gli adattatori ad essa connessi:
+ ciascun adattatore identifica i frame che sono destinati al **suo indirizzo**
+ controlla il CRC
+ passa soltanto quelli all'host
+ ignora gli altri indirizzi **unicast**

>[!definition]
>Indirizzo Broadcast
>>Tutti i bit a 1: i frame con destinazione broadcast vengono passati da tutti gli adattatori al proprio host.

>[!definition]
>Indirizzo Multicast
>>Primo bit ha valore 1.
>>Sono usati per inviare messaggi a sottoinsiemi degli host di una Ethernet.

Adattatore Ethernet **riceve** tutti i frame e accetta soltanto:
+ i frame destinati al **proprio indirizzo**
+ i frame destinati **all'indirizzo broadcast**
+ frame destinati ad un indirizzo multicast se ha ricevuto istruzioni per ascoltare il traffico destinato a tale indirizzo
+ tutti i frame, se è stato configurato per funzionare in modalità promiscua
## Algoritmo del trasmettitore

**Media Access Control (MAC)**

>[!definition]
>>Il frame viene trasmesso immediatamente senza alcuna negoziazione con gli altri adattatori.

>[!tip]
>Il limite superiore di **1500 byte** per il messaggio garantisce che l'adattatore può impegnare la linea solo per un **periodo di tempo prefissato**.

+ Quando la linea è **impegnata** adattatore ha un frame da inviare :
	+ aspetta finché la linea non diventa **idle**
	+ **protocollo con persistenza**: adattatore trasmette con probabilità $0\leq p \leq 1$ dopo che una linea è diventata **idle**.
### CSMA/CD Protocol
![[materie/anno_2025-2026/reti_di_calcolatori/assets/csma-cd.jpg]]
+ **Idle**: linea inattiva
+ **Contesa**: alcune stazioni vogliono trasmettere e devono aspettare che la linea sia **liberata**
	+ Significa che non ci sarà segnale sulla linea per il tempo **IPG**: 12 byte = 96 bit 9.6$\micro s$ in 10Base-5 e 2
+ **Trasmissione**: una o più stazioni trasmettono
>[!tip]
>Dividere il tempo in **intervalli discreti** dove ciascun intervallo corrisponde al tempo necessario per **trasmettere un intero frame**.

+ un nodo ha un frame da inviare:
	+ presenza di intervallo libero
	+ trasmette con **probabilità** $p$
	+ attende l'intervallo successivo con probabilità $q=1-p$
	+ se anche il successivo è vuoto
		+ nodo decide se trasmettere oppure no
		+ con **stesse** probabilità $p$ e $q$
	+ se il successivo **non è vuoto**:
		+ il nodo **attende** il successivo intervallo inattivo
		+ algoritmo si ripete

+ Poiché non esiste controllo **centralizzato**:
	+ due o più adattatori inizino a trasmettere nello **stesso momento**
	+ perché linea inattiva oppure hanno aspettato che lo diventasse
	+ si dice che i due frame hanno **colliso**

#### Collisioni
Ethernet è in grado di gestire le collisioni:
+ ciascuna sorgente può stabilire che si sta verificando una collisione
	+ comparano cosa tramettono e cosa ricevono: se la differenza non è **0** c'è collisione
+ quando un adattatore si accorge che il suo frame sta entrando in collisione con un altro
	+ trasmette una sequenza di disturbo di **32 bit** (**jamming sequence**)
	+ interrompe la trasmissione
	+ **in caso di collisione** il trasmettitore invierà minimo soltanto **96 bit**: 64 bit di preambolo e 32 bit di sequenza di disturbo
>[!definition]
>Runt Frame
>>Caso in cui un adattatore invierà soltanto 96 bit, quando due host che **generano collisione**, sono **adiacenti**.

#### Caso peggiore
>[!definition]
>>I due host si trovano in posizione opposte della rete.

+ Il trasmettitore dovrebbe inviare fino a 512 bit:
	+ ogni frame Ethernet ha almeno 512 bit (64 byte):
		+ 14 byte di intestazione
		+ 46 byte di dati
		+ 4 byte di CRC
>[!question] Perché proprio 512 bit ? Perché la lunghezza è limitata a soli 2500 m ?
> Più due nodi sono distanti, **più tempo serve** al frame inviato da un nodo per raggiungere l'altro nodo, in tale intervallo di tempo la **rete è vulnerabile** al fenomeno della **collisione**.

>[!example]
>- l'host A inizia a trasmettere un frame all'istante $t$
>	- $t\_{prop}$ = latenza del collegamento (tempo di propagazione)
>	- frame impiega un tempo $t\_{prop}$ per raggiungere A
>	- il primo bit del frame di A arriva in B all'istante $t+t\_{prop}$
>- supponiamo che un'istante prima che il frame di A arrivi in B (B vede la linea **inattiva**)
>	- host B inizia a trasmette il suo frame
>	- colliderà subito con il frame A
>	- tale **collisione** sarà rilevata da B
>	- B invierà una sequenza di disturbo di 32 bit
>	- A non saprà della collisione finché non arriverà il frame di B
>	- che accadrà dopo un tempo uguale **alla latenza della linea** $t+2\times t\_{prop}$
>	- per rilevare la collisione A deve continuare a trasmettere fino a tale istante: $2\times t\_{prop}$

Considerando che:
+ Ethernet più estesa al massimo di 2500 m
+ tra due host qualsiasi ci possono essere fino a **quattro** ripetitori
	+ con **delay** limitato a 3.7$\micro s$
+ **ritardo round-trip** è stato quantificato in 51.2$\micro s$
	+ in una Ethernet a 10 Mbps equivale a 512 bit

>[!tip]
>Limitare la **latenza massima** di una Ethernet ad un valore **sufficientemente piccolo** perché l'algoritmo funzioni.

>[!definition]
>Backoff esponenziale
>> - Quando un adattatore ha rilevato una collisione e interrotto la propria trasmissione attende un certo periodo di tempo e riprova:
>> 	- ogni volta che tenta di **trasmettere** e **fallisce:**
>> 	- **raddoppia** il periodo di tempo di attesa prima del tentativo successivo

>[!tip] Conseguenza
>Il tempo necessario per trasmettere il frame non è **deterministico**: dipende da **quante collisioni avvengono**, cioè da quanti **adattatori stanno tentando di trasmettere** e quindi **del carico complessivo della rete**.

>[!example]
> - SlotTime = 51.2$\micro s$
> 	- primo tentativo: adattatore prova a trasmettere immediatamente **dopo aver atteso l' IPG**. (Se non sono rilevate collisioni durante lo SlotTime).
> 	- altrimenti l'adattatore:
> 		- manda un *runt frame*
> 		- aspetta l'IPG e riprova
> 		- ma con un **delay** di 0 o SlotTime (scelta random)
> 	- se fallisce (collisione) prova ancora ma sta volta
> 		- tempo di attesa: $k\times \textrm{SlotTime}$ per $k=0...3$ random
> 	- nel caso di altra collisione aspetta $k\times \textrm{SlotTime}$ con $k=0...2^{3}-1$

+ In generale dopo $n$ collisioni l'algoritmo seleziona random $k=0 ... 2^{n}-1$:
	+ Se $10<n<16$ l'esponente è fissato a 10
+ $n$ è limitato a 15
	+ dopo 16 collisioni consecutive il pacchetto viene scartato e segnala un errore
	+ **praticamente impossibile**: solo se il cavo ha un difetto hardware
![[materie/anno_2025-2026/reti_di_calcolatori/assets/transmitteralgorithm.jpg]]

## Efficienza
- L’efficienza è la **frazione a lungo termine delle trasmissioni riuscite**, cioè la **frazione a lungo termine del canale effettivamente usata per i dati**.

- L’efficienza è data dal **rapporto tra il tempo di trasmissione** e il **tempo effettivo necessario per trasmettere un frame**.

- Il protocollo **CSMA/CD** non è semplice da analizzare, a causa della sua natura **non deterministica** e del fatto che **non tutte le stazioni si comportano nello stesso modo**.

- Consideriamo alcune situazioni semplificate:
    - Quando **una sola stazione trasmette**.
    - Quando **tutte le stazioni si comportano nello stesso modo**.

### Stazione trasmittente singola

- Caso molto semplice: **una singola stazione trasmette** sul canale e tutte le altre **ricevono soltanto**.
    
- Questa è la situazione tipica di una **LAN basata su hub o switch**: ogni doppino (coppia di fili) rappresenta un **dominio di collisione**, con **1 trasmettitore** e **1 ricevitore**.
    
- In questo scenario **non si verificano collisioni**: un frame viene inviato con successo **immediatamente dopo l’intervallo IPG**.

**Parametri:**
- $IPG = 9.6\ \mu s = 96\ bit = 12\ byte$
- Preambolo + SFD = 8 byte
- $P$ = lunghezza del payload (fino a 1500 byte)
- Header + CRC = 18 byte

**Efficienza teorica:**
$$
η= \frac{P}{12 + 8 + P + 18} = \frac{P}{P + 38} = \frac{1}{1 + \frac{38}{P}}​
$$

$$
η=\frac{1}{1+\frac{38}{P}​}​
$$
- Più grande è $P$, **più efficiente** è il protocollo.
- **Caso peggiore con padding:** $P = 1$ ma in realtà $P = 46$ (a causa del padding)
$$
    η=\frac{1}{46 + 38} = \frac{1}{84} \approx 1.2\%
    $$
- **Caso peggiore senza padding:** $P = 46$
$$
η=\frac{46}{46 + 38} = 0.54 = 54\%
$$
- **Caso migliore:** $P = 1500$
$$
η=\frac{1500}{1500 + 38} \approx 0.97 = 97\%
$$
![[materie/anno_2025-2026/reti_di_calcolatori/assets/ethernetefficiency.jpg]]

### N stazioni uguali in competizione
![[materie/anno_2025-2026/reti_di_calcolatori/assets/stationscompeting.jpg]]
- $N$ stazioni identiche **competono** per l’uso di un mezzo condiviso (cavo, hub, ecc.).
- A ogni _slot_, ogni stazione vuole trasmettere un frame (nuovo o ritrasmesso dopo una collisione) con **probabilità $p$**.
- Il valore medio di stazioni che vogliono trasmettere in ogni slot è **$N \cdot p$**, che rappresenta il **carico complessivo della rete**.
- Una trasmissione ha **successo** se, per l’intera durata dello slot, **una sola stazione** trasmette e **non si verificano collisioni** (tutte le altre restano silenti).  
    In tal caso, **l’intero frame viene trasmesso**, anche se la durata supera un singolo slot.
- Se invece si verifica **un errore** (slot vuoto o collisione), la stazione **ritenta nello slot successivo** (_1-persistence_).

- Qual è la **probabilità che uno slot venga usato con successo** per la trasmissione di un frame?
$$P(\text{successo}) = P(\text{esattamente una delle N stazioni trasmette}) = Np(1 - p)^{N - 1}
$$
- La **probabilità massima** si ha quando $p = 1/N$, cioè $Np = 1$.
- Di conseguenza, per **evitare collisioni** e **massimizzare il throughput complessivo** (cioè l’uso utile del mezzo condiviso), **più stazioni ci sono, minore deve essere la loro probabilità di trasmissione**.

Nel caso $N$ grande:

$$
P(\text{successo}) = (1 - \frac{1}{N})^{N - 1} \approx \frac{1}{e} \approx 0.37
$$

- Al massimo, **solo il 37% degli slot** è utilizzato da trasmissioni riuscite (per $N$ grande).
- Numero medio di tentativi per inviare un frame:  
    $\frac{1}{(1/e)} = e \approx 2.7$

#### Grafico
![[materie/anno_2025-2026/reti_di_calcolatori/assets/efficiencygraph.jpg]]

Il grafico mostra la **frazione di slot occupati con successo** (cioè **senza collisioni**) in funzione della probabilità $p$ che ogni stazione trasmetta in un dato slot.
>[!example] 
>$N = 10$.
>L’efficienza cresce inizialmente con $p$, ma oltre un certo punto diminuisce a causa dell’aumento delle collisioni.

Definizioni:
- $t\_{trans}$ = tempo per trasmettere il payload  
    $t\_{trans} = \frac{\text{payload}}{\text{bitrate}}$
- Tempo di slot = $2t\_{prop}$
- $t\_{oh}$ = overhead del frame  
    $(\text{preambolo} + \text{header} + \text{CRC}) / \text{bitrate}$
    
**Tempo medio di trasmissione** (massimizzando il throughput, cioè $Np = 1$):  
$$t\_{avg} = IPG + e \cdot 2t\_{prop} + t\_{trans} + t\_{oh}
$$  
(dato che, in media, servono $e$ tentativi)

**Efficienza:**  
$$
\eta = \frac{t\_{trans}}{t\_{trans} + IPG + t\_{oh} + 2e t\_{prop}} = \frac{1}{1 + \frac{IPG + t\_{oh} + 2e t\_{prop}}{t\_{trans}}}
$$

**Per aumentare l’efficienza:**
- Ridurre $t\_{prop}$: se il ritardo di propagazione tende a zero, i nodi in collisione interrompono immediatamente la trasmissione senza sprecare il canale.
- Aumentare $t\_{trans}$: quando una stazione ottiene il canale, lo mantiene a lungo, rendendo il canale produttivo per la maggior parte del tempo.

### Caso 10Base-5
Nel caso dell’Ethernet 10Base-5 (10 Mbps), esprimendo i tempi in byte:
- $IPG = 9.6,\mu s = 96,bit = 12,byte$
- $t\_{prop} = 25.6,\mu s = 256,bit = 32,byte$
- $t\_{oh} = 8 + 14 + 4 = 26,byte$
- $P$ = payload (in byte)

**Efficienza:**  
$$
\eta = \frac{1}{1 + \frac{38 + 64e}{P}} = \frac{1}{1 + \frac{212}{P}}
$$

>[!example]
> - Se $P = 1500$ byte → $\eta = 87.6\%$
> - Se $P = 46$ byte → $\eta = 17.8 \%$
>Una rete Ethernet classica a 10 Mbps, condivisa tra molte stazioni equivalenti, offre in pratica solo 8.7–8.8 Mbps complessivi, da dividere tra tutti i nodi.
>- L’efficienza $\eta \to 1$ quando $t\_{prop} \to 0$ oppure $P \to \infty$.  
>	- → Reti piccole e/o frame grandi migliorano l’efficienza.
>- Per questo motivo, gli standard Ethernet più recenti prevedono:
>	- Distanze massime più brevi (fino a <35 m)
>	- Frame più grandi (_Jumbo Frames_, fino a 8 KB o più)

**Tuttavia:**
- Frame più grandi implicano che le altre stazioni debbano attendere più a lungo, aumentando il ritardo medio.
- Ethernet funziona al meglio sotto **condizioni di carico leggero**: quando il traffico è intenso, una parte significativa della capacità viene sprecata in collisioni.
- Per questo motivo, la maggior parte delle reti Ethernet:
    - Ha meno di 200 host, ben al di sotto del massimo teorico di 1024.
    - È molto più corta di 2500 m, con un ritardo di andata e ritorno di circa 5 μs, molto inferiore al limite di 51.2 μs.

## Esperienza con Ethernet
- Le **Ethernet classiche** sono **facili da amministrare e mantenere**.
- È semplice **aggiungere un nuovo host** alla rete: basta collegarlo al cavo.
- È una tecnologia **economica**: il cavo è poco costoso, e l’unico altro costo è quello dell’adattatore di rete su ciascun host (che comunque è necessario).  
    _(Nota: ciò non è più vero nelle Ethernet commutate, dove servono switch.)_
- **Non ci sono switch** che possono guastarsi né tabelle di instradamento o configurazione da mantenere aggiornate.  
    _(Anche questo non è più valido per le Ethernet commutate.)_
- Ethernet è riuscita a **tenere il passo con l’evoluzione tecnologica**.
- Per queste ragioni, Ethernet è stata **enormemente di successo**, mentre i protocolli concorrenti — come **IEEE 802.4 (Token Bus)**, **802.5 (Token Ring)** o **HYPERchannel** — sono scomparsi.
- Sono state sviluppate **molte varianti**, tra cui versioni per:
    - **Industria**,
    - **Avionica**,
    - **Ferrovia**,
    - e persino versioni **deterministiche**.
- Ethernet ha **ispirato altri protocolli**, in particolare **IEEE 802.11 (Wi-Fi)**.
- La maggior parte delle considerazioni fatte per l’Ethernet classica **vale anche per il Wi-Fi**.

# Wireless Communication
Range di segnali elettromagnetici
+ Mezzo: etere
	+ è un mezzo condiviso
	+ si ripropongono tutte le problematiche dei mezzi condivisi (come Ethernet)
+ Cercare di rendere **efficiente** questo mezzo
+ range di frequenze **suddiviso in bande**
+ **ISM**: esistono frequenze liberalizzate (esenti da licenza)

## ISM 2.4 GHz
+ Va da i 2400 MHz ai 2480 MHz
+ dove vivono gran parte delle comunicazioni di uso normale
>[!question] Perché è stata scelta questa frequenza ?
>Semplice per lavorarci
>Frequenza di vibrazione della molecola dell'acqua

+ suddivisa in tanti canali ciascuno di una banda di 20 MHz

## ISM 5 GHz
+ parte dai 5070 MHz e termina a 5835 MHz
+ suddivisi in canali da 20 MHz
+ si possono aggregare i canali da 20 in canali più grandi
+ più soggetta a disturbi
## Regole
* Liberalizzate non significa deregolamentate
* **Potenza**: sulla 2.4 GHz possiamo trasmettere al massimo 100 mW
	* limitare la portata del segnale (qualche centinaio di metri)
### Spread Spectrum (spettro disperso)
>[!definition]
>>Non occupare una frequenza in maniera fissa, cercare di occupare il canale il più possibile
+ **sparpagliando il segnale** su tutta la banda diminuiamo la possibilità di interferenza
#### Frequency hopping
>[!definition]
>>prendere un range di frequenze e saltellare da una all'altra (Hedy Lamarr)
>>
- ordine dei salti **pseudocasuale**
- chi riceve deve seguire la stessa sequenza dei salti
- evitare conflitti tra trasmissioni diverse

#### Direct sequence (sequenza diretta): 
* se abbiamo una sequenza di bit da trasmettere, trasmettiamo il risultato dello XOR tra questa sequenza e un'altra sequenza di bit (**chipping sequence**) casuali (ogni bit dura 1$\micro s$)
* facendo lo XOR tra i due segnali otteniamo un segnale
* chi riceve per avere il segnale originale rifà una XOR sul segnale che riceve utilizzando la stessa chipping sequence

+ tecnologie wireless differiscono in varie cose:
	+ quanta banda usano
	+ quanto lontani possono essere i nodi che devono comunicare
+ Quattro tecnologie principali:
	+ Wi-Fi 802.11
	+ Bluetooth
	+ WiMAX 802.16 (eolo)
	+ 3G/4G/5G
+ ognuna di queste tecnologie ha un ambito di utilizzo
	+ bluetooth: distanza di lavoro **bassa** (decina di metri)
	+ Wi-Fi: analogo della ethernet solo wireless
		+ distanza di lavoro sui 100 m
		+ Bitrate: dai 54 ai 320 Mbps
	+ Cellulare: rete di accesso a lunga distanza
		+ Bitrate: centinaia di Kbps

+ Reti wireless sono **asimmetriche**:
	+ due end-point sono due tipi di nodi diversi
	+ il segnale non è diretto ma è trasmesso in maniera **sferica**
	+ potenza del segnale scende con il quadrato della distanza
+ wireless supporta una comunicazione punto-multipunto:
	+ diretta (Wi-Fi)
	+ attraverso routing (cellulari e bluetooth)
+ mobilità:
	+ No mobilità: il ricevitore deve essere in una location fissa per ricevere il segnale (tipo eolo)
	+ Mobilità all'interno del range (Bluetooth)
	+ Mobilità tra stazioni: mi muovo e cambio cella (cellulari e Wi-Fi)
+ Reti Mesh o ad-hoc
	+ nodi si organizzano tra loro senza avere un access point
	+ utile quando non ci sono stazioni base fisse (nell'IoT) per raggiungere aree che non sono coperte

# Wi-Fi

Pensato per creare reti locali (decine/centinaia di metri).

## Standard
+ utilizzare il frequency hopping su 79 canali (1 usato per controllo)
+ direct sequence usando una sequenza chipping sequence da 11 bit
+ migliorata con la 802.11b
	+ usando una variante della direct sequence arrivando fino a 11 Mbps
+ infine la 802.11a che arriva fino a 54 Mbps usando OFDM
	+ 5 GHz
	+ velocità possibile si aggira attorno ai 20 Mbps
+ 802.11ac
	+ usata per la 5GHz e arriva fino a 1300 Mbps
+ Il rapporto segnale rumore può essere molto variabile
+ 802.11n 
	+ si può andare da i 6.5 Mbps ai 600 Mbps
+ si adatta in base alla quantità di rumore del canale

## Evitare collisioni
>[!tip]
>In una rete wireless il problema è ulteriormente complicato, perché non tutti i nodi sono sempre raggiungibili da tutti gli altri.

>[!example]
>![[materie/anno_2025-2026/reti_di_calcolatori/assets/reti_wifi.jpg]]
>- B può scambiare frame con A e con C ma non può raggiungere D
>- C può raggiungere B e D ma non A
>- supponiamo che sia A sia C vogliono comunicare con B
>	- entrambi trasmettono un frame
>	- A e C non sono consapevoli della reciproca presenza
>- questi due frame **collidono** l'uno con l'altro in B
>- ma né A né C si accorgono di questa collisione
>- A e C sono **nodi nascosti** l'uno all'altro

#### Problema del nodo esposto
+ supponiamo che B stia trasmettendo verso A
+ il nodo C e consapevole di tale comunicazione (ascolta la trasmissione di B)
	+ sarebbe un errore per C decidere di non trasmettere a nessuno solo perché sta assistendo alla trasmissione di B
	+ C potrebbe trasmettere a D
	+ interferirebbe se la trasmissione fosse da A a B
### MACA o CSMA/CA (Multiple Access with Collision Avoidance)
>[!definition]
>>La sorgente e la destinazione si scambiano frame di controllo l'un l'altro **prime che la sorgente trasmetta** realmente i dati.
>>Questo scambio informa **tutti i nodi vicini** che sta per iniziare una trasmissione.

+ Sorgente trasmette un frame **richiesta di invio** RTS:
	+ indica per quanto tempo la sorgente intende impegnare il mezzo 
+ Ricevitore risponde con un frame di tipo **libero di inviare CTS**
	+ dove viene ricopiata la lunghezza dichiarata dalla sorgente
+ un nodo che veda frame CTS sa di essere vicino al ricevitore quindi non potrà trasmettere per il tempo del RTS
	+ questo tempo è chiamato **NAV (Network Allocation Vector)**
	+ questo risolve il problema del **nodo nascosto**
+ un nodo che veda l'RTS ma non il CTS non è abbastanza vicino al ricevitore per interferire (può trasmettere liberamente)
	+ questo risolve il problema del nodo esposto

+ Il ricevitore invia un ACK alla sorgente dopo aver ricevuto con successo un frame
	+ tutti i nodi devono attendere tale ACK prima di provare a trasmettere
+ se due o più nodi dovessero trovare il mezzo inattivo e provassero a trasmettere un frame RTS nello stesso istante
	+ ci sarebbe **collisione**

802.11 non consente la rilevazione di collisione: 
+ le sorgenti capiscono che è avvenuta una collisione quando non ricevono il frame CTS dopo un certo periodo
+ ciascuna di esse aspetta un intervallo casuale prima di riprovare
+ durata dell'attesa definita dall'**algoritmo di backoff esponenziale** usato da Ethernet

>[!example]
>![[materie/anno_2025-2026/reti_di_calcolatori/assets/dstributed_coordination.jpg]]
>![[materie/anno_2025-2026/reti_di_calcolatori/assets/dstributed_coordination_2.jpg]]
>- S1 e S2 vogliono trasmettere
>	- stanno in ascolto e vedono che c'è segnale
>	- aspettano un certo tempo fisso
>	- S1 aspetta 5 volte
>	- S2 aspetta 9 volte 
>	- S1 manda l'RTS a R
>	- S2 è in ascolto (sente l'RTS di S1) quindi alloca sul NAV
>	- R risponde con un CTS dopo il SIFS
>		- nel CTS c'è scritto quanto manca alla fine della comunicazione
>		- S1 ricevuto il CTS, switcha e trasmette il vero frame di dati
>		- R riceve il frame di dati poi switcha e manda un frame di ACK
>- questo costa 
#### Intervalli
Sempre definiti come: SIFS < PIFS < DIFS
+ **Slot time**: intervallo minimo usato nel **backoff esponenziale**
+ **SIFS (Short Inter Frame Space)**: spazio di silenzio minimo che c'è tra due frame all'interno di una stessa trasmissione
	+ tempo usato per processare e rispondere un frame 
+ **PIFS (Point Control Function Interframe Space)**: tempo minimo che deve aspettare una stazione per trasmettere i suoi dati
	+ PIFS = SIFS + Slot time tempo che deve aspettare l'access point
	+ PIFS ha la priorità perché è minore
+ **DIFS (Distributed Control Function Interframe Space)**: tempo che la stazione deve aspettare prima di mandare un RTS

![[materie/anno_2025-2026/reti_di_calcolatori/assets/intervalli.jpg]]

+ PIFS = SIFS + Slot time
+ DIFS = SIFS + 2 * Slot time

## Formato del frame
+ BEACON: serve agli access point a segnalare la presenza
+ Intestazione 802.11:
	+ 30 byte
+ FCS: sarebbe un CRC 32
+ 34 byte fissi
+ Address 1,2,3 sono indirizzi di 802 e sono univoci
	+ cambia a seconda della modalità di trasmissione
+ Dati di network: sono quelli che vengono dai livelli superiori
	+ da 0 a 2312 Byte
	+ non c'è bisogno di un valore minimo perché non abbiamo collisioni da gestire
+ Frame protocol:
	+ Type: scrive se è un RTS, CTS, ACK, ecc...
	+ Power Mgmt: abilitare e disabilitare la scheda di rete
	+ WEP: serve a verificare se il PAYLOAD è cifrato o no
+ RTS:
	+ bit di controllo che serve di riconoscimento
	+ duration serve per il NAV
+ CTS:
	+ duration di prima - RTS - SIFS
	+ Receiver address è quello di A

30 Byte di intestazione + 4 Byte di CRC del Data + 14 Byte + 20 Byte + 14 Byte = 82 Byte più gli intervalli

## Efficienza
Modellare bene il CSMA/CA è difficile
+ andiamo a 54 Mbps
+ abbiamo un ricevitore e trasmettitore
	+ 1 DIFS + 3 SIFS = 4 SIFS + 2 Slot time = 4 * 10+2 * 9 = 58 $\micro s$
	+ 58$\micro s$ * 54 Mbps = 3132 bit = 391.5 byte
	+ intestazione, CRCs e altri frame = 82 byte
	+ Totale = 473.5 byte per ogni trasmissione
+ se il payload è di 1500 byte l'efficienza non è più di $1500/(1500+473.5)=76\%$
	+ la larghezza di banda è $\leq 41Mbps$ non 54 Mbps
	+ comparando all'ethernet in condizioni simili: efficienza pari al 97%
## Frame fragmentation

## Distribution
+ mobilità tra le celle: cambio da un access point all'altro man mano che mi sposto
+ abbiamo tanti access point con un loro range collegati ad una rete ethernet
	+ se A deve mandare un frame a qualche nodo deve solo sapere il MAC Address di quel nodo
		+ se deve mandarlo ad E (lontanissimo in un'altra cella) il frame avendo quattro indirizzi che corrispondo ai MAC address degli Access Point intermedi 
		+ passo da AP-1 che lo passa ad AP-3 che lo passa ad E

# IEEE 802.15

+ Sostituire i cavi a breve distanza.
+ lavora in frequenza 2.4 GHz con il frequency hopping
+ range di 10-50m con basso consumo di potenza

+ preso una decina di gruppi di persone perché era da applicare a diverse applicazioni (venuto un disastro)
+ Due tipi di connessioni:
	+ SCO: sincrono a circuito
		+ tempi di risposta e delay sono determinati
		+ telefonia/ real time
		+ poca banda ma molto costante piuttosto che avere tanta banda che però non è stabile
	+ ACL: sistema a pacchetti
		+ per trasferimento dati normali

## Stack
+ Logical Link Control e Link manager protocol = nostro livello 2 della rete
+ Baseband: audio
+ RFCOMM implementa una seriale
+ AT commands: comandi per gestire i modem analogici
+ PPP: per implementare pacchetti 
	+ sopra PPP possiamo mettere lo stack TCP

## Piconet

Cella bluetooth:
+ dispositvo master
+ 7 dispositivi slave
+ Comunicazione avviene per TDM (Time Division Multiplexing)
+ comunicazione avviene sempre tra master e slave (a stella)
+ possono esserci anche 8 slave che dormono (a bassa energia)

## Livello fisico
+ Usa tutti i 79 canali della band 2.4 GHz
+ Salta random tra questi canali 
+ trasmissione avviene dentro uno slot di tempo **hopping time** = 625 $\micro s$
+ banda effettiva 1 MHz
+ bluetooth molto arrogante: se dice che deve usare una certa stazione per trasmettere, trasmette e basta
+ crea problemi al Wi-Fi quando incontra una frequenza usata dal Wi-Fi

## Piconet MAC

+ supponiamo ci sia due master e due slave
	+ Master comunica sempre nello slot pari
	+ se uno slave ha ricevuto poi switcha e trasmette al master
	+ cambia slave 
	+ e così via
	+ se slave 2 non ha niente da dire non succede niente (slot perso)
+ parte nera: tempo morto dell'hopping time

## Formato dei pacchetti
+ Header: MAC address, CRC
+ Payload: può essere di 483 bit con singolo slot fino a 1124 bit per tre slot e fino a 2745 bit per 5 slot

## Efficienza
+ Piconet con $n$ slave
+ ogni round prende 625 * 2 * n $\micro s$ = 1.25 * n $ms$
+ massimo delay che un nodo deve aspettare per trasmettere nel caso peggiore è 1.25 * 7=8.75 ms 
	+ Jitter = 0
+ **throughput** da ogni slave al master e viceversa è 483 / 1.25n = 386.4/n kbps
	+ caso peggiore 386.4/7 = 55.2 kbps
+ efficienza:
	+ ogni slot di dati occupa 483 $\micro s$
	+ 483/625 = 77.3%


