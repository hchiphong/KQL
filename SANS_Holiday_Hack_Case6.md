<h1>Intro</h1>

**The final step!**

Wow! You decoded those secret messages with easy! You're a rockstar. It seems like we're getting near the end of this investigation, but we need your help with one more thing...

We know that the attackers stole Santa's naughty or nice list. What else happened? Can you find the final malicious command the attacker ran?

<h3>Question</h3> 
What is the name of the executable the attackers used in the final malicious command?

**Query**

```
let ClickTime = datetime(2023-12-02T10:12:42Z);
ProcessEvents
| where timestamp > ClickTime
| where hostname == 'Y1US-DESKTOP'
| where process_commandline has "powershell"
| extend base64String = extract(@'\s+([A-Za-z0-9+/]{20}\S+$)', 1, process_commandline)
| extend DecodedCommandLine = base64_decode_tostring(base64String)
| where not(isempty(base64String) and isempty(DecodedCommandLine))
```

**Result**

```"timestamp": 2023-12-25T10:44:27Z,
"process_commandline": C:\Windows\System32\powershell.exe -Nop -ExecutionPolicy bypass -enc QzpcV2luZG93c1xTeXN0ZW0zMlxkb3dud2l0aHNhbnRhLmV4ZSAtLXdpcGVhbGwgXFxcXE5vcnRoUG9sZWZpbGVzaGFyZVxcYyQ=,
"hostname": Y1US-DESKTOP,
"username": alsnowball,
"DecodedCommandLine": C:\Windows\System32\downwithsanta.exe --wipeall \\\\NorthPolefileshare\\c$
```
`downwithsanta.exe`

<h3>Question</h3> 
What was the command line flag used alongside this executable?


**Result**

`--wipeall`
