# security-portfolio
Computer science student learning offensive security through hands-on practice. 
This repository documents my journey.

Everything here is built by doing: breaking things, understanding why they break, and writing it down.

---

## What's in here

```
security-portfolio/
├── writeups/
│   ├── metasploitable/   # exploits and post-exploitation on Metasploitable 2
│   └── ctf/picoctf/      # CTF challenge writeups
├── tools/
│   ├── port-scanner/     # TCP port scanner with banner grabbing (Python)
│   ├── hash-cracker/     # wordlist-based hash cracker for MD5/SHA (Python)
│   └── sqli-tester/      # basic SQL injection tester (Python)
├── fuzzing/              # coverage-guided fuzzing on open source libraries (AFL++)
└── hardware/
    ├── rfid-cloner/      # RFID tag reader/writer with Arduino + RC522
    └── bad-usb/          # HID injection demo with Digispark
```

---
## Stack

**Offensive tools** — Kali Linux, Metasploit, nmap, Burp Suite, sqlmap  
**Scripting** — Python, C  
**Fuzzing** — AFL++, libFuzzer, AddressSanitizer  
**Hardware** — Arduino, ESP32, Digispark

---
## Ethics

All activity in this repository is performed on machines I own or systems explicitly designed for security research (Metasploitable, DVWA, CTF platforms). 
Never use these techniques on systems you don't have explicit written permission to test.