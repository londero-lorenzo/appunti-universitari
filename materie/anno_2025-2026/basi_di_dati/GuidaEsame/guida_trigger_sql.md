# Guida definitiva ai trigger SQL per l’esame

## 1. Idea generale

Un **trigger** serve quando un vincolo non è controllabile facilmente con `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL` o `CHECK`.

Di solito serve un trigger quando il vincolo richiede di controllare:

- altre righe della stessa tabella;
- altre tabelle;
- un conteggio;
- l’esistenza o non esistenza di associazioni;
- il valore precedente e quello nuovo di una riga;
- una condizione che può diventare falsa dopo `INSERT`, `UPDATE` o `DELETE`.

Un trigger è un’azione automatica eseguita dal DBMS in seguito a una modifica della base di dati, cioè `INSERT`, `UPDATE` o `DELETE`; in PostgreSQL il trigger richiama una funzione `RETURNS trigger`. fileciteturn8file0

---

# 2. Struttura base di un trigger

In PostgreSQL un trigger si scrive sempre in due parti:

1. **funzione trigger**;
2. **trigger vero e proprio**, collegato a una tabella.

## Template generale

```sql id="130o51"
CREATE OR REPLACE FUNCTION nome_funzione()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    -- controllo del vincolo

    IF condizione_di_violazione THEN
        RAISE EXCEPTION 'Messaggio di errore';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER nome_trigger
BEFORE INSERT OR UPDATE
ON nome_tabella
FOR EACH ROW
EXECUTE FUNCTION nome_funzione();
```

---

# 3. `NEW` e `OLD`

Nei trigger si usano due variabili speciali:

```sql id="5jsx3d"
NEW
OLD
```

## `NEW`

Si usa con:

```sql id="4aac3z"
INSERT
UPDATE
```

Rappresenta la nuova riga che sto inserendo o aggiornando.

Esempio:

```sql id="h12cvb"
NEW.stato
NEW.referente
NEW.gradazione
```

## `OLD`

Si usa con:

```sql id="ktvv6f"
UPDATE
DELETE
```

Rappresenta la riga prima della modifica o prima della cancellazione.

Esempio:

```sql id="6h17wn"
OLD.squadra
OLD.afferenza
OLD.codice_isbn_libro
```

Le slide specificano che `NEW` è disponibile per `INSERT` e `UPDATE`, mentre `OLD` è disponibile per `DELETE` e `UPDATE`. fileciteturn8file0

---

# 4. Quale `RETURN` usare?

Dipende dall’operazione.

| Operazione | Variabile disponibile | Return normale |
|---|---|---|
| `INSERT` | `NEW` | `RETURN NEW;` |
| `UPDATE` | `NEW` e `OLD` | `RETURN NEW;` |
| `DELETE` | `OLD` | `RETURN OLD;` |

Esempi:

```sql id="g9edhx"
RETURN NEW;
```

per inserimenti e aggiornamenti.

```sql id="cwiktr"
RETURN OLD;
```

per cancellazioni.

Nei trigger `BEFORE FOR EACH ROW`, restituire `NEW` permette all’operazione di proseguire; su `DELETE`, convenzionalmente si restituisce `OLD`. fileciteturn8file0

---

# 5. Metodo da usare sempre all’esame

Quando leggi un vincolo, segui sempre questi passaggi.

## Passo 1 — Traduci il vincolo in modo logico

Esempio:

> Ogni autore può scrivere al massimo 5 libri.

Traduzione:

```text id="x8bjq8"
Per ogni autore, il numero di righe in HA_SCRITTO associate a quell’autore deve essere <= 5.
```

---

## Passo 2 — Capisci quali tabelle sono coinvolte

Esempio:

```text id="ik53ib"
AUTORE
LIBRO
HA_SCRITTO
```

Il conteggio dei libri scritti non sta in `AUTORE`, ma in `HA_SCRITTO`.

Quindi il trigger probabilmente va su:

```sql id="3pxip0"
HA_SCRITTO
```

---

## Passo 3 — Chiediti quali operazioni possono rompere il vincolo

Domanda fondamentale:

> Quali `INSERT`, `UPDATE` o `DELETE` possono trasformare una base dati valida in una base dati non valida?

Le slide insistono proprio su questo punto: per modellare correttamente un vincolo con trigger bisogna prima chiedersi quali operazioni e su quali tabelle possano portare a una violazione. fileciteturn8file0

---

## Passo 4 — Scegli una delle operazioni

Molti esercizi dicono:

> Si scelga una delle operazioni individuate e si scriva un trigger.

Quindi non devi per forza coprire tutto il vincolo. Puoi scegliere una sola operazione.

Però devi sapere spiegare che il tuo trigger copre solo quella.

---

## Passo 5 — Scrivi la query che cerca la violazione

Di solito hai due forme:

### Forma con `COUNT`

Quando devi controllare un numero massimo o minimo.

```sql id="cc526y"
SELECT COUNT(*) INTO n
FROM tabella
WHERE condizione;
```

### Forma con `EXISTS`

Quando ti basta sapere se esiste almeno una riga proibita.

```sql id="asr9fj"
IF EXISTS (
    SELECT 1
    FROM tabella
    WHERE condizione
)
THEN
    RAISE EXCEPTION '...';
END IF;
```

---

# 6. Tipo 1 — Vincolo di massimo numero

## Forma tipica

Esempi:

```text id="o5alt2"
Ogni autore può scrivere al massimo 5 libri.
Una squadra può avere al massimo 13 giocatori.
Una sala può ospitare al massimo N reperti.
```

Qui devi controllare che un conteggio non superi un massimo.

---

## Operazioni problematiche

Di solito:

```sql id="zfdtmr"
INSERT
```

perché aggiunge un elemento.

```sql id="wjalkx"
UPDATE
```

se sposta un elemento da un gruppo a un altro.

Di solito `DELETE` non viola un massimo, perché rimuove elementi.

---

## Schema mentale

```text id="b5l5tv"
Sto aggiungendo/spostando X nel gruppo G.
Quanti elementi ha già G?
Se ne ha già N, non posso aggiungerne un altro.
```

---

## Template

```sql id="uat8p5"
CREATE OR REPLACE FUNCTION check_massimo()
RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    n INTEGER;
BEGIN
    SELECT COUNT(*) INTO n
    FROM tabella_associazione T
    WHERE T.gruppo = NEW.gruppo;

    IF n >= limite THEN
        RAISE EXCEPTION 'Violazione: limite massimo superato';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_massimo
BEFORE INSERT OR UPDATE OF gruppo
ON tabella_associazione
FOR EACH ROW
EXECUTE FUNCTION check_massimo();
```

---

## Esempio: autore massimo 5 libri

```sql id="yw8azk"
CREATE OR REPLACE FUNCTION check_max_5_libri_autore()
RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    n_libri INTEGER;
BEGIN
    IF TG_OP = 'INSERT'
       OR NEW.codice_fiscale_autore IS DISTINCT FROM OLD.codice_fiscale_autore
    THEN
        SELECT COUNT(*) INTO n_libri
        FROM HA_SCRITTO H
        WHERE H.codice_fiscale_autore = NEW.codice_fiscale_autore;

        IF n_libri >= 5 THEN
            RAISE EXCEPTION
                'Violazione: un autore può scrivere al massimo 5 libri';
        END IF;
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_max_5_libri_autore
BEFORE INSERT OR UPDATE OF codice_fiscale_autore
ON HA_SCRITTO
FOR EACH ROW
EXECUTE FUNCTION check_max_5_libri_autore();
```

---

# 7. Tipo 2 — Vincolo di minimo numero

## Forma tipica

Esempi:

```text id="z6a6s9"
Ogni libro deve avere almeno un autore.
Ogni squadra deve avere almeno 6 giocatori.
Ogni professore deve insegnare almeno un corso.
```

Qui devi impedire che un gruppo rimanga senza elementi, oppure sotto una soglia minima.

---

## Operazioni problematiche

Di solito:

```sql id="6afbrp"
DELETE
```

perché rimuove un elemento.

```sql id="tqo8xv"
UPDATE
```

se sposta un elemento da un gruppo a un altro.

A volte anche:

```sql id="hvemsx"
INSERT sulla tabella principale
```

perché posso creare un’entità senza associazioni.

Esempio:

```text id="kafq69"
Inserisco un libro, ma non gli assegno nessun autore.
```

---

## Schema mentale

```text id="x4048m"
Sto togliendo X dal gruppo G.
Quanti elementi ha G prima della cancellazione?
Se ne ha 1, togliendo X diventa 0.
Quindi blocco.
```

---

## Template per `DELETE`

```sql id="hazfy8"
CREATE OR REPLACE FUNCTION check_minimo_delete()
RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    n INTEGER;
BEGIN
    SELECT COUNT(*) INTO n
    FROM tabella_associazione T
    WHERE T.gruppo = OLD.gruppo;

    IF n <= minimo THEN
        RAISE EXCEPTION 'Violazione: limite minimo non rispettato';
    END IF;

    RETURN OLD;
END;
$$;

CREATE TRIGGER trigger_check_minimo_delete
BEFORE DELETE
ON tabella_associazione
FOR EACH ROW
EXECUTE FUNCTION check_minimo_delete();
```

---

## Esempio: ogni libro almeno un autore

```sql id="8k5gp6"
CREATE OR REPLACE FUNCTION check_libro_almeno_un_autore_delete()
RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    n_autori INTEGER;
BEGIN
    SELECT COUNT(*) INTO n_autori
    FROM HA_SCRITTO H
    WHERE H.codice_isbn_libro = OLD.codice_isbn_libro;

    IF n_autori = 1 THEN
        RAISE EXCEPTION
            'Violazione: ogni libro deve avere almeno un autore';
    END IF;

    RETURN OLD;
END;
$$;

CREATE TRIGGER trigger_check_libro_almeno_un_autore_delete
BEFORE DELETE
ON HA_SCRITTO
FOR EACH ROW
EXECUTE FUNCTION check_libro_almeno_un_autore_delete();
```

---

# 8. Tipo 3 — Vincolo condizionale sulla stessa tabella

## Forma tipica

Esempio:

```text id="aons6t"
Per passare allo stato attivo, un progetto deve avere un referente.
```

Traduzione:

```text id="8wi30n"
Se stato = 'attivo', allora referente IS NOT NULL.
```

Questo vincolo riguarda una singola riga, ma l’esercizio può comunque chiedere il trigger.

---

## Operazioni problematiche

```sql id="6md2x1"
INSERT
```

perché posso inserire un progetto già attivo senza referente.

```sql id="z3t6un"
UPDATE OF stato
```

perché posso trasformare un progetto in attivo.

```sql id="hdgdxr"
UPDATE OF referente
```

perché posso togliere il referente a un progetto attivo.

---

## Template

```sql id="czvj1y"
CREATE OR REPLACE FUNCTION check_condizione_stessa_tabella()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.attributo1 = 'valore'
       AND NEW.attributo2 IS NULL
    THEN
        RAISE EXCEPTION 'Violazione del vincolo';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_condizione
BEFORE INSERT OR UPDATE OF attributo1, attributo2
ON tabella
FOR EACH ROW
EXECUTE FUNCTION check_condizione_stessa_tabella();
```

---

## Esempio: progetto attivo con referente

```sql id="3q93is"
CREATE OR REPLACE FUNCTION check_progetto_attivo_referente()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.stato = 'attivo' AND NEW.referente IS NULL THEN
        RAISE EXCEPTION
            'Violazione: un progetto attivo deve avere un referente';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_progetto_attivo_referente
BEFORE INSERT OR UPDATE OF stato, referente
ON progetti
FOR EACH ROW
EXECUTE FUNCTION check_progetto_attivo_referente();
```

---

# 9. Tipo 4 — Vincolo condizionale tra due tabelle

## Forma tipica

Esempi:

```text id="qe572v"
Una botte contenente vino rosso non può avere gradazione > 17.
Un esopianeta non può orbitare attorno a una supergigante rossa.
Il direttore di un dipartimento deve afferire al dipartimento stesso.
```

Qui un’informazione sta in una tabella e l’altra informazione sta in un’altra tabella.

---

## Schema mentale

```text id="y3crdi"
Sto modificando una riga della tabella A.
Per sapere se è valida, devo controllare una riga collegata nella tabella B.
```

---

## Template

```sql id="6dfs9h"
CREATE OR REPLACE FUNCTION check_vincolo_due_tabelle()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM tabella_collegata B
        WHERE B.chiave = NEW.chiave_esterna
          AND B.attributo = 'valore_proibito'
    )
    THEN
        RAISE EXCEPTION 'Violazione del vincolo';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_vincolo_due_tabelle
BEFORE INSERT OR UPDATE OF chiave_esterna
ON tabella_principale
FOR EACH ROW
EXECUTE FUNCTION check_vincolo_due_tabelle();
```

---

## Esempio: vino rosso con gradazione massimo 17

```sql id="3ikk7e"
CREATE OR REPLACE FUNCTION check_gradazione_vino_rosso()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.gradazione > 17
       AND EXISTS (
           SELECT 1
           FROM Vini V
           WHERE V.nome = NEW.vino
             AND V.tipologia = 'rosso'
       )
    THEN
        RAISE EXCEPTION
            'Violazione: una botte contenente vino rosso non può superare i 17 gradi';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_gradazione_vino_rosso
BEFORE UPDATE OF vino, gradazione
ON Botti
FOR EACH ROW
EXECUTE FUNCTION check_gradazione_vino_rosso();
```

---

# 10. Tipo 5 — Vincolo che può essere violato da entrambe le tabelle

## Forma tipica

Esempio:

```text id="kha4lm"
Un esopianeta non può orbitare attorno a una stella che è una supergigante rossa.
```

Questo può essere violato in due modi:

```sql id="2uaiao"
INSERT OR UPDATE ON Esopianeti
```

assegno un esopianeta a una stella già supergigante rossa.

Oppure:

```sql id="qky8el"
UPDATE ON Stelle
```

trasformo in supergigante rossa una stella che ha già esopianeti.

---

## Regola importante

Un singolo `CREATE TRIGGER` può essere collegato a **una sola tabella**.

Quindi non puoi scrivere:

```sql id="6yshiw"
ON Esopianeti, Stelle
```

Devi scrivere:

```text id="jnpgjj"
un trigger su Esopianeti
un trigger su Stelle
```

Eventualmente possono richiamare la stessa funzione, ma per l’esame è più chiaro scrivere due funzioni separate.

---

## Trigger su tabella figlia

```sql id="nxfe2w"
CREATE OR REPLACE FUNCTION check_stella_non_supergigante_rossa()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Stelle S
        WHERE S.nome = NEW.stella
          AND S.classificazione = 'supergigante rossa'
    )
    THEN
        RAISE EXCEPTION
            'Violazione: un esopianeta non può orbitare attorno a una supergigante rossa';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_stella_non_supergigante_rossa
BEFORE INSERT OR UPDATE OF stella
ON Esopianeti
FOR EACH ROW
EXECUTE FUNCTION check_stella_non_supergigante_rossa();
```

---

## Trigger su tabella padre

```sql id="s6tvtr"
CREATE OR REPLACE FUNCTION check_classificazione_stella()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF NEW.classificazione = 'supergigante rossa'
       AND EXISTS (
           SELECT 1
           FROM Esopianeti E
           WHERE E.stella = NEW.nome
       )
    THEN
        RAISE EXCEPTION
            'Violazione: una stella con esopianeti non può diventare supergigante rossa';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_classificazione_stella
BEFORE UPDATE OF classificazione
ON Stelle
FOR EACH ROW
WHEN (NEW.classificazione IS DISTINCT FROM OLD.classificazione)
EXECUTE FUNCTION check_classificazione_stella();
```

---

# 11. Tipo 6 — Vincolo di coerenza tra ruolo e appartenenza

## Forma tipica

Esempio:

```text id="jy6f1w"
Il direttore di ogni dipartimento deve afferire al dipartimento stesso.
```

Traduzione:

```text id="ty1cco"
Per ogni dipartimento D,
il ricercatore D.direttore deve avere afferenza = D.id_dip.
```

---

## Operazioni problematiche

Su `Dipartimento`:

```sql id="mko1e4"
INSERT
UPDATE OF direttore
UPDATE OF id_dip
```

Su `Ricercatore`:

```sql id="tb4sm4"
UPDATE OF afferenza
DELETE
```

Perché se sposto o cancello un ricercatore che è direttore, posso lasciare il dipartimento con un direttore non valido.

---

## Trigger su `Ricercatore`

```sql id="o1qxof"
CREATE OR REPLACE FUNCTION check_afferenza_direttore()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Dipartimento D
        WHERE D.direttore = OLD.nome
          AND D.id_dip <> NEW.afferenza
    )
    THEN
        RAISE EXCEPTION
            'Violazione: il direttore deve afferire al dipartimento che dirige';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_afferenza_direttore
BEFORE UPDATE OF afferenza
ON Ricercatore
FOR EACH ROW
WHEN (NEW.afferenza IS DISTINCT FROM OLD.afferenza)
EXECUTE FUNCTION check_afferenza_direttore();
```

---

# 12. Tipo 7 — Vincolo di non sovrapposizione tra intervalli

## Forma tipica

Esempio:

```text id="mkzurc"
Per una stessa auto, gli intervalli dei servizi non possono sovrapporsi.
```

Questa è una delle forme più importanti.

---

## Condizione di sovrapposizione

Due intervalli:

```text id="0i6k36"
[inizio1, fine1]
[inizio2, fine2]
```

si sovrappongono se:

```sql id="jd3z2y"
inizio1 <= fine2
AND
fine1 >= inizio2
```

Nel trigger:

```sql id="hgkh5f"
NEW.data_inizio <= S.data_fine
AND
NEW.data_fine >= S.data_inizio
```

---

## Operazioni problematiche

```sql id="xamhp6"
INSERT
```

perché inserisco un nuovo intervallo.

```sql id="7cnra5"
UPDATE OF auto, data_inizio, data_fine
```

perché modifico un intervallo esistente.

---

## Template

```sql id="62iju1"
CREATE OR REPLACE FUNCTION check_sovrapposizione()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM tabella_intervalli T
        WHERE T.entita = NEW.entita
          AND T.id <> NEW.id
          AND NEW.data_inizio <= T.data_fine
          AND NEW.data_fine >= T.data_inizio
    )
    THEN
        RAISE EXCEPTION 'Violazione: intervalli sovrapposti';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_sovrapposizione
BEFORE INSERT OR UPDATE OF entita, data_inizio, data_fine
ON tabella_intervalli
FOR EACH ROW
EXECUTE FUNCTION check_sovrapposizione();
```

---

## Nota importante

Questa condizione:

```sql id="gu925k"
T.id <> NEW.id
```

serve negli `UPDATE`.

Senza questa condizione, una riga risulterebbe sovrapposta a sé stessa.

---

# 13. Tipo 8 — Vincolo con azione automatica invece di errore

## Forma tipica

Esempio:

```text id="gquuw6"
Se una sala è piena, il reperto deve essere collocato automaticamente nel magazzino.
```

Qui non blocchi l’operazione. Modifichi `NEW`.

---

## Template

```sql id="o8o5e4"
CREATE OR REPLACE FUNCTION gestisci_automaticamente()
RETURNS trigger
LANGUAGE plpgsql AS $$
DECLARE
    n INTEGER;
    capacita INTEGER;
BEGIN
    SELECT COUNT(*) INTO n
    FROM Reperto R
    WHERE R.collocazione = NEW.collocazione
      AND R.codice <> NEW.codice;

    SELECT S.capacita_expo INTO capacita
    FROM Sala S
    WHERE S.codice = NEW.collocazione;

    IF n >= capacita THEN
        NEW.collocazione := '100';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_gestisci_automaticamente
BEFORE INSERT OR UPDATE OF collocazione
ON Reperto
FOR EACH ROW
EXECUTE FUNCTION gestisci_automaticamente();
```

---

## Regola

Se devi **bloccare**, usi:

```sql id="6chaad"
RAISE EXCEPTION '...';
```

Se devi **correggere automaticamente**, modifichi `NEW`:

```sql id="jzdflj"
NEW.attributo := nuovo_valore;
RETURN NEW;
```

---

# 14. Tipo 9 — Vincolo su coppie o relazioni molti-a-molti

## Forma tipica

Esempio:

```text id="4lpbqf"
Nessun musicista può suonare con un altro musicista a cui piace Indie.
```

Tabelle coinvolte:

```text id="wjgic8"
SUONA_CON(mid1, mid2)
PIACE(mid, gid)
GENERE(gid, nome)
```

---

## Operazioni problematiche

Su `SUONA_CON`:

```sql id="rj78bn"
INSERT
UPDATE OF mid1, mid2
```

perché posso creare una coppia proibita.

Su `PIACE`:

```sql id="ja719z"
INSERT
UPDATE OF mid, gid
```

perché posso aggiungere `Indie` a un musicista che suona già con qualcuno.

Su `GENERE`:

```sql id="67ttcs"
UPDATE OF nome
```

perché posso rinominare un genere in `Indie`.

---

## Trigger su `PIACE`

```sql id="u6oeam"
CREATE OR REPLACE FUNCTION check_piace_indie()
RETURNS trigger
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Genere G
        WHERE G.gid = NEW.gid
          AND G.nome = 'Indie'
    )
    AND EXISTS (
        SELECT 1
        FROM Suona_con S
        WHERE S.mid1 = NEW.mid
           OR S.mid2 = NEW.mid
    )
    THEN
        RAISE EXCEPTION
            'Violazione: nessun musicista può suonare con un musicista a cui piace Indie';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trigger_check_piace_indie
BEFORE INSERT OR UPDATE OF mid, gid
ON Piace
FOR EACH ROW
EXECUTE FUNCTION check_piace_indie();
```

---

# 15. Come scegliere tra `COUNT` ed `EXISTS`

## Usa `COUNT` quando devi confrontare un numero

Esempi:

```text id="orqkyr"
al massimo 5 libri
almeno 6 giocatori
capienza massima della sala
```

Template:

```sql id="2noksx"
DECLARE
    n INTEGER;
BEGIN
    SELECT COUNT(*) INTO n
    FROM tabella
    WHERE condizione;

    IF n >= limite THEN
        RAISE EXCEPTION '...';
    END IF;
END;
```

---

## Usa `EXISTS` quando devi sapere se esiste una violazione

Esempi:

```text id="lc8w4q"
esiste una stella supergigante rossa?
esiste un genere Indie?
esiste un dipartimento diretto da questo ricercatore?
```

Template:

```sql id="ivezjh"
BEGIN
    IF EXISTS (
        SELECT 1
        FROM tabella
        WHERE condizione
    )
    THEN
        RAISE EXCEPTION '...';
    END IF;

    RETURN NEW;
END;
```

---

# 16. Come scegliere tra `BEFORE` e `AFTER`

Per gli esercizi che abbiamo visto, quasi sempre conviene usare:

```sql id="8k34cy"
BEFORE
```

perché vuoi impedire che la modifica venga salvata.

Usa `BEFORE` quando vuoi:

```text id="0v483e"
bloccare l'operazione;
modificare automaticamente NEW;
controllare prima che la base dati venga alterata.
```

Esempi:

```sql id="j2gdex"
BEFORE INSERT
BEFORE UPDATE
BEFORE DELETE
```

Le slide indicano che un trigger può essere `BEFORE` o `AFTER`, e può essere attivato da `INSERT`, `UPDATE` o `DELETE`. fileciteturn8file0

---

# 17. Come usare `WHEN`

La clausola `WHEN` serve per evitare che il trigger venga eseguito inutilmente.

Esempio:

```sql id="2tqfdr"
CREATE TRIGGER trigger_nome
BEFORE UPDATE OF afferenza
ON Ricercatore
FOR EACH ROW
WHEN (NEW.afferenza IS DISTINCT FROM OLD.afferenza)
EXECUTE FUNCTION funzione_nome();
```

Meglio usare:

```sql id="8hg5kr"
IS DISTINCT FROM
```

invece di:

```sql id="up6j1q"
<>
```

perché funziona bene anche con `NULL`.

Esempio:

```text id="byfr5x"
OLD.afferenza = NULL
NEW.afferenza = 'id111'
```

Con `IS DISTINCT FROM`, il cambiamento viene riconosciuto.

---

# 18. Attenzione a `BEFORE UPDATE` e ai valori nella tabella

Nei trigger `BEFORE UPDATE`, la tabella contiene ancora i valori vecchi.

Perciò devi usare:

```sql id="5oqfkh"
NEW
```

per i valori nuovi;

```sql id="yvplvt"
OLD
```

per i valori vecchi.

Esempio sbagliato:

```sql id="hdrfwp"
SELECT *
FROM Botti B
JOIN Vini V ON B.vino = V.nome
WHERE B.codice = NEW.codice;
```

Questo può leggere il vino vecchio della botte, non quello nuovo.

Meglio:

```sql id="vnpusz"
SELECT 1
FROM Vini V
WHERE V.nome = NEW.vino
  AND V.tipologia = 'rosso';
```

---

# 19. Elenco rapido: quale operazione può violare cosa?

| Tipo di vincolo | Operazioni che di solito violano |
|---|---|
| Massimo N elementi | `INSERT`, `UPDATE` verso il gruppo |
| Minimo N elementi | `DELETE`, `UPDATE` fuori dal gruppo |
| Almeno un’associazione | `DELETE` su tabella associazione, `UPDATE` della FK, a volte `INSERT` entità principale |
| Nessuna sovrapposizione intervalli | `INSERT`, `UPDATE` degli estremi o dell’entità |
| Vincolo condizionale sulla stessa riga | `INSERT`, `UPDATE` degli attributi coinvolti |
| Vincolo tra tabella figlia e padre | `INSERT/UPDATE` sulla figlia, `UPDATE` sulla tabella padre |
| Vincolo su ruolo/appartenenza | `UPDATE` ruolo, `UPDATE` appartenenza, `DELETE` entità collegata |
| Vincolo su coppie | `INSERT/UPDATE` coppia, `INSERT/UPDATE` proprietà degli elementi |
| Vincolo con classificazione esterna | `INSERT/UPDATE` FK, `UPDATE` classificazione |

---

# 20. Frasi pronte per l’esame

## Per elencare le operazioni

```text id="albelh"
Il vincolo può essere violato da tutte le operazioni che modificano il numero o la natura delle associazioni coinvolte. In particolare, l’inserimento può violare un vincolo di massimo, la cancellazione può violare un vincolo di minimo, mentre l’aggiornamento può violare entrambi se sposta una tupla da un gruppo a un altro.
```

---

## Per motivare un trigger su `INSERT`

```text id="irw34z"
Il trigger viene eseguito prima dell’inserimento perché la nuova tupla potrebbe rendere falsa la condizione di integrità. Si usano i valori di NEW per controllare se l’inserimento provocherebbe una violazione.
```

---

## Per motivare un trigger su `UPDATE`

```text id="dl06ix"
Il trigger viene eseguito prima dell’aggiornamento perché la modifica di uno degli attributi coinvolti nel vincolo può trasformare una situazione valida in una non valida. Si confrontano i valori OLD e NEW quando serve distinguere la situazione precedente da quella successiva.
```

---

## Per motivare un trigger su `DELETE`

```text id="166520"
Il trigger viene eseguito prima della cancellazione perché la rimozione della tupla potrebbe eliminare l’ultima associazione necessaria al rispetto del vincolo. Si usa OLD perché la tupla cancellata non avrà un valore NEW.
```

---

# 21. Checklist finale prima di consegnare

Prima di consegnare un trigger, controlla sempre:

- Ho scelto la tabella giusta?
- Ho scelto l’operazione giusta?
- Uso `NEW` solo dove esiste?
- Uso `OLD` solo dove esiste?
- Se è `DELETE`, restituisco `OLD`?
- Se è `INSERT` o `UPDATE`, restituisco `NEW`?
- Se sto contando, ho considerato che in un `BEFORE` la riga non è ancora stata inserita/modificata/cancellata?
- Se è un `UPDATE`, devo escludere la riga stessa?
- Se il vincolo coinvolge due tabelle, ho considerato anche le modifiche sull’altra tabella?
- Se la consegna dice “scegli una operazione”, ho spiegato che il trigger copre solo quella?

---

# 22. Formula definitiva da ricordare

```text id="fvjq1v"
1. Capisco il vincolo.
2. Trovo le tabelle coinvolte.
3. Elenco INSERT / UPDATE / DELETE che possono violarlo.
4. Scelgo una di queste operazioni.
5. Scrivo una funzione RETURNS trigger.
6. Uso NEW per INSERT/UPDATE, OLD per DELETE/UPDATE.
7. Cerco la violazione con COUNT o EXISTS.
8. Se la trovo, RAISE EXCEPTION.
9. Altrimenti RETURN NEW o RETURN OLD.
10. Creo il trigger con BEFORE ... ON ... FOR EACH ROW.
```

Questa è la struttura che puoi applicare praticamente a tutti gli esercizi di trigger che abbiamo svolto.
