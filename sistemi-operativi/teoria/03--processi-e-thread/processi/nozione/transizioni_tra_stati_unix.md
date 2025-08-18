---
title: Transizioni tra Stati Unix
aliases:
  - Transizioni tra Stati Unix
created: 2025-08-18
---
>[!abstract]
>In questa sezione vengono introdotti e definiti i vari stati dei processi in un sistema Unix

---
# Transizioni tra gli Stati: il caso UNIX

|                 Stato | Descrizione                                                                            |
| --------------------: | -------------------------------------------------------------------------------------- |
|             `created` | processo appena creato                                                                 |
| `user/kernel running` | in esecuzione in modalità utente/kernel                                                |
|     `ready in memory` | pronto per andare in esecuzione                                                        |
|           `preempted` | bloccato dal kernel al fine di eseguire un altro processo                              |
|    `asleep in memory` | caricato in memoria, ma in attesa di un evento                                         |
|       `ready swapped` | pronto per eseguire, ma attualmente swapped-out (su disco)                             |
|    `sleeping swapped` | attualmente swapped-out e in attesa di un evento                                       |
|              `zombie` | terminato, ma in attesa che il padre riceva (eseguendo la wait()) lo status di ritorno |

<!-- TODO(sistemi-operativi): aggiungere schema per transizione stati Linux (slide 20) -->

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025