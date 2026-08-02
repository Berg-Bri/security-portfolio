##### 🛠️ Cos'è

`zbarimg` è un'utility a riga di comando del pacchetto `zbar-tools` per decodificare codici a barre e QR code direttamente da immagini, senza bisogno di uno smartphone o di un'interfaccia grafica.

##### 💻 Uso base

```bash
zbarimg immagine.png
```

##### 🧭 Funzionalità principali

Riconosce sia QR code che diversi formati di codici a barre lineari (EAN, Code128, ecc.) nella stessa immagine.

Restituisce tipo di codice e contenuto decodificato, es. `QR-Code:testo_decodificato`.

Può processare più immagini in sequenza passandole come argomenti multipli.

##### 🔁 Workflow tipico

1. Ottieni/estrai un'immagine che sospetti contenga un QR code o codice a barre.
2. `zbarimg immagine.png`.
3. Leggi il contenuto decodificato direttamente dall'output.

##### 💡 Suggerimenti pratici

Se l'immagine ha bassa qualità o il codice è parzialmente danneggiato, il riconoscimento può fallire: aiuta ritagliare/ingrandire la sola porzione con il codice prima di ripassarla a `zbarimg`.

Utile in ambienti CTF headless/SSH dove non è possibile scansionare fisicamente il codice con un telefono.

##### ⚠️ Attenzione / Problemi comuni

Non riconosce tutti i formati esotici — per elaborazioni più custom può servire una libreria diversa (es. `pyzbar` in Python).

Immagini con QR code ruotati, molto piccoli o a basso contrasto possono richiedere un pre-processing (ridimensionamento, conversione in bianco e nero) prima che il riconoscimento funzioni.