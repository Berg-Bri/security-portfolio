##### 🛠️ Tool usati

- [unzip](../../../../../../tools/unzip.md)
- [exiftool](../../../../../../tools/exiftool.md)
- [base64](../../../../../../tools/base64.md)

##### 🧩 Descrizione

_Che ne dici di giocare a nascondino?_

##### 🔍 Analisi / Ricognizione

La challenge parte facendo scaricare un file `.zip`.

##### ⚙️ Sfruttamento

Estraggo il contenuto dell'archivio:

```bash
unzip unknown.zip
Archive:  unknown.zip
  inflating: ukn_reality.jpg
```

Controllo i metadati dell'immagine ottenuta:

```bash
exiftool ukn_reality.jpg
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==
```

Il campo "Attribution URL" (non uno dei campi metadata più comuni/attesi) contiene una stringa in base64. La decodifico:

```bash
echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fZDhjMzgxZmR9Cg==" | base64 --decode
picoCTF{ME74D47A_HIDD3N_d8c381fd}
```

##### 🚩 Flag

picoCTF{ME74D47A_HIDD3N_d8c381fd}

##### 💡 Lezioni apprese

I dati nascosti nei metadati non sempre finiscono nei campi più "ovvi" (Comment, Author, Description): qui la flag era in "Attribution URL", un campo che nell'uso reale non ha nulla a che fare con contenuto arbitrario codificato. Conviene sempre dare un'occhiata all'output completo di `exiftool` invece di guardare solo i campi che ci si aspetta di trovare popolati, perché qualsiasi campo di testo libero può essere riutilizzato per nascondere dati.