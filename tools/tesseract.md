#### 🛠️Cos'è

Motore OCR (Optical Character Recognition) open source. Estrae testo leggibile da immagini — utile quando dati o flag sono "stampati" graficamente nei pixel di un'immagine invece che come testo selezionabile.

#### 💻Uso base

```bash
tesseract input.png output
cat output.txt
```

Il primo argomento è l'immagine di input, il secondo è il nome base del file di output (`.txt` viene aggiunto automaticamente).

#### 🎯Migliorare l'accuratezza

Se il testo è piccolo, sgranato o l'OCR sbaglia caratteri:

```bash
# Ritagliare solo l'area con il testo
convert input.png -crop WxH+X+Y -resize 300% crop.png

# Aumentare il contrasto in bianco e nero
convert crop.png -colorspace Gray -threshold 50% clean.png

tesseract clean.png output
```

#### 🔠Limitare il set di caratteri riconosciuti

Utile per stringhe hex, solo `0-9A-F`:

```bash
tesseract input.png output -c tessedit_char_whitelist=0123456789ABCDEF
```

#### 🕵️Nel contesto CTF

L'OCR evita la trascrizione manuale di stringhe lunghe da un'immagine, processo lento e a rischio di errori, specialmente con stringhe esadecimali dove un singolo carattere sbagliato invalida l'intera decodifica.