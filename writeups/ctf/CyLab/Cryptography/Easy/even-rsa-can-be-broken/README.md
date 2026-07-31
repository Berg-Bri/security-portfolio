#### 🛠️Tool usati

- [[tools/netcat|netcat]]
- Python

#### 🧩Descrizione

_"Questo servizio fornisce un flag criptato. Puoi decifrarlo con solo N & e?"_

#### 🔍Analisi / Ricognizione

La macchina fornisce uno script Python che genera una coppia di chiavi RSA a 1024 bit tramite una funzione `get_primes()` importata da un modulo `setup.py` non visibile, cifra la flag con la chiave pubblica e restituisce `N`, `e` e il ciphertext. La challenge include tre hint espliciti che indirizzano verso un problema di randomness debole nella generazione dei primi, suggerendo di confrontare `N` tra più richieste.

Un primo tentativo di fattorizzazione diretta di un singolo `N`, per quanto `N` risultasse pari (quindi apparentemente con `p=2`), ha prodotto un risultato illeggibile — segno che il singolo valore trascritto a mano conteneva probabilmente un errore, dato quanto sono lunghi questi numeri da copiare manualmente da terminale.

Seguendo gli hint, ho connesso al servizio più volte con `nc`, raccogliendo `N`, `e` e ciphertext da tre sessioni distinte. Calcolando il massimo comun divisore tra le coppie di `N` ottenute, il risultato è stato costantemente 2 per tutte le combinazioni testate:

```python
import math
print(math.gcd(N1, N2))  # 2
print(math.gcd(N1, N3))  # 2
print(math.gcd(N2, N3))  # 2
```

Un gcd sempre pari a 2 tra `N` generati in sessioni indipendenti conferma che il servizio usa sempre `p=2` come uno dei due fattori primi, ad ogni singola generazione della chiave — non un errore di trascrizione, ma un vero bug nella funzione `get_primes()` del setup, coerente con l'hint "quanto ci fidiamo della randomness?".

#### ⚙️Sfruttamento

Conoscendo `p=2`, il secondo fattore si ricava immediatamente per semplice divisione:

```python
p = 2
q = N // 2
```

Da qui si ricostruisce la chiave privata esattamente come nell'RSA standard:

```python
e = 65537
phi = (p - 1) * (q - 1)   # = q - 1, dato che p-1 = 1
d = pow(e, -1, phi)       # inverso modulare nativo, Python 3.8+

m = pow(c, d, N)
flag_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
print(flag_bytes)
```

Ho scritto lo script sopra in Python, usando `pow(e, -1, phi)` per l'inverso modulare e `int.to_bytes()` al posto di `long_to_bytes()`.

Eseguendo lo script con i valori reali di `N` e ciphertext ottenuti da una connessione, ho ottenuto la flag in chiaro.

#### 🚩Flag

`picoCTF{tw0_1$_pr!m305af7255}`

#### 💡Lezioni apprese

La sicurezza di RSA dipende interamente dalla qualità della generazione dei numeri primi, non solo dalla dimensione della chiave dichiarata. Una chiave "a 1024 bit" può sembrare sicura sulla carta, ma se uno dei due fattori primi è fisso o prevedibile (nel caso estremo, addirittura `p=2`), l'intero schema crolla immediatamente, indipendentemente da quanto sia grande `N`.