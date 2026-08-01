#### 🛠️Tool usati

- [exiftool](../../../../../../tools/exiftool.md)
- [base64](../../../../../../tools/base64.md)
- [steghide](../../../../../../tools/steghide.md)

#### 🧩Descrizione

Ti viene data un'immagine JPG apparentemente ordinaria. Qualcosa è nascosto fuori dalla vista all'interno del file. Il vostro compito è scoprire il carico utile nascosto ed estrarre la flag.

#### 🔍Analisi / Ricognizione

Come spesso accade, se viene fatto scaricare un file pdf, jpeg o png è spesso fondamentale controllare i metadati. Così sono partito da quello.

#### ⚙️Sfruttamento

Con il comando:

```bash
exiftool img.png
```

Il campo comment era una stringa codificata in base64.

Allora ho eseguito la decodifica su quest'ultimo:

```bash
echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 --decode
steghide:cEF6endvcmQ=
```

L'output contiene la parola `steghide`, che è il tool usato per nascondere dati nelle immagini, e una seconda stringa in base64.

Ho decodificato anche l'ultima stringa ottenendo la password:

```bash
echo "cEF6endvcmQ=" | base64 --decode
pAzzword
```

Controllo se nell'immagine ci sono dati nascosti:

```bash
steghide --info img.jpg
```

Una volta verificato che effettivamente ci sono dati nascosti ho fatto l'estrazione:

```bash
steghide extract -sf img.jpg -p pAzzword
```

estraendo il file `flag.txt` contenente la flag.

#### 🚩Flag

picoCTF{h1dd3n_1n_1m4g3_871ba555}

#### 💡Lezioni apprese

- I metadati (`exiftool`) sono spesso il primo posto dove nascondere indizi o credenziali: vanno controllati prima di passare a tecniche più invasive.
- Stringhe che sembrano rumore vanno sempre testate contro base64 (o altre codifiche comuni): qui hanno rivelato sia il tool da usare (`steghide`) sia la password.
- `steghide --info` prima di `extract` conferma la presenza di dati nascosti ed evita di tentare l'estrazione alla cieca.