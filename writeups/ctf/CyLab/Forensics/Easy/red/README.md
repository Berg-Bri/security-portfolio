#### 🛠️Tool usati

- [exiftool](../../../../../../tools/exiftool.md)
- [xxd](../../../../../../tools/xxd.md)
- [zsteg](../../../../../../tools/zsteg.md)
- [base64](../../../../../../tools/base64.md)

#### 🧩Descrizione

RED, RED, RED, RED

#### 🔍Analisi / Ricognizione

Una volta scaricata l'immagine ho provato a controllare i metadati con `exiftool` e ho dato un'occhiata ai byte grezzi con `xxd`, ma nessuno dei due tool mi ha portato a qualcosa di utile.

Successivamente ho pensato ad altri strumenti per la steganografia su PNG. `steghide` non supporta il formato PNG, quindi era da escludere a prescindere.

Sono così passato allo strumento `zsteg`, che analizza sistematicamente i bit meno significativi (LSB) dei pixel su diverse combinazioni di canale, ordine dei bit e direzione di scansione.

#### ⚙️Sfruttamento

Il primo comando è stato il seguente:

```bash
zsteg -a red.png
```

Tra le decine di combinazioni testate da zsteg, un paio di righe saltavano subito all'occhio perché contenevano stringhe che sembravano in base64:

```bash
1,rgba,lsb,xy      .. text: "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ=="
```

Questa stringa appariva 2 volte, e nel secondo caso la stringa appariva stampata al contrario perché le informazioni erano lette con canali e ordine di scansione invertiti.

Una volta ottenuta la stringa in base64 è bastato fare una decodifica ottenendo la flag:

```bash
echo "cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==" | base64 --decode
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}
```

#### 🚩Flag

picoCTF{r3d1s_th3_ult1m4t3_cur3_f0r_54dn355}

#### 💡Lezioni apprese

- Quando `exiftool` e un'ispezione a byte grezzi (`xxd`) non danno risultati su un PNG, il passo successivo è pensare alla steganografia LSB: `zsteg -a` copre in un colpo solo tutte le combinazioni di canale/ordine/bit.
- `steghide` non supporta PNG: per quel formato serve un tool dedicato come `zsteg`.
- I dati LSB possono comparire "specchiati" (canali/ordine di scansione invertiti): se una stringa sembra corrotta o al contrario, vale la pena controllare le varianti prima di scartarla.