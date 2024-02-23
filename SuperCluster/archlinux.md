### Tested with mpirun (Open MPI) 5.0.2

1. Install Arch Linux on each device: You can download the latest ArchLinux ISO file from the official website and create a bootable USB drive. Then, install ArchLinux on each device by booting from the USB drive.

2. Install the required software packages: After installing ArchLinux, you need to install the necessary software packages for cluster computing. Open a terminal and type the following command to install OpenMPI and Cockpit:

   ```
   clear && sudo pacman -Syuu --needed --noconfirm --disable-download-timeout --noprogressbar --overwrite '*' openssh openmpi openmpi-docs cockpit cockpit-machines cockpit-packagekit cockpit-pcp cockpit-podman cockpit-storaged && sudo groupadd cockpit && sudo usermod -aG cockpit $USER && sudo systemctl enable cockpit.socket && sudo systemctl start cockpit.socket && mpirun -V
   ```

3. Configure the network: You need to configure the network settings for each device to be able to communicate with each other. You can connect them using a network switch or a router. Alternatively, you can use Wi-Fi if all devices support it.

   http://localhost:9090/ (Cockpit)

4. Set up SSH: Secure Shell (SSH) is a network protocol that allows you to access and control one computer from another over a secure channel. You need to set up SSH on each device to enable remote access and control. Type the following command to install SSH:

   ```
   sudo systemctl enable sshd && sudo systemctl start sshd && sudo systemctl status sshd
   ```

   Then create a public and private key pair, generate SSH keys on each device by typing the following command:

   ```
   cd ~/.ssh && ssh-keygen
   ```

   Copy the public key to each device by typing the following command:

   ```
   ssh-copy-id -i key_name.pub user@ip_address
   ```

   Replace `user` with your username and `ip_address` with the IP address or the hostname of each device.
