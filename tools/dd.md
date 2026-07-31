#### 🧠Cos'è

Un'immagine `.dd` è una copia bit-per-bit (raw) di un disco o di una partizione, creata tipicamente con il comando Unix `dd` ("data duplicator" / "disk dump").

A differenza di un backup normale, che copia solo i file visibili nel filesystem, `dd` legge il dispositivo a livello di blocchi grezzi: copia ogni singolo byte, incluso il boot sector, la tabella delle partizioni, lo spazio non allocato e persino i file cancellati (finché non sono stati sovrascritti). Il risultato è un file `.dd` identico, byte per byte, al disco originale.

#### ⚙️Come funziona

`dd` legge il dispositivo sorgente blocco per blocco (dimensione impostabile con `bs`) e scrive lo stream grezzo in un file di output, senza interpretare in alcun modo il filesystem presente — non sa (e non gli interessa) se sopra ci sia NTFS, ext4 o nulla di riconoscibile. Copia semplicemente i byte così come sono.

#### 💻Uso da riga di comando

```bash
dd if=/dev/sda of=disco.dd bs=4M
```

`if` è il device sorgente (input file), `of` è il file immagine di destinazione (output file), `bs` la dimensione del blocco letto/scritto per volta (influisce sulla velocità, non sul risultato).

#### 📌Perché è rilevante in ambito forensics/CTF

Un'immagine `.dd` può essere analizzata senza toccare il disco originale, preservando l'integrità della prova. Strumenti come `strings`, `binwalk`, `foremost` o un file manager forense possono cercare al suo interno dati che nel filesystem normale sarebbero nascosti o cancellati — proprio come nella challenge **Disko 1**, dove la flag non era in un file "visibile" ma solo recuperabile scandendo il testo grezzo dell'immagine con `strings`.

#### ⚠️Attenzione

Il formato `.dd` non ha un header o una struttura propria: è puro raw. Questo significa che:

- può essere montato direttamente (`mount -o loop`) solo se contiene un filesystem valido e riconoscibile;
- in caso contrario (o se non vuoi montarlo), va comunque ispezionato byte per byte con altri strumenti;
- non essendoci nessun metadato che descriva il contenuto, è il tool di analisi (non il formato del file) a doverlo dedurre — per questo `strings`/`binwalk` sono spesso il primo passo, indipendentemente da cosa contenga davvero l'immagine