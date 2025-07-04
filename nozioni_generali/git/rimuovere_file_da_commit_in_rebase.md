# 🔧 Rimuovere un file da un commit durante rebase + gestire conflitto con stash

## 🎯 Obiettivo
Rimuovere un file da un commit in rebase interattivo **come se non fosse mai stato modificato**, e ripristinarlo dallo stash in seguito.

## 🧩 Scenario

- Sei in un `git rebase -i` fermo su un commit (`pick`) che contiene un file **incluso per errore**, ad es: `.obsidian/app.json`.
- Vuoi rimuoverlo dal commit.
- Hai precedentemente salvato le modifiche corrette via `git stash`.

---

## ✅ Rimuovere il file dal commit corrente

### 🔹 Caso 1: Il file **esisteva già** nei commit precedenti

```bash
git restore --source=HEAD^ .obsidian/app.json
git add .obsidian/app.json
git commit --amend
git rebase --continue
```

### 🔹 Caso 2: Il file era nuovo (non esisteva in HEAD^)

```bash
git restore --staged .obsidian/app.json
del .obsidian\app.json              # Windows
# oppure: rm .obsidian/app.json     # Linux/macOS

git commit --amend
git rebase --continue
```

---

### 🧰 Recuperare il file con git stash pop
Dopo il rebase:

```bash
git stash pop
```

Se compare un conflitto tipo:

```
CONFLICT (add/add): Merge conflict in .obsidian/app.json
```

vuol dire che **il file è stato aggiunto sia nello stash che nel commit appena riscritto**.


#### 🔧 Risoluzione del conflitto
➕ Tenere la versione dallo stash:

```bash
git checkout --theirs .obsidian/app.json
```

➕ Tenere la versione dal branch:

```bash
git checkout --ours .obsidian/app.json
```

🖊️ Modificare a mano:

Apri `.obsidian/app.json`, risolvi i conflitti manualmente, poi:

```bash
git add .obsidian/app.json
```


Infine, se non ti serve più lo stash:

```bash
git stash drop
```

---

### ✅ Stato finale atteso

```bash
git status
# working tree pulito
```

Il file .obsidian/app.json è stato rimosso dal commit sbagliato e ripristinato correttamente per usi futuri.