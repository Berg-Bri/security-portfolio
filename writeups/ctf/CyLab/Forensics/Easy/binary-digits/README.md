#### Descrizione
Questo file non sembra un granché... solo una serie di 1 e 0. Ma forse non si tratta di semplice rumore casuale. Riesci a ricavarne qualcosa di significativo?

#### Analisi / Ricognizione
Viene fornito un file con estensione .bin contenente solo 0 e 1.
Prima di convertire tutto, conviene guardare i primi byte e confrontarli con i **magic number** dei formati più comuni:

| Byte iniziali (hex) | Formato |
| ------------------- | ------- |
| `FF D8 FF`          | JPEG    |
| `89 50 4E 47`       | PNG     |
| `47 49 46 38`       | GIF     |
| `25 50 44 46`       | PDF     |
| `50 4B 03 04`       | ZIP     |

In questo caso, i primi bit erano:
```
11111111 11011000 11111111 11100000
```

che in esadecimale è `FF D8 FF E0` — l'header standard di un **JPEG**.

#### Sfruttamento
Scrivo uno scipt che mi permette di:
- Leggere e ripulire i bit dal file di input.
- Convertirli in byte grezzi con `bytes(...)`.
- Riconoscere automaticamente il formato tramite magic number.
- Salvare il risultato con l'estensione corretta (es. `recovered.jpg`).

```python
data = bytes(
    int(bits[i:i+8], 2)
    for i in range(0, len(bits), 8)
)

with open("recovered.jpg", "wb") as f:
    f.write(data)
```

Ottengo cosi un immagine che contiene la flag.
<p align="center"> <img src="assets/flag.png" > </p>
#### Flag
picoCTF{h1dd3n_1n_th3_b1n4ry_a59b2b0a}


