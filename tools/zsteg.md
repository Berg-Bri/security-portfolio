#### 🛠️Cos'è

`zsteg` è un tool a riga di comando scritto in Ruby, pensato per individuare dati nascosti con tecniche di steganografia in immagini PNG e BMP. È lo strumento di riferimento in ambito CTF per la steganografia LSB (Least Significant Bit).

#### ⚙️Cosa fa

Un'immagine bitmap è una sequenza di pixel, ognuno composto da canali di colore (R, G, B, e talvolta A per la trasparenza), ciascuno rappresentato da byte. La steganografia LSB nasconde dati modificando il bit meno significativo di questi byte: una modifica che altera il colore in modo impercettibile all'occhio umano ma che, se letta bit per bit, ricostruisce un messaggio.

Il problema è che non si sa a priori:

- quanti bit per canale sono stati usati (1, 2, 3... fino a 8),
- quali canali (solo R? RGB? RGBA? in che ordine, es. BGR invece di RGB?),
- in che ordine sono stati letti i pixel (riga per riga, colonna per colonna, dal basso, con numeri "primi" invece che sequenziali, ecc.).

`zsteg` prova automaticamente tutte queste combinazioni e, per ciascuna, verifica se il risultato assomiglia a testo leggibile o a un file conosciuto (usando internamente una libreria simile a `file`).

#### 💻Uso base

```bash
zsteg immagine.png
```

Mostra solo i risultati più probabili, filtrando il rumore.

```bash
zsteg -a immagine.png
```

`-a` ("all") esegue la scansione esaustiva su tutte le combinazioni di bit-plane, canale e ordine di lettura. Produce output molto più lungo ma non tralascia nulla.

Altre opzioni utili:

```bash
# estrae SOLO quella combinazione specifica in un file
zsteg -E "b1,rgba,lsb,xy" immagine.png 

# come sopra ma stampa su stdout   
zsteg -e "b1,r,lsb,xy" immagine.png  

# limita quanti byte analizzare     
zsteg --limit N immagine.png              
```

#### 📖Come leggere l'output

Ogni riga ha un identificatore del tipo:

```
b1,rgba,lsb,xy   .. text: "..."
```

- **b1** → numero di bit per canale usati (1 = solo il bit meno significativo, 2 = i due meno significativi, ecc.)
- **rgba** (o rgb, bgr, abgr...) → quali canali di colore sono coinvolti e in che ordine vengono letti
- **lsb / msb** → se il bit estratto viene considerato il meno o il più significativo del byte ricostruito
- **xy / yx / XY / YX** → direzione di scansione dei pixel (righe/colonne, in ordine normale o invertito)
- **prime** → variante che scandisce solo pixel in posizioni "prime" (una tecnica di offuscamento aggiuntiva)

Il risultato dopo `..` può essere:

- `text: "..."` → i byte estratti sembrano testo stampabile
- `file: ...` → i byte estratti, passati a un identificatore di tipo file, corrispondono a un formato noto (a volte falsi positivi, specialmente su combinazioni "esotiche")

#### ⚠️Cose da tenere a mente

- La maggior parte delle righe in una scansione `-a` sono falsi positivi: rumore che per caso assomiglia a un formato conosciuto. Bisogna usare intuito e contesto (nome del file, tema della sfida, pattern riconoscibili come `picoCTF{` o intestazioni base64 tipo `cGljb0NURn`).
- `zsteg` analizza anche i metadati/chunk del PNG (es. il campo `meta` visto nella challenge "red"), non solo i pixel.
- Combinazioni "speculari" (es. `rgba/xy` vs `abgr/XY`) a volte restituiscono lo stesso dato letto in ordine invertito: se una stringa base64 non decodifica, vale la pena provarla al contrario con `rev`.
- Non copre steganografia in JPEG, WAV, AU (per quei formati si usano `steghide`, `stegseek`, `wavsteg`, ecc.).