#### 🛠️Tool usati

- [unzip](../../../../../../tools/unzip.md)
- [xdg-open](../../../../../../tools/xdg-open.md)
- [zbarimg](../../../../../../tools/zbarimg.md)
#### 🧩Descrizione

_Mi sono stufato di inserire i flag come testo. Non sarebbe bello se fossero invece delle immagini?_

#### 🔍Analisi / Ricognizione

La challenge inizia scaricando il file `.zip` in allegato.

#### ⚙️Sfruttamento

Il primo passo è stato unzippare il file:

```bash
unzip challenge.zip 
Archive:  challenge.zip
   creating: home/ctf-player/drop-in/
 extracting: home/ctf-player/drop-in/flag.png  
```

Poi mi sono spostato nella cartella e ho aperto l'immagine presente con il comando `xdg-open`:

```bash
xdg-open flag.png 
```

<p> <img src="assets/qrcode.png" align="center"></p>

Siccome volevo leggere il QR code senza scannerizzarlo con il telefono ma usando la CLI, ho usato il tool `zbarimg`:

```bash
zbarimg flag.png
QR-Code:picoCTF{p33k_@_b00_19eccd10}
```


#### 🚩Flag

picoCTF{p33k_@_b00_19eccd10}

#### 💡Lezioni apprese

Non tutte le flag vengono fornite come testo semplice: qui era codificata visivamente in un QR code dentro un'immagine, un promemoria a controllare sempre il contenuto reale dei file ricevuti (soprattutto immagini) invece di aspettarsi solo testo o metadati nascosti. Strumenti come `zbarimg` permettono di decodificare codici a barre/QR direttamente da riga di comando, senza bisogno di uno smartphone — utile soprattutto in ambienti CTF headless o via SSH, dove non è disponibile un'interfaccia grafica per scansionare fisicamente il codice.









