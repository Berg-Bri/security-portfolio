#### Descrizione
I testi saltano dai versi al ritornello come una chiamata di subroutine. C'è un ritornello nascosto che questo programma non stampa per impostazione predefinita. Puoi farlo stampare? Potrebbe esserci qualcosa per te.

#### Analisi / Ricognizione
Viene fornito il sorgente di `lyric-reader.py`, uno script Python che implementa un piccolo "interprete di canzoni": legge un testo strutturato a etichette (`[REFRAIN]`, `[VERSE1]`) e lo esegue riga per riga, in modo simile a un mini linguaggio a `goto`/subroutine. L'hint conferma che esiste una strofa nascosta, mai raggiunta durante l'esecuzione normale, che probabilmente contiene la flag.

Lo script carica la flag da `flag.txt` e la incolla dentro una strofa iniziale (`secret_intro`):

```python
secret_intro = \
'''Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether's ours to conquer, '''\
+ flag + '\n'
```

Questa strofa viene messa in testa a tutta la "canzone" (`song_flag_hunters`), che contiene poi un'etichetta `[REFRAIN]` (il ritornello, richiamato più volte dalle varie strofe) e un'etichetta `[VERSE1]` (la prima strofa vera e propria). Il punto chiave è qui:

```python
reader(song_flag_hunters, '[VERSE1]')
```

L'esecuzione parte da `[VERSE1]`, **non** dall'inizio del testo: `secret_intro`, e quindi la flag, esiste in memoria ma non viene mai raggiunta durante una lettura "normale" — proprio la strofa nascosta a cui allude l'hint.

##### L'interprete `reader()`
La funzione divide la canzone in righe (`song_lines`) e mantiene un puntatore di lettura `lip` (line pointer). Ad ogni riga, il contenuto viene ulteriormente diviso per `;` e ogni "istruzione" ottenuta viene interpretata:

|Istruzione|Comportamento|
|---|---|
|`REFRAIN`|Salva il punto di ritorno nella riga fissa `RETURN` (dentro `[REFRAIN]`) come `RETURN <lip+1>`, poi salta all'inizio del ritornello|
|`CROWD...`|Chiede input all'utente (`input('Crowd: ')`) e **sovrascrive la riga corrente** con `'Crowd: ' + input_utente`|
|`RETURN N`|Salta alla riga `N` (`lip = N`)|
|`END`|Termina l'esecuzione|
|qualsiasi altra riga|La stampa a video e avanza di una riga|

##### La vulnerabilità
Il problema è in questo blocco:
```python
elif re.match(r"CROWD.*", line):
    crowd = input('Crowd: ')
    song_lines[lip] = 'Crowd: ' + crowd
    lip += 1
```

L'input dell'utente **non viene sanitizzato** e finisce direttamente dentro `song_lines`, l'array che l'interprete rilegge ed esegue come "codice". Dato che ogni riga viene poi divisa per `;` prima di essere interpretata, se l'input contiene un `;` seguito da un comando valido (es. `RETURN 0`), quel comando verrà eseguito la **prossima volta** che l'interprete ripassa da quella riga — cosa che succede automaticamente, perché il testo contiene più chiamate a `REFRAIN;` in sequenza.

In pratica: il primo passaggio nel ritornello scrive l'input al posto della riga `CROWD`; il secondo passaggio nel ritornello rilegge quella riga, ora modificata, e la interpreta come due istruzioni separate dal `;`. Poiché `RETURN` accetta un numero di riga arbitrario e la riga `0` corrisponde all'inizio assoluto del testo (dove si trova `secret_intro` con la flag), basta forzare un salto a `RETURN 0` per far stampare la strofa nascosta.

#### Sfruttamento
Input da fornire al primo prompt `Crowd:`:

```
some_string;RETURN 0
```

Sequenza degli eventi:

1. Lo script parte da `[VERSE1]`, stampa la prima strofa e arriva a `REFRAIN;` → salta al ritornello.
2. Il ritornello stampa le sue 4 righe e arriva a `CROWD (Singalong here!)` → chiede input. Inseriamo `some_string;RETURN 0`. Questa riga viene sovrascritta con `Crowd: some_string;RETURN 0` (non eseguita subito, solo salvata).
3. L'interprete torna alla strofa successiva (tramite `RETURN <n>` salvato automaticamente) e la stampa fino a incontrare di nuovo `REFRAIN;`.
4. Il ritornello riparte, ristampa le 4 righe fisse e arriva di nuovo alla riga `CROWD`, ora modificata. Il testo `Crowd: some_string;RETURN 0` viene diviso per `;` in due istruzioni:
    - `Crowd: some_string` → non corrisponde a nessun pattern speciale → viene stampata come testo normale.
    - `RETURN 0` → corrisponde a `re.match(r"RETURN [0-9]+", line)` → `lip = 0`.
5. L'interprete riparte dalla riga 0, cioè dall'inizio assoluto del testo: viene stampata `secret_intro`, la strofa nascosta con la flag.

##### Verifica pratica (locale)

Script ricreato con una flag fittizia (`picoCTF{test_flag_1234}`), input simulato via pipe:

```bash
echo "some_string;RETURN 0" | python3 lyric-reader.py
```

Output (estratto):

```
...
We're flag hunters in the ether, lighting up the grid,
No puzzle too dark, no challenge too hid.
With every exploit we trigger, every byte we decrypt,
We're chasing that victory, and we'll never quit.
Crowd: some_string
Pico warriors rising, puzzles laid bare,
Solving each challenge with precision and flair.
With unity and skill, flags we deliver,
The ether's ours to conquer, picoCTF{test_flag_1234}
```

Confermato: dopo il secondo passaggio nel ritornello, il salto a `RETURN 0` fa stampare `secret_intro` con la flag. Da quel punto in poi lo script continua a ciclare (torna sempre su `[REFRAIN]` e poi di nuovo a riga 0), ristampando la flag ripetutamente fino al limite di `MAX_LINES = 100`.

Ora bisogna ripetere la procedura sulla macchina online e otteniamo la flag.

#### Flag
```
picoCTF{70637h3r_f0r3v3r_75053bc3}
```

#### Lezioni apprese
- Un mini-interprete "a righe" che rilegge e reinterpreta dati modificabili dall'utente (qui `song_lines`) è di fatto un motore di esecuzione: qualsiasi input inserito lì dentro senza sanitizzazione è potenzialmente codice, non semplice testo.
- Il carattere separatore usato dal parser (`;`) va trattato come un metacarattere pericoloso quando proviene da input utente: va filtrato, escapato o l'input va validato con un pattern rigido prima di essere riscritto nella struttura interpretata.
- "Nascondere" un dato (qui la flag) semplicemente non facendolo raggiungere dal normale flusso di controllo non è una protezione: se il flusso di controllo stesso è manipolabile dall'utente (tramite `RETURN N` arbitrario), il dato resta comunque accessibile.
- Utile, quando si analizza codice simile, mappare esplicitamente tutte le etichette/indirizzi raggiungibili (qui bastava capire che l'indice `0` = inizio testo) prima di cercare l'exploit.