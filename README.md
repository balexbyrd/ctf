GITHUB README MARKDOWN
----
https://guides.github.com/features/mastering-markdown/

KALI LINUX
----
http://www.blackmoreops.com/2014/04/08/detailed-guide-installing-kali-linux-on-virtualbox/

everything worked except up to the last step to install the guest additions (which is important for having a shared clipboard)

solution here:

https://forums.kali.org/showthread.php?18973-Issues-installing-VirtualBox-Guest-Additions

ran:
````
uname -r
aptitude install linux-headers-3.12-kalil-amd64
./VBoxLinuxAdditions.run
````

CH1
----
hosterbox's ftp server at 184.22.118.62:2082


CH2
----
pretty printing json
````
print json.dumps(<json>,  sort_keys=True, indent=4, separators=(',',':'))
````

free ssh account
----
ssh lawmicha@sdf.org

pass: compsex
