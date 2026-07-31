#### 🧠Cos'è

Un hash è il risultato dell'applicazione di una **funzione di hash** a un input di lunghezza arbitraria (un file, una password, un messaggio), che produce sempre un output di **lunghezza fissa**, chiamato **digest**.

`es:` SHA256 produce sempre un digest di 256 bit (64 caratteri esadecimali), sia che l'input sia una parola sia che sia un file da 10 GB.

#### 🔐Proprietà fondamentali di un hash sicuro

**Deterministico**: lo stesso input produce sempre esattamente lo stesso hash.

**Effetto valanga**: cambiare anche un solo bit dell'input produce un hash completamente diverso e imprevedibile. `es:` cambiare un solo punto in un testo stravolge completamente il digest risultante.

**One-way (non invertibile)**: dato un hash, non deve essere computazionalmente fattibile risalire all'input originale. Questo è il motivo per cui gli hash si usano per le password: anche chi ha accesso al database non può leggere le password reali degli utenti.

**Resistenza alle collisioni**: non deve essere fattibile trovare due input diversi che producano lo stesso hash. Una collisione trovata rompe questa proprietà (è successo storicamente con MD5 e, più recentemente, con SHA1).

#### 🔀Algoritmi principali

|Algoritmo|Lunghezza digest|Stato attuale|
|---|---|---|
|MD5|128 bit (32 hex)|Rotto (collisioni pratiche), da non usare per sicurezza|
|SHA1|160 bit (40 hex)|Rotto (collisione dimostrata da Google nel 2017), deprecato|
|SHA256|256 bit (64 hex)|Sicuro, ampiamente usato oggi (famiglia SHA2)|
|SHA512|512 bit (128 hex)|Sicuro, variante più lunga di SHA2|

#### 📌Casi d'uso comuni

**Verifica di integrità**: calcolando l'hash di un file scaricato e confrontandolo con l'hash pubblicato dalla fonte, si può verificare che il file non sia stato alterato/corrotto in transito.

**Archiviazione delle password**: invece di salvare la password in chiaro, si salva il suo hash. Al login, si ricalcola l'hash della password inserita e si confronta con quello salvato — se combaciano, la password è corretta, senza che il sistema debba mai conoscere/memorizzare la password reale.

**Firme digitali**: si firma l'hash di un documento (più piccolo e veloce da elaborare) invece del documento intero, garantendo comunque integrità e autenticità.

#### ⚠️Attenzione in ambito sicurezza

Un algoritmo di hash **crittograficamente robusto** (es. SHA256, senza collisioni note) protegge comunque **solo l'algoritmo**, non la scelta della password — questo è il punto centrale dimostrato nelle challenge di cracking.

Se la password è debole (comune, presente in dizionari/wordlist come rockyou), un attaccante non ha bisogno di violare l'algoritmo di hash: gli basta calcolare l'hash di milioni di password comuni e cercare una corrispondenza con l'hash rubato. Questo attacco si chiama **dictionary attack** (attacco a dizionario), ed è indipendente dalla robustezza matematica dell'algoritmo usato.

```
Password debole + hash fortissimo  →  comunque craccabile (dictionary attack)
Password forte  + hash debole      →  comunque craccabile (collisioni/attacchi noti sull'algoritmo)
Password forte  + hash forte       →  sicuro
```

#### 🧂Hashing delle password: perché non MD5/SHA (bcrypt, scrypt, Argon2)

MD5, SHA1, SHA256 sono progettati per essere **veloci** — ottimi per verificare l'integrità di un file, pessimi per proteggere le password, perché la stessa velocità permette a un attaccante di provare miliardi di combinazioni al secondo (specialmente con GPU dedicate, come fa hashcat).

Per le password si usano invece funzioni **volutamente lente** e con **salt** (un valore casuale univoco per ogni utente, aggiunto alla password prima dell'hashing):

- **bcrypt**: standard consolidato, include il salt automaticamente
- **scrypt**: pensato per essere costoso anche in termini di memoria, non solo di tempo CPU
- **Argon2**: vincitore della Password Hashing Competition, oggi considerato lo standard più moderno

Il salt in particolare serve a impedire l'uso di **rainbow table** (tabelle precalcolate hash→password): con un salt diverso per ogni utente, anche due utenti con la stessa password ottengono hash completamente diversi.