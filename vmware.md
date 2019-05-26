### How to Install VMware Workstation in Linux            
#
    sudo apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y
#
    sudo apt-get install linux-headers-$(uname -r) -y
#
    sudo apt-get install libcanberra-gtk-module libcanberra-gtk-module:i386 libcanberra-gtk-module && wget https://www.vmware.com/go/getworkstation-linux && chmod +x getworkstation-linux && ./getworkstation-linux && vmware-modconfig --console --install-all
#
    openssl req -new -x509 -newkey rsa:2048 -keyout MOK.priv -outform DER -out MOK.der -nodes -days 36500 -subj "/CN=VMware/"
#
    sudo /usr/src/linux-headers-`uname -r`/scripts/sign-file sha256 ./MOK.priv ./MOK.der $(modinfo -n vmmon)
#
    sudo /usr/src/linux-headers-`uname -r`/scripts/sign-file sha256 ./MOK.priv ./MOK.der $(modinfo -n vmnet)
#
    mokutil --import MOK.der
#    
    sudo dpkg --configure -a
#
    sudo grub-mkconfig
#
Open VMware and enjoy ;)  


https://kb.vmware.com/s/article/2146460
