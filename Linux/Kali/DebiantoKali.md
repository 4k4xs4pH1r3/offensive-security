# Login as root
```
sudo -i
```
----------

Edit APT Repo
----------
```
sudo nano /etc/apt/sources.list
```
Add this repos
```
deb https://deb.debian.org/debian/ bookworm main contrib non-free non-free-firmware
deb-src https://deb.debian.org/debian/ bookworm main
deb https://security.debian.org/debian-security bookworm-security main
deb-src https://security.debian.org/debian-security bookworm-security main
deb https://deb.debian.org/debian/ bookworm-updates main
deb-src https://deb.debian.org/debian/ bookworm-updates main
```


## Debian Bookworm Ninja
```
apt clean && apt update -y && apt install sudo gdebi dirmngr aptitude -y && sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt full-upgrade -y
```

### Add Kali Repo for Debian

On a standard, clean install of Debian Distro Based Linux, you should have the following entry present in /etc/apt/sources.list:
```
sudo nano /etc/apt/sources.list
```

For Parrot Security add here
```
sudo nano /etc/apt/sources.list.d/parrot.list
```
#       
    deb https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware
    deb-src https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware
 #      
```
sudo apt install dirmngr -y && apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6 && wget https://kali.download/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_2024.1_all.deb && apt --fix-broken install && dpkg -i ./kali-archive-keyring_2024.1_all.deb && rm kali-archive-keyring_2024.1_all.deb && apt-get update -y && apt-get install neofetch lolcat -y && echo "Activated Kali Ninja Repos"
```      

### Convert Debian Bookworm Ninja to Kali Ninja
```
sudo apt install aptitude -y && apt-get autoclean && apt-get clean cache && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update -y && apt-get dist-upgrade -y && apt-get full-upgrade -y && sudo apt-get update -y && apt-get full-upgrade -y && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig
```

Now reboot your machine to complete the conversion of Debian to Kali


### Install Kali Extras
```
sudo apt install aptitude -y && aptitude install locales -y && locale-gen en_US.UTF-8 && localedef -i en_US -f UTF-8 en_US.UTF-8 && export LANGUAGE=en_US.UTF-8 && export LANG=en_US.UTF-8 && export LC_ALL=en_US.UTF-8 && locale-gen en_US.UTF-8 && apt-get update -y && apt-get full-upgrade -y && aptitude install wget -y && apt-get autoclean && apt-get clean cache && apt update -y && aptitude install kali-linux-default kali-linux-everything kali-linux-large -y && apt-get full-upgrade -y
```
