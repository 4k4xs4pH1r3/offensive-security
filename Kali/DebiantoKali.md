----------

Edit APT Repo
----------
```
nano /etc/apt/sources.list
```
Add this repo
```
deb http://ftp.debian.org/debian/ stretch main contrib non-free
```


## Debian Buster Ninja
```
apt clean && apt update -y && apt install sudo gdebi dirmngr aptitude -y && sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt full-upgrade -y
```

### Add Kali Repo for Debian

On a standard, clean install of Debian Distro Based Linux, you should have the following entry present in /etc/apt/sources.list:

    nano /etc/apt/sources.list
       
For Parrot Security add here

    nano /etc/apt/sources.list.d/parrot.list
#       
    deb http://http.kali.org/kali kali-rolling main contrib non-free
    deb-src http://http.kali.org/kali kali-rolling main contrib non-free
 #      
```
sudo apt install dirmngr -y && sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6
```      

### Integrate Kali with Debian
```
sudo apt install aptitude -y && apt-get autoclean && apt-get clean cache && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update -y && apt-get full-upgrade -y && sudo apt-get update -y && apt-get full-upgrade -y && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig
```
