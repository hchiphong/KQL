<h1>Intro</h1>

```.execute database script <|
.create table AuthenticationEvents (timestamp:datetime, hostname:string, src_ip:string, user_agent:string, username:string, result:string, password_hash:string, description:string)
.create table Email (timestamp:datetime, sender:string, reply_to:string, recipient:string, subject:string, verdict:string, link:string)
.create table Employees (hire_date:datetime, name:string, user_agent:string, ip_addr:string, email_addr:string, company_domain:string, username:string, role:string, hostname:string)
.create table FileCreationEvents (timestamp:datetime, hostname:string, username:string, sha256:string, path:string, filename:string, process_name:string)
.create table InboundNetworkEvents (timestamp:datetime, ['method']:string, src_ip:string, user_agent:string, url:string)
.create table OutboundNetworkEvents (timestamp:datetime, ['method']:string, src_ip:string, user_agent:string, url:string)
.create table PassiveDns (timestamp:datetime, ip:string, domain:string)
.create table ProcessEvents (timestamp:datetime, parent_process_name:string, parent_process_hash:string, process_commandline:string, process_name:string, process_hash:string, hostname:string, username:string)
.create table SecurityAlerts (timestamp:datetime, alert_type:string, severity:string, description:string, indicators:dynamic)
// Ingest data into tables
.ingest into table AuthenticationEvents ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/AuthenticationEvents.csv') with (ignoreFirstRecord = true)
.ingest into table Email ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/Email.csv') with (ignoreFirstRecord = true)
.ingest into table Employees ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/Employees.csv') with (ignoreFirstRecord = true)
.ingest into table FileCreationEvents ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/FileCreationEvents.csv') with (ignoreFirstRecord = true)
.ingest into table InboundNetworkEvents ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/InboundNetworkEvents.csv') with (ignoreFirstRecord = true)
.ingest into table OutboundNetworkEvents ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/OutboundNetworkEvents.csv') with (ignoreFirstRecord = true)
.ingest into table PassiveDns ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/PassiveDns.csv') with (ignoreFirstRecord = true)
.ingest into table ProcessEvents ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/ProcessEvents.csv') with (ignoreFirstRecord = true)
.ingest into table SecurityAlerts ('https://kustodetectiveagency.blob.core.windows.net/sans2023c0start/SecurityAlerts.csv') with (ignoreFirstRecord = true)
```



<h3>Question</h3> 
How many Craftperson Elf's are working from laptops?

<h3>Solution</h3> 

```
Employees
| where hostname endswith "LAPTOP"
| where role == 'Craftsperson Elf'
| summarize dcount( username)
```

<h3>anwser</h3> 

`23`
