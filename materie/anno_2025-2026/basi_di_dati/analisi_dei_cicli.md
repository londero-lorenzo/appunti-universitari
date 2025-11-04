---
title: "Analisi dei Cicli"
aliases: ["Analisi dei Cicli"]
tags: [università, "materie", "anno-2025-2026", "basi-di-dati", "analisi-dei-cicli"]
created: 2025-10-28
---
- I cicli non sono sempre problematici

## Ciclo Dip. --- Progetto --- Impiegto
- Non problematico

## Ciclo Dip. --- Impiegato
- Molto problematico: non c'è niente che mi vieti che il manager di informatica afferisca ad ingegneria
- potrebbe esistere una coppia (X, ROSSI) nella relazione AFFERENZA ma anche la coppia (Y, ROSSI) nella relazione GESTISCE (ROSSI è il manager del dipartimento Y)

# Vincoli di integrità
## Primo ciclo (Dip. --- Progetto --- Impiegto)
-  Ogni impiegato può essere il manager solo del dipartimento al quale afferisce
## Terzo ciclo (Impiegato---Supervisione)
- un impiegato potrebbe supervisionare se stesso
- no cicli in supervisione
- un impiegato non può essere supervisionato da un altro supervisore di un altro dipartimento


