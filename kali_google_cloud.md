
How to install Kali Linux on Google Cloud

On this post, I am going to guide you how to install & upload your Kali Linux into Google Cloud Platform.

Requirements:
    
    Google Cloud Account 
    https://console.cloud.google.com/
    
    Google Cloud SDK Installed and Configured 
    curl https://sdk.cloud.google.com | bash
    https://cloud.google.com/sdk/install
    
    VirtualBox 
    https://www.virtualbox.org/wiki/Downloads
    
    Kali Linux ISO (or VirtualBox images) 
    https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/
    
    150 GB Free Space in your machine
    
    Grab a cofee or beers
    

Let’s start! Create VirtualBox virtual machine

It’s easy to create a Kali Linux Virtualbox virtual machine so in this post, I will use Kali VirtualBox image that I downloaded from Kali Linux download page.

Import kali-linux-2018.4-vbox-amd64.ova in Virtual Box (The virtual size of the hdd is 80GB)

Turn on the Kali Linux virtual machine to install and configure openssh-server:

    apt-get install openssh-server -y

Change the configuration file

    nano /etc/ssh/sshd_config

Add or set the below line in this config file

    #PermitRootLogin yes

Set ssh run on the boot

    update-rc.d –f ssh enable 2 3 4 5

Turn off the Kali Linux virtual machine.

Convert Kali linux vdi (11 GB) to raw file (85,9 GB).

    vboxmanage clonehd kali.vdi disk.raw --format raw

Convert raw into tar.gz format

    tar –zcvf disk.tar.gz disk.raw

Create bucket at Google Cloud

    https://console.cloud.google.com/storage/browser

Upload Kali disk.raw (4,2 GB) to your GCP bucket

    gsutil cp kali.tar.gz gs://bucket-name/kali/disk.tar.gz

Create image for Kali Linux in GCP

     gcloud compute --project=name images create kali --source-uri=https://storage.googleapis.com/bucket-name.appspot.com/kali/disk.tar.gz

Start Kali Linux virtual machine in GCP and create Firewall

gcloud beta compute --project=project-name instances create kali --zone=us-central1-f --machine-type=n1-highmem-4 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=name-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server,https-server --image=kali --image-project=project-name --boot-disk-size=80GB --boot-disk-type=pd-ssd --boot-disk-device-name=kali

gcloud compute --project=projet-name firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server    


Update the ssh keys in your metadata

    gcloud compute config-ssh
    
Connect via SSH
     
    gcloud compute --project "project_name" ssh --zone "us-central1-f" "kali"
    
    or
    
    ssh kali.us-central1-f.project-name

