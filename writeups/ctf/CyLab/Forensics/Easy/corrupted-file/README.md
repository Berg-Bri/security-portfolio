#### 🛠️Tool usati

- [xxd](../../../../../../tools/xxd.md)
- [tesseract](../../../../../../tools/tesseract.md)

#### 🧩Descrizione

Questo file sembra rotto... o è così? Forse un paio di byte potrebbero fare la differenza. Riesci a capire come riportarlo in vita?

#### 🔍Analisi / Ricognizione

Viene fornito un file senza estensione che non si apriva con nessun visualizzatore di immagini. Il primo istinto è stato quello di vedere i metadati ed è qui che sono partito.

#### ⚙️Sfruttamento

Ho usato il tool `xxd` per vedere i metadati del file:

```bash
xxd  file       
00000000: 5c78 ffe0 0010 4a46 4946 0001 0100 0001  \x....JFIF......
```

Si trattava di un file `.jfif`, a tutti gli effetti un'immagine JPEG standard utilizzata per l'archiviazione e lo scambio sul web.

Ho fatto l'errore di rinominare il file aggiungendogli l'estensione, però continuavo ad osservare che nessun visualizzatore di immagini riusciva a leggerla correttamente.

Sono andato così a controllare i magic numbers dei file `.jfif` su internet e ho notato che c'era un errore nell'header:

`corretto: FFD8 FFE0 4A46 4946 00` `errato: FFE0 0010 4A46 4946 00`

Mancavano i due byte `D8 FF`, così ho cambiato l'header del file con questo comando:

```bash
(printf '\xff\xd8' && tail -c +3 file) > repair.jpg
```

Il comando: stampa i 2 byte corretti `FF D8`, poi concatena il resto del file originale saltando i primi 2 byte corrotti (`tail -c +3`), salvando tutto in `repair.jpg`. Così facendo il resto dell'header (`FF E0` e il payload JFIF successivo) risultava già intatto.

Ho ottenuto così l'immagine con all'interno la flag, che non ho trascritto a mano ma ho estratto con il tool `tesseract`:

```bash
tesseract repair.jpg output
cat output.txt
```

ottenendo così la flag.

#### 🚩Flag

picoCTF{r3st0r1ng_th3_by73s_684e09bc}

#### 💡Lezioni apprese

- L'estensione di un file è solo metadato, non il formato reale. Rinominare `file` in `file.jpg` non cambia un solo byte del contenuto: se l'header interno è corrotto, il file resta illeggibile indipendentemente dal nome.
- Il vero passaggio di riconoscimento è verificare i magic bytes (`file`, `hexdump -C`, `xxd`) prima di assumere qualsiasi cosa sul formato.