
How to install Kali Linux on Google Cloud

On this post, I am going to guide you how to install & upload your Kali Linux into Google Cloud Platform.

Requirements:
    Google Cloud account number 
    Google Cloud SDK https://cloud.google.com/sdk/install
    VirtualBox https://www.virtualbox.org/wiki/Downloads
    Kali Linux ISO (or VirtualBox images) https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/
    150 GB Free Space in your machine
    Grab a cofee or beers

Let’s start!
Create VirtualBox virtual machine

It’s easy to create a Kali Linux Virtualbox virtual machine so in this post, I will use Kali VirtualBox image that I downloaded from Kali Linux download page.
Configure kali sshd service

Extract and import Kali Virtual Image. Turn on the Kali Linux virtual machine to install and configure openssh-server.

Install openssh-server

    apt-get install openssh-server

Change the configuration file

    nano /etc/ssh/sshd_config

    Add or set the below line in this config file
    #PermitRootLogin yes

Set ssh run on the boot

    update-rc.d –f ssh enable 2 3 4 5

Turn off the Kali Linux virtual machine.

Convert vdi to raw file.

    vboxmanage clonehd kali.vdi kali.raw --format raw

Convert into tar format

    tar –zcvf kali.tar.gz kali.raw

Upload image to Google Cloud

Create bucket at

    https://console.cloud.google.com/storage/browser

Upload kali.raw to your bucket

    gsutil cp kali.tar.gz gs://bucket-name/kali.tar.gz

Start Kali Linux virtual machine

gcloud compute images create kali –source-uri gs://bucket-name//kali/kali.tar.gz

gcloud compute instances create kali –image kali –machine-type n1-highmem-4 –zone us-central1-f
    
    Connect via SSH
    gcloud compute --project "project_name" ssh --zone "us-central1-f" "kali"
