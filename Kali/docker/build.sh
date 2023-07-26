#!/bin/sh

DISTROS="${*:-kali-rolling}"

echo "Building images for $DISTROS"
for distro in $DISTROS; do
    sudo ./build-rootfs.sh $distro
    sudo ./docker-build.sh $distro
    sudo ./docker-push.sh $distro
done
