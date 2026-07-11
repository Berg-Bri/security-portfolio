##### Diffie-Hellman e il significato di g, p, a, b

Lo scambio Diffie-Hellman permette a due parti di concordare un segreto condiviso comunicando su un canale pubblico, senza mai trasmettere il segreto stesso. Nello script della challenge i parametri hanno questo ruolo:

**g** è il generatore, un numero pubblico e fisso (qui `g = 2`), usato come base per tutte le potenze modulari.

**p** è un numero primo grande e pubblico (qui generato a 1048 bit con `getPrime`), che definisce il gruppo moltiplicativo su cui si lavora. Più `p` è grande, più è difficile calcolare il logaritmo discreto e quindi risalire ai segreti partendo dai valori pubblici.

**a** è il segreto del server, un numero casuale mai rivelato, da cui si calcola il valore pubblico `A = g^a mod p`.

**b** è il segreto del client, generato allo stesso modo, da cui si calcolerebbe `B = g^b mod p`.

**shared** è il segreto condiviso finale, calcolato da ciascuna parte come `A^b mod p` oppure `B^a mod p` — entrambi i calcoli danno lo stesso risultato per le proprietà matematiche dell'esponenziazione modulare, ma nessuno dei due lati deve mai conoscere il segreto dell'altro per arrivarci.

In teoria, un attaccante che vede solo `g`, `p` e `A` dovrebbe affrontare il problema del logaritmo discreto per risalire ad `a` — un problema computazionalmente difficile se `p` è abbastanza grande, esattamente come ripassato per l'esame di crittografia.