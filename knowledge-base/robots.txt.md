#### 🧠Cos'è
File di testo, posizionato nella root di un sito (`https://esempio.com/robots.txt`), che indica ai **web crawler/bot** (Googlebot, Bingbot, ecc.) quali percorsi **non dovrebbero** scansionare/indicizzare.

**Importante**: è una convenzione (Robots Exclusion Protocol), **non un controllo di sicurezza** → è solo una richiesta, i bot "onesti" la rispettano, ma niente impedisce a un browser, uno script o un attaccante di visitare comunque quei path.

#### 📝Sintassi base

```
User-agent: *
Disallow: /admin/
Disallow: /backup/
Allow: /public/
Sitemap: https://esempio.com/sitemap.xml
```

- **User-agent**: a quale bot si applica la regola (`*` = tutti)
- **Disallow**: path che il bot non dovrebbe visitare
- **Allow**: eccezione dentro un path bloccato
- **Sitemap**: indica dove trovare la mappa del sito

#### 🕵️Perché interessa in un pentest/recon

`robots.txt` è spesso uno dei **primi file da controllare** in fase di ricognizione, perché involontariamente **rivela la struttura del sito**, inclusi path che l'amministratore voleva tenere "nascosti" dai motori di ricerca ma che restano comunque raggiungibili.

`es:`

```
Disallow: /admin-panel/
Disallow: /old-backup/
Disallow: /.git/
Disallow: /config/
```

Un attaccante legge semplicemente il file e ottiene una lista di path potenzialmente interessanti da testare direttamente (`curl https://esempio.com/admin-panel/`).

#### 💻Workflow pratico di recon

```bash
curl https://target.com/robots.txt
```

oppure semplicemente aprirlo nel browser.

Poi verificare manualmente ogni path elencato → cercare pannelli di amministrazione esposti, backup dimenticati, repository `.git/` esposte, file di configurazione, ecc.

#### ⚠️Errore comune da parte degli sviluppatori

Usare `robots.txt` pensando che sia un meccanismo di **protezione** ("se lo blocco qui, nessuno lo trova"). In realtà:

- Non impedisce l'accesso diretto tramite URL
- Non impedisce a scanner/bot malevoli (che ignorano volutamente il file) di accedere comunque
- **Anzi**, elenca esplicitamente i path "sensibili", facilitando il lavoro di un attaccante

**Lezione**: la vera protezione deve essere autenticazione/autorizzazione lato server (es. HTTP auth, controllo sessione), mai l'esclusione da robots.txt.

#### 🔗Collegamento con altri file simili

|File|Scopo|
|---|---|
|`robots.txt`|Istruzioni per crawler sui path da non indicizzare|
|`sitemap.xml`|Mappa di tutte le pagine da indicizzare (può rivelare struttura del sito)|
|`security.txt` (`/.well-known/security.txt`)|Contatti per segnalare vulnerabilità responsabilmente|
|`humans.txt`|Info sul team/tecnologie usate (raramente interessante per security)|

`Tutti questi file vanno controllati di routine in fase di recon — nessuno è un controllo di accesso, sono solo metadati pubblici.`