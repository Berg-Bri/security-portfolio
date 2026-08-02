##### 🛠️ Tool usati

- [exiftool](../../../../../../tools/exiftool.md)
- [base64](../../../../../../tools/base64.md)

##### 🧩 Descrizione

_I file possono sempre essere modificati in modo segreto. Puoi trovare la bandiera?_

##### 🔍 Analisi / Ricognizione

La challenge parte facendoti scaricare un file `.jpg`.

##### ⚙️ Sfruttamento

Controllo i metadati dell'immagine:

```bash
exiftool cat.jpg
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

Riconosco subito `cGlj` come prefisso tipico di una stringa base64 che nasconde una flag `picoCTF{...}`, quindi la decodifico:

```bash
echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 --decode
picoCTF{the_m3tadata_1s_modified}
```

##### 🚩 Flag

picoCTF{the_m3tadata_1s_modified}

##### 💡 Lezioni apprese

Ancora una volta la flag era nascosta in un campo metadata non scontato (`License`, non `Comment`/`Author`), a conferma che conviene sempre controllare l'output completo di `exiftool` invece di guardare solo i campi più comuni.

Riconoscere `cGlj` come prefisso tipico della codifica base64 di `picoCTF{` è una scorciatoia utile per individuare a colpo d'occhio quale tra più stringhe candidate vale la pena decodificare, senza doverle provare tutte.