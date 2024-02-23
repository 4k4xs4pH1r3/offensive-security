1. Install Kali Linux on each device: You can download the latest Kali Linux ISO file from the official website and create a bootable USB drive. Then, install Kali Linux on each device by booting from the USB drive.

2. Install the required software packages: After installing Kali Linux, you need to install the necessary software packages for cluster computing. Open a terminal and type the following command to install OpenMPI and Cockpit:

   ```
   sudo apt-get update
   sudo apt-get install openmpi-bin openmpi-common libopenmpi-dev cockpit* -y && sudo systemctl enable cockpit.socket && sudo systemctl start cockpit.socket
   ```

3. Configure the network: You need to configure the network settings for each device to be able to communicate with each other. You can connect them using a network switch or a router. Alternatively, you can use Wi-Fi if all devices support it.

   http://localhost:9090/ (Cockpit)

4. Set up SSH: Secure Shell (SSH) is a network protocol that allows you to access and control one computer from another over a secure channel. You need to set up SSH on each device to enable remote access and control. Type the following command to install SSH:

   ```
   sudo apt-get install ssh -y && sudo systemctl enable ssh && sudo systemctl start ssh && sudo systemctl status ssh
   ```

   Then create a public and private key pair, generate SSH keys on each device by typing the following command:

   ```
   mkdir ~/.ssh && cd ~/.ssh && ssh-keygen
   ```

   Copy the public key to each device by typing the following command:

   ```
   ssh-copy-id -i key_name user@ip_address
   ```

   Replace `user` with your username and `ip_address` with the IP address or the hostname of each device.
