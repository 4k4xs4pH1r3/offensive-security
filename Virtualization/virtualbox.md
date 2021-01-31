# Ubuntu Groovy Gorilla | Focal | Eoan | Disco

Tested and verifed: 30 January 2021

    su
#    
    cd ~/ && mkdir Downloads
#

    nano /etc/apt/sources.list
#
    deb http://us.archive.ubuntu.com/ubuntu eoan main
    deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian eoan contrib

#

    wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add - && sudo apt-get update -y && apt install libvpx5 -y

#

    cd ~/Downloads && wget https://download.virtualbox.org/virtualbox/6.1.16/virtualbox-6.1_6.1.16-140961~Ubuntu~eoan_amd64.deb && chmod +x virtualbox-*.deb && dpkg -i virtualbox-*.deb && apt install -f -y
    
#    

Reboot and Enjoy
    
    
    
# Ubuntu Bionic

    su
    
    cd ~/ && mkdir Downloads
#

    nano /etc/apt/sources.list


    deb http://us.archive.ubuntu.com/ubuntu bionic main
    deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian bionic contrib

#

    wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add - && sudo apt-get update -y && apt install libvpx5 -y

#

    cd ~/Downloads && wget https://download.virtualbox.org/virtualbox/6.1.16/virtualbox-6.1_6.1.16-140961~Ubuntu~eoan_amd64.deb && chmod +x virtualbox-*.deb && dpkg -i virtualbox-*.deb && apt install -f -y
    
    
For Install VirtualBox 6.1 in Ubuntu 18.04.3 LTS x86_64 use:

        
    cd ~/Downloads && wget https://download.virtualbox.org/virtualbox/6.1.16/virtualbox-6.1_6.1.16-140961~Ubuntu~eoan_amd64.deb && chmod +x virtualbox-*.deb && dpkg -i virtualbox-*.deb && apt install -f -y && sudo apt update -y && sudo apt install --reinstall linux-headers-$(uname -r) virtualbox-dkms dkms

Then reboot your system and after reboot run this command:

    sudo modprobe vboxdrv
    
#    

Reboot and Enjoy
    
# Install virtualbox in Kali Linux or Parrot Security

    su
    
    cd ~/ && mkdir Downloads
#
Add Debian repo

    nano /etc/apt/sources.list

    deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian stretch contrib

#

    sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 3B4FE6ACC0B21F32 && sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 40976EAF437D05B5 && wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add - && sudo apt-get update -y

#

    cd ~/Downloads && wget http://ftp.br.debian.org/debian/pool/main/libv/libvpx/libvpx5_1.7.0-3+deb10u1_amd64.deb && chmod +x *.deb && dpkg -i libvpx5_1.7.0-3+deb10u1_amd64.deb && wget https://download.virtualbox.org/virtualbox/6.1.8/virtualbox-6.1_6.1.8-137981~Debian~buster_amd64.deb && chmod +x virtualbox-*.deb && dpkg -i virtualbox-*.deb && apt install -f -y
    
#    

Reboot and Enjoy


# Uninstall

sudo apt-get remove virtualbox-\* -y && sudo apt-get purge virtualbox-\* -y
