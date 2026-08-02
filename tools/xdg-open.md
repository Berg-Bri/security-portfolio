##### 🛠️ Cos'è

`xdg-open` apre un file, una cartella o un URL con l'applicazione predefinita associata dal sistema, l'equivalente da riga di comando del doppio click "apri con l'app giusta".

##### 💻 Uso base

```bash
xdg-open file.png
```

##### 🧭 Funzionalità principali

Apre immagini con il visualizzatore predefinito, PDF con il lettore predefinito, URL con il browser predefinito — sceglie l'app in base al tipo di file/MIME type.

Funziona anche con cartelle (le apre nel file manager predefinito) e con URL: `xdg-open https://example.com`.

##### 🔁 Workflow tipico

1. Hai un file di cui non vuoi specificare manualmente il visualizzatore.
2. `xdg-open nomefile`.
3. Il sistema apre l'app associata a quel tipo di file.

##### 💡 Suggerimenti pratici

Comodo nei CTF quando estrai un file e non sai ancora di che tipo si tratta — a volte conviene comunque controllare prima con `file nomefile`.

Su una VM senza ambiente grafico (headless), `xdg-open` non ha nulla da aprire: serve un'interfaccia grafica sottostante.

##### ⚠️ Attenzione / Problemi comuni

Non aprire file non fidati con l'app predefinita senza sapere cosa sono: se un file è malevolo camuffato da immagine/documento, l'app che lo apre potrebbe essere vulnerabile — meglio identificare il vero tipo di file (`file`, `exiftool`) prima di aprirlo alla cieca.