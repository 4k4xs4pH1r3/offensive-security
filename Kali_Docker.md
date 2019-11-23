### Install Kali Linux in Docker


Deploy Portainer tool for manage your Containers through a Web Intranet Portal

    docker volume create portainer_data && docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer


Deploy & Run Kali Linux image in Docker

    docker run -t -i kalilinux/kali-linux-docker /bin/bash

List actual Docker images 

    docker ps -a
#
or

    docker container ls

Start Portainer * only after reboot your physical machine 

    sudo docker start portainer
#
or

    docker start xxxxxxxxxxxx

Start Kali Linux * only after reboot your physical machine 

    docker start xxxxxxxxxxxx

For open Portainer go to

    http://localhost:9000
