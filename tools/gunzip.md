#### 🛠️Cos'è 
`gunzip` è l'utility a riga di comando (pacchetto `gzip` su Linux) usata per decomprimere file compressi con l'algoritmo DEFLATE nel formato `.gz`. È il complemento di `gzip`: dove `gzip` comprime, `gunzip` riporta il file al suo contenuto originale. In molti contesti CTF/forensics è il primo passo obbligato quando un file scaricato o un'immagine disco arriva compressa (es. `disk.dd.gz`), perché tool come `strings`, `binwalk` o un file manager non possono analizzare correttamente i dati finché restano compressi.

#### ⚙️Come funziona Sintassi base:

```bash
gunzip <file>.gz
```

Questo decomprime `<file>.gz` e lo sostituisce con `<file>` (senza estensione `.gz`), rimuovendo l'originale compresso. Equivalente a `gzip -d <file>.gz`.

Opzioni utili:

- `-k`: mantiene il file `.gz` originale invece di cancellarlo dopo la decompressione (utile se si vuole preservare l'archivio scaricato).
- `-c`: scrive l'output su stdout invece di creare un file, comodo per incanalare direttamente il contenuto in un altro comando (es. `gunzip -c file.gz | strings | grep picoCTF`).
- `-t`: verifica l'integrità del file compresso senza estrarlo (test).
- `-l`: mostra informazioni sul contenuto compresso (dimensione originale, rapporto di compressione) senza decomprimere.

#### 💡Perché è utile 
Molti file distribuiti nelle CTF (immagini disco, dump di memoria, archivi di log) vengono compressi per ridurre la dimensione del download. `gunzip` è il modo più rapido per riportarli al formato originale prima di passarli ad altri tool di analisi (`strings`, `xxd`, `binwalk`, `file`, un filesystem viewer, ecc.). Usare `-c` insieme a una pipe evita di dover scrivere file intermedi su disco quando si vuole solo ispezionare rapidamente il contenuto.

#### ⚠️Limiti

- Funziona solo su file in formato `.gz` (DEFLATE/gzip): non decomprime zip, tar, rar, 7z o altri formati di archiviazione, per cui servono tool diversi (`unzip`, `tar`, `7z`, ecc.).
- Di default cancella il file compresso originale dopo l'estrazione: se serve conservarlo va usato `-k`.
- Non ripara archivi corrotti; su un `.gz` danneggiato l'estrazione può fallire o produrre un output incompleto (in quel caso può aiutare `gzip -dc` combinato con la gestione degli errori, o strumenti come `zcat`/`gzrecover`).