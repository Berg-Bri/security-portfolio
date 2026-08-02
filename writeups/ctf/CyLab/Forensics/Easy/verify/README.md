##### 🛠️ Tool usati

- [ssh](../../../../../../tools/ssh.md)
- [sha256sum](../../../../../../tools/sha256sum.md)
- [grep](../../../../../../tools/grep.md)

##### 🧩 Descrizione

_C'è sempre qualcuno che cerca di ingannare i miei giocatori con flag falsi. Voglio assicurarmi che ricevano quelli autentici! Fornirò l'hash SHA-256 e uno script di decrittografia per aiutarvi a verificare che i miei flag siano autentici._

```
ssh -p 56233 ctf-player@rhea.picoctf.net
```

_Usare la password `84b12bae`. Accettare il fingerprint con `yes`, e `ls` una volta connessi per iniziare. Ricorda, in una shell, le password sono nascoste!_

- Checksum: `3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4`
- Per decriptare il file una volta verificato l'hash, usare `./decrypt.sh files/<file>`.

##### 🔍 Analisi / Ricognizione

Il primo passo è stato controllare il contenuto della cartella:

```bash
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
```

- Nel file `checksum.txt` troviamo l'hash per verificare il file corretto.
- Nel file `decrypt.sh` troviamo invece l'algoritmo per la decrittazione.
- Nella directory `files` troviamo tutte le flag false più quella corretta.

##### ⚙️ Sfruttamento

Il passo successivo è stato controllare, attraverso il checksum, quale fosse il file corretto. L'idea è stata quella di usare il tool `sha256sum` su tutti i file, e filtrare con `grep` l'unico che iniziava con `3ad`:

```bash
sha256sum files/* | grep '\<3ad'
3ad37ed6c5ab81d31e4c94ae611e0adf2e9e3e6bee55804ebc7f386283e366a4  files/e018b574
```

Una volta ottenuto il file corretto, è bastato usarlo come input per l'algoritmo presente in `decrypt.sh`, ottenendo così la flag:

```bash
./decrypt.sh files/e018b574
picoCTF{trust_but_verify_e018b574}
```

##### 🚩 Flag

picoCTF{trust_but_verify_e018b574}`

##### 💡 Lezioni apprese

Prima di fidarsi di un file va sempre verificata la sua integrità/autenticità tramite un hash checksum fornito da una fonte affidabile, lo stesso principio con cui si verificano i download di software o immagini disco ufficiali. `sha256sum` calcolato su tutti i candidati e confrontato con l'hash atteso permette di isolare rapidamente il file genuino tra molte varianti contraffatte, senza doverle ispezionare una per una a mano.