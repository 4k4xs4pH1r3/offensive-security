    sudo pacman-key --populate archlinux blackarch && gpg --recv-keys D4A753468A5A5B67 && sudo pacman -Scc
#    
    sudo pacman -Syyu --needed --disable-download-timeout --noprogressbar --overwrite y
#
    sudo pacman -Syyu --needed gnome --disable-download-timeout --noprogressbar --overwrite y
#
    sudo pacman -Syyu --needed blackarch yay --disable-download-timeout --noconfirm --noprogressbar --overwrite='*'
#
    sudo reflector --threads 10 --verbose --save "/etc/pacman.d/mirrorlist" --protocol https --sort rate --age 24 --score 100 --fastest 100 --latest 100
#
    sudo pacman -Syyu haveged pacman-contrib --disable-download-timeout --noconfirm --needed --noprogressbar --overwrite y && systemctl start haveged && systemctl enable haveged && haveged && sudo paccache -r
    
