echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list

apt-get update -y

apt-get -y --allow-unauthenticated install kali-archive-keyring

apt-cache search kali-linux

apt-get -y install kali-linux-all

sudo apt-get update && sudo apt-get dist-upgrade -f -y

sudo apt-get autoclean $$ apt-get clear cache

apt-get install software-properties-common -y

apt-get install apt-file -y

apt-file update

apt-get upgrade -y

apt autoremove -y

sudo apt-get update --fix-missing

sudo apt-get install --fix-broken && sudo apt-get autoremove && sudo apt-get update -y

apt-get install libcurl4 curl -y

sudo apt-get update && apt-get upgrade -y -f

sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y

sudo apt-get update && sudo apt-get dist-upgrade -f -y

sudo dpkg --configure -a

sudo grub-mkconfig

sudo reboot





