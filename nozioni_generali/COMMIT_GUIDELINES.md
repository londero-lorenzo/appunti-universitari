
# Convenzione per i Messaggi di Commit

Ogni messaggio di commit dovrebbe seguire la seguente struttura:
```
<tipo>(<scopo>): descrizione in italiano
```
Se necessario, dopo la prima riga (titolo) seguire con una riga vuota e un corpo più dettagliato.

---

## Tipi supportati

| Tipo       | Scopo                                                                      |
|------------|----------------------------------------------------------------------------|
| `build`    | Modifiche al sistema di build o configurazioni esterne                     |
| `chore`    | Attività di manutenzione (aggiornamento tool, dipendenze, ecc.)            |
| `docs`     | Modifiche esclusivamente alla documentazione                               |
| `feat`     | Aggiunta di nuove funzionalità o contenuti                                 |
| `fix`      | Correzione di bug o problemi                                               |
| `refactor` | Refactoring del codice o della struttura senza modificare il comportamento |
| `style`    | Cambiamenti di formattazione o stile (spazi, indentazione, virgole, ecc.)  |
| `test`     | Aggiunta o modifica di test                                                |
| `perf`     | Miglioramento prestazioni senza modificare comportamento visibile          |


---


## Formato del titolo

1. **Lunghezza massima consigliata: 50 caratteri**  
   - Deve essere conciso, senza punto finale.  
   - Se supera i 50 caratteri, Vim o plugin di linting potrebbero segnalare un warning.
2.
 - **Imperativo / forma attiva (in inglese)**  
   - Il titolo completa la frase implicita:  
     > “If applied, this commit will...”  
   - Esempi:  
     - `feat(algorithms): add new research method`  
     - `fix(link): fix image path in README file`

 - **Infinito con senso lato (in italiano)**  
   - Il titolo completa la frase implicita:  
     > “Se applicato, questo commento farà...
   - Esempi:  
     - `feat(algorithms): aggiungere un nuovo metodo di ricerca`  
     - `fix(link): aggiustare il percorso dell'immagine nel file README`


3. **Una sola riga**, senza andare a capo.  
   - In caso di commit più descrittivi, aggiungere il corpo a partire dalla riga successiva.

4. **Scopo tra parentesi**  
   - Specificare sempre lo scopo (es. `docs(readme)`, `feat(benchmark)`, `fix(cartelle)`).

---

## Corpo del commit (opzionale)

- **Separato da una riga vuota** dopo il titolo.  
- **Lunghezza massima per riga: 72 caratteri**  
- Fornire dettagli utili, esempi di file modificati, motivazioni e contesto:  
  ```text
  feat(benchmark): aggiungere grafici interattivi (scala lineare e log)

  Dati:
  ArraySampleContainer con chiavi geometriche da 10 a 10^6
  (7 campioni, ciascuno con 10 array di lunghezza 10^4).

  Algoritmi benchmarkati:
  - CountingSort
  - QuickSort
  - QuickSort3Way
  - RadixSort

  I grafici sono stati salvati in Report/Charts/D_variability.
  ```

---

## Regole generali
- Titolo in italiano, breve e descrittivo.

- Imperativo in inglese, infinito con senso lato in italiano:

- Corretto: feat(storage): aggiungere i parametri di generazione dati

- Non corretto: feat(storage): aggiunti i parametri di generazione dati

- Non usare caratteri speciali o emoji nel titolo.

- Una riga vuota tra titolo e corpo.

- Il corpo è facoltativo: scriverlo solo se serve chiarire contesto, elenco di file, motivazioni.

- Evitare abbreviazioni ambigue (es. “repo” vs “repository”).

- Mantenere il log leggibile: numeri di ticket o issue, se necessario, alla fine del corpo.

---

## Esempi
```text
chore(obsidian): caricata struttura della vault

docs(readme): aggiunta guida sullo stile dei commit

feat(algoritmi): aggiunti appunti su RBTree e BTree

fix(link): corretti link interni nel README principale

refactor(cartelle): riorganizzata la struttura dei file
```

```text
feat(Variability): aggiunto supporto onDigitRange e flag per geometrica

Aggiunto enable_geometric_serie per passare da
spaziatura lineare a geometrica nei generatori di chiavi.

Rispetta lo standard per 7 campioni di 10^4 elementi
nel range [10, 10^7].
```

---

## Buone pratiche (ispirate da Chris Beams)
- Separare il titolo dal corpo con una riga vuota
 
	- Migliora la leggibilità e la compatibilità con strumenti Git.

- Limitare il titolo a 50 caratteri

	- Mantiene i log concisi e facilmente scansionabili.

- Usare l'infinito per il verbo nel titolo

	- Ad esempio: aggiungere, correggere, rimuovere.

- Evitare il punto finale nel titolo

	- Il titolo è una frase breve, non una frase completa.

- Scrivere il corpo come spiegazione del "perché"

	- Il codice mostra il "come", il messaggio dovrebbe spiegare il "perché".

- Utilizzare elenchi puntati nel corpo se necessario

	- Aiuta a strutturare informazioni complesse.

- Evitare commit "vuoti" o generici

 - Ogni commit dovrebbe rappresentare una modifica significativa e comprensibile.

---

## Note aggiuntive
Se la modifica coinvolge più ambiti (es. codice + documentazione), si può usare un unico commit con titolo generico e corpo dettagliato, oppure due commit distinti (feat + docs).

Non creare commit “vuoti”: ogni commit deve aggiungere o modificare qualcosa di concreto.

Non creare commit “create new branch”: il branch si crea senza commit, committare solo quando si hanno modifiche sostanziali.

Usare git commit -m solo per messaggi molto brevi; preferire l’editor (es. git commit) per messaggi con corpo.

