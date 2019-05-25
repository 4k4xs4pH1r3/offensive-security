
How to install Kali Linux 2019.2.3 on Google Cloud Platform - GCP

On this post, I am going to guide you how to install & upload your Kali Linux into Google Cloud Platform.

Requirements:

  
A Google Cloud Platform Account with credits
    
    https://console.cloud.google.com/
      
VirtualBox 6 with VirtualBox Guest Additions (bidirectional enabled)

    https://www.virtualbox.org/wiki/Downloads
    
Kali Linux ISO

    https://images.offensive-security.com/kali-linux-2019.1a-amd64.iso.torrent


137 GB Free Space in your machine


Grab a tea/cofee/beer!!!
    

# Create VirtualBox virtual machine, 

using the ISO downloaded from Kali Linux. Deploy a Kali Linux Ninja (gnome) inside of Virtualbox with UEFI and SSD Storage of 337 GB, once you installed this OS, execute: 
#
    sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt install kali-linux-full kali-linux-all gnome gdm3 neofetch screenfetch synaptic lsb-release software-properties-common curl dirmngr apt-transport-https openssh-server openvpn network-manager-openvpn-gnome resolvconf jq -y && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot

Change configuration of openssh-server
#
    nano /etc/ssh/sshd_config

Set the below value:
#
    PermitRootLogin yes

Set ssh run on the boot
#
    update-rc.d -f ssh enable 2 3 4 5
    
# Install Azure CLI + VS Code + PowerShell + MS SQL Cli + .Net Core
#    
    nano /etc/apt/sources.list
#    
    deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ stretch main
    deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main
    deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main
    deb [arch=amd64] https://packages.microsoft.com/debian/9/prod stretch main


For Ubuntu Disco
#
    deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.10/prod cosmic main
    deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main
#    
#
    
Ctrl + x + y + Enter
#    
    sudo apt-key --keyring /etc/apt/trusted.gpg.d/Microsoft.gpg adv \
     --keyserver packages.microsoft.com \
     --recv-keys BC528686B50D79E339D3721CEB3E94ADBE1229CF
#  
#     
    sudo apt-get update -y && wget http://mirror.edatel.net.co/deepin/pool/main/i/icu/libicu57_57.1-9_amd64.deb && dpkg -i libicu57_57.1-9_amd64.deb && wget http://security-cdn.debian.org/debian-security/pool/updates/main/o/openssl1.0/libssl1.0.2_1.0.2r-1~deb9u1_amd64.deb && wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu6.2_amd64.deb && wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu55_55.1-7ubuntu0.4_amd64.deb && chmod +x l*.deb && dpkg -i l*.deb && sudo apt-get update && sudo apt install azure-cli code powershell  dotnet-runtime-deps-2.2 dotnet-runtime-2.2 aspnetcore-runtime-2.2 dotnet-sdk-2.2 mssql-cli mssql-tools mssql-server unixodbc-dev -y && sudo /opt/mssql/bin/mssql-conf setup && rm -r /etc/apt/sources.list.d/*.list && sudo apt-get update -y && sudo dpkg --configure -a && sudo grub-mkconfig
#
     sudo reboot
#     
     az login
#     
# Install VirtualBox 6

    echo "deb https://download.virtualbox.org/virtualbox/debian stretch contrib" | sudo tee -a /etc/apt/sources.list && apt remove libcurl4 -y && mkdir /root/Downloads && cd /root/Downloads && wget http://ftp.br.debian.org/debian/pool/main/c/curl/libcurl3_7.52.1-5+deb9u9_amd64.deb && wget http://ftp.br.debian.org/debian/pool/main/libv/libvpx/libvpx4_1.6.1-3+deb9u1_amd64.deb && wget http://ftp.us.debian.org/debian/pool/main/libs/libssh2/libssh2-1_1.7.0-1_amd64.deb && chmod +x libcurl3_7.52.1-5+deb9u9_amd64.deb libvpx4_1.6.1-3+deb9u1_amd64.deb libssh2-1_1.7.0-1_amd64.deb && dpkg -i libcurl3_7.52.1-5+deb9u9_amd64.deb libvpx4_1.6.1-3+deb9u1_amd64.deb libssh2-1_1.7.0-1_amd64.deb && wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add - && wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add - && sudo apt update && sudo apt-get install virtualbox-6.0 -y && apt autoremove -y && rm -r lib* && sudo apt-get update -y && apt full-upgrade && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot
    
# Install Google Cloud SDK & GCP Linux Guest Environment

    curl https://sdk.cloud.google.com | bash
    
Close the terminal and open again

    gcloud init && gcloud beta --help && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && nano /etc/apt/sources.list.d/google-cloud.list
#    
    deb http://packages.cloud.google.com/apt google-compute-engine-sid main
    deb http://packages.cloud.google.com/apt google-cloud-packages-archive-keyring-sid main
#    
Ctrl + x + y + Enter
#

    sudo apt-get autoclean && apt-get clean cache && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig
#
sudo reboot
#

If all works as expected Kali Linux restarted, correctly, now login as root and execute:
#
    declare -a PKG_LIST=(google-cloud-packages-archive-keyring \
     python-google-compute-engine \
    python3-google-compute-engine \
    google-compute-engine-oslogin \
    google-compute-engine)
    for pkg in ${PKG_LIST[@]}; do
       sudo apt install -y $pkg
    done
#    
Restart Kali Linux and inspect that no errors ocurred.
#
    sudo reboot
#
Turn off the Kali Linux virtual machine.
#
Convert Kali linux vdi (37 GB) to raw file (85,9 GB) & Convert raw into tar.gz format
#
    vboxmanage clonehd kali.vdi disk.raw --format raw && tar -zcvf disk.tar.gz disk.raw
#
Create bucket at Google Cloud
#
    https://console.cloud.google.com/storage/browser
#
Upload Kali disk.raw (4,2 GB) to your GCP bucket
#
    gsutil cp kali.tar.gz gs://bucket-name/kali/disk.tar.gz
#
Create image for Kali Linux in GCP
#
     gcloud compute --project=name images create kali --source-uri=https://storage.googleapis.com/bucket-name.appspot.com/kali/disk.tar.gz
#
Start Kali Linux virtual machine in GCP and create Firewall
#
    gcloud beta compute --project=project-name instances create kali --zone=us-central1-f --machine-type=n1-highmem-4 --subnet=default      --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=name-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --image=kali --image-project=project-name --boot-disk-size=80GB --boot-disk-type=pd-ssd --boot-disk-device-name=kali
#
    gcloud compute --project=projet-name firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server    
#

Actually for connect you can do it via web, ssh & PowerShell
# 
    nano ~/.ssh/config
#
    Host *
        IPQoS=lowdelay throughput
# 
Connect via ssh keys in your metadata
#
    gcloud compute config-ssh
#    
Connect via SSH in Linux or PowerShell + Putty in Windows with debugg mode (OS Login Mode)
#     
    gcloud compute --project "project_name" ssh --zone "us-east1-b" "roo@kali"
#
#
#
If Kali Linux only show's the command line after boot, enter the below command 
#     
     startx    
#      
then edit the below file in a terminal
#
     sudo nano .xinitrc
#
Adding this 

    exec startx
    
Ctrl + x + y + Enter
#

For copy files from Google Bucket
#    
    gsutil cp -r gs://proyect_name.appspot.com/folder /root/
