<h1>Intro</h1>

**Someone got phished! Let's dig deeper on the victim...**

Nicely done! You found evidence of the spear phishing email targeting someone in our organization. Now, we need to learn more about who the victim is!

If the victim is someone important, our organization could be doomed! Hurry up, let's find out more about who was impacted!



<h3>Question</h3> 
What is the role of our victim in the organization?

<h3>Solution</h3> 

```
Employees
|   where email_addr == 'alabaster_snowball@santaworkshopgeeseislands.org'
```

**Result**
```
Head Elf
```

<h3>Question</h3> 
What is the hostname of the victim's machine?

**Result**

```
Y1US-DESKTOP
```


<h3>Question</h3> 
What is the source IP linked to the victim?


**Result**
```
10.10.0.4
```




