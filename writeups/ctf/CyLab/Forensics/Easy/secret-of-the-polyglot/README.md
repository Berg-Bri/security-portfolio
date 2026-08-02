##### 🛠️ Tool usati

- [xxd](../../../../../../tools/xxd.md)
- file
- Firefox

##### 🧩 Descrizione

_Il Network Operations Center (NOC) della tua istituzione locale ha individuato un file sospetto, ma sta ricevendo informazioni contrastanti sulla natura del file stesso. Ti hanno chiamato in qualità di esperto esterno per esaminare il file. Riesci a estrarre tutte le informazioni contenute in questo strano file?_

##### 🔍 Analisi / Ricognizione

Si viene reindirizzati a un PDF online contenente solo la parte finale della flag: `1n_pn9_&_pdf_90974127}`.

Il file fornito, `flag2of2-final.pdf`, ha però un'estensione ingannevole. Controllando i primi byte con `file` e `xxd`:

```bash
file flag2of2-final.pdf
flag2of2-final.pdf: PNG image data, 50 x 50, 8-bit/color RGBA, non-interlaced

xxd flag2of2-final.pdf | head -5
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

I primi byte corrispondono esattamente alla firma PNG (`89 50 4E 47 0D 0A 1A 0A`), posizionata proprio all'inizio del file: il "PDF" è in realtà un'immagine PNG rinominata.

##### ⚙️ Sfruttamento

Ho copiato il file dandogli l'estensione corretta:

```bash
cp flag2of2-final.pdf flag2of2-final.png
```

Aprendolo con il visualizzatore immagini di default ho ottenuto un errore ("Unsupported image format"). Il file, oltre a essere un PNG valido, conteneva probabilmente anche dati residui del formato PDF originale (un vero file "polyglot", coerente col nome della challenge), dati che un decoder PNG rigoroso rifiuta, ma che parser più tolleranti ignorano tranquillamente dopo il chunk `IEND`.

Aprendo il file con Firefox, molto più permissivo nel parsing dei PNG, l'immagine si è visualizzata correttamente, rivelando la prima metà della flag scritta al suo interno: `picoCTF{f13u3n7_`.

Unendo questa alla seconda metà trovata nel PDF online, si ottiene la flag completa.

##### 🚩 Flag

picoCTF{f1u3n7_1n_pn9_&\_pdf_90974127}

##### 💡 Lezioni apprese

L'estensione di un file non garantisce nulla sul suo contenuto reale: va sempre verificata con `file`/`xxd` guardando i magic bytes, specialmente quando una challenge esplicitamente parla di file "polyglot" o dà informazioni contrastanti sulla natura del file.

Non tutti i visualizzatori/parser si comportano allo stesso modo davanti a un file leggermente "non conforme": strumenti con decoder rigorosi (come alcuni visualizzatori immagini minimali) si rifiutano di aprire un file se trovano dati inaspettati oltre la fine della struttura attesa, mentre software più maturi (Firefox, GIMP) leggono solo i dati fino al marcatore di fine formato (`IEND` per i PNG) e ignorano il resto — ed è proprio questa tolleranza a rendere possibile la tecnica dei polyglot: due formati diversi che convivono nello stesso file, ciascuno leggibile ignorando la parte che appartiene all'altro.

