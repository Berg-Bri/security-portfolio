#### 🛠️Tool usati

- Base64

#### 🧩Descrizione

_"Si può ottenere il vero significato da questo file."_

#### 🔍Analisi / Ricognizione

La stringa fornita era la seguente:

```
idkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg==
```

La lunghezza non era quella di un hash, il che ha escluso subito un hash e indirizzato verso una codifica reversibile.

#### ⚙️Sfruttamento

Ho pensato fosse un base64, quindi ho eseguito il primo comando:

```bash
echo YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg== | base64 --decode
b d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==
```

Ho subito pensato che ci fosse un altro base64 da decodificare, quindi ho dato il secondo comando:

```bash
echo d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ== | base64 --decode
wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69}
```

Arrivati a questo punto si vedeva chiaramente la classica struttura della flag di CyLab.

Sapendo che la prima lettera è di solito la `p` di pico, ho pensato subito a un cifrario di Cesare con chiave = 7 e ho ottenuto la flag.

#### 🚩Flag

`picoCTF{caesar_d3cr9pt3d_a47c6d69}`

#### 💡Lezioni apprese

Quando una stringa non ha la lunghezza tipica di un hash, vale la pena controllare subito se è una codifica reversibile (Base64 è il primo sospetto, riconoscibile dall'alfabeto e dal padding `=`). Anche dopo una decodifica riuscita, se il risultato non sembra ancora leggibile è normale sospettare un ulteriore livello — gli offuscamenti "a strati" (Base64 + Base64 + cifrario di Cesare, qui) sono comuni nei CTF proprio per rallentare chi si ferma al primo tentativo.