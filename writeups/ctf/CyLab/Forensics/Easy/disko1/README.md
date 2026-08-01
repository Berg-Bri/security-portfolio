#### 🛠️Tool usati

- [strings](../../../../../../tools/strings.md)
- [gunzip](../../../../../../tools/gunzip.md)
#### 🧩Descrizione

Potete trovare la flag in questa immagine del disco?

#### 🔍Analisi / Ricognizione

Viene fatto scaricare un file zip e da questo si partirà con la ricerca della flag.

#### ⚙️Sfruttamento

Come primo passo unzippiamo il file appena scaricato:

```bash
gunzip disko-1.dd.gz
```

Utilizziamo il tool `strings` per riuscire a leggere il testo nel disk image file, concatenandolo con il comando `grep` per trovare la flag:

```bash
strings disko-1.dd | grep picoCTF
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
```

#### 🚩Flag

picoCTF{1t5_ju5t_4_5tr1n9_be6031da}

#### 💡Lezioni apprese

- Prima di lanciarsi in analisi forensi complesse su un'immagine disco, vale sempre la pena tentare `strings | grep` sulla flag format: spesso basta questo.
- `gunzip`/`gzip -d` per decomprimere `.gz` prima di poter analizzare il contenuto.