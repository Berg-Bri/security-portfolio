##### 🛠️ Cos'è

`sha256sum` è un'utility a riga di comando (parte di GNU coreutils) che calcola l'hash SHA-256 di uno o più file, usata per verificarne l'integrità o l'autenticità confrontando l'hash calcolato con uno di riferimento fornito.

##### 💻 Uso base

```bash
sha256sum file.txt
```

##### 🧭 Funzionalità principali

Calcolo dell'hash su più file in un solo comando, con supporto ai wildcard (es. `sha256sum files/*`).

Modalità di verifica automatica: `sha256sum -c checksums.txt` confronta una lista di file con gli hash attesi contenuti in un file, stampando `OK`/`FAILED` per ciascuno.

Output in formato `hash nomefile`, facilmente filtrabile con `grep`/`awk`.

##### 🔁 Workflow tipico

1. Ottieni l'hash di riferimento (dalla challenge o da una fonte ufficiale).
2. Calcola l'hash dei file candidati: `sha256sum cartella/*`.
3. Filtra l'output con `grep` cercando il prefisso/hash noto, invece di confrontare a occhio.
4. Se combacia, il file è verificato.

##### 💡 Suggerimenti pratici

Con molti file candidati, è più veloce lanciare `sha256sum` su tutti insieme con un wildcard e poi filtrare l'output, piuttosto che controllarli uno per uno.

Esistono varianti identiche per altri algoritmi: `md5sum`, `sha1sum`, `sha512sum`.

##### ⚠️ Attenzione / Problemi comuni

Un hash che combacia garantisce solo che il file non sia stato alterato rispetto al riferimento — non dice nulla sull'affidabilità della fonte da cui arriva l'hash atteso stesso.

Attenzione a spazi o caratteri extra quando si copia un hash a mano per confrontarlo: un errore di trascrizione può far sembrare "diverso" un hash che in realtà è corretto.