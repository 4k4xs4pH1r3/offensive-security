## Create NetHunter Installer

Tested 6 Feb 2023

Kali Linux Last Version 2023.1.2

Linux-image-6.0.0-kali6-arm64 (6.0.12-1kali1)

https://www.kali.org/docs/nethunter/building-nethunter/
https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-devices

### Xiaomi 9T Pro aka davinci 
Code Name: raphael/raphaelin / Android 13 / Rom = Evolution X

```ShellSession
python3 build.py -d davinci-miui --ten -f -u -nf -su -fs full -r ni
```

### Samsung Galaxy S20 FE 5G (Snapdragon) aka r8q 
Android 13 / Rom = ProjectX / arch = arm64 / author = Svirusx

```ShellSession
python3 build.py -d r8q-thirteen --thirteen -f -u -nf -su -fs full -r ni
```

## Activate NetHunter Ninja


```ShellSession
echo -ne "\033]0;Updating\007" && clear;apt update && apt install kali-linux-nethunter kali-linux-labs kali-tools-top10 kali-linux-default kali-linux-large kali-linux-everything kali-linux-arm kali-desktop-core kali-desktop-gnome kali-desktop-lxde kali-desktop-xfce kali-tools-802-11 kali-tools-bluetooth kali-tools-crypto-stego kali-tools-database kali-tools-forensics kali-tools-fuzzing kali-tools-gpu kali-tools-hardware kali-tools-information-gathering kali-tools-passwords kali-tools-post-exploitation kali-tools-reporting kali-tools-reverse-engineering kali-tools-rfid kali-tools-sdr kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-voip kali-tools-vulnerability kali-tools-web kali-tools-windows-resources kali-tools-wireless  -y && apt-get autoclean && apt install -f && apt install aptitude -y && apt install neofetch -y && apt -f install && apt autoremove -y && apt-get clean cache && apt update && apt-get autoclean && apt-get clean cache && apt update -y && apt full-upgrade -y --allow-downgrades && dpkg --configure -a &&  grub-mkconfig && cd && aptitude upgrade --full-resolver -y && apt autoremove -y && neofetch && apt install aptitude -y && aptitude install locales -y && locale-gen en_US.UTF-8 && localedef -i en_US -f UTF-8 en_US.UTF-8 && export LANGUAGE=en_US.UTF-8 && export LANG=en_US.UTF-8 && export LC_ALL=en_US.UTF-8 && locale-gen en_US.UTF-8 && apt-get update -y && apt-get full-upgrade -y && aptitude install wget -y && apt-get install python3 python3-venv python3-pip -y && apt-get autoclean && apt-get clean cache && apt update -y && aptitude install kali-linux-default kali-linux-everything kali-linux-large -y && apt-get full-upgrade -y && echo "(You can close the terminal now)
"
```
