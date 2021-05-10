# Ubuntu | Kodachi | Hirsute | Groovy | Focal | Eoan | Disco | Bionic | Docker

Tested and verifed: 10 May 2021

    su
#    
    cd ~/ && mkdir Downloads && wget http://ftp.br.debian.org/debian/pool/main/libv/libvpx/libvpx5_1.7.0-3+deb10u1_amd64.deb && chmod +x *.deb && dpkg -i libvpx5_1.7.0-3+deb10u1_amd64.deb && wget https://download.virtualbox.org/virtualbox/6.1.22/virtualbox-6.1_6.1.22-144080~Debian~buster_amd64.deb && chmod +x virtualbox-*.deb && dpkg -i virtualbox-*.deb && apt install -f -y
    
#    

Reboot and Enjoy


# Uninstall

sudo apt-get remove virtualbox-\* -y && sudo apt-get purge virtualbox-\* -y
