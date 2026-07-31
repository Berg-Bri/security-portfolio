#### 🧠Cos'è
La steganografia è l'arte di nascondere l'esistenza stessa di un messaggio, non solo il suo contenuto. Il nome deriva dal greco _steganos_ (coperto, nascosto) e _graphein_ (scrittura).

La differenza fondamentale con la crittografia è concettuale:

- **Crittografia**: rendere un messaggio illeggibile a chi non ha la chiave, ma è evidente che un messaggio cifrato esiste
- **Steganografia**: nascondere il fatto stesso che ci sia un messaggio; chi osserva il "contenitore" non deve sospettare nulla

Le due tecniche non si escludono: spesso un messaggio viene prima cifrato e poi nascosto steganograficamente, per avere entrambe le protezioni.

#### 🧩Componenti di un sistema steganografico

- **Messaggio (payload)**: il dato da nascondere.
- **Copertura (carrier/cover)**: il file "innocuo" che ospiterà il messaggio (immagine, audio, video, testo, eseguibile...).
- **Stego-oggetto**: il risultato finale, cioè la copertura con il messaggio incorporato.
- **Chiave (opzionale)**: un parametro che stabilisce come/dove il messaggio è stato inserito, necessario per l'estrazione.

#### 🖼️Steganografia su immagini

**LSB (Least Significant Bit)**: si sostituisce il bit meno significativo di ogni byte (es. di ogni canale colore di ogni pixel) con un bit del messaggio. Poiché quel bit ha un peso minimo sul valore del colore, la modifica è impercettibile all'occhio umano ma recuperabile bit per bit da chi sa dove cercare. È la tecnica più comune nelle CTF (vedi `zsteg`).

Varianti che aumentano la capacità o la resistenza all'analisi:

- uso di più bit per byte (2, 3... bit-plane più alti, a scapito della qualità visiva)
- scelta di canali specifici (solo blu, solo alpha...) o ordini non standard
- pattern di scansione non sequenziali (per rendere l'estrazione più difficile senza la chiave)

**Manipolazione della palette**: nelle immagini indicizzate, il messaggio viene codificato nell'ordine dei colori della palette anziché nei pixel.

**Dati appesi o embedded**: un file completo (zip, altro binario) viene semplicemente concatenato dopo la fine "logica" del file immagine (es. dopo il chunk `IEND` di un PNG). Il visualizzatore immagini ignora i dati in eccesso, ma sono comunque presenti nel file. Si individuano con `binwalk` o ispezionando gli ultimi byte con `xxd`/`hexdump`.

#### 🔊Steganografia su audio

Tecniche analoghe all'LSB ma sui campioni audio (es. WAV non compresso), oppure nascondendo dati nello spettro di frequenza (steganografia nel dominio della frequenza), meno percettibile all'orecchio.

#### 📝Steganografia su testo

- Spazi bianchi extra o invisibili (Unicode zero-width characters) tra parole.
- Scelta di sinonimi o pattern linguistici che codificano bit.
- Whitespace steganography classica: sequenze di spazi/tab a fine riga.

#### 🌐Steganografia di rete (network steganography)

Nasconde dati in campi normalmente inutilizzati o poco osservati dei protocolli di rete (es. campi opzionali TCP/IP, timing dei pacchetti).

#### 🔬Steganalisi (rilevare la steganografia)

L'analisi statistica dei file può rivelare tracce di manipolazione:

- distribuzioni di colore anomale (istogrammi con pattern innaturali dopo modifiche LSB)
- differenze tra dimensione attesa e reale del file
- entropia anomala in certe regioni (dati cifrati/compressi hanno entropia alta e uniforme, diversa da quella naturale di un'immagine)

Strumenti pratici usati in ambito CTF per la steganalisi: `zsteg` (LSB su PNG/BMP), `stegsolve` (ispezione visiva dei bit-plane), `binwalk` (file nascosti/appesi), `exiftool` (metadati), `steghide`/`stegseek` (per JPEG/BMP/WAV/AU con embedding basato su password).