    clear && sudo reflector --threads 20 --verbose --save "/etc/pacman.d/mirrorlist" --protocol https --sort rate --age 24 --score 100 --fastest 100 --latest 50
#    
    clear && sudo pacman-key --populate archlinux blackarch && gpg --recv-keys D4A753468A5A5B67 && sudo pacman -Scc --noconfirm
#
    clear && sudo pacman-key --init && sudo pacman-key --populate archlinux blackarch && gpg --recv-keys D4A753468A5A5B67 && sudo pacman-key --lsign-key D4A753468A5A5B67 && sudo pacman -Scc --noconfirm
#
    clear && sudo pacman -Syyu haveged pacman-contrib --disable-download-timeout --noconfirm --needed --noprogressbar --overwrite y && systemctl start haveged && systemctl enable haveged && haveged && sudo paccache -r    
#    
    clear && sudo pacman -Syyu --needed --disable-download-timeout --noprogressbar --overwrite y
#
    clear && sudo pacman -Syyu --needed gnome --disable-download-timeout --noprogressbar --overwrite y
#
    clear && sudo pacman -Syyu --needed blackarch yay --disable-download-timeout --noconfirm --noprogressbar --overwrite='*  
