This script will convert your Debian 9 “stretch” to a new Kali Linux Ninja in Azure

    echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list && apt-get update -y &&     apt-get -y --allow-unauthenticated install kali-archive-keyring && apt-cache search kali-linux && apt-get -y install kali-linux-all && sudo apt-get update && sudo apt-get full-upgrade -f -y && sudo apt-get autoclean && apt-get clear cache && apt-get install software-properties-common -y && apt-get install apt-file -y && apt-file update && apt-get upgrade -y && apt autoremove -y && sudo apt-get update --fix-missing && sudo apt-get install --fix-broken && sudo apt-get autoremove && sudo apt-get update -y && apt-get install libcurl4 curl -y && sudo apt-get update && apt-get upgrade -y -f && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get update && sudo apt-get full-upgrade -f -y && sudo dpkg --configure -a && sudo grub-mkconfig && sudo reboot
    


1) Login to the VM using SSH, we can check the size of the disk by using:
sudo dmesg | grep -i sda

We should see something similar to the output below (assuming you changed the size to 100GB on the portal for the disk):
[    3.100914] sd 2:0:0:0: [sda] 209715200 512-byte logical blocks: (107 GB/100 GiB)

2) To proceed with the partition resize, we will use:
sudo fdisk /dev/sda

type: p
this will show partition /dev/sda1

type: d
type: n then p, 1 (to recreate partition 1) you can accept the default values
NOTE: if you receive a message about deleting or keeping a signature on the disk, just answer N
type: w (to save the new partition)
type: q (to exit fdisk)
sudo reboot (to reboot the VM so the partition is updated)

3) To finalize the resize, after the reboot, execute the command:
resize2fs /dev/sda1

4) Use the command: df -h to verify its size:
Filesystem Size Used Avail Use% Mounted on
/dev/sda1 99G 698M 94G 1% /



    az vm deallocate --resource-group y --name y

    az disk show --name y_741d336ac0aa4affacf0f56b54800ad3 --resource-group y

    az disk update --name y_741d336ac0aa4affacf0f56b54800ad3 --resource-group y --size-gb 337

    az vm start --resource-group y --name y

    https://blogs.msdn.microsoft.com/linuxonazure/2017/04/03/how-to-resize-linux-osdisk-partition-on-azure/


