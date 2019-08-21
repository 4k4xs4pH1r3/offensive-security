### How to Install VMware Workstation

Last test and verifed: 20 July 2019
#

Close VMware
#
## For Ubuntu Disco

    sudo apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y && sudo apt-get install linux-headers-$(uname -r) -y && sudo apt-get install libcanberra-gtk* libcanberra-gtk-module:i386 -y && wget https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle && chmod +x VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle && ./VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle
    
## For Debian Buster amd64
    
    sudo -
#    
    export PATH=/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin && export PATH=$PATH:/usr/local/sbin:/usr/local/bin && sudo apt-get install aptitude -y && sudo aptitude install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib linux-headers-$(uname -r) -y && cd /var/cache/debconf && rm *.dat &&  wget http://ftp.us.debian.org/debian/pool/main/libc/libcanberra/libcanberra-gtk-module_0.30-7_amd64.deb && chmod +x *.deb && dpkg -i *deb && wget https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle && chmod +x VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle && ./VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle
    
    
## For Debian Buster i386
sudo -
#    
    export PATH=/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin && export PATH=$PATH:/usr/local/sbin:/usr/local/bin && sudo apt-get install aptitude -y && sudo aptitude install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib linux-headers-$(uname -r) -y && cd /var/cache/debconf && rm *.dat && wget http://ftp.us.debian.org/debian/pool/main/libc/libcanberra/libcanberra-gtk-module_0.30-7_i386.deb && chmod +x *.deb && dpkg -i *deb && wget https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle && chmod +x VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle && ./VMware-Workstation-Full-15.1.0-13591040.x86_64.bundle
    
#
#   
Check the VMware installation status

    sudo vmware-modconfig --console --install-all

You'll see that there are issues with monitor and net, thas ok.
#
#
#
Install the VMware Host modules

    cd && wget https://github.com/mkubecek/vmware-host-modules/archive/workstation-15.1.0.tar.gz && tar -xzf workstation-15.1.0.tar.gz && cd vmware-host-modules-workstation-15.1.0 && make && make install && /etc/init.d/vmware restart && sudo dpkg --configure -a && sudo grub-mkconfig && tar -cf vmmon.tar vmmon-only && tar -cf vmnet.tar vmnet-only && cp -v vmmon.tar vmnet.tar /usr/lib/vmware/modules/source/ && vmware-modconfig --console --install-all && sudo dpkg --configure -a && sudo grub-mkconfig 
    
Verify your kernel version

        uname -r

Based on the result replace the value in the below line "VM_UNAME" and execute

    make VM_UNAME='5.0.0-16-generic' && make install && vmware-modconfig --console --install-all && sudo dpkg --configure -a && sudo grub-mkconfig
#
    

Generate a key MOK

    openssl req -new -x509 -newkey rsa:2048 -keyout VMWARE15.priv -outform DER -out VMWARE15.der -nodes -days 36500 -subj "/CN=VMWARE/"

You'll see info that it did it ok.
#
#

Install the drivers modules
#
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./VMWARE15.priv ./VMWARE15.der $(modinfo -n vmmon)
#
    sudo /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 ./VMWARE15.priv ./VMWARE15.der $(modinfo -n vmnet)
#
#
This does not give any feedback
#
#
#
#
Check the modules installed

    tail $(modinfo -n vmmon) | grep "Module signature appended"

You should get:

    Binary file (standard input) matches
    
# Only for UEFI
Request the VMware 15 sign key enrollment MOK 

    sudo mokutil --import VMWARE15.der

This will ask you for set a new password
#
# Update Grub

    sudo dpkg --configure -a && sudo grub-mkconfig
#
#
#
## Reboot your Linux

Once restarted should be presented with a menu with blue screen background, you have to make your way to enroll the key and enter the password you just created, this happens only once, then continue to boot / reboot.

## Only for UEFI
Test the driver/module installed correctly enter the command

    cd /root/vmware-host-modules-workstation-15.1.0 && mokutil --test-key VMWARE15.der && cd

You should get 
    
    VMWARE15.der is already enrolled

That means the VMWare keys now are signed.

Note: UEFI Secure Boot is working only for Linux VM's by now.

#


All credits to OP.
    
#
Open VMware and enjoy ;)



