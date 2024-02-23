1. Install Kali Linux on each laptop: You can download the latest Kali Linux ISO file from the official website and create a bootable USB drive. Then, install Kali Linux on each laptop by booting from the USB drive.

2. Install the required software packages: After installing Kali Linux, you need to install the necessary software packages for cluster computing. Open a terminal and type the following command to install OpenMPI and Cockpit:

   ```
   sudo apt-get update
   sudo apt-get install openmpi-bin openmpi-common libopenmpi-dev cockpit* -y && sudo systemctl enable cockpit.socket && sudo systemctl start cockpit.socket
   ```

3. Configure the network: You need to configure the network settings for each laptop to be able to communicate with each other. You can connect them using a network switch or a router. Alternatively, you can use Wi-Fi if all devices support it.

   http://localhost:9090/ (Cockpit)

4. Set up SSH: Secure Shell (SSH) is a network protocol that allows you to access and control one computer from another over a secure channel. You need to set up SSH on each laptop to enable remote access and control. Type the following command to install SSH:

   ```
   sudo apt-get install ssh
   ```

   Then, generate SSH keys on each laptop by typing the following command:

   ```
   ssh-keygen
   ```

   This will create a public and private key pair. Copy the public key to each laptop by typing the following command:

   ```
   ssh-copy-id user@ip_address
   ```

   Replace `user` with your username and `ip_address` with the IP address of each laptop.
