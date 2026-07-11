#### Tool usati
steghide
#### Descrizione
Ti viene data un’immagine JPG apparentemente ordinaria. Qualcosa è nascosto fuori dalla vista all'interno del file. Il vostro compito è quello di scoprire il carico utile nascosto ed estrarre la bandiera.
#### Analisi / Ricognizione
Come spesso accade, se viene fatto scaricare un file pdf, jpeg o png è spesso fondamentale controllare i metadati.
Cosi sono partito da quello.
#### Sfruttamento
Con il comando:
```bash
exiftool img.png
```
Il campo *comment* era una stringa codificata in base 64.

Allora ho eseguito la decodifica su quest'ultimo:
```bash 
echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 --decode
steghide:cEF6endvcmQ=                                                
```                                                            
L'output contiene la parola *steghide* che è il tool usato per nascondere dati nelle immagini e una seconda stringa in bas64.

Ho decodificato anche l'ultima stringa ottenendo la password:
```bash
echo "cEF6endvcmQ=" | base64 --decode                
pAzzword
```

Controllo se nell'immagine ci sono dati nascosti:
```bash
steghide --info img.jpg
```

Una volta controllato che effettivamente ci sono dati nascosti ho fattol'estrazione:
```bash
steghide extract -sf img.jpg -p pAzzword
```
estraendo il file flag.txt contenente la flag.
#### Flag
picoCTF{h1dd3n_1n_1m4g3_871ba555}