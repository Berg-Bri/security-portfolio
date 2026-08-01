#### 🧠Cos'è

Lo scambio Diffie-Hellman permette a due parti di concordare un segreto condiviso comunicando su un canale pubblico, senza mai trasmettere il segreto stesso.

#### 🔑Parametri e significato

Nello script della challenge [shared-secrets](../writeups/ctf/CyLab/Cryptography/Easy/shared-secrets/README.md) i parametri hanno questo ruolo:

|Simbolo|Ruolo|Note|
|---|---|---|
|`g`|Generatore, un numero pubblico e fisso|qui `g = 2`, usato come base per tutte le potenze modulari|
|`p`|Numero primo grande e pubblico|qui generato a 1048 bit con `getPrime`; definisce il gruppo moltiplicativo su cui si lavora|
|`a`|Segreto del server, numero casuale mai rivelato|da cui si calcola il valore pubblico `A = g^a mod p`|
|`b`|Segreto del client, generato allo stesso modo|da cui si calcolerebbe `B = g^b mod p`|
|`shared`|Segreto condiviso finale|calcolato come `A^b mod p` oppure `B^a mod p`|

#### ⚙️Come funziona

Entrambi i calcoli (`A^b mod p` e `B^a mod p`) danno lo stesso risultato per le proprietà matematiche dell'esponenziazione modulare, ma nessuno dei due lati deve mai conoscere il segreto dell'altro per arrivarci — è questo il punto centrale del protocollo: il segreto condiviso emerge senza che le parti si scambino mai `a` o `b`.

Più `p` è grande, più è difficile calcolare il logaritmo discreto e quindi risalire ai segreti partendo dai valori pubblici.

#### ⚠️Attenzione in ambito sicurezza

Un attaccante che vede solo `g`, `p` e `A` dovrebbe affrontare il **problema del logaritmo discreto** per risalire ad `a` — un problema computazionalmente difficile se `p` è abbastanza grande. La sicurezza dello scambio dipende interamente dalla dimensione (e dalla qualità) di `p`: valori piccoli o mal generati rendono il logaritmo discreto attaccabile in pratica.