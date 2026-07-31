#### 🧠Cos'è 
La Server-Side Template Injection (SSTI) è una vulnerabilità che si verifica quando input controllato dall'utente viene passato a un motore di template lato server senza sanitizzazione adeguata. Se l'input finisce dentro la sintassi di template ed è concatenato (invece che passato come dato), il motore lo valuta come codice — con conseguenze che vanno dalla lettura di dati interni fino alla remote code execution (RCE).

In pratica: un template engine si aspetta di ricevere variabili da inserire in un layout statico. Se l'utente riesce a controllare la struttura del template stesso (non solo il valore di una variabile), può far eseguire al motore espressioni arbitrarie.

#### ⚙️Come funziona 
La root cause tipica è l'input utente concatenato direttamente nella stringa di template invece che passato come variabile sicura.

Il test più semplice per confermare la vulnerabilità è iniettare un'espressione aritmetica nel campo di input e osservare se viene valutata invece che trattata come stringa letterale:

```
{{7*7}}
```

- Se l'output è `49` → il motore sta valutando l'espressione, forte indizio di SSTI (tipicamente Jinja2 o Twig, che condividono la sintassi `{{ }}`).
- Se l'output è `{{7*7}}` letterale → l'input viene trattato come testo semplice, nessuna injection (almeno con questa sintassi — provare le altre sintassi note per l'engine).

Spesso i filtri lato server bloccano solo keyword dirette (`import`, `os`, `system`, ecc.) invece di sandboxare davvero il contesto di esecuzione. Il linguaggio spesso offre percorsi alternativi (introspezione degli oggetti, attributi dunder) che bypassano blacklist superficiali.

#### 🔀Varianti 
Ogni motore ha una sintassi caratteristica, utile sia per riconoscerlo osservando l'output della pagina, sia per costruire il probing giusto:

|Engine|Linguaggio|Sintassi|
|---|---|---|
|Jinja2|Python|`{{ }}` `{% %}`|
|Twig|PHP|`{{ }}`|
|Freemarker|Java|`${}` `<#assign>`|
|Velocity|Java|`${}` `#set()`|
|Handlebars|JavaScript|`{{ }}`|
|ERB|Ruby|`<%= %>`|

#### 💻Uso da riga di comando 
Il probing viene tipicamente fatto inserendo il payload in un campo dell'applicazione web (form, query string, header). Esempio generico di test via `curl` (payload adattato al parametro/endpoint reale):

```bash
curl -G "http://target/render" --data-urlencode "name={{7*7}}"
```

Se la risposta contiene `49`, il parametro è vulnerabile a SSTI.

#### 🐍Python 
Payload base per RCE (Jinja2/Flask):

```
{{ import('os').popen('ls').read() }}
```

- `import('os')` → importa il modulo per le funzioni di sistema operativo
- `popen('ls')` → apre una shell ed esegue il comando `ls`
- `read()` → legge l'output del comando eseguito

Bypass di filtri lato server: se `import`, `os`, `system` ecc. sono filtrati come keyword dirette, si può sfruttare la catena di introspezione che Python/Flask espongono, sempre raggiungibile anche con la keyword diretta bloccata:

```
{{ request.application.globals.builtins.import('os').popen('ls').read() }}
```

Come funziona questa catena:

1. `request.application` — in Flask, l'oggetto `request` (sempre disponibile nel contesto del template) espone l'istanza dell'applicazione stessa.
2. `__globals__` — l'app, essendo una funzione/oggetto Python, mantiene un riferimento alle proprie variabili globali tramite questo attributo, dando accesso allo scope interno.
3. `__builtins__` — all'interno di `__globals__` si trovano tutte le funzioni built-in di Python, incluso `__import__`, che permette di importare moduli arbitrari senza mai scrivere letteralmente la parola `import` come chiamata diretta.

Questo è un pattern generale: se un filtro blocca solo la keyword esplicita, spesso esistono percorsi alternativi (attributi, introspezione, encoding) per raggiungere la stessa funzionalità.

#### 📌Casi d'uso comuni

- Probing rapido in penetration test o CTF per confermare la presenza di SSTI (`{{7*7}}` o equivalenti per l'engine sospettato).
- Lettura di file sensibili sul server, es. flag di una challenge:

```
{{ request.application.globals.builtins.import('os').popen('cat flag').read() }}
```

- Esecuzione di comandi di sistema arbitrari tramite RCE una volta confermata la vulnerabilità.
- Enumerazione dell'ambiente applicativo tramite introspezione degli oggetti (utile quando le funzioni dirette sono filtrate).

#### ⚠️Attenzione 
In ambito sicurezza Root cause tipica:

- Input utente concatenato direttamente nella struttura del template invece che passato come variabile sicura.
- Filtro lato server a blacklist su singole keyword (es. blocca `import()` diretto) invece che sandboxing reale del contesto di esecuzione.
- Il linguaggio offre percorsi alternativi (introspezione, attributi dunder) che bypassano blacklist superficiali.

Mitigazioni (lato sviluppatore):

- Non concatenare mai input utente nella struttura del template — passarlo sempre come variabile.
- Usare un sandboxed environment del template engine quando disponibile (es. `SandboxedEnvironment` di Jinja2).
- Evitare filtri a blacklist su keyword; preferire whitelist rigide di caratteri/pattern ammessi nell'input.
- Applicare il principio del minimo privilegio al processo che esegue il motore di template (limita il danno anche in caso di RCE).