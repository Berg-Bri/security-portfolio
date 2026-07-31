#### 🛠️Cos'è

Tool a riga di comando per leggere/scrivere dati su connessioni di rete usando **TCP** o **UDP**. Spesso descritto come il "coltellino svizzero" del networking — utile sia per attività legittime di debug/test sia, in ambito CTF/pentest, per interagire con servizi remoti o ottenere shell.

#### 💻Sintassi base

```bash
nc [opzioni] <host> <porta>
```

#### 📡Uso più comune nelle CTF: connettersi a un servizio remoto

```bash
nc <ip_target> <porta>
```

`es:` una challenge PicoCTF spesso fornisce un'istanza remota tipo:

```bash
nc jupiter.challenges.picoctf.org 54321
```

Questo apre una connessione TCP interattiva: quello che scrivi viene inviato al server, e quello che il server risponde appare a schermo — esattamente come è successo nella challenge degli hash, dove il servizio ti chiedeva la password per ogni hash craccato.

#### 🎛️Opzioni principali

|Opzione|Effetto|
|---|---|
|`-l`|Modalità **listen**: mette nc in ascolto invece di connettersi (usato per creare un server improvvisato)|
|`-p <porta>`|Specifica la porta locale da usare (con `-l`)|
|`-v`|Verbose, mostra informazioni aggiuntive sulla connessione|
|`-n`|Salta la risoluzione DNS, usa direttamente indirizzi IP (più veloce)|
|`-u`|Usa **UDP** invece di TCP (default)|
|`-w <secondi>`|Timeout di connessione|
|`-z`|Modalità scan (non invia dati, utile per port scanning veloce)|

#### 🔁Casi d'uso pratici

**Connettersi a un servizio (client), come nelle CTF:**

```bash
nc target.com 1337
```

**Mettersi in ascolto su una porta (server):**

```bash
nc -lvp 4444
```

Utile per ricevere una **reverse shell**: un target compromesso si connette verso di te, e quello che digiti sul tuo terminale viene eseguito lì.

**Port scanning veloce (alternativa "povera" a nmap):**

```bash
nc -zv target.com 20-100
```

Prova a connettersi a tutte le porte nel range indicato e mostra quali rispondono aperte.

**Trasferire un file tra due macchine:**

```bash
# sulla macchina ricevente (in ascolto)
nc -lvp 4444 > file_ricevuto.txt
# sulla macchina che invia
nc <ip_ricevente> 4444 < file_da_inviare.txt
```

**Banner grabbing (identificare il servizio/versione su una porta aperta):**

```bash
nc -v target.com 80
```

poi digitando manualmente una richiesta tipo `HEAD / HTTP/1.1` seguito da invio doppio, per vedere gli header di risposta (collegamento diretto con la nota sui metodi HTTP).

#### ↔️Differenza chiave: client vs listener

```
nc target.com 1337      →  MODALITÀ CLIENT: ti connetti tu a un servizio esistente
nc -lvp 4444             →  MODALITÀ LISTENER: aspetti che qualcun altro si connetta a te
```

Questa distinzione è fondamentale per capire il concetto di **reverse shell** (il target si connette a te, che sei in ascolto) rispetto a una **bind shell** (il target si mette in ascolto e tu ti connetti a lui) — pattern molto comune nelle macchine di Binary Exploitation/privilege escalation che affronterai più avanti nella tua roadmap.

#### 🧰Varianti/alternative

|Tool|Differenza|
|---|---|
|`ncat` (incluso in Nmap)|Versione più moderna, supporta SSL/TLS nativamente|
|`socat`|Più potente e flessibile di nc, ma sintassi più complessa|
|`netcat-traditional` vs `netcat-openbsd`|Due implementazioni diverse su Linux, con piccole differenze di opzioni disponibili (Kali usa di default la versione OpenBSD)|