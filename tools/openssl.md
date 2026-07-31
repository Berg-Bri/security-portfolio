#### 🛠️Cos'è

`openssl` è una libreria e tool a riga di comando per operazioni crittografiche: generazione e gestione di chiavi/certificati, cifratura/decifratura, hashing, ispezione di connessioni SSL/TLS. È lo strumento standard per lavorare con crittografia asimmetrica (RSA, ECC) e simmetrica da terminale.

#### 💻Gestione chiavi e certificati

**Generare una coppia di chiavi RSA:**

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

**Vedere i dettagli di una chiave privata:**

```bash
openssl rsa -in private.pem -text -noout
```

**Vedere i dettagli di un certificato:**

```bash
openssl x509 -in cert.pem -text -noout
```

#### 🔐Cifratura/decifratura RSA

```bash
openssl pkeyutl -decrypt -inkey private.pem -in flag.enc -out output.txt
openssl pkeyutl -encrypt -inkey public.pem -pubin -in message.txt -out message.enc
```

#### 🧮Hashing

```bash
openssl dgst -sha256 file.txt
openssl dgst -md5 file.txt
```

#### 🔒Cifratura simmetrica

```bash
# Cifrare con AES-256-CBC (chiede la password interattivamente)
openssl enc -aes-256-cbc -salt -in file.txt -out file.enc

# Decifrare
openssl enc -aes-256-cbc -d -in file.enc -out file.txt
```

#### 🌐Ispezionare una connessione SSL/TLS

```bash
openssl s_client -connect host:443
```

Utile per vedere il certificato presentato da un server, la catena di certificazione, e i dettagli dell'handshake TLS — comodo in fase di ricognizione su servizi HTTPS.

#### 🔁Workflow tipico in CTF: decifratura con chiave privata recuperata

```bash
# 1. Hai recuperato una chiave privata (es. da metadati, file esposto, ecc.)
# 2. Salvala come file .pem
cp chiave_estratta.txt private.pem

# 3. Decifra il file cifrato con quella chiave
openssl pkeyutl -decrypt -inkey private.pem -in flag.enc -out output.txt
cat output.txt
```

#### ⚠️Attenzione

Da OpenSSL 3.0 in poi, il comando **`rsautl` è deprecato** in favore di **`pkeyutl`** — funzionano in modo simile ma `rsautl` può stampare un avviso di deprecazione o, in futuro, essere rimosso del tutto. Se trovi guide/writeup più vecchi che usano:

```bash
openssl rsautl -decrypt -inkey private.pem -in flag.enc -out output.txt
```

l'equivalente moderno è:

```bash
openssl pkeyutl -decrypt -inkey private.pem -in flag.enc -out output.txt
```

Su Kali (basato su Debian, con OpenSSL 3.x) conviene abituarsi direttamente a `pkeyutl`.