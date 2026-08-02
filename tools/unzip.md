##### 🛠️Cos'è

`unzip` è un'utility a riga di comando per estrarre il contenuto di archivi in formato ZIP, uno dei formati di compressione/archiviazione più comuni.

##### 💻 Uso base

```bash
unzip archivio.zip
```

##### 🧭 Funzionalità principali

Estrazione in una cartella specifica con `-d`: `unzip archivio.zip -d cartella/`.

Elenco del contenuto senza estrarre: `unzip -l archivio.zip`.

Estrazione di un singolo file dall'archivio: `unzip archivio.zip nomefile`.

Test di integrità dell'archivio senza estrarre: `unzip -t archivio.zip`.

##### 🔁 Workflow tipico

1. Ricevi un file `.zip` dalla challenge.
2. `unzip -l archivio.zip` per vedere cosa contiene prima di estrarre.
3. `unzip archivio.zip` per estrarre.
4. Esplora la struttura estratta con `ls`/`find`.

##### 💡 Suggerimenti pratici

Se l'archivio è protetto da password: `unzip -P password archivio.zip` (attenzione: la password resta in chiaro nella history della shell).

`unzip -l` prima di estrarre è una buona abitudine, per controllare che l'archivio non contenga path assoluti o `../` che potrebbero scrivere fuori dalla cartella di destinazione.

##### ⚠️ Attenzione / Problemi comuni

Archivi ZIP costruiti ad arte possono sfruttare path traversal (Zip Slip) per scrivere file fuori dalla cartella di estrazione — non un problema nei CTF "amichevoli", ma buona pratica generale controllare sempre il contenuto con `-l` prima di estrarre da fonti non fidate.