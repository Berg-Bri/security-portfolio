##### 🛠️Cos'è

SSH (Secure Shell) è un protocollo per accedere in modo sicuro e cifrato a una shell remota su un altro host. Oltre alla shell interattiva permette trasferimento file (`scp`/`sftp`) e port forwarding/tunneling. Nei CTF è lo strumento standard per connettersi alle macchine remote fornite dalla piattaforma.

##### 💻 Uso base

```bash
# Connessione base
ssh utente@host

# Con porta non standard
ssh -p 2222 utente@host
```

##### 🧭 Funzionalità principali

Autenticazione a password o a chiave pubblica/privata.

`scp` per copiare file da/verso l'host remoto.

Port forwarding/tunneling (`-L`, `-R`, `-D`) per instradare traffico attraverso la connessione cifrata.

Verifica del fingerprint della chiave host al primo collegamento, come protezione contro attacchi man-in-the-middle.

##### 🔁 Workflow tipico

1. Ricevi indirizzo, porta, utente e password/chiave dalla challenge.
2. `ssh -p <porta> <utente>@<host>`.
3. Accetta il fingerprint (`yes`) al primo collegamento.
4. Inserisci la password quando richiesta.
5. Una volta dentro, esplora con `ls`, `cat`, ecc.

##### 💡Suggerimenti pratici

Se non specificata, la porta di default è 22 — va sempre controllata quella indicata dalla challenge, spesso diversa.

La password non appare a schermo (né come asterischi) mentre la digiti: è comportamento normale del terminale, non un errore o un blocco.

##### ⚠️ Attenzione / Problemi comuni

Se l'host cambia (es. macchina CTF riavviata su un nuovo container), il fingerprint cambia e ssh mostra un warning "REMOTE HOST IDENTIFICATION HAS CHANGED" — nei laboratori è normale, si risolve rimuovendo la vecchia voce con `ssh-keygen -R host` o ripulendo `~/.ssh/known_hosts`.


