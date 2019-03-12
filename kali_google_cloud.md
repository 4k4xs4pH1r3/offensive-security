
How to install Kali Linux 2019.1 on Google Cloud Platform - GCP

On this post, I am going to guide you how to install & upload your Kali Linux into Google Cloud Platform.

Requirements:
    
    Google Cloud Account 
    https://console.cloud.google.com/
    
    Google Cloud SDK Installed and Configured 
    curl https://sdk.cloud.google.com | bash
    gcloud init
    
    VirtualBox 
    https://www.virtualbox.org/wiki/Downloads
    
    Kali Linux VirtualBox Image
    https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/
    
    100 GB Free Space in your machine
    
    Grab a cofee or beers
    

Let’s start! Create VirtualBox virtual machine

It’s easy to create a Kali Linux Virtualbox virtual machine so in this post, I will use Kali VirtualBox image that I downloaded from Kali Linux download page.

Import kali-linux-2018.4-vbox-amd64.ova in Virtual Box (The virtual size of the hdd is 80GB)

Turn on the Kali Linux virtual machine to install and configure openssh-server:

    apt-get install openssh-server -y

Change the configuration file

    nano /etc/ssh/sshd_config

Add or set the below line in this config file

    PermitRootLogin yes

Set ssh run on the boot

    update-rc.d -f ssh enable 2 3 4 5
    
Installing the GCP Linux Guest Environment and Upgrade Kali Linux
    
    sudo apt-get install jq
    
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

    nano /etc/apt/sources.list.d/google-cloud.list
    
    deb http://packages.cloud.google.com/apt google-compute-engine-sid main
    deb http://packages.cloud.google.com/apt google-cloud-packages-archive-keyring-sid main
    
    Ctrl + x 
    yes
    Enter

    sudo apt-get update && sudo apt-get full-upgrade -y
    sudo apt-get autoclean $$ apt-get clear cache
    apt-get install software-properties-common -y
    apt-get install apt-file -y
    apt-file update
    sudo apt-get update --fix-missing
    sudo apt-get install --fix-broken && sudo apt-get autoremove && sudo apt-get update -y
    apt-get install curl -y
    sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y
    sudo dpkg --configure -a
    sudo grub-mkconfig
    
    declare -a PKG_LIST=(google-cloud-packages-archive-keyring \
     python-google-compute-engine \
    python3-google-compute-engine \
    google-compute-engine-oslogin \
    google-compute-engine)
    for pkg in ${PKG_LIST[@]}; do
       sudo apt install -y $pkg
    done
    
Restart the instance and inspect its console to make sure the Guest Environment loads as it starts back up.

    sudo reboot

Turn off the Kali Linux virtual machine.

Convert Kali linux vdi (11 GB) to raw file (85,9 GB).

    vboxmanage clonehd kali.vdi disk.raw --format raw

Convert raw into tar.gz format

    tar -zcvf disk.tar.gz disk.raw

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


Work in Progress: Connect with Cloud Shell or using third-party tools (like kali liux terminal, remmina, etc...)


Install Azure CLI + VS Code + PowerShell + MS SQL cli

    sudo apt-get install apt-transport-https lsb-release software-properties-common dirmngr -y
    apt-get install --fix-missing
    apt-get update --fix-missing
    sudo apt-get update && apt-get full-upgrade -y
    sudo apt-get install aptitude -y && sudo aptitude safe-upgrade
    sudo dpkg --configure -a && sudo grub-mkconfig
    
    nano /etc/apt/sources.list
    
    deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ stretch main
    deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main
    deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main
    deb [arch=amd64] https://packages.microsoft.com/debian/9/prod stretch main

    
    
    Ctrl + x 
    yes
    Enter
    
    sudo apt-key --keyring /etc/apt/trusted.gpg.d/Microsoft.gpg adv \
     --keyserver packages.microsoft.com \
     --recv-keys BC528686B50D79E339D3721CEB3E94ADBE1229CF
     
     
     sudo apt-get update -y
     wget http://mirror.edatel.net.co/deepin/pool/main/i/icu/libicu57_57.1-9_amd64.deb
     dpkg -i libicu57_57.1-9_amd64.deb
     sudo apt-get install azure-cli code powershell mssql-cli dotnet-runtime-deps-2.1 dotnet-runtime-2.1 aspnetcore-runtime-2.1 dotnet-sdk-2.1 -y
     rm -r /etc/apt/sources.list.d/vscode.list
     sudo apt-get update -y
     az login
     
     
     
If your installation starts up to a command line, enter the command 
     
     startx    
    
If this results in a command not found message, install the Kali Linux desktop GUI, running: 

    apt install kali-linux-full kali-linux-all gnome gdm3 -y
    
then editing your file

     .xinitrc 

and add the line 

    exec startx
