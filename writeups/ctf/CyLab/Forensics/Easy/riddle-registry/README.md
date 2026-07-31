#### 🛠️Tool usati

- [[exiftool]]
- [[base64]]

#### 🧩Descrizione

Ciao, intrepido investigatore! 📄🔍 Ti sei imbattuto in un PDF peculiare pieno di ciò che sembra nient'altro che una sciocchezza. Ma attenzione! Non tutto è come appare. In mezzo al caos si trova un tesoro nascosto, una bandiera sfuggente che aspetta di essere scoperta.

#### 🔍Analisi / Ricognizione

Viene fatto scaricare un file dove vengono date molte informazioni inutili, anche quelle "nascoste" dalle sottolineature nere.

#### ⚙️Sfruttamento

Sono partito con il leggere i metadati del pdf con il tool `exiftool`:

```bash
exiftool confidential.pdf                       
ExifTool Version Number         : 13.50
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2026:07:11 16:27:56+02:00
File Access Date/Time           : 2026:07:11 16:27:57+02:00
File Inode Change Date/Time     : 2026:07:11 16:27:56+02:00
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV8zNTc4NzM5YX0=
```

Ho notato che il campo Author aveva una stringa molto simile alle classiche stringhe in base64.

Così ho applicato la decodifica e ho ottenuto la flag:

```bash
echo "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV8zNTc4NzM5YX0=" | base64 --decode 
picoCTF{puzzl3d_m3tadata_f0und!_3578739a}
```

#### 🚩Flag

picoCTF{puzzl3d_m3tadata_f0und!_3578739a}

#### 💡Lezioni apprese

- I campi metadata di un PDF (Author, Producer, Title, ecc.) sono un nascondiglio classico: `exiftool` li mostra tutti in un colpo solo, prima ancora di guardare il contenuto visibile del documento.
- Elementi visivi "distraenti" nel PDF (testo nascosto da sottolineature, riempitivo inutile) possono essere un depistaggio: conviene controllare i metadati prima di perdere tempo a decifrare il contenuto visivo.
- Una stringa che termina con `=` o `==` è quasi sempre un indizio di base64: vale la pena provare subito la decodifica.