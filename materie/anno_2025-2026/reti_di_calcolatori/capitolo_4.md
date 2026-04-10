---
title: "Capitolo 4"
aliases: ["Capitolo 4"]
tags: [università, "materie", "anno-2025-2026", "reti-di-calcolatori", "capitolo-4"]
created: 2026-04-10
---
# Problemi
- Come costruiamo un sistema di instradamento che possa gestire centinaia di migliaia di reti e miliardi di nodi ?
- Come gestiamo l'esaurimento dello spazio di indirizzamento IPv4?
- Come migliorare le funzionalità di internet?

# Interdominio
- Internet è organizzato come **sistemi autonomi** i quali sono sotto il controllo di una singola entità amministrativa
- **Sistemi autonomi**
	- corrisponde a un dominio amministrativo
	- es: Università, aziende, backbone network
- una rete interna di un'azienda potrebbe essere un singolo sistema autonomo, come una rete di un singolo Internet service provider
## Route Propagation
• Idea: fornire un ulteriore modo per **aggregare gerarchicamente le informazioni di routing** in una rete Internet di grandi dimensioni
	• Migliora la **scalabilità**
• Divide il problema del routing in due parti:
- routing **all’interno di un singolo sistema autonomo (AS)**
- routing **tra sistemi autonomi diversi**
• Un altro nome per i sistemi autonomi in Internet è **domini di routing**
• Gerarchia a due livelli per la propagazione delle rotte:
- protocollo di routing **inter-dominio** (standard a livello Internet)
- protocollo di routing **intra-dominio** (ogni AS sceglie il proprio)
### Protocolli Inter-domain
#### Exterior Gateway Protocol (EGP)
- topologia ad albero
- non permette alla topologia di assumere forme più generali
#### Border Gateway Protocol (BGP)
- Internet è un insieme di sistemi autonomi arbitrariamente interconnessi
- oggi Internet è formata dall'interconnessione di più **reti backbone** (reti fornitrici di servizi gestite da compagnie private ) e da **siti connessi** l'uno all'altro in modi diversi
- alcune grandi aziende sono direttamente connesse ad uno o più backbone, mentre altre si connettono a fornitori più piccoli di servizi non di tipo backbone
- molti fornitori hanno come clienti solo "consumer" (persone come noi con PC a casa) e devono connettersi anche loro a fornitori backbone
- molti fornitori si interconnettono l'un l'altro in un singolo **peering point**

