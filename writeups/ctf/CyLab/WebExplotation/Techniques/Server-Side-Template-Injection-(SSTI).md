## Cos'è

La Server-Side Template Injection è una vulnerabilità che si verifica quando input controllato dall'utente viene passato a un motore di template lato server senza sanitizzazione adeguata. Se l'input finisce dentro la sintassi di template ed è concatenato (invece che passato come dato), il motore lo valuta come codice — con conseguenze che vanno dalla lettura di dati interni fino alla remote code execution (RCE).

In pratica: un template engine si aspetta di ricevere _variabili_ da inserire in un layout statico. Se l'utente riesce a controllare la struttura del template stesso (non solo il valore di una variabile), può far eseguire al motore espressioni arbitrarie.

## 1. Identificazione del template engine

Ogni motore ha una sintassi caratteristica, utile sia per riconoscerlo osservando l'output della pagina, sia per costruire il probing giusto:

|Engine|Linguaggio|Sintassi|
|---|---|---|
|Jinja2|Python|`{{ }}` `{% %}`|
|Twig|PHP|`{{ }}`|
|Freemarker|Java|`${}` `<#assign>`|
|Velocity|Java|`${}` `#set()`|
|Handlebars|JavaScript|`{{ }}`|
|ERB|Ruby|`<%= %>`|

## 2. Probing — conferma della vulnerabilità

Il test più semplice è iniettare un'espressione aritmetica nel campo di input e osservare se viene _valutata_ invece che trattata come stringa letterale:

```
{{7*7}}
```

- Se l'output è `49` → il motore sta valutando l'espressione, forte indizio di SSTI (tipicamente Jinja2 o Twig, che condividono la sintassi `{{ }}`)
- Se l'output è `{{7*7}}` letterale → l'input viene trattato come testo semplice, nessuna injection (almeno con questa sintassi — provare le altre sintassi della tabella)

## 3. Sfruttamento

### Payload base per RCE (Jinja2/Flask)

```
{{ import('os').popen('ls').read() }}
```

- `import('os')` → importa il modulo per le funzioni di sistema operativo
- `popen('ls')` → apre una shell ed esegue il comando `ls`
- `read()` → legge l'output del comando eseguito

### Bypass di filtri lato server

Spesso i filtri bloccano keyword dirette come `import`, `os`, `system`, ecc. Un modo comune per aggirarli è sfruttare l'introspezione che Python/Flask espongono attraverso la catena degli oggetti built-in, che restano raggiungibili anche se la keyword diretta è filtrata:

```
{{ request.application.globals.builtins.import('os').popen('ls').read() }}
```

Come funziona questa catena:

1. **`request.application`** — in Flask, l'oggetto `request` (sempre disponibile nel contesto del template) espone l'istanza dell'applicazione stessa
2. **`__globals__`** — l'app, essendo una funzione/oggetto Python, mantiene un riferimento alle proprie variabili globali tramite questo attributo, dando accesso allo scope interno
3. **`__builtins__`** — all'interno di `__globals__` si trovano tutte le funzioni built-in di Python, incluso `__import__`, che permette di importare moduli arbitrari senza mai scrivere letteralmente la parola `import` come chiamata diretta

Questo è un pattern generale: se un filtro blocca solo la keyword esplicita, spesso esistono percorsi alternativi (attributi, introspezione, encoding) per raggiungere la stessa funzionalità.

### Lettura di file (es. flag)

```
{{ request.application.globals.builtins.import('os').popen('cat flag').read() }}
```

Stessa logica del comando `ls`, sostituendo il comando eseguito.

## Root cause tipica

- Input utente concatenato direttamente nella stringa di template invece che passato come variabile sicura
- Filtro lato server a blacklist su singole keyword (es. blocca `import()` diretto) invece che sandboxing reale del contesto di esecuzione del template
- Il linguaggio offre percorsi alternativi (introspezione degli oggetti, attributi dunder) che bypassano blacklist superficiali

## Mitigazioni (lato sviluppatore)

- Non concatenare mai input utente nella struttura del template — passarlo sempre come variabile
- Usare un sandboxed environment del template engine quando disponibile (es. `SandboxedEnvironment` di Jinja2)
- Evitare filtri a blacklist su keyword; preferire whitelist rigide di caratteri/pattern ammessi nell'input
- Principio del minimo privilegio per il processo che esegue il motore di template (limita il danno anche se l'RCE avviene)
