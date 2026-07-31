#### 🛠️Cos'è 
`grep` (Global Regular Expression Print) è un'utility a riga di comando che cerca righe di testo corrispondenti a un pattern (letterale o espressione regolare) all'interno di uno o più file, e ne stampa le righe che fanno match. È uno dei tool più universali su sistemi Unix/Linux: funziona su qualsiasi file di testo o testo estratto da un binario (es. tramite `strings`), ed è spesso il collante tra altri tool in una pipeline.

#### ⚙️Come funziona Sintassi base:

```bash
grep "pattern" file
```

Cerca ogni riga di `file` che contiene `pattern` e la stampa a video. Può leggere anche da stdin, il che lo rende ideale in pipeline (`comando | grep "pattern"`).

Opzioni utili:

- `-i`: case-insensitive, ignora maiuscole/minuscole.
- `-o`: stampa solo la porzione di riga che fa match, non l'intera riga (utile per estrarre esattamente una stringa, es. una flag).
- `-r` / `-R`: ricerca ricorsiva in una directory.
- `-n`: mostra il numero di riga del match.
- `-v`: inverte il match, mostra le righe che NON contengono il pattern.
- `-A <n>` / `-B <n>` / `-C <n>`: mostra n righe di contesto dopo/prima/attorno al match.
- `-E`: abilita le extended regular expressions (equivalente a `egrep`), utile per pattern più complessi con `{}`, `+`, `|` senza escaping.
- `-c`: conta il numero di righe corrispondenti invece di stamparle.

#### 🔀Varianti

- `egrep` / `grep -E`: extended regex (sintassi più ricca, meno escaping).
- `fgrep` / `grep -F`: match su stringhe letterali, nessuna interpretazione come regex (più veloce su pattern semplici).
- `zgrep`: come `grep` ma su file compressi `.gz`, senza doverli decomprimere prima.
- `ripgrep` (`rg`): reimplementazione moderna, molto più veloce su grandi codebase, con supporto ricorsivo e `.gitignore` di default.

#### 💻Uso da riga di comando 
Esempi pratici in ambito CTF/forensics:

```bash
# Cercare una flag con pattern noto dentro l'output di strings
strings file.bin | grep picoCTF

# Estrarre solo la porzione che fa match (es. la flag completa tra parentesi graffe)
grep -o "picoCTF{[^}]*}" file.txt

# Ricerca ricorsiva case-insensitive di una parola in una directory
grep -rin "password" ./progetto

# Cercare un pattern su un dump di memoria/heap
grep -a -o "picoCTF{[^}]*}" heapdump.heapsnapshot
```

#### 📌Casi d'uso comuni

- Filtrare l'output di altri tool (`strings`, `xxd`, `curl`, log applicativi) per isolare solo le righe rilevanti.
- Estrarre una flag con formato noto (`picoCTF{...}`) da un file di testo, un dump di memoria o l'output di un comando.
- Cercare credenziali, chiavi API, commenti sospetti o TODO nel codice sorgente di un progetto.
- Verificare rapidamente la presenza/assenza di una stringa in decine di file con `-r`.

#### ⚠️Attenzione in ambito sicurezza

- `grep` opera solo su testo: su un file binario può servire `-a` (forza il trattamento come testo) oppure combinarlo con `strings` per estrarre prima le sequenze leggibili.
- Pattern regex mal scritti possono generare falsi positivi o negativi; su stringhe con caratteri speciali (`{`, `}`, `.`, `*`) vanno sempre valutati escaping o l'uso di `-F` per match letterali.
- Su file molto grandi una regex complessa può essere lenta: per performance su grandi codebase conviene valutare `ripgrep`.