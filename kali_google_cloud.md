
How to install Kali Linux 2019.2.2 on Google Cloud Platform - GCP

On this post, I am going to guide you how to install & upload your Kali Linux into Google Cloud Platform.

Requirements:

  
A Google Cloud Platform Account with credits
    
    https://console.cloud.google.com/
      
VirtualBox with VirtualBox Guest Additions (bidirectional enabled)

    https://www.virtualbox.org/wiki/Downloads
    
Kali Linux ISO

    https://images.offensive-security.com/kali-linux-2019.1a-amd64.iso.torrent


137 GB Free Space in your machine


Grab a tea/cofee/beer!!!
    

Let’s start! Create VirtualBox virtual machine, using the ISO downloaded from Kali Linux.

Deploy a Kali Linux Ninja (gnome) inside of Virtualbox with UEFI and SSD Storage of 337 GB, once you installed this OS, execute: 

    sudo apt install kali-linux-full kali-linux-all gnome gdm3 neofetch screenfetch synaptic curl apt-transport-https lsb-release software-properties-common dirmngr openssh-server jq -y && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && sudo apt-get autoclean && apt-get clean cache && apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot

Change configuration of openssh-server

    nano /etc/ssh/sshd_config

Set the below value:

    PermitRootLogin yes

Set ssh run on the boot

    update-rc.d -f ssh enable 2 3 4 5
    
Install Azure CLI + VS Code + PowerShell + MS SQL Cli + .Net Core
    
    nano /etc/apt/sources.list
    
    deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ stretch main
    deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main
    deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main
    deb [arch=amd64] https://packages.microsoft.com/debian/9/prod stretch main

    
Ctrl + x + y + Enter
    
    sudo apt-key --keyring /etc/apt/trusted.gpg.d/Microsoft.gpg adv \
     --keyserver packages.microsoft.com \
     --recv-keys BC528686B50D79E339D3721CEB3E94ADBE1229CF
     
     
     sudo apt-get update -y && wget http://mirror.edatel.net.co/deepin/pool/main/i/icu/libicu57_57.1-9_amd64.deb && dpkg -i libicu57_57.1-9_amd64.deb && sudo apt-get install azure-cli code powershell mssql-cli dotnet-runtime-deps-2.2 dotnet-runtime-2.2 aspnetcore-runtime-2.2 dotnet-sdk-2.2 -y && rm -r /etc/apt/sources.list.d/vscode.list && sudo apt-get update -y && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot
     
     az login
     
Install VirtualBox 6

    su
    
    nano /etc/apt/sources.list

    deb https://download.virtualbox.org/virtualbox/debian stretch contrib
     
    apt remove libcurl4 -y && cd /root/Downloads && wget http://ftp.br.debian.org/debian/pool/main/c/curl/libcurl3_7.52.1-5+deb9u9_amd64.deb && wget http://ftp.br.debian.org/debian/pool/main/libv/libvpx/libvpx4_1.6.1-3+deb9u1_amd64.deb && chmod +x libcurl3_7.52.1-5+deb9u9_amd64.deb libvpx4_1.6.1-3+deb9u1_amd64.deb && dpkg -i libcurl3_7.52.1-5+deb9u9_amd64.deb libvpx4_1.6.1-3+deb9u1_amd64.deb && sudo apt-get install virtualbox-6.0 -y && apt autoremove -y && rm -r lib* && sudo apt-get update -y && apt full-upgrade && apt install kali-linux-full kali-linux-all && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot
    
Install Google Cloud SDK & GCP Linux Guest Environment

    curl https://sdk.cloud.google.com | bash
    
Close the terminal and open again

    gcloud init && gcloud beta --help && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - && nano /etc/apt/sources.list.d/google-cloud.list
    
    deb http://packages.cloud.google.com/apt google-compute-engine-sid main
    deb http://packages.cloud.google.com/apt google-cloud-packages-archive-keyring-sid main
    
Ctrl + x + y + Enter


    sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get autoclean $$ apt-get clear cache && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y &&     apt-get install apt-file -y && apt-get install -y && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot
    

If all works as expected Kali Linux restarted, correctly, now login as root and execute:

    declare -a PKG_LIST=(google-cloud-packages-archive-keyring \
     python-google-compute-engine \
    python3-google-compute-engine \
    google-compute-engine-oslogin \
    google-compute-engine)
    for pkg in ${PKG_LIST[@]}; do
       sudo apt install -y $pkg
    done
    
Restart Kali Linux and inspect that no errors ocurred.

    sudo reboot

Turn off the Kali Linux virtual machine.

Convert Kali linux vdi (37 GB) to raw file (85,9 GB) & Convert raw into tar.gz format

    vboxmanage clonehd kali.vdi disk.raw --format raw && tar -zcvf disk.tar.gz disk.raw

Create bucket at Google Cloud

    https://console.cloud.google.com/storage/browser

Upload Kali disk.raw (4,2 GB) to your GCP bucket

    gsutil cp kali.tar.gz gs://bucket-name/kali/disk.tar.gz

Create image for Kali Linux in GCP

     gcloud compute --project=name images create kali --source-uri=https://storage.googleapis.com/bucket-name.appspot.com/kali/disk.tar.gz

Start Kali Linux virtual machine in GCP and create Firewall

    gcloud beta compute --project=project-name instances create kali --zone=us-central1-f --machine-type=n1-highmem-4 --subnet=default      --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=name-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --image=kali --image-project=project-name --boot-disk-size=80GB --boot-disk-type=pd-ssd --boot-disk-device-name=kali

    gcloud compute --project=projet-name firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server    


Actually for connect via ssh, only works via web browser 

And using PowerShell
 
Update the ssh keys in your metadata

    gcloud compute config-ssh
    
Connect via SSH with debugg mode
     
    gcloud compute --project "project_name" ssh --ssh-flag="-vvv" --zone "us-central1-f" "kali"
    
    or
    
    ssh kali.us-central1-f.project-name -vvv





     
If Kali Linux only show's the command line after boot, enter the below command 
     
     startx    
      
then edit the below file in a terminal

     sudo nano .xinitrc

Adding this 

    exec startx
    
Ctrl + x + y + Enter
