##### 🛠️Cos'è

Wireshark è un analizzatore di protocolli di rete (packet analyzer) con interfaccia grafica: cattura e ispeziona il traffico di rete pacchetto per pacchetto, mostrando header e payload di ogni livello (Ethernet, IP, TCP/UDP, protocolli applicativi). Ha anche una controparte a riga di comando, `tshark`, utile per analisi scriptabili o su file molto grandi.

##### 💻Uso base

```bash
# Aprire un file di cattura nell'interfaccia grafica
wireshark file.pcap

# Leggere lo stesso file da riga di comando con tshark
tshark -r file.pcap
```

##### 🧭Funzionalità principali

**Display filter** (barra in alto nella GUI): filtra i pacchetti già catturati/caricati, es. `http`, `ip.addr == 10.0.0.5`, `tcp.port == 80`, `frame.len == 8`.

**Follow → TCP Stream / UDP Stream** (tasto destro su un pacchetto): ricostruisce un'intera conversazione (richiesta + risposta) in un colpo solo, invece di leggere pacchetto per pacchetto.

**File → Export Objects** (HTTP, SMB, ecc.): estrae automaticamente file trasferiti nel traffico (immagini, documenti) senza doverli ricostruire a mano.

**Statistics → Protocol Hierarchy / Conversations**: panoramica rapida di quali protocolli sono presenti e chi comunica con chi, utile come primo passo su un file sconosciuto.

**Colonna "Length"**: ordinabile cliccando sull'intestazione, utile per individuare pacchetti anomali per dimensione rispetto al resto del traffico.

##### 🔁Workflow tipico

1. Apri il file `.pcap`.
2. Dai un'occhiata generale con Statistics → Protocol Hierarchy per capire che tipo di traffico è presente (HTTP? DNS? qualcosa di non standard?).
3. Applica un display filter per isolare il protocollo/host di interesse.
4. Se sospetti dati nascosti o esfiltrati, ordina per dimensione pacchetto (colonna Length) o cerca pattern temporali anomali (timing insolitamente regolare o isolato).
5. Segui lo stream (Follow TCP/UDP Stream) per ricostruire conversazioni complete.
6. Esporta oggetti se il traffico contiene file trasferiti.

##### 💡Suggerimenti pratici

I **display filter** (barra in alto) sono diversi dai **capture filter** (usati solo mentre si cattura dal vivo): nei CTF, dove si parte quasi sempre da un file già pronto, si usano praticamente solo i primi.

`ip.addr == x.x.x.x` mostra traffico sia in entrata che in uscita da/verso quell'IP; `ip.src`/`ip.dst` filtrano solo un verso.

Tasto destro su un campo del pacchetto → "Apply as Filter" genera automaticamente il filtro corretto, utile quando non si ricorda la sintassi esatta.

##### ⚠️Attenzione / Problemi comuni

Catturare traffico dal vivo richiede permessi elevati (root o gruppo `wireshark`) — non è un problema nei CTF, dove di solito si analizza un file già fornito.

File `.pcap` molto grandi possono rallentare la GUI: in quei casi conviene usare `tshark` da riga di comando con filtri specifici invece di caricare tutto nell'interfaccia grafica.

Attenzione a non confondere campi di lunghezza simili (`frame.len` = dimensione del frame Ethernet completo, `ip.len`, `tcp.len` = lunghezze a livelli diversi) quando si cerca di isolare pacchetti per dimensione: usare il campo sbagliato può far perdere il pattern cercato.