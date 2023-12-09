<h1>Intro</h1>

**Welcome to Operation Giftwrap: Defending the Geese Island network**

An urgent alert has just come in, 'A user clicked through to a potentially malicious URL involving one user.' This message hints at a possible security incident, leaving us with critical questions about the user's intentions, the nature of the threat, and the potential risks to Santa's operations. Your mission is to lead our security operations team, investigate the incident, uncover the motives behind email, assess the potential threats, and safeguard the operations from the looming cyber threat.

The clock is ticking, and the stakes are high - are you up for this exhilarating challenge? Your skills will be put to the test, and the future of Geese Island's digital security hangs in the balance. Good luck!

The alert says the user clicked the malicious link 'hxxp:[//]madelvesnorthpole[.]org/published/search/MonthlyInvoiceForReindeerFood.docx'



<h3>Question</h3> 
What is the email address of the employee who received this phishing email?

<h3>Solution</h3> 

```
Email
| where link == 'http://madelvesnorthpole.org/published/search/MonthlyInvoiceForReindeerFood.docx'
```

**Result**
```
alabaster_snowball@santaworkshopgeeseislands.org
```

<h3>Question</h3> 
What is the email address that was used to send this spear phishing email?

**Result**
```
cwombley@gmail.com
```


<h3>Question</h3> 
What was the subject line used in the spear phishing email?

```
[EXTERNAL] Invoice foir reindeer food past due
```




