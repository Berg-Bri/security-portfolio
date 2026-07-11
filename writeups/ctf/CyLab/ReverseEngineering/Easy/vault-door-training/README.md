#### Tool usati

#### Descrizione
La tua missione consiste nell'infiltrarti nel laboratorio del Dottor Male e recuperare i progetti del suo "Progetto Apocalisse". Il laboratorio è protetto da una serie di porte blindate; ciascuna di esse è gestita da un computer e richiede una password per l'apertura. Purtroppo, i nostri agenti sotto copertura non sono riusciti a ottenere le password segrete, ma uno dei nostri agenti alle prime armi ha recuperato il codice sorgente del computer di ogni porta! Dovrai analizzare il codice sorgente di ciascun livello per scoprire la password della relativa porta blindata. Come esercizio preliminare, abbiamo realizzato una replica del caveau presso il nostro centro di addestramento.
#### Analisi / Ricognizione
Viene dato fornito il codice sorgente su come viene controllata la password.
In questo caso nel codice viene mostrato anche il valore che la password deve assumere per essere considerata valida.
#### Sfruttamento
Ho analizzato come veniva utilizzato il substring e inserito la password che richiedeva la verifica, così da ottenere la flag.
#### Flag
picoCTF{w4rm1ng_Up_w1tH_jAv4_000HPpgh7Ph}