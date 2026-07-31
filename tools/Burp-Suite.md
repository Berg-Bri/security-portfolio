#### 🛠️Cos'è

Burp Suite è un proxy di intercettazione: si posiziona tra il browser e il server web, permettendo di vedere e modificare ogni richiesta/risposta HTTP prima che venga inviata o processata.

#### ⚙️Setup iniziale

1. Apri Burp Suite → Proxy → Intercept.
2. Usa il browser integrato di Burp (pulsante **Open browser**, in genere in Proxy o Dashboard): è già preconfigurato per passare dal proxy, senza dover toccare le impostazioni di rete del sistema.
3. Se navighi con un browser esterno (es. Chrome), configura manualmente il proxy su `127.0.0.1:8080` e installa il certificato CA di Burp (menu **CA Certificate**) per evitare errori SSL su siti HTTPS.

#### 🧭 Funzionalità principali

**Proxy → Intercept** Mostra in tempo reale le richieste in transito quando "Intercept is on". Da qui puoi:

- Modificare la richiesta al volo prima che parta
- Cliccare **Forward** per farla proseguire invariata
- Cliccare **Drop** per scartarla
- Tasto destro → **Send to Repeater** per lavorarci con più calma

**Repeater** Spazio di lavoro per modificare e reinviare la stessa richiesta più volte, senza dover rifare il giro dal browser ogni volta. Utile per:

- Provare varianti di header, parametri, cookie
- Osservare come cambia la risposta modificando un solo elemento alla volta

Modalità **Pretty** vs **Raw**: Pretty applica syntax highlighting e formattazione automatica; Raw mostra il testo puro della richiesta HTTP. Se Pretty dà errori di formattazione (es. riga vuota finale mancante), passare a Raw e verificare manualmente la struttura può risolvere il problema.

**Inspector** (pannello laterale in Repeater/Proxy) Riassume in modo strutturato la richiesta selezionata: header, cookie, parametri query/body. Comodo per controllare rapidamente quanti cookie/header sono presenti senza scorrere tutto il testo grezzo.

#### 🔁 Workflow tipico: sostituzione di un cookie di sessione

1. Intercetta una richiesta verso l'applicazione target (Proxy → Intercept).
2. Inviala a Repeater.
3. Aggiungi o modifica l'header:
```
    Cookie: session=<valore_del_token>
```
Attenzione: se l'applicazione mostra il contenuto decodificato del cookie (es. un dizionario Python `{'key': 'admin'}`), quello non va nell'header — serve solo il token firmato originale.

4. Send e analizza la risposta: status code, header `Set-Cookie`, e contenuto del body per verificare se l'autenticazione è cambiata.

#### 💡Suggerimenti pratici

- Usa la barra di ricerca nel pannello Response per trovare velocemente parole chiave (es. `admin`, `flag`, `picoCTF{`) senza scorrere manualmente HTML lunghi.
- Community Edition non ha lo scanner automatico, ma Proxy + Repeater coprono la maggior parte dei casi di manipolazione manuale.

#### ⚠️Attenzione / Problemi comuni

Una richiesta HTTP valida richiede una riga vuota tra il blocco degli header e il body (anche se il body è assente, come in una GET). Se manca, Burp mostra un avviso tipo:

```
The HTTP header block doesn't have a blank line at the end. This may cause a request timeout.
```

Se il problema persiste anche aggiungendo una riga vuota manualmente, può aiutare:

- Passare alla tab **Raw** e verificare l'assenza di caratteri invisibili residui
- Riordinare/ritoccare leggermente le ultime righe di header per forzare Burp a ricalcolare la formattazione