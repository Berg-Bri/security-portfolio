#### 🛠️Cos'è

Tool per leggere, scrivere e manipolare i metadata di file (immagini, PDF, video, audio, ecc.). Fondamentale nelle challenge di steganografia/forensics per cercare dati nascosti nei metadata (EXIF, IPTC, XMP).

#### 💻Comandi base

**Leggere i metadata di un file:**

```bash
exiftool file.jpg
```

**Vedere ANCHE i tag nascosti/duplicati, raggruppati per categoria:**

```bash
exiftool -a -u -g1 file.jpg
```

Utile perché il comando base a volte nasconde tag ridondanti o poco comuni che invece potrebbero contenere dati interessanti (es. flag CTF).

**Estrarre un singolo tag specifico:**

```bash
exiftool -Comment file.jpg
exiftool -UserComment file.jpg
exiftool -GPS* file.jpg      # tutti i tag GPS
```

**Output in formato solo valori (utile per scripting/grep):**

```bash
exiftool -s -Comment file.jpg
```

#### ✏️Modificare i metadata

**Scrivere/modificare un tag:**

```bash
exiftool -Comment="testo nascosto" file.jpg
```

(exiftool crea automaticamente un backup `file.jpg_original`)

**Rimuovere TUTTI i metadata:**

```bash
exiftool -all= file.jpg
```

**Rimuovere il backup automatico dopo la modifica:**

```bash
exiftool -overwrite_original -Comment="testo" file.jpg
```

#### 📂Analisi su più file / batch

```bash
exiftool *.jpg
exiftool -r cartella/          # ricorsivo su tutta una cartella
```

#### 🏷️Tag utili da controllare sempre in CTF

|Tag|Cosa può contenere|
|---|---|
|`Comment` / `UserComment`|Testo libero, spesso usato per nascondere flag|
|`Title`, `Author`, `Creator Tool`|A volte rivelano il tool usato o indizi|
|`GPS Position`|Coordinate nascoste|
|`Software`|Versione del programma usato per creare/modificare il file|
|`Copyright`|A volte contiene messaggi nascosti|

#### 🔁Workflow rapido in CTF

```bash
# 1. Overview veloce
exiftool file.jpg

# 2. Deep dive su tag nascosti
exiftool -a -u -g1 file.jpg

# 3. Grep mirato su parole chiave (es. "flag", "picoctf")
exiftool file.jpg | grep -i flag
```

#### ⚠️Note

- ExifTool legge SOLO i metadata dichiarati nel formato del file — non trova dati appesi grezzamente in coda al file (per quello serve `binwalk`) né dati nascosti nei pixel (per quello serve `zsteg`/`steghide`).
- Alcuni formati (PNG) hanno pochissimi metadata di default rispetto a JPEG: se un PNG sembra "vuoto" con exiftool, non significa che non contenga dati nascosti altrove.