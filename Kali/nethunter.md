## Building NetHunter

https://www.kali.org/docs/nethunter/building-nethunter/


```ShellSession
python3 build.py -d davinci-miui --ten -f -u -nf -su -fs full -r ni
```

## Install NetHunter Ninja


```ShellSession
echo -ne "\033]0;Updating\007" && clear;apt update && apt install kali-linux-nethunter kali-tools-top10 kali-linux-default kali-linux-large kali-linux-everything kali-tools-802-11 kali-tools-bluetooth kali-tools-crypto-stego kali-tools-database kali-tools-forensics kali-tools-fuzzing kali-tools-gpu kali-tools-hardware kali-tools-information-gathering kali-tools-passwords kali-tools-post-exploitation kali-tools-reporting kali-tools-reverse-engineering kali-tools-rfid kali-tools-sdr kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-voip kali-tools-vulnerability kali-tools-web kali-tools-windows-resources kali-tools-wireless  -y && apt-get autoclean && apt install -f && apt install aptitude -y && apt install neofetch -y && apt -f install && apt autoremove -y && apt-get clean cache && apt update && apt-get autoclean && apt-get clean cache && apt update -y && apt full-upgrade -y --allow-downgrades && dpkg --configure -a &&  grub-mkconfig && cd && aptitude upgrade --full-resolver -y && apt autoremove -y && neofetch && echo "(You can close the terminal now)
"
```