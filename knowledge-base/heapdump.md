#### cos'è un Heap Dump

Un **heap dump** è una "fotografia" completa dello stato della memoria heap di un'applicazione in un dato istante. Contiene tutti gli oggetti allocati dinamicamente durante l'esecuzione: variabili, stringhe, strutture dati, sessioni utente, e — se non gestite correttamente — anche **dati sensibili** come password, token di sessione, chiavi API o secret che l'applicazione ha tenuto in memoria durante il suo funzionamento.

Gli heap dump sono pensati come strumenti di **debugging e diagnostica** (analisi di memory leak, profiling delle performance), non per essere esposti pubblicamente. Esistono formati diversi a seconda del runtime:

|Runtime|Formato|Tool di analisi tipico|
|---|---|---|
|Java (JVM)|`.hprof`|Eclipse MAT, `jhat`|
|Node.js / V8|`.heapsnapshot` (JSON)|Chrome DevTools (tab Memory)|

Il rischio principale non è tecnico ma di **esposizione**: molti framework offrono endpoint di diagnostica pronti all'uso, spesso lasciati accidentalmente accessibili senza autenticazione in ambienti di produzione o test — permettendo a chiunque di scaricare uno snapshot completo della memoria dell'applicazione.