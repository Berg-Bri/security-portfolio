##### 🛠️ Tool usati

- [xxd](../../../../../../tools/xxd.md)

##### 🧩 Descrizione

_Il file contiene più di quanto sembra_

##### 🔍 Analisi / Ricognizione

Viene data un'immagine in formato `.jpg`.

##### ⚙️ Sfruttamento

Sono partito analizzando il contenuto grezzo del file con lo strumento `xxd`:

```bash
xxd garden.jpg

00230560: 7265 2069 7320 6120 666c 6167 3a20 7069  re is a flag: pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3339 3865  m33ts_the_3y398e
00230590: 6532 3239 617d 0a
```

Scorrendo l'output esadecimale, verso la fine del file, è visibile del testo in chiaro nella colonna ASCII a destra, la flag stessa, senza alcuna codifica.

##### 🚩 Flag

picoCTF{more_than_m33ts_the_3y398ee229a}

##### 💡 Lezioni apprese

Non tutti i dati nascosti sono codificati o cifrati: qui la flag era testo semplice appeso in fondo al file JPEG, visibile direttamente nella colonna ASCII di un dump esadecimale, senza bisogno di alcuna decodifica. Quando si sospetta un file "più pesante di quanto dovrebbe" o con dati oltre la fine dei dati immagine attesi, un semplice `xxd`/hex dump (o in alternativa `strings`, se si cerca solo testo leggibile senza doverlo individuare a occhio nell'esadecimale) è spesso sufficiente a scovare contenuto nascosto in chiaro.