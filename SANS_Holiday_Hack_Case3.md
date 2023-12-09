<h1>Intro</h1>

**That's not good. What happened next?**

The victim is Alabaster Snowball? Oh no... that's not good at all! Can you try to find what else the attackers might have done after they sent Alabaster the phishing email?

Use our various security log datasources to uncover more details about what happened to Alabaster.



<h3>Question</h3> 
What time did Alabaster click on the malicious link? Make sure to copy the exact timestamp from the logs!



**Query**

```
OutboundNetworkEvents
| where src_ip == '10.10.0.4'
| where url == 'http://madelvesnorthpole.org/published/search/MonthlyInvoiceForReindeerFood.docx'
```

**Result**
```
2023-12-02T10:12:42Z
```

<h3>Question</h3> 
What file is dropped to Alabaster's machine shortly after he downloads the malicious file?

**Query**

```
let ClickTime = datetime(2023-12-02T10:12:42Z);
FileCreationEvents
| where timestamp between ( ClickTime .. ( ClickTime + 1min) )
| where hostname == 'Y1US-DESKTOP'
```

**Result**

```
"timestamp": 2023-12-02T10:14:21Z,
"hostname": Y1US-DESKTOP,
"username": alsnowball,
"sha256": 4c199019661ef7ef79023e2c960617ec9a2f275ad578b1b1a027adb201c165f3,
"path": C:\ProgramData\Windows\Jolly\giftwrap.exe,
"filename": giftwrap.exe,
"process_name": explorer.exe
```
