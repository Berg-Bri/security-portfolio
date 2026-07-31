#### 🧩Descrizione

Mi chiedo cosa sia veramente...

#### 🔍Analisi / Ricognizione

La sfida fornisce uno script che genera una stringa cifrata a partire dalla flag:

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

E il risultato cifrato da decifrare:

```
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽
```

A prima vista sembra testo cinese o giapponese, ma non lo è: sono caratteri Unicode "esotici" usati come contenitori numerici. Lo script originale non fa altro che prendere due caratteri della flag alla volta e "incollarli" insieme dentro un unico numero a 16 bit, che Python poi trasforma in un carattere. Per questo il risultato appare come simboli CJK: sono solo numeri grandi convertiti in modo forzato in caratteri.

Scomponiamo l'operazione originale:

1. `ord(flag[i])` — prende il valore numerico del primo carattere (es. `'A'` → 65).
2. `ord(flag[i]) << 8` — sposta quel numero di 8 bit a sinistra, cioè lo moltiplica per 256.
3. Si somma `ord(flag[i+1])`, il valore numerico del secondo carattere.
4. `chr(...)` converte il numero risultante in un carattere.

In pratica due caratteri normali (8 bit ciascuno) vengono "impacchettati" in un unico carattere da 16 bit: il primo occupa la parte alta del numero, il secondo la parte bassa.

Esempio con `'A'` (65) e `'B'` (66):

```
(65 << 8) + 66 = 16640 + 66 = 16706
```

In binario: `01000001 01000010` — i primi 8 bit sono 'A', gli ultimi 8 bit sono 'B'.

#### ⚙️Sfruttamento

Per tornare indietro basta separare i due byte impacchettati in ogni carattere cifrato:

```python
def reverse_operation(combined_char):
    combined_value = ord(combined_char)
    first_char = chr(combined_value >> 8)     # bit alti = primo carattere
    second_char = chr(combined_value & 0xFF)  # bit bassi = secondo carattere
    return first_char, second_char

enc_flag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'

flag = ''
for combined_char in enc_flag:
    first_char, second_char = reverse_operation(combined_char)
    flag += first_char + second_char

print(flag)
```

Spiegazione delle due operazioni chiave:

- `>> 8` (shift a destra di 8 bit): butta via la parte bassa e riporta in primo piano il primo carattere.
- `& 0xFF` (AND con 255, binario `11111111`): "maschera" tutto tranne gli ultimi 8 bit, isolando il secondo carattere.

Alternativa più semplice, senza bit a bit, usando la divisione:

```python
char1, char2 = divmod(ord(combined_char), 256)
# quoziente = primo carattere, resto = secondo carattere
```

#### 🚩Flag

```
picoCTF{16_bits_inst34d_of_8_b7f62ca5}
```

#### 💡Lezioni apprese

- Un carattere Unicode può occupare più di 8 bit: questo permette di "nascondere" due byte dentro un solo carattere, e il risultato appare come simboli di alfabeti esotici (CJK).
- Shift (`<<`/`>>`) e AND bit a bit (`&`) sono gli strumenti base per impacchettare/spacchettare dati a livello di bit.
- Quando un output "strano" contiene caratteri non standard, conviene sempre controllarne il valore numerico (`ord()`) prima di pensare a una vera codifica testuale.