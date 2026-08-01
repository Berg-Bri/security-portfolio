#### 🛠️Tool usati

- [netcat](../../../../../../tools/netcat.md)
- [hashcat](../../../../../../tools/hashcat.md)

#### 🧩Descrizione

_"Un'azienda ha memorizzato un messaggio segreto su un server che è stato violato a causa dell'amministratore utilizzando password debolmente hash. È possibile ottenere l'accesso al segreto memorizzato all'interno del server?"_

#### 🔍Analisi / Ricognizione

Ogni hash fornito ha una lunghezza diversa in caratteri esadecimali, ed è proprio la lunghezza a rivelare l'algoritmo usato, senza bisogno di altri indizi:

- 32 caratteri → MD5
- 40 caratteri → SHA1
- 64 caratteri → SHA256

La challenge fornisce gli hash uno alla volta, in ordine crescente di robustezza dell'algoritmo, ma il punto centrale resta lo stesso in tutti e tre i casi: la password sottostante è debole e presente nella wordlist rockyou, quindi craccabile a prescindere da quanto sia sicuro l'algoritmo di hash usato per proteggerla.

#### ⚙️Sfruttamento

Per ogni hash ricevuto, il procedimento è identico, cambia solo il modulo/algoritmo da specificare:

**Primo hash (MD5, 32 caratteri):**

```
482c811da5d5b4bc6d497ffa98491e38
```

```bash
echo "482c811da5d5b4bc6d497ffa98491e38" > hash.txt
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
hashcat -m 0 hash.txt --show
```

Password trovata: `password123`

**Secondo hash (SHA1, 40 caratteri):**

```
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
```

```bash
echo "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3" > hash2.txt
hashcat -m 100 -a 0 hash2.txt /usr/share/wordlists/rockyou.txt
hashcat -m 100 hash2.txt --show
```

Password trovata: `letmein`

**Terzo hash (SHA256, 64 caratteri):**

```
916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
```

```bash
echo "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745" > hash3.txt
hashcat -m 1400 -a 0 hash3.txt /usr/share/wordlists/rockyou.txt
hashcat -m 1400 hash3.txt --show
```

Password trovata: `qwerty098`

In tutti e tre i casi il tempo di cracking è pressoché immediato, perché la wordlist rockyou contiene già in chiaro tutte e tre le password: non serve alcuna forma di attacco più sofisticato (bruteforce puro, mask attack, rainbow table), un dizionario standard è più che sufficiente.

#### 🚩Flag

`picoCTF{UseStr0nGh@shEs&PaSswDs!_4c95d69f}`

#### 💡Lezioni apprese

Un algoritmo di hash robusto (fino a SHA256) non compensa una password debole: se la password è presente in una wordlist comune come rockyou, un dictionary attack la recupera in pochi secondi indipendentemente dalla robustezza matematica dell'algoritmo usato per proteggerla (vedi anche [[Hash]], sezione "Attenzione in ambito sicurezza"). La vera protezione richiede sia un algoritmo pensato per le password (bcrypt/scrypt/Argon2, con salt) sia una password non presente in dizionari comuni — mancarne anche solo una vanifica l'altra.