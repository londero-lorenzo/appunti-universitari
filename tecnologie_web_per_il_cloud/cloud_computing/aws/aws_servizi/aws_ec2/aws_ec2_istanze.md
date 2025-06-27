---
title: Aws Ec2 Istanze
aliases:
  - Aws Ec2 Istanze
tags:
  - aws-ec2-istanze
created: 2025-06-21
---
# Amazon EC2 – Tipologie di Istanze, Costi e Famiglie

## ⚙️ Tipologie di istanze EC2

| Tipo                     | Descrizione                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| **On-Demand**            | Pagamento a consumo puro (orario). Nessun impegno. Flessibile.                               |
| **Reserved**             | Sconto significativo in cambio di un impegno (1 o 3 anni). Ideale per uso costante.          |
| **Spot**                 | Asta su risorse inutilizzate: bassissimo costo, ma possono essere terminate senza preavviso. |
| **Burstable (T series)** | Uso flessibile con sistema a **crediti CPU**. Ottime per carichi variabili e poco intensivi. |

> ℹ️ Le istanze On-Demand sono ideali per test, sviluppo o carichi imprevedibili. Le Spot per processi batch tolleranti a interruzioni. Le Reserved per ambienti di produzione.

### Istanze Spot
- Basate su un sistema d’asta: si imposta un prezzo massimo orario.
- Le istanze si attivano solo quando il prezzo è inferiore al massimo.
- Lavoro deve essere resiliente all’interruzione: no real-time/web.
- Ideale per carichi batch o simulazioni.

---

## 🧱 Persistenza delle risorse

| Tipo di risorsa | Persistenza |
|-----------------|-------------|
| Istanze EC2 | ❌ Disco volatile: dati persi allo spegnimento (a meno di EBS) |
| Volumi EBS | ✅ Disco permanente: può essere staccato/riattaccato |
| Security Groups | ✅ Configurazioni permanenti |
| AMI salvate | ✅ Se su EBS o S3 |
| Elastic IP | ✅ Associabili a nuove istanze |
| Load Balancer (ELB) | ✅ Infrastruttura resiliente |

---

## 💰 Costi EC2

### Esempio: `m3.large` (Irlanda)
| Sistema Operativo | Prezzo On-Demand |
|--------------------|-------------------|
| Linux base | 0.133 $/h |
| RedHat | 0.206 $/h |
| Windows | 0.258 $/h |
| Windows + SQL | 0.703 $/h |

### Esempio minimo: `t2.nano`
- **On-demand**: ~4.18 $/mese
- **Reserved (1 anno, pagamento anticipato)**: ~2.63 $/mese

> ℹ️ I costi **variano anche in base alla regione AWS**, al traffico, allo storage e al sistema operativo.

---

## 📦 Costi accessori

### EBS (Elastic Block Store)
- Standard: ~100 IOPS
- Provisioned IOPS: fino a 30 IOPS/GB
- Snapshot persistenti (compressi) su S3

### Banda e storage
- EBS: ~0.08 €/GB/mese
- S3: ~0.023 €/GB/mese + richieste (0.0004€/1000 GET)

### Altri
- Elastic IP
- Load Balancer
- AMI personalizzate (memorizzate in EBS o S3)

---

## ⚖️ EC2 vs S3 – Quale storage usare?

| Criterio | EBS | S3 |
|---------|-----|----|
| Tipo di accesso | File system persistente per EC2 | Oggetti statici accessibili via API/HTTP |
| Prezzo base | ~0.08 €/GB/mese | ~0.023 €/GB/mese |
| Uso tipico | Sistema operativo, DB | File statici, media, backup |

> ⚠️ Per siti web con contenuti multimediali statici, **S3 è più conveniente e scalabile**.

---

## 🧬 Famiglie di istanze

| Famiglia | Scopo | Esempi |
|----------|-------|--------|
| **T** | Uso generale, burstable | T2, T3 |
| **M** | Uso generico stabile | M3 (SSD), M4 (ottimizzate EBS) |
| **C** | Calcolo intensivo | C3 (SSD), C4 (EBS) |
| **R** | Ottimizzate per memoria | R3 |
| **I / D** | Ottimizzate per storage | I2 (SSD), D2 (HDD denso) |
| **G** | GPU (machine learning, rendering) | G2: NVIDIA GPU + Xeon E5-2670 |

### 🏷️ Nomi delle istanze EC2

I nomi seguono una convenzione che indica **famiglia, generazione, capacità aggiuntive e dimensione**:

```
R5d.xLarge
└┬┘ └───┬─┘
 │      └────── instance size (es. xLarge, 2xLarge, etc.)
 └──────────── instance family + generazione
      d        → capacità aggiuntiva (es. d = local storage SSD)

```

> Esempio: `t3.micro`, `m5.large`, `r5d.2xlarge`


---

## 📏 Misura della potenza di calcolo

- EC2 usa **vCPU** (Virtual CPU), normalmente 1 hyperthread di un core fisico.
- Il vecchio parametro **ECU** (EC2 Compute Unit) è stato deprecato.
- Le prestazioni **variano a parità di vCPU** in base alla famiglia, alla generazione e alla tecnologia sottostante (es. AMD, Intel, Graviton).

 >⚠️ Il tipo di vCPU varia in base alla **famiglia di istanza**: è consigliato sperimentare diverse opzioni per valutarne le prestazioni effettive.
 
---

## 🔗 Collegamenti utili
- Torna a [AWS Servizi](../aws_servizi.md)
- Torna alla panoramica EC2: [README](./README.md)
- Funzionalità avanzate: [EC2 Funzioni avanzate](./aws_ec2_funzioni_avanzate.md)
- [Prezzi EC2 aggiornati](https://aws.amazon.com/ec2/pricing/on-demand/)

---

## 📁 Note organizzative
- Cartella: `aws/aws_servizi/aws_ec2/`

---

## 📚 Fonti e riferimenti  
Slide: `04-Cloud-AWS-1.pdf`  
Titoli:  
- *Amazon Web Services (AWS) – Un caso di studio*  
- *Amazon EC2/1*, *Amazon EC2/2: istanze*  
- *AWS: immagini, istanze, volumi*  
- *Famiglie di istanze EC2*, *Virtual CPU*, *Ottimizzazione, un esempio: Tx*  
- [Documentazione EC2](https://docs.aws.amazon.com/ec2/)
