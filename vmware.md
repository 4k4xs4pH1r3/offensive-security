### How to Install VMware Workstation in Linux            
#
    sudo apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y
#
    sudo apt-get install linux-headers-$(uname -r) -y
#
    sudo apt-get install libcanberra-gtk-module libcanberra-gtk-module:i386 libcanberra-gtk-module && wget https://www.vmware.com/go/getworkstation-linux && chmod +x getworkstation-linux && ./getworkstation-linux
#
#   
    sudo vmware-modconfig --console --install-all
#
    openssl req -new -x509 -newkey rsa:2048 -keyout VMWARE.priv -outform DER -out VMWARE.der -nodes -days 36500 -subj "/CN=VMWARE/"
#
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./VMWARE.priv ./VMWARE.der $(modinfo -n vboxdrv)
#
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./VMWARE.priv ./VMWARE.der $(modinfo -n vboxdrv)
mokutil --import MOK.der

    tail $(modinfo -n vboxdrv) | grep "Module signature appended"
    
    sudo mokutil --import VMWARE.der
#    
    sudo dpkg --configure -a
#
    sudo grub-mkconfig
#
Open VMware and enjoy ;)  


https://kb.vmware.com/s/article/2146460

https://askubuntu.com/questions/1096052/vmware-15-error-on-ubuntu-18-4-could-not-open-dev-vmmon-no-such-file-or-dire
