#### 🛠️Cos'è

Crea o inverte un dump esadecimale di un file o di uno stream. Utile sia per ispezionare byte grezzi sia per decodificare stringhe hex.

#### 💻Comandi principali

**Visualizzare un file in hex:**

```bash
xxd file.bin
```

**Decodificare una stringa hex in testo/binario (l'operazione usata nella challenge):**

```bash
echo "7069636F4354467B..." | xxd -r -p
```

- `-r` → modalità reverse (da hex a binario)
- `-p` → formato "plain", cioè solo i byte in sequenza senza offset/colonna ASCII a lato (necessario quando l'input è una stringa hex pura, non un dump completo di xxd)

**Convertire binario in hex plain:**

```bash
xxd -p file.bin
```