# Kali Linux WSL Ninja

1. Install Kali Linux WSL fron Windows Store 

        https://www.microsoft.com/en-us/p/kali-linux/9pkr34tncv07?activetab=pivot:overviewtab
    
2. Open Kali Linux, follow the wizard for install define your username and password and reset root password

        sudo passwd
    
3. Add this path to Windows Defender as an exception

        C:\Users\usuario\AppData\Local\Packages\KaliLinux.*

#
The below cycle will use 13.37 GB more in your disk. Repeat it until you see that really were installed successfully at 100%.

    sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt install kali-linux-full kali-linux-all && sudo apt full-upgrade -y
#    
    sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt install git screen neofetch screenfetch synaptic lsb-release software-properties-common forensics-all forensics-all-gui forensics-extra-gui forensics-extra zipalign curl dirmngr apt-transport-https jq postgresql nginx sslstrip hping3 hashcat openvpn network-manager-openvpn-gnome gnome gdm3 gnome-tweaks gnome-tweak-tool synaptic caca-utils inetutils-traceroute python-nautilus gir1.2-nautilus-3.0 sshfs resolvconf nmap net-tools ssh gcc python2 python3 gimp php-mbstring php-gettext python-dev python-setuptools python-setuptools python-dev python-pip python3-pip gparted pvm-dev compiz ndisc6 steghide httrack mesa-utils ethtool build-essential macchanger gnome winbind wget nano git mercurial make pulseaudio libcanberra-pulse mpg123 libldap-2.4-2 libpulse0 libxml2 giflib-tools libc6 gtk2-engines gcc gcc-multilib g++ g++-multilib cmake gtk+2.0 gtk+3.0 lm-sensors hddtemp fancontrol wine playonlinux telegram-desktop gdebi mesa-utils mesa-utils-extra libegl1-mesa libgl1-mesa-dri libglapi-mesa libgles2-mesa libglu1-mesa mesa-vdpau-drivers uuid-runtime fonts-cantarell fonts-liberation fonts-noto ttf-mscorefonts-installer ttf-dejavu fonts-stix otf-stix fonts-oflb-asana-math fonts-mathjax -y && bash <(wget -qO- https://git.io/vAtmB) && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo apt update -y && sudo apt dist-upgrade -y && cd && neofetch
    
#
    sudo apt full-upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
    
# Add GUI xfce 

(select lightdm after execute this command)

    sudo apt install xfce4 xrdp -y && sudo /etc/init.d/xrdp start

