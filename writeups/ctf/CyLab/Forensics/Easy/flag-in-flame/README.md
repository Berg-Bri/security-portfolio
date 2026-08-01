#### 🛠️Tool usati

- [base64](../../../../../../tools/base64.md)
- [tesseract](../../../../../../tools/tesseract.md)
- [xxd](../../../../../../tools/xxd.md)
#### 🧩Descrizione

Il team di SOC ha scoperto un file di registro sospettosamente grande dopo una recente violazione. Quando l'hanno aperto, hanno trovato un enorme blocco di testo codificato invece di registri tipici. Potrebbe esserci qualcosa di nascosto dentro? La tua missione è ispezionare il file risultante e rivelarne il vero scopo. Il team si affida alle tue abilità per scoprire qualsiasi informazione nascosta all'interno di questo registro insolito.

#### 🔍Analisi / Ricognizione

Viene fornito un file `.txt` abbastanza grande con testo codificato illeggibile.

#### ⚙️Sfruttamento

La prima idea è stata quella di decodificarlo in base64 e trasformarlo in png:

```bash
base64 --decode logs.txt > logs.png
```

<p align="center"> <img src="assets/hacker.png" width="400" height="500"> </p>

Invece di trascrivere manualmente la stringa dall'immagine, ho usato il tool `tesseract`:

```bash
tesseract logs.png output
```

mi sono fatto scrivere la stringa nel file `output.txt`.

La stringa è la seguente: `7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F65633139383466637D`.

Si nota che la stringa è codificata in hex, così l'ho decodificata con lo strumento `xxd`:

```bash
echo "7069636F43544..." | xxd -r -p
```

Ottenendo così la flag.

#### 🚩Flag

picoCTF{forensics_analysis_is_amazing_ec1984fc}

#### 💡Lezioni apprese

- Quando ci si trova davanti a un "log" enorme fatto di solo testo codificato, vale la pena provare a decodificarlo (base64, hex) prima di cercare pattern nei log stessi: spesso il file non è affatto un log.
- Incatenare più livelli di codifica (base64 → immagine → OCR → hex) è una tecnica comune nelle challenge forensics: ogni layer va riconosciuto e rimosso uno alla volta.
- `tesseract` evita errori di trascrizione manuale su stringhe lunghe estratte da un'immagine.





