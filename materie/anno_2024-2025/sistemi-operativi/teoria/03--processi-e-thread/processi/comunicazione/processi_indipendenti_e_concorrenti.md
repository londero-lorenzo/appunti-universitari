---
title: Processi Indipendenti e Concorrenti
aliases:
  - Processi Indipendenti e Concorrenti
created: 2025-08-19
---
# Processi Indipendenti e Concorrenti

>[!abstract]
>In questa sezione si introducono i concetti di processi **indipendenti** e **concorrenti**, insieme alle loro possibili relazioni di cooperazione o competizione. 

---

## Processi Indipendenti

>[!definition]
>Processi Indipendenti  
>>Due processi si dicono indipendenti se l’esecuzione dell’uno **non influenza** in alcun modo l’esecuzione dell’altro.  
>>>[!note]
>>>In questo caso è garantita la proprietà di **riproducibilità** della computazione: ripetendo più volte l’esecuzione, l’esito rimane lo stesso.

---

## Processi Concorrenti

>[!definition]
>Processi Concorrenti  
>>Due processi si dicono concorrenti se l’esecuzione dell’uno **influenza** l’esecuzione dell’altro.  
>>>[!note]
>>>In questo caso **la riproducibilità non è garantita**: l’esito della computazione dipende dalla velocità relativa e dall’ordine di esecuzione dei processi.

>[!note]
>I processi concorrenti possono essere:
>- **<span style="color:indianred">Cooperanti</span>**  
>- **<span style="color:indianred">Competitori</span>**

>[!question] Qual è l’utilità della cooperazione tra processi?
>- Condividere informazioni e risorse  
>- Migliorare i tempi di computazione  
>- Aumentare la modularità nell’implementazione/soluzione di un problema  
>- Consentire l’esecuzione contemporanea di azioni diverse  

---

## 📚 Fonti

- Slide (Processi): _[Processi - hand03p.pdf](https://elearning.uniud.it/moodle/pluginfile.php/849180/mod_page/content/103/hand03p.pdf)_
- Autore: A. Formisano  
- Corso: Sistemi Operativi e Laboratorio, DMIF — UniUD, A.A. 2024/2025
