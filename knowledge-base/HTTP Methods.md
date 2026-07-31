#### 📥GET

Richiede una risorsa. **Non dovrebbe** avere side-effect sul server (safe + idempotent).

`es: GET /users/1` → restituisce i dati dell'utente 1

**Security note**: parametri spesso in query string → finiscono in log, browser history, referer header. Mai usare per dati sensibili (token, password).

#### 👀HEAD

Identico a GET, ma il server restituisce **solo gli header di risposta**, senza il body.

`es: HEAD /users/1` → stessi header di GET, ma nessun contenuto

**Perché è utile in pentest**:

- Permette di verificare l'esistenza/metadati di una risorsa (status code, `Content-Length`, `Last-Modified`) senza scaricarne il contenuto
- Alcuni server/WAF applicano controlli di autorizzazione **diversi** su GET vs HEAD → un endpoint protetto su GET potrebbe rispondere senza autenticazione su HEAD (**bypass di access control**)
- Usato per fingerprinting silenzioso (versione server, tecnologie) senza generare traffico/log pesanti

#### 📤POST

Invia dati al server per creare una risorsa o eseguire un'azione. **Non idempotente** (richieste ripetute possono creare più risorse).

`es: POST /login` con body `{user, pass}` → crea sessione

**Security note**: target principale per SQLi, injection nei body (JSON/form), CSRF (mancanza di token).

#### 📝PUT

Crea o **sostituisce interamente** una risorsa a un URI specifico. Idempotente (ripetere la stessa PUT dà lo stesso risultato).

`es: PUT /users/1` con body completo → sovrascrive l'utente 1

**Security note**: se non correttamente autorizzato, può permettere upload/overwrite arbitrario di file (**unrestricted file upload**).

#### 🩹PATCH

Modifica **parzialmente** una risorsa esistente. Non necessariamente idempotente.

`es: PATCH /users/1` con body `{email: "new@x.com"}` → aggiorna solo l'email

#### 🗑️DELETE

Elimina la risorsa specificata. Idempotente (eliminarla due volte → stesso stato finale).

`es: DELETE /users/1`

**Security note**: da testare sempre per **IDOR** (Insecure Direct Object Reference) — posso cancellare risorse di altri utenti cambiando l'ID?

#### ❓OPTIONS

Richiede quali metodi HTTP sono supportati da una risorsa/endpoint.

`es: OPTIONS /api/users` → risposta header `Allow: GET, POST, HEAD`

**Perché è utile in pentest**: enumera rapidamente i metodi disponibili su un endpoint, utile per scoprire metodi "nascosti" o non documentati (es. PUT/DELETE esposti per errore).

#### 🪞TRACE

Il server rimanda indietro (echo) la richiesta ricevuta, per debug.

**Security note**: **da disabilitare sempre** in produzione → vulnerabile a **Cross-Site Tracing (XST)**, permette di bypassare la protezione `HttpOnly` sui cookie in certi scenari con XSS.

#### 🔌CONNECT

Usato per stabilire un tunnel (tipicamente TCP) attraverso un proxy, es. per HTTPS.

#### 📊Tabella riassuntiva

|Metodo|Safe|Idempotente|Ha body richiesta|Nota sicurezza|
|---|---|---|---|---|
|GET|✅|✅|❌|dati sensibili in query = leak|
|HEAD|✅|✅|❌|può bypassare controlli su GET|
|POST|❌|❌|✅|injection, CSRF|
|PUT|❌|✅|✅|overwrite/upload arbitrario|
|PATCH|❌|❌|✅|injection parziale|
|DELETE|❌|✅|❌|IDOR|
|OPTIONS|✅|✅|❌|enumerazione metodi|
|TRACE|✅|✅|❌|XST, va disabilitato|

**Safe** = non modifica lo stato del server. **Idempotente** = richieste ripetute → stesso risultato finale.

#### 🔬Caso pratico: GET → HEAD (Burp Suite)

Scenario tipico: un endpoint blocca l'accesso non autenticato su GET, ma un controllo di autorizzazione mal implementato (es. verificato solo su `req.method === 'GET'`) lascia HEAD non filtrato.

**Workflow in Burp**:

1. Intercettare la richiesta GET con Proxy
2. Inviarla a Repeater
3. Cambiare la prima riga da `GET /path HTTP/1.1` a `HEAD /path HTTP/1.1`
4. Confrontare lo status code e gli header di risposta → se torna `200 OK` invece di `401/403`, è un **access control bypass via HTTP method**

Da annotare: HEAD non restituisce body, quindi non si "vedono" i dati, ma la conferma dello status/header è già una falla di per sé (information disclosure / conferma bypass), utile combinata con altre tecniche.