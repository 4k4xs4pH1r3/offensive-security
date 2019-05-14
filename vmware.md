### How to Install VMware Workstation in Linux with Kernel 4              
#
    sudo apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y
#
    sudo apt-get install linux-headers-$(uname -r) -y
#
    wget https://www.vmware.com/go/getworkstation-linux && chmod +x getworkstation-linux && ./getworkstation-linux
#
    sudo dpkg --configure -a
#
    sudo grub-mkconfig
#
Open VMware and enjoy ;)  
