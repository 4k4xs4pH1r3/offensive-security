#!/bin/sh

distro=$1
mirror=${2:-http://http.kali.org/kali}

rootfsDir=rootfs-$distro
debootstrap=${DEBOOTSTRAP:-debootstrap}

rootfs_chroot() {
        PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' \
                chroot "$rootfsDir" "$@"
}


if [ ! -e /usr/share/debootstrap/scripts/$distro ]; then
    echo "ERROR: debootstrap has no script for $distro"
    echo "ERROR: use a newer debootstrap"
    exit 1
fi

if [ ! -e /usr/share/keyrings/kali-archive-keyring.gpg ]; then
    echo "ERROR: you need /usr/share/keyrings/kali-archive-keyring.gpg"
    echo "ERROR: install kali-archive-keyring"
    exit 1
fi

rm -rf $rootfsDir $distro.tar.xz

debootstrap --variant=minbase --components=main,contrib,non-free \
    --include=kali-archive-keyring \
    $distro $rootfsDir $mirror

rootfs_chroot apt-get clean

# Inspired by /usr/share/docker.io/contrib/mkimage/debootstrap
cat > "$rootfsDir/usr/sbin/policy-rc.d" <<-'EOF'
	#!/bin/sh
	exit 101
EOF
chmod +x "$rootfsDir/usr/sbin/policy-rc.d"

echo 'force-unsafe-io' > $rootfsDir/etc/dpkg/dpkg.cfg.d/docker-apt-speedup

aptGetClean='"rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin || true";'
cat > "$rootfsDir/etc/apt/apt.conf.d/docker-clean" <<-EOF
	DPkg::Post-Invoke { ${aptGetClean} };

	Dir::Cache::pkgcache "";
	Dir::Cache::srcpkgcache "";
EOF

echo 'Acquire::Languages "none";' >$rootfsDir/etc/apt/apt.conf.d/docker-no-languages

cat > $rootfsDir/etc/apt/apt.conf.d/docker-gzip-indexes <<-'EOF'
	Acquire::GzipIndexes "true";
	Acquire::CompressionTypes::Order:: "gz";
EOF

echo 'Apt::AutoRemove::SuggestsImportant "false";' >$rootfsDir/etc/apt/apt.conf.d/docker-autoremove-suggests

rm -rf $rootfsDir/var/lib/apt/lists/*
mkdir $rootfsDir/var/lib/apt/lists/partial

echo "Creating $distro.tar.xz"
tar -C $rootfsDir -cf $distro.tar.xz .
