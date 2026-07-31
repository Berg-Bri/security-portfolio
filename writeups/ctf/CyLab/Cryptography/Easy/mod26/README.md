#### 🧩Descrizione

_"La crittografia può essere facile, sai cos'è ROT13?"_

#### 🔍Analisi / Ricognizione

Viene fornita questa stringa:

```
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}
```

#### ⚙️Sfruttamento

Dalla stringa e dalla descrizione della challenge si capisce subito che si parla di un cifrario di Cesare con chiave 13 (ROT13), stesso schema già visto nella sfida precedente. Applicando la trasformazione si ottiene la flag.

#### 🚩Flag

`picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}`

#### 💡Lezioni apprese

Il testo della flag stessa contiene una battuta interna sul funzionamento di ROT13: applicarlo due volte di seguito non aumenta la sicurezza, anzi riporta esattamente al testo originale in chiaro. Questo perché ROT13 sposta ogni lettera di 13 posizioni su un alfabeto di 26 lettere — applicarlo due volte significa uno spostamento totale di 26, equivalente a un giro completo (26 mod 26 = 0), quindi un no-op. È un promemoria pratico che "applicare di nuovo la stessa trasformazione" non equivale a rafforzarla, specialmente con cifrari a rotazione fissa.