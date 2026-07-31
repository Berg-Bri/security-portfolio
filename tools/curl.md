#### 🛠️Cos'è

`curl` è un tool a riga di comando (Client URL) per trasferire dati da/verso un server, usando protocolli come HTTP, HTTPS, FTP, ecc.

Permette di fare richieste di rete manualmente da terminale, senza usare un browser — fondamentale in ambito sicurezza/pentest per:

- Testare API ed endpoint direttamente
- Automatizzare richieste (script, scanning)
- Scaricare file da URL
- Ispezionare header di risposta, codici di stato, cookie

#### 💻Sintassi base

```bash
curl [opzioni] URL
```

#### 🎛️ Opzioni principali

|Opzione|Significato|Esempio|
|---|---|---|
|`-o file`|Salva l'output in un file|`curl -o out.json https://api.example.com`|
|`-O`|Salva usando il nome file originale dell'URL|`curl -O https://site.com/file.zip`|
|`-X METODO`|Specifica il metodo HTTP|`curl -X POST url`|
|`-H "header"`|Aggiunge un header alla richiesta|`curl -H "Accept: application/json" url`|
|`-d "dati"`|Invia dati nel body (POST)|`curl -d '{"user":"admin"}' url`|
|`-I`|Mostra solo gli header di risposta (no body)|`curl -I url`|
|`-i`|Mostra header + body|`curl -i url`|
|`-s`|Modalità silenziosa (nasconde barra progresso)|`curl -s url`|
|`-v`|Verbose, mostra tutta la comunicazione (utile per debug)|`curl -v url`|
|`-L`|Segue i redirect automaticamente|`curl -L url`|
|`-k`|Ignora errori certificato SSL (attenzione, solo per test)|`curl -k https://url`|

#### 🔁Esempi pratici dal tuo lab

Scaricare un file specifico salvandolo con nome custom:

```bash
curl -o heapdump.heapsnapshot "http://target:port/heapdump"
```

Vedere solo gli header di risposta (utile per capire tipo di contenuto, dimensione, server):

```bash
curl -I "http://target:port/api-docs"
```

Fare una richiesta GET con header specifico (come genera Swagger "Try it out"):

```bash
curl -X GET "http://target:port/heapdump" -H "accept: */*"
```

Inviare una richiesta POST con dati JSON (es. login):

```bash
curl -X POST "http://target:port/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"test"}'
```

Analisi dei file caricati dalla pagina principale con `curl`:

```bash
curl -s http://titan.picoctf.net:PORT | grep -oE 'src="[^"]*"|href="[^"]*"'
```

#### ⚠️Nota di sicurezza

`curl` è spesso il primo tool usato in fase di **enumerazione/ricognizione** di un'app web: prima di scaricare file pesanti o lanciare exploit, è buona pratica controllare rapidamente cosa risponde un endpoint con `-I` o `-v`, per capire tipo di contenuto, header di sicurezza presenti/assenti, e comportamento del server — senza doverlo aprire nel browser.