#### Cos'è RSA

Algoritmo di crittografia **asimmetrica**, basato sulla difficoltà computazionale di fattorizzare il prodotto di due numeri primi grandi. Usa una coppia di chiavi: una **pubblica** (per cifrare/verificare) e una **privata** (per decifrare/firmare), matematicamente collegate ma computazionalmente impossibile derivare l'una dall'altra se i parametri sono scelti correttamente.

---
#### Generazione delle chiavi — cosa significano i parametri

**p, q**: due numeri primi grandi, generati casualmente, mantenuti segreti. La sicurezza di RSA dipende interamente dal fatto che siano scelti in modo **veramente casuale** e **sufficientemente grandi**.

**N (modulo)**: N=p⋅qN = p \cdot q N=p⋅q, pubblico. È il numero che compare nella chiave pubblica e privata.

**ϕ(N)\phi(N) ϕ(N) (funzione di Eulero)**: ϕ(N)=(p−1)(q−1)\phi(N) = (p-1)(q-1) ϕ(N)=(p−1)(q−1), il numero di interi minori di N e coprimi con N. Resta segreto (deriva da p, q).

**e (esponente pubblico)**: scelto tale che 1<e<ϕ(N)1 < e < \phi(N) 1<e<ϕ(N) e gcd⁡(e,ϕ(N))=1\gcd(e, \phi(N)) = 1 gcd(e,ϕ(N))=1. Solitamente fisso e standard: e=65537e = 65537 e=65537 (buon compromesso tra sicurezza e velocità).

**d (esponente privato)**: d=e−1mod  ϕ(N)d = e^{-1} \mod \phi(N) d=e−1modϕ(N), l'inverso moltiplicativo di e modulo ϕ(N)\phi(N) ϕ(N).

**Chiave pubblica**: (N,e)(N, e) (N,e) — condivisa con chiunque. **Chiave privata**: (N,d)(N, d) (N,d) (o equivalentemente p,q,dp, q, d p,q,d) — mai condivisa.

---
#### Cifratura e decifratura

Cifratura: c=memod  N\text{Cifratura: } c = m^e \mod NCifratura: c=memodN Decifratura: m=cdmod  N\text{Decifratura: } m = c^d \mod NDecifratura: m=cdmodN

Funziona perché, per costruzione, med≡m(modN)m^{ed} \equiv m \pmod N med≡m(modN) — proprietà garantita dal teorema di Eulero-Fermat, grazie alla relazione ed≡1(modϕ(N))ed \equiv 1 \pmod{\phi(N)} ed≡1(modϕ(N)).

---
#### Perché RSA è sicuro (in teoria)

Un attaccante che vede solo la chiave pubblica (N,e)(N, e) (N,e) dovrebbe, per calcolare dd d, prima calcolare ϕ(N)\phi(N) ϕ(N) — che richiede conoscere pp p e qq q. **Fattorizzare N** (risalire a p,qp, q p,q partendo solo dal loro prodotto) è un problema computazionalmente difficile per numeri sufficientemente grandi (tipicamente 2048+ bit oggi), anche con i computer più potenti disponibili.

---
## Attacchi comuni contro implementazioni deboli di RSA

**Fattori primi deboli/prevedibili**: se pp p o qq q sono generati con poca entropia (randomness debole), diventano fattorizzabili facilmente. Caso estremo: uno dei due fattori è un numero piccolo/fisso (es. p=2p=2 p=2) — basta una divisione, non serve alcun attacco sofisticato.

**Common factor attack (fattori condivisi tra chiavi diverse)**: se due chiavi RSA generate dallo stesso sistema (con RNG debole) condividono accidentalmente un fattore primo, si può calcolare gcd⁡(N1,N2)\gcd(N_1, N_2) gcd(N1​,N2​) per trovarlo immediatamente:

N1=p⋅q1,N2=p⋅q2⇒gcd⁡(N1,N2)=pN_1 = p \cdot q_1, \quad N_2 = p \cdot q_2 \quad \Rightarrow \quad \gcd(N_1, N_2) = pN1​=p⋅q1​,N2​=p⋅q2​⇒gcd(N1​,N2​)=p

**p e q troppo vicini tra loro (Fermat factorization)**: se ∣p−q∣|p-q| ∣p−q∣ è piccolo, NN N si fattorizza rapidamente esprimendolo come differenza di quadrati.

**e troppo piccolo con messaggio corto (attacco di Håstad)**: se ee e è piccolo (es. e=3e=3 e=3) e il messaggio mm m è abbastanza corto che me<Nm^e < N me<N, non avviene alcuna riduzione modulare — basta calcolare la radice e-esima intera del ciphertext.

**Riutilizzo dello stesso modulo N con e diversi (common modulus attack)**: se lo stesso messaggio viene cifrato con la stessa NN N ma due esponenti pubblici diversi e coprimi tra loro, si può recuperare il messaggio originale senza fattorizzare N, usando l'algoritmo di Euclide esteso.

**Padding assente o debole**: RSA "puro" (senza OAEP/PKCS#1) su messaggi brevi o strutturati è vulnerabile a vari attacchi (incluso Håstad, o attacchi di malleabilità).

---
## Tabella riassuntiva vulnerabilità

|Vulnerabilità|Causa|Come si sfrutta|
|---|---|---|
|Fattore primo fisso/debole (es. p=2)|RNG rotto/prevedibile|Divisione diretta di N|
|Fattori condivisi tra chiavi diverse|Poca entropia nel RNG|gcd⁡(N1,N2)\gcd(N_1, N_2) gcd(N1​,N2​)|
|p, q troppo vicini|Generazione primi non abbastanza casuale|Fermat factorization|
|e piccolo + messaggio corto|Nessun padding, e basso|Radice e-esima intera (Håstad)|
|Stesso N, e diversi coprimi|Riutilizzo del modulo|Common modulus attack|
