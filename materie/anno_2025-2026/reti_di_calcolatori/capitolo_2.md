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
