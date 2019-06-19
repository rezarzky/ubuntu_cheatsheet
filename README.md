# Ubuntu Command That I Always Forgot

## Firewall
***
using ufw firewall (Uncomplicated Firewall) -PS:Always use sudo

##### Install UFW
```
sudo apt-get install ufw
```
##### See the Firewall Status UFW
```
sudo ufw status
sudo ufw status verbose
```
##### See the Firewall Status UFW
```
sudo ufw status
sudo ufw status verbose
```
##### Block Specific IP & port UFW
```
sudo ufw deny from {ip-address-here} to any port {port-number-here}
```
##### Enable/Disable UFW
```
sudo ufw enable/disable
```
##### Configure UFW
```
sudo ufw allow ssh #allow ssh
sudo ufw allow 25 #allow port
sudo ufw default deny incoming #set default to deny
sudo ufw default allow outgoing #set default to allow
sudo ufw delete allow ssh #delete allow port/service
sudo ufw reset #ufw reset rules
```
##### UFW delete Nubered role
```
sudo ufw status numbered
sudo ufw delete {number}
```

## SSH Server
***
##### Install SSH Server
```
sudo apt install openssh-server
```
##### Check SSH Status
```
systemctl status ssh
```
##### Starting SSH/Stopping SSH
```
systemctl stop/start ssh
```
##### SSH service to start during system boot run:
```
systemctl enable/disable ssh
```
##### Configure SSH
```
nano /etc/ssh/sshd_config
```
##### Reload SSH
```
service ssh reload
```

## VPNSERVER
***
##### Softether
[Instalation](https://www.digitalocean.com/community/tutorials/how-to-setup-a-multi-protocol-vpn-server-using-softether)
##### OpenVPN
[Instalation](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-18-04)

## HAPROXY
***
Load balancing & Routing
##### Install Haproxy
```
apt-get install haproxy
```
##### Setting Haproxy
```
sudo nano /etc/haproxy/haproxy.cfg
```
##### Restart Haproxy
```
systemctl restart haproxy.service
```

# Kill Process
***
##### Kill process running under certain port:
```
sudo fuser -k -n tcp 8000

```



## Services
***

#### Service Commands
Use the service command *(Requires sudo)*
```
service ssh status      (service status)
service --status-all    (all services status)
```


Almost every service has the following commands, some may have more like apache `graceful-restart`:
```
service servicename start
service servicename stop
service servicename restart
service servicename status
service servicename force-reload
```

#### Autostart

Add Service links:
```
sudo update-rc.d servicename defaults
```

Whether you get a warning if they already exist or not, enable it now:
```
sudo update-rc.d servicename enable
```

#### Remove Autostart
Pass the Force flag
```
sudo update-rc.d -f servicename remove
```


#### Autostart Daemons

There is are several startup popular daemons: 
- CentOS uses SystemV 
- Ubuntu 14 uses Upstart
- Ubuntu 14.10+ uses SystemD (15, 16, 17..)

Focus on **SystemD**. 

#### SystemD Commands
This would only apply to Ubuntu 14.10+, otherwise you would use Upstart.

```
systemctl     <-- You'll use this more often 
journalctl    <-- You'll use this more often
update-rc.d   <-- You'll use this more often
                  --------------------------
                  Installs/Removes System-V style init script links
                  Note: System-V Style, but it's really SystemD. (Confusing huh?)

                  "NNname" is the runlevel, lower means startup sooner
                  ----------------------------------------------------
                  The Location is: /etc/rcrunlevel.d/NNname  
                  The Target is:   /etc/init.d/name.
notify 
analyze 
cgis 
cgtop 
loginctl 
nspawn
```

# Shutdown
***
```
shutdown
reboot
shutdown -h now
shutdown -h +10     (shutdown 10 mins)
shutdown -r now     (reboot now)
```

# Compress/UnCompress
***
##### Uncompress
```
gzip -dvk file.txt.gz     
bzip2 -d file.txt.bz2
tar -xvf file.tar
tar -zxvf file.tar.gz
unzip test.zip
```
##### Compress
```
gzip -vk file.txt                   (Creates file.txt.gz)
bzip2 file.txt                      (Creates  file.txt.bz2)
tar -cvf file.tar file.txt          (Creates tar)
tar -czvf file.tar.gz file.txt      (Creates tar.gz)
zip filename.zip file.txt           (Creates filename.zip)
zip -r folder.zip path/to/folder    (Creates  folder.txt.bz2)
```

# Running Process on Background
***
##### Using TMUX on ssh terminal
```
tmux #start this on SSH Terminal
tmux attach #open tmux session
exit #close tmux
```

# Checking Information
***
##### Check cpu information
```
1. /proc/cpuinfo
2. lscpu
3. hardinfo
```

# Switch User on Terminal
***
##### Check current user
```
whoami
```
##### Check current user
```
sudo -u [username]
ex:
sudo -u User2 zsh
```