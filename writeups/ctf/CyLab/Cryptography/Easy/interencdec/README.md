#### Descrizione
Si può ottenere il vero significato da questo file.

#### Analisi / Ricognizione
La stringa che veniva fornita era la seguente:
`idkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg==`
La lunghezza non era quella di un hash.
#### Sfruttamento
Ho pensato fose un base64, allora ho eseguito il primo comando:
```bash
echo YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyZzBOMm8yYXpZNWZRPT0nCg== | base64 --decode
b d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ==
```

Ho subito pensato che ci fosse un altro base64 da decriptare, così ho dato il secondo comando:
```bash
echo d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2g0N2o2azY5fQ== | base64 --decode
wpjvJAM{jhlzhy_k3jy9wa3k_h47j6k69} 
```

Arrivati a questo punto si vedeva chiaramente la classica struttura della flag di CyLab.
Sapendo che la prima lettera di solito è la p di pico, ho pensato subito ad un cifrario di cesare con chiave = 7 e ho ottenuto la flag.
#### Flag
picoCTF{caesar_d3cr9pt3d_a47c6d69}