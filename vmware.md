### How to Install VMware 15 in Kali GNU/Linux Rolling x 
Kernel: 4.18.0-kali2-amd64                
#
wget https://www.vmware.com/go/getworkstation-linux
#
apt install build-essential gcc-7 gcc-7-base gcc-7-base gcc-7-multilib -y
#
sudo apt-get install linux-headers-$(uname -r) -y
#
chmod +x VMware-Workstation-Full-15.0.2-10952284.x86_64.bundle 
#
./VMware-Workstation-Full-15.0.2-10952284.x86_64.bundle 
#
sudo dpkg --configure -a
#
sudo grub-mkconfig
#
Open VMware and enjoy ;)  
