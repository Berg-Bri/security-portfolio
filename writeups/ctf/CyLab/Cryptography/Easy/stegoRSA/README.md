#### 🛠️ Tool usati

- [exiftool](../../../../../../tools/exiftool.md)
- [xxd](../../../../../../tools/xxd.md)
- [openssl](../../../../../../tools/openssl.md)
#### 🧩Descrizione

_"Un messaggio è stato criptato utilizzando RSA. La chiave pubblica non c'è più... ma qualcuno potrebbe essere stato disattento con la chiave privata. Puoi recuperarlo e decifrare il messaggio?"_

#### 🔍Analisi / Ricognizione

La challenge fa scaricare un'immagine di una chiave e un file `flag.enc`.

Ipotesi iniziale: ispezionando i metadati dell'immagine si potrebbe trovare la key per decodificare la flag.

#### ⚙️Sfruttamento

Uso lo strumento `exiftool` e ottengo i metadati dell'immagine. Noto che il campo `Comment` potrebbe essere interessante:

```
Comment                         : 2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d494945766749424144414e42676b....
```

Provo a convertirlo usando `xxd`:

```bash
echo "2d2d2d2d2d42454749..." | xxd -r -p
```

e ottengo la chiave privata:

```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCyi2qh7k1+l1Q7...
-----END PRIVATE KEY-----
```

Creo un file `.txt` con dentro la chiave e lo converto in un file `.pem`:

```bash
cp chiave.txt private.pem
```

E ora uso `openssl` per decifrare il file `flag.enc`:

```bash
openssl rsautl -decrypt -inkey private.pem -in flag.enc -out output.txt
```

Così facendo ottengo la flag.

#### 🚩Flag

`picoCTF{rs4_k3y_1n_1mg_a9a7c4c9}`

#### 💡Lezioni apprese

I metadati di un'immagine possono nascondere qualsiasi tipo di dato testuale, non solo brevi commenti — in questo caso un'intera chiave privata RSA codificata in hex dentro il campo `Comment`. Controllare i metadati con `exiftool` resta uno dei primi passi da fare davanti a qualunque file immagine sospetto, indipendentemente da quanto grande o "improbabile" sembri il contenuto che potrebbe esserci nascosto.