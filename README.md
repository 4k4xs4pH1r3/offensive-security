# Kali Linux WSL Ninja

Repeat the below cycle until you see that really were installed 100%

    sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt install kali-linux-full kali-linux-all git gnome gdm3 screen neofetch screenfetch synaptic lsb-release software-properties-common curl dirmngr apt-transport-https openssh-server jq postgresql nginx libesedb-utils openvpn network-manager-openvpn-gnome resolvconf -y && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig
    
#
    sudo apt full-upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
