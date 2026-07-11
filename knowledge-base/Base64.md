#### Cos'è
Base64 è uno schema di codifica binario-testo: converte dati binari (o testo) in una sequenza di caratteri ASCII stampabili, usando un alfabeto di 64 simboli (`A-Z`, `a-z`, `0-9`, `+`, `/`), con `=` come carattere di padding.

**Importante**: base64 non è crittografia. Non offre alcuna sicurezza: è solo una rappresentazione reversibile di byte come testo, decodificabile da chiunque senza bisogno di chiavi.

#### Come funziona
L'algoritmo prende gruppi di 3 byte (24 bit) di input e li riorganizza in 4 gruppi da 6 bit. Ogni gruppo da 6 bit (valore 0-63) viene mappato a uno dei 64 caratteri dell'alfabeto. Se il numero di byte in input non è multiplo di 3, l'output viene completato con uno o due `=` di padding.

Per questo motivo l'output è sempre circa il 33% più grande dell'input (4 caratteri di output ogni 3 byte di input).

#### Varianti dell'alfabeto

| Variante            | Caratteri 62/63 | Uso tipico                |
| ------------------- | --------------- | ------------------------- |
| Standard (RFC 4648) | `+` `/`         | file, MIME, dati generici |
| URL-safe            | `-` `_`         | URL, nomi file, JWT       |

#### Uso da riga di comando (Linux)

```bash
# Codificare una stringa
echo -n "ciao mondo" | base64
# Y2lhbyBtb25kbw==

# Decodificare
echo "Y2lhbyBtb25kbw==" | base64 -d
# ciao mondo

# Codificare/decodificare un file
base64 file.bin > file.b64
base64 -d file.b64 > file.bin
```

#### Python

```python
import base64

encoded = base64.b64encode(b"ciao mondo")
print(encoded)          # b'Y2lhbyBtb25kbw=='

decoded = base64.b64decode(encoded)
print(decoded)           # b'ciao mondo'

# variante URL-safe
url_encoded = base64.urlsafe_b64encode(b"ciao mondo")
```

#### Casi d'uso comuni

- Allegati email (MIME)
- Embedding di immagini in HTML/CSS (data URI, es. `data:image/png;base64,...`)
- Trasmissione di dati binari dentro JSON/XML
- Credenziali nell'header HTTP `Authorization: Basic <base64>`
- CTF e analisi malware: offuscamento leggero di stringhe o payload, spesso combinato con altre codifiche (hex, rot13, XOR) per aumentare la difficoltà di lettura a occhio

#### Attenzione in ambito sicurezza

Trovare una stringa in base64 in un payload, in un file di configurazione o in traffico di rete non significa che i dati siano protetti: la decodifica è immediata e non richiede alcuna chiave. Se vedi dati "cifrati" in base64, è quasi certo che si tratti solo di offuscamento, non di crittografia reale.