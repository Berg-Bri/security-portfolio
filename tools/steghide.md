#### 🛠️Cos'è

Steghide è un tool di steganografia open source che permette di nascondere dati arbitrari all'interno di file immagine o audio, senza alterarne in modo percepibile l'aspetto o il suono.

#### ⚙️Come funziona

Steghide sostituisce i bit meno significativi (LSB, least significant bit) dei dati del file copertura con i bit del payload da nascondere. Prima di scrivere i dati, applica compressione e cifratura (AES-128 di default) al contenuto da incorporare, poi seleziona in modo pseudo-casuale (basato sulla password) quali byte del file modificare — questo rende più difficile individuare i pattern nascosti rispetto a una sostituzione sequenziale banale.

#### 📁Formati supportati

JPEG, BMP, WAV e AU come file "copertura".

#### 💻Comandi principali

**Nascondere un file dentro un'immagine:**

```bash
steghide embed -cf img.jpg -ef secret.txt -p password
```

- `-cf` → file copertura
- `-ef` → file da nascondere
- `-p` → passphrase (opzionale ma consigliata)

**Verificare se un file contiene dati nascosti:**

```bash
steghide info img.jpg
```

Senza password mostra solo se la struttura è compatibile; con la password corretta restituisce nome, dimensione e tipo di crittografia del file nascosto.

**Estrarre il contenuto nascosto:**

```bash
steghide extract -sf img.jpg -p password
```

`-sf` indica lo "stego file", cioè il file che contiene i dati nascosti.

#### 🕵️Nel contesto CTF

Steghide è uno strumento ricorrente nelle challenge di forensics/steganografia proprio perché la sua firma è riconoscibile, ma l'estrazione richiede sempre una password. Da qui nascono spesso puzzle a più fasi in cui bisogna prima trovare la password nascosta altrove (metadata, stringhe, altre codifiche) prima di poter estrarre il payload.

#### ⚠️Limiti noti

La capacità di nascondere dati è limitata (dipende dalla dimensione del file copertura). Tool come `stegdetect` o `stegbreak` (bruteforce di password comuni) possono talvolta rilevare o craccare contenuti nascosti con steghide, soprattutto se la password è debole.