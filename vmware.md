### How to Install VMware 15 in Linux with Kernel: 4              
#
    wget https://www.vmware.com/go/getworkstation-linux
#
    apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y
#
    sudo apt-get install linux-headers-$(uname -r) -y
#
    chmod +x getworkstation-linux
#
    ./getworkstation-linux
#
    sudo dpkg --configure -a
#
    sudo grub-mkconfig
#
Open VMware and enjoy ;)  
