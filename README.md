# 📘 Appunti Universitari

Questa repository raccoglie appunti in formato Markdown scritti durante il percorso accademico.  
Ogni sezione rappresenta una materia specifica, organizzata per massima chiarezza e navigabilità all'interno di Obsidian.

---

## 📚 Materie attualmente disponibili

- [Algoritmi e Strutture Dati](algoritmi-e-strutture-dati/README.md)
- [Machine Learning](machine-learning/README.md)
- [Tecnologie web per il cloud](tecnologie_web_per_il_cloud/README.md)

Ogni cartella contiene un `README.md` che descrive la struttura degli appunti e l’organizzazione dei contenuti della materia.

---

## 🛠️ Requisiti

Per una visualizzazione ottimale si consiglia di utilizzare [**Obsidian**](https://obsidian.md/) con i seguenti plugin:

### 🔌 Plugin consigliati

| Plugin | Descrizione |
|--------|-------------|
| [Templater](https://github.com/SilentVoid13/Templater) | Per la generazione dinamica di note da template. |
| [Front Matter Title](https://github.com/snezhig/obsidian-front-matter-title) | Per visualizzare i metadati nel titolo e nella nota. |
| [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) | Per aggiungere schizzi e diagrammi interattivi. |

---

### ⚙️ Configurazione Plugin

#### Templater
- `Template folder location`: `./templates/`
- `Scripts files folder location`: `./utils/templates`

#### Front Matter Title
- Chiave configurata: `title`
- Funzionalità abilitate:
  - ✅ Alias
  - ✅ Graph
  - ✅ Header
  - ✅ Bookmarks
  - ✅ Inline

---

## 📁 Struttura dei file

- Tutti gli appunti sono in formato `.md` (Markdown).
- I file contengono un blocco **Front Matter** YAML con metadati:

  ```yaml
  ---
  title: "Titolo della nota"
  aliases: ["Alias della nota"]
  tags: [università, materia, argomento]
  created: 2025-06-08
  ---
