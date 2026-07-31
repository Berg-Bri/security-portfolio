#### 🛠️Cos'è

Codifica/decodifica dati in formato Base64, usato per convertire testo o dati binari in una rappresentazione ASCII stampabile (e viceversa).

#### 💻Uso base

```bash
# Decodificare un file Base64
base64 --decode logs.txt > logs.png

# Codificare un file
base64 file_originale > file_codificato.txt

# Da stringa diretta
echo "SGVsbG8gV29ybGQ=" | base64 --decode
```

#### 💡Suggerimenti pratici

- Nei CTF, Base64 è spesso il primo livello di offuscamento da riconoscere: si individua facilmente perché usa solo caratteri `A-Z`, `a-z`, `0-9`, `+`, `/` e padding con `=`.