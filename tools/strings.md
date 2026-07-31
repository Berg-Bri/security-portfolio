#### 🛠️Cos'è

`strings` è un'utility a riga di comando (pacchetto `binutils` su Linux) che estrae le sequenze di caratteri stampabili da un file, indipendentemente dal suo formato. Funziona bene su file binari, eseguibili, immagini disco, core dump o qualsiasi altro file non testuale, perché non richiede di interpretare la struttura del file: scansiona i byte grezzi e restituisce ogni sequenza di caratteri stampabili abbastanza lunga da poter essere testo leggibile.

#### ⚙️Come funziona

Di default `strings` cerca sequenze di almeno 4 caratteri stampabili consecutivi (lettere, numeri, simboli, spazi) terminate da un carattere non stampabile o dalla fine del file. Se una sequenza è più corta della soglia minima, viene scartata.

Sintassi base:

```bash
strings <file>
```

Opzioni utili:

- `-n <numero>`: cambia la lunghezza minima delle stringhe da estrarre (es. `strings -n 8 file` per stringhe di almeno 8 caratteri, utile per ridurre il rumore).
- `-a`: forza la scansione dell'intero file (necessario su alcuni file oggetto, dove di default vengono controllate solo le sezioni dati).
- `-t x` / `-t d`: mostra l'offset (in esadecimale o decimale) a cui ogni stringa è stata trovata nel file, utile per poi ispezionare quel punto con un hex editor.
- `-e l` o `-e b`: interpreta caratteri a 16 bit (little/big endian), utile per testo codificato in UTF-16 (comune su Windows).

#### 💡Perché è utile

Molti file contengono testo "annegato" tra dati binari: percorsi di file, messaggi di errore, URL, chiavi, credenziali hardcoded, nomi di funzioni, o — nel contesto CTF — flag lasciate nel filesystem. Aprire questi file con un editor di testo normale produce output illeggibile pieno di caratteri di controllo; `strings` filtra automaticamente il rumore e lascia solo ciò che è potenzialmente leggibile.

Poiché non interpreta la struttura del file (partizioni, filesystem, formati eseguibili), è spesso il primo strumento da provare quando ci si trova davanti a un file sconosciuto: è veloce, non modifica nulla e può rivelare informazioni utili senza bisogno di montare o parsare nulla.

#### ⚠️Limiti

- Estrae solo testo stampabile: dati binari, cifrati o compressi non produrranno stringhe leggibili.
- Non capisce la struttura del file (a differenza di tool come `file`, `binwalk` o un parser di filesystem), quindi non dice dove nel contesto logico del file si trova una stringa, solo il suo offset grezzo.
- Può generare falsi positivi: sequenze di byte casuali che per caso formano caratteri stampabili.