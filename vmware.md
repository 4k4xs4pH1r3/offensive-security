### How to Install VMware Workstation in Ubuntu Disco       
#
    sudo apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y
#
    sudo apt-get install linux-headers-$(uname -r) -y
#
    sudo apt-get install libcanberra-gtk-module libcanberra-gtk-module:i386 libcanberra-gtk-module && wget https://www.vmware.com/go/getworkstation-linux && chmod +x getworkstation-linux && ./getworkstation-linux
#
#   
Run this

    sudo vmware-modconfig --console --install-all

You'll see that there are issues with monitor and net, thas ok.

Generate a key

    openssl req -new -x509 -newkey rsa:2048 -keyout VMWARE15.priv -outform DER -out VMWARE15.der -nodes -days 36500 -subj "/CN=VMWARE/"

You'll see info that it did it ok.

Install the drivers modules
#
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./VMWARE15.priv ./VMWARE15.der $(modinfo -n vmmon)
#
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./VMWARE15.priv ./VMWARE15.der $(modinfo -n vmnet)
#
#
This does not give any feedback

Check the modules installed

    tail $(modinfo -n vmmon) | grep "Module signature appended"

You should get Binary file (standard input) matches

Have key signed on reboot

    sudo mokutil --import VMWARE15.der

This will ask you for a password, enter some new password a bit long like 1515vmware. Reenter same password

Reboot, When reboot you should be presented with a menu with blue screen background, you have to make your way to enroll the key and enter the password you just created, this happens only once, then continue to boot / reboot.

To test the driver / module installed correctly enter the command

    mokutil --test-key VMWARE15.der

You should get 
    
    VMWARE15.der is already enrolled

and that means VMWare now is working, with UEFI

Note: (Secure Boot is not working by now).

All credits to OP.
#    
    sudo dpkg --configure -a
#
    sudo grub-mkconfig
#
Open VMware and enjoy ;)
