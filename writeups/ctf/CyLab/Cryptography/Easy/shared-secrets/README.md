#### Tool usati

#### Descrizione
Un messaggio è stato criptato usando un segreto condiviso... ma sembra che un lato dello scambio abbia fatto trapelare qualcosa. Puoi mettere insieme il segreto e prendere la bandiera?
#### Analisi / Ricognizione
La challenge fornisce due file: uno script Python che genera i parametri di uno scambio Diffie-Hellman e cifra la flag con la chiave condivisa, e un file `.txt` contenente i valori pubblici effettivamente generati (`g`, `p`, `A`) più il ciphertext (`enc`). L'obiettivo è recuperare la flag partendo da questi dati.
Guardando lo script con attenzione, il vero problema non sta nello scambio DH in sé, che è impostato correttamente e con un primo abbastanza grande da essere sicuro. Il problema sta in come viene usato il segreto condiviso subito dopo averlo calcolato:
```python
enc = bytes([x ^ (shared % 256) for x in flag])
#     └────┘  └─┘   └─────────┘   └────────┘
#   converte  XOR   chiave a      per ogni byte
#   in bytes  bit   1 solo byte   della flag
```

Qui `shared`, che teoricamente potrebbe essere un numero enorme (fino a 1048 bit), viene ridotto con `% 256` a un singolo byte. Questo byte viene poi usato come chiave XOR ripetuta su ogni carattere della flag. Di fatto, tutta la robustezza di Diffie-Hellman viene vanificata: invece di dover risolvere un problema di logaritmo discreto, basta indovinare un numero tra 0 e 255.

#### Sfruttamento
Non serve calcolare `a` o `b`, né toccare `g`, `p` o `A` in alcun modo: bastano il file di ciphertext e un bruteforce su tutti i possibili valori a un byte.

Ho estratto l'hex del campo `enc` dal file `.txt` fornito dalla challenge:

```
ffe6ece0ccdbc9f4ebe7d0fcbcecfdbcfbd0b9ebeeebbfb6ecebf2
```

Ho scritto ed eseguito questo script Python per provare tutti i 256 possibili valori di chiave XOR:

python

```python
enc = bytes.fromhex('ffe6ece0ccdbc9f4ebe7d0fcbcecfdbcfbd0b9ebeeebbfb6ecebf2')

for key in range(256):
    flag = bytes([b ^ key for b in enc])
    try:
        decoded = flag.decode()
        if 'picoCTF' in decoded:
            print(key, decoded)
    except UnicodeDecodeError:
        pass
```

Eseguito da terminale con:

bash

```bash
python3 script.py
```

Lo script prova ogni chiave da 0 a 255, applica lo XOR byte per byte contro `enc`, tenta di decodificare il risultato come testo, e stampa solo i casi in cui compare la sottostringa `picoCTF`, scartando automaticamente i tentativi che non sono nemmeno decodificabili come testo valido.

L'unico valore che ha prodotto un output leggibile è stato `key = 143`.
#### Flag
`picoCTF{dh_s3cr3t_6dad09cd}`
#### Lezioni apprese
a sicurezza di un intero sistema è determinata dall'anello più debole della catena, non dalla parte più complessa. Diffie-Hellman con un primo a 1048 bit è, in teoria, sicuro contro un attaccante che deve risolvere il logaritmo discreto. Ma se il segreto condiviso che ne risulta viene poi ridotto in modo grossolano tutto il lavoro fatto a monte diventa inutile. L