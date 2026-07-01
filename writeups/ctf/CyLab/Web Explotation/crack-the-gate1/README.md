#### Descrizione
Siamo nel bel mezzo di un'indagine. 
Si sospetta che una delle persone che stiamo indagando, nota come ctf player, stia nascondendo dati sensibili all'interno di un portale web ad accesso limitato. 
Abbiamo scoperto l'indirizzo email che usa per accedere: ctf-player@picoctf.org. 
Purtroppo, non conosciamo la password e i soliti tentativi non hanno funzionato. 
Ma qualcosa non quadra... è quasi come se lo sviluppatore avesse lasciato un accesso segreto. Riuscite a scoprirlo?

#### Analisi del codice sorgente
Ispezionando il sorgente HTML della pagina di login, è stato trovato un commento sospetto subito sopra il form:
```html
<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
```

#### Decifratura
Il testo era cifrato con **Cifrario di Cesare, k=13** (ROT13). Decifrato risulta:
```
NOTE JACK - TEMPORARY BYPASS: USE HEADER "X-DEV-ACCESS: YES"
```
Uno sviluppatore (Jack) aveva lasciato un backdoor temporaneo non rimosso prima del deploy in produzione.

#### Sfruttamento
- Intercettata una richiesta POST verso `/login` con Burp Suite
- Aggiunto l'header custom: X-Dev-Access: yes
- Inserisco nel Body l'email suggerita dalla descrizione della Macchina
- Ottengo la risposta:
<p align="center"> <img src="assets/01-post-burpsuite.png" > </p>

#### Flag
picoCTF{brut4_f0rc4_125f752d}