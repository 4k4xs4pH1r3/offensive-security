#    
    clear && sudo rm /var/lib/pacman/db.lck && sudo pacman -Syyu --needed --disable-download-timeout --noprogressbar --overwrite y
#    
    clear && sudo reflector --threads 20 --verbose --save "/etc/pacman.d/mirrorlist" --protocol https --sort rate --age 24 --score 100 --fastest 100 --latest 50
#
    clear && sudo pacman-key --init && sudo pacman-key --populate archlinux blackarch && gpg --recv-keys D4A753468A5A5B67 && sudo pacman-key --lsign-key D4A753468A5A5B67 && sudo pacman -Scc --noconfirm
#
    clear && sudo pacman-key --refresh-keys && sudo pacman -Scc --noconfirm && sudo pacman -Syyu --noconfirm && sudo pacman-key --populate archlinux blackarch && gpg --recv-keys --keyserver keyserver.ubuntu.com C7246DCCAB907BF6B5F02BE7C6245B6A5F2E86E0 && sudo pacman -Syyu --noconfirm
#
    clear && sudo pacman -Syyu haveged pacman-contrib --disable-download-timeout --noconfirm --needed --noprogressbar --overwrite y && systemctl start haveged && systemctl enable haveged && haveged && sudo paccache -r
#    
    clear && sudo rm /var/lib/pacman/db.lck && sudo pacman -Syyu --needed --disable-download-timeout --noprogressbar --overwrite y
#
    clear && sudo pacman -Syyu --needed gnome guake --disable-download-timeout --noprogressbar --overwrite y
#
    curl -O https://blackarch.org/strap.sh && echo 26849980b35a42e6e192c6d9ed8c46f0d6d06047 strap.sh | sha1sum -c && chmod +x strap.sh && sudo ./strap.sh
#
    clear && sudo pacman -Syyu --needed --noconfirm --disable-download-timeout --noprogressbar --overwrite '*'
#
    clear && sudo pacman -Syuu --needed --noconfirm --disable-download-timeout --noprogressbar --overwrite '*' blackarch blackarch-webapp blackarch-fuzzer blackarch-scanner blackarch-proxy blackarch-windows blackarch-dos blackarch-disassembler blackarch-cracker blackarch-voip blackarch-exploitation blackarch-recon blackarch-spoof blackarch-forensic blackarch-crypto blackarch-backdoor blackarch-networking blackarch-misc blackarch-defensive blackarch-wireless blackarch-automation blackarch-sniffer blackarch-binary blackarch-packer blackarch-reversing blackarch-mobile blackarch-malware blackarch-code-audit blackarch-social blackarch-honeypot blackarch-hardware blackarch-fingerprint blackarch-decompiler blackarch-config blackarch-debugger blackarch-firmware blackarch-bluetooth blackarch-database blackarch-automobile blackarch-webap blackarch-nfc blackarch-tunnel blackarch-drone blackarch-unpacker blackarch-radio blackarch-keylogger blackarch-stego blackarch-anti-forensic blackarch-ids blackarch-gpu

