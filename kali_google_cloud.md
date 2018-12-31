
How to install Kali Linux on Google Cloud

On this post, I am going to guide you how to install & upload your Kali Linux into Google Cloud Platform.

Requirements:
    
    Google Cloud Account 
    https://console.cloud.google.com/
    
    Google Cloud SDK Installed and Configured 
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

Upload kali.raw (4,2 GB) to your bucket

    gsutil cp kali.tar.gz gs://bucket-name/kali.tar.gz

Create image for Kali Linux in GCP

     gcloud compute --project=name images create kg --source-uri=https://storage.googleapis.com/bucket-name.appspot.com/kali/disk.tar.gz

Start Kali Linux virtual machine in GCP

    gcloud compute --project=name instances create kali –image kali –machine-type n1-highmem-4 –zone us-central1-f
    
Connect via SSH

    gcloud compute --project "project_name" ssh --zone "us-central1-f" "kali"
