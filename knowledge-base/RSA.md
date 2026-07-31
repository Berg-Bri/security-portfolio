#### 🧠Cos'è 

Algoritmo di crittografia **asimmetrica**, basato sulla difficoltà computazionale di fattorizzare il prodotto di due numeri primi grandi. Usa una coppia di chiavi: una **pubblica** (per cifrare/verificare) e una **privata** (per decifrare/firmare), matematicamente collegate ma computazionalmente impossibile derivare l'una dall'altra se i parametri sono scelti correttamente.

#### 🔑Generazione delle chiavi — cosa significano i parametri

|Simbolo|Ruolo|Note|
|---|---|---|
|$p$, $q$|Due numeri primi grandi, generati casualmente|mantenuti segreti; la sicurezza di RSA dipende interamente dal fatto che siano scelti in modo **veramente casuale** e **sufficientemente grandi**|
|$N$ (modulo)|$N = p \cdot q$|pubblico, compare sia nella chiave pubblica che in quella privata|
|$\phi(N)$ (funzione di Eulero)|$\phi(N) = (p-1)(q-1)$|numero di interi minori di $N$ e coprimi con $N$; resta segreto (deriva da $p$, $q$)|
|$e$ (esponente pubblico)|$1 < e < \phi(N)$, con $\gcd(e, \phi(N)) = 1$|solitamente fisso e standard: $e = 65537$ (buon compromesso tra sicurezza e velocità)|
|$d$ (esponente privato)|$d = e^{-1} \mod \phi(N)$|l'inverso moltiplicativo di $e$ modulo $\phi(N)$|

**Chiave pubblica**: $(N, e)$ — condivisa con chiunque. **Chiave privata**: $(N, d)$ (o equivalentemente $p, q, d$) — mai condivisa.

#### 🔄Cifratura e decifratura

Cifratura: $c = m^e \mod N$ Decifratura: $m = c^d \mod N$

Funziona perché, per costruzione, $m^{ed} \equiv m \pmod N$ — proprietà garantita dal teorema di Eulero-Fermat, grazie alla relazione $ed \equiv 1 \pmod{\phi(N)}$.

#### 🛡️Perché RSA è sicuro (in teoria)

Un attaccante che vede solo la chiave pubblica $(N, e)$ dovrebbe, per calcolare $d$, prima calcolare $\phi(N)$ — che richiede conoscere $p$ e $q$. **Fattorizzare $N$** (risalire a $p, q$ partendo solo dal loro prodotto) è un problema computazionalmente difficile per numeri sufficientemente grandi (tipicamente 2048+ bit oggi), anche con i computer più potenti disponibili.

#### ⚠️Attacchi comuni contro implementazioni deboli

**Fattori primi deboli/prevedibili**: se $p$ o $q$ sono generati con poca entropia (randomness debole), diventano fattorizzabili facilmente. Caso estremo: uno dei due fattori è un numero piccolo/fisso (es. $p = 2$) — basta una divisione, non serve alcun attacco sofisticato.

**Common factor attack (fattori condivisi tra chiavi diverse)**: se due chiavi RSA generate dallo stesso sistema (con RNG debole) condividono accidentalmente un fattore primo, si può calcolare $\gcd(N_1, N_2)$ per trovarlo immediatamente:

$$N_1 = p \cdot q_1, \quad N_2 = p \cdot q_2 \quad \Rightarrow \quad \gcd(N_1, N_2) = p$$

**p e q troppo vicini tra loro (Fermat factorization)**: se $|p - q|$ è piccolo, $N$ si fattorizza rapidamente esprimendolo come differenza di quadrati.

**e troppo piccolo con messaggio corto (attacco di Håstad)**: se $e$ è piccolo (es. $e = 3$) e il messaggio $m$ è abbastanza corto che $m^e < N$, non avviene alcuna riduzione modulare — basta calcolare la radice $e$-esima intera del ciphertext.

**Riutilizzo dello stesso modulo N con e diversi (common modulus attack)**: se lo stesso messaggio viene cifrato con lo stesso $N$ ma due esponenti pubblici diversi e coprimi tra loro, si può recuperare il messaggio originale senza fattorizzare $N$, usando l'algoritmo di Euclide esteso.

**Padding assente o debole**: RSA "puro" (senza OAEP/PKCS#1) su messaggi brevi o strutturati è vulnerabile a vari attacchi (incluso Håstad, o attacchi di malleabilità).

#### 📊Tabella riassuntiva vulnerabilità

|Vulnerabilità|Causa|Come si sfrutta|
|---|---|---|
|Fattore primo fisso/debole (es. $p=2$)|RNG rotto/prevedibile|Divisione diretta di $N$|
|Fattori condivisi tra chiavi diverse|Poca entropia nel RNG|$\gcd(N_1, N_2)$|
|$p$, $q$ troppo vicini|Generazione primi non abbastanza casuale|Fermat factorization|
|$e$ piccolo + messaggio corto|Nessun padding, $e$ basso|Radice $e$-esima intera (Håstad)|
|Stesso $N$, $e$ diversi coprimi|Riutilizzo del modulo|Common modulus attack|
