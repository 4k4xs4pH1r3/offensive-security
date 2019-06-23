# Kali Linux WSL Ninja

1. Install Kali Linux WSL fron Windows Store 

        https://www.microsoft.com/en-us/p/kali-linux/9pkr34tncv07?activetab=pivot:overviewtab
    
2. Open Kali Linux, follow the wizard for install define your username and password and reset root password

        sudo passwd
    
3. Add this path to Windows Defender as an exception

        C:\Users\usuario\AppData\Local\Packages\KaliLinux.*

#
Repeat the below cycle until you see that really were installed successfully at 100%, this step will use 13.37 GB more in your disk

    sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt install kali-linux-full kali-linux-all git gnome gdm3 screen neofetch screenfetch synaptic lsb-release software-properties-common curl dirmngr apt-transport-https openssh-server jq postgresql nginx libesedb-utils openvpn network-manager-openvpn-gnome resolvconf -y && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig
    
#
    sudo apt full-upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y
