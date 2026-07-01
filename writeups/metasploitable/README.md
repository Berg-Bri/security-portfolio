# Metasploitable 2 — Lab Writeup

Writeup progressivo del lab su Metasploitable 2, diviso per fasi. Ogni sezione viene aggiornata man mano che procedo con ricognizione, enumerazione ed exploitation.

---

## 1. Ricognizione — Nmap Scan

### Info target

- **IP:** `192.168.56.101`
- **OS:** Ubuntu Linux 32-bit
- **Data scan:** 10/06/2026

### Comando usato

```bash
nmap -sV 192.168.56.101
```

### Risultati

|Porta|Stato|Servizio|Versione|
|---|---|---|---|
|21/tcp|open|ftp|vsftpd 2.3.4|
|22/tcp|open|ssh|OpenSSH 4.7p1 Debian 8ubuntu1|
|23/tcp|open|telnet|Linux telnetd|
|25/tcp|open|smtp|Postfix smtpd|
|53/tcp|open|domain|ISC BIND 9.4.2|
|80/tcp|open|http|Apache httpd 2.2.8|
|139/tcp|open|netbios-ssn|Samba smbd 3.X - 4.X|
|445/tcp|open|netbios-ssn|Samba smbd 3.X - 4.X|
|1099/tcp|open|java-rmi|GNU Classpath grmiregistry|
|1524/tcp|open|bindshell|Metasploitable root shell|
|2049/tcp|open|nfs|2-4 (RPC #100003)|
|3306/tcp|open|mysql|MySQL 5.0.51a|
|5432/tcp|open|postgresql|PostgreSQL DB 8.3.0|
|5900/tcp|open|vnc|VNC (protocol 3.3)|
|6667/tcp|open|irc|UnrealIRCd|
|8180/tcp|open|http|Apache Tomcat|

### Osservazioni

- **vsftpd 2.3.4** (porta 21): versione con backdoor nota, primo target da exploitare
- **Porta 1524**: shell root letteralmente aperta, basta connettersi con netcat
- **UnrealIRCd** (porta 6667): altra backdoor documentata
- **Telnet** (porta 23): protocollo in chiaro, credenziali visibili su rete
- **MySQL** (porta 3306): database esposto senza firewall
- **Tomcat** (porta 8180): vulnerabile a deploy WAR malizioso
- **VNC** (porta 5900): accesso desktop remoto aperto

---

## 2. Vulnerability Assessment

### Metodologia

Per ogni servizio trovato con nmap, ho cercato exploit pubblici con `searchsploit` e su CVE Details.

### Servizi analizzati

#### vsftpd 2.3.4 (porta 21)

- **searchsploit result:** _da completare_
- **CVE:** _da completare_
- **Gravità:** _da completare_
- **Note:** _da completare_

#### UnrealIRCd (porta 6667)

- **searchsploit result:** _da completare_
- **CVE:** _da completare_
- **Gravità:** _da completare_
- **Note:** _da completare_

<!-- Prossimi servizi da valutare, in ordine di priorità (vedi osservazioni sopra): - Porta 1524 (bindshell) - Samba smbd (139/445) - Tomcat 8180 - MySQL 3306 - VNC 5900 -->

---

## 3. Exploitation

_Sezione da completare man mano che sblocco gli exploit._

---

## 4. Post-exploitation

_Sezione da completare._