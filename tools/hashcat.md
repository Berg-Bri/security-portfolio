#### 🛠️Cos'è

Tool a riga di comando per il **recupero/cracking di password** a partire dal loro hash. Sfrutta CPU e/o GPU per calcolare velocemente l'hash di enormi quantità di candidati e confrontarli con l'hash target, fino a trovare una corrispondenza.

#### 💻Sintassi base

```bash
hashcat -m <tipo_hash> -a <tipo_attacco> hash.txt wordlist.txt
```

- **`-m`**: identifica l'algoritmo di hash da craccare (es. MD5, SHA1, SHA256...)
- **`-a`**: identifica la modalità di attacco (dizionario, bruteforce, mask, ecc.)
- **`hash.txt`**: file con l'hash (o gli hash, uno per riga) da craccare
- **`wordlist.txt`**: la lista di password candidate da provare

#### 🔢Come scegliere `-m` (modulo/algoritmo)

Il modo più rapido è contare i caratteri esadecimali dell'hash:

|Lunghezza hash|Algoritmo|Modulo `-m`|
|---|---|---|
|32 caratteri|MD5|`0`|
|40 caratteri|SHA1|`100`|
|64 caratteri|SHA256|`1400`|
|128 caratteri|SHA512|`1700`|

`es:` per contare i caratteri direttamente da terminale:

```bash
echo -n "482c811da5d5b4bc6d497ffa98491e38" | wc -c
```

Se non sei sicuro dell'algoritmo, puoi anche lasciare che sia hashcat a suggerirlo:

```bash
hashcat --identify hash.txt
```

#### 🎯Come scegliere `-a` (tipo di attacco)

|Codice|Nome|Cosa fa|
|---|---|---|
|`0`|Straight (dizionario)|Prova ogni parola di una wordlist così com'è|
|`1`|Combination|Combina parole da due wordlist diverse|
|`3`|Brute-force / Mask|Genera tutte le combinazioni possibili secondo un pattern (es. solo numeri, 6 caratteri)|
|`6` / `7`|Hybrid|Combina wordlist + mask (es. parola + numeri finali)|

Per la maggior parte delle CTF con password "deboli ma non banalissime", l'attacco **`-a 0`** con la wordlist **rockyou.txt** è il primo tentativo standard.

#### ⚡Comandi essenziali

**Craccare un hash con dizionario:**

```bash
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

**Vedere il risultato già trovato (senza rilanciare il crack):**

```bash
hashcat -m 0 hash.txt --show
```

**Forzare l'uso della CPU se non c'è GPU disponibile/riconosciuta:**

```bash
hashcat -m 0 -a 0 hash.txt rockyou.txt --force
```

#### 🔁Workflow tipico in una CTF

```bash
echo "HASH_DA_CRACCARE" > hash.txt
hashcat -m <modulo> -a 0 hash.txt /usr/share/wordlists/rockyou.txt
hashcat -m <modulo> hash.txt --show
```

#### 🔀Alternative equivalenti

|Tool|Quando preferirlo|
|---|---|
|**John the Ripper**|Sintassi diversa (`--format=`), utile se hashcat non riconosce un formato particolare|
|**Script Python (hashlib)**|Utile a scopo didattico, per capire/mostrare cosa succede byte per byte, ma molto più lento su wordlist grandi|

`Nota`: hashcat resta lo strumento standard del settore, usato anche in ambito professionale (penetration test, incident response, audit password aziendali).