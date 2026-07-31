#### 🛠️Tool usati

Nessuno.

#### 🧩Descrizione

_"La crittografia può essere facile, sai cos'è ROT13?" `cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}`.

#### 🔍Analisi / Ricognizione

La flag cifrata viene fornita direttamente nella descrizione della challenge, senza bisogno di scaricare file o connettersi a un servizio remoto. L'indizio nel testo ("sai cos'è ROT13?") suggerisce già la tecnica di cifratura da usare.

#### ⚙️Sfruttamento

Sapendo che ogni flag di picoCTF inizia sempre con `picoCTF{`, è possibile confrontare la prima lettera cifrata (`c`) con quella attesa (`p`) e calcolare lo shift necessario: la distanza tra `c` e `p` nell'alfabeto è 13 posizioni, confermando che si tratta di un cifrario di Cesare con shift 13 — cioè ROT13, dove applicare la stessa trasformazione una seconda volta restituisce il testo in chiaro (ROT13 è la propria inversa, essendo 13 esattamente metà di un alfabeto di 26 lettere).

Applicando ROT13 alla stringa cifrata si ottiene la flag in chiaro.

#### 🚩Flag

`picoCTF{not_too_bad_of_a_problem}`

#### 💡Lezioni apprese

ROT13 non è un vero meccanismo di sicurezza: è una permutazione fissa e nota, quindi va trattato come un semplice offuscamento, non come crittografia. Conoscere il formato atteso dell'output (qui, il prefisso `picoCTF{`) è spesso sufficiente per dedurre la chiave anche senza strumenti automatici, semplicemente confrontando un carattere cifrato con quello atteso in chiaro.