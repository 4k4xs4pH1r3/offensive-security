√

🍎

# Pre-Requisite

This will take up to a few minutes, now is a great time to go for a coffee ☕...

1. Install Homebrew
```ShellSession
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"  
```
#

3. Install Xcode + Brew including Formulae and Casks (218 packages)
```ShellSession
sudo softwareupdate --install-rosetta --agree-to-license && sudo gem install xcode-install && xcversion update && xcversion list
```
#
```ShellSession
brew install --cask gitfinder powershell dotnet && brew install cask && brew install python && brew install macfuse && brew link cask && brew install pyenv htop jq keybase cask npm node helm kubectl neofetch screenfetch minikube newman kops awscli sqlmap subfinder hashcat dnsmap nmap git git-lfs git-gui pcre2 mysql burp-suite metasploit vagrant telegram-desktop docker-compose cmatrix tfenv jython jruby istioctl aom fb303 helm libnghttp2 six apr fbthrift icu4c libpng snappy apr-util fdupes imath libpq node argon2 fizz isl oniguruma metasploit aircrack-ng linkerd nushell sslscan testssl yasm bandit c7n cargo-audit cyrus-sasl dcfldd flawfinder gosec hubble ipv6toolkit kube-score kubeaudit libprelude libxmlsec1 lynis nss opensaml prowler rats scorecard sf-pwgen suricata terrascan tfsec xml-security-c zeek sqlite aspell fmt istioctl libsodium openexr autoconf folly jansson libssh2 openjdk syck fontconfig jenv libtasn1 openldap bash-completion freetds jpeg libtiff openssl@1.1 telnet bdw-gc freetype jpeg-xl libtool p11-kit boost gcc libunistring pcre brotli gd libuv pcre2 tidy-html5 c-ares gdb mvn libvmaf php unbound ca-certificates gdbm krb5 libzip pipx unixodbc gettext kubernetes-cli lua@5.3 pkg-config wangle gflags libavif lz4 protobuf watchman giflib libcbor m4 pv webp composer libconfig python-tabulate wget coreutils glog libevent mpdecimal python@3.9 python@3.10 python@3.11 xz curl gmp libffi mpfr yarn gnutls libfido2 mycli readline zstd grep libidn2 rtmpdump double-conversion guile liblinear emacs libmpc nettle screenresolution zsh zsh-completions && brew install --cask github telegram telegram-desktop && brew install rbenv ruby-build && brew tap anchore/grype && brew install grype && brew install go && brew install powershell && brew install jq && brew install wget && brew install --cask remoteviewer && brew install skaffold && brew install aquasecurity/trivy/trivy && brew install luarocks && brew install android-platform-tools && brew tap snyk/tap && brew install snyk && brew install checkov && brew unlink tfenv && softwareupdate --all --install --force && brew update-reset && brew update && brew upgrade && brew unlink terraform && brew link tfenv && tfenv install && tfenv list && tfenv install latest && tfenv install 1.4.6 && tfenv use 1.4.6 && tfenv list && terraform -v && pipx upgrade-all --force && pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U -q --no-warn-script-location --ignore-installed --force-reinstall > /dev/null 2>&1 && pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U -q --no-warn-script-location --ignore-installed --force-reinstall > /dev/null 2>&1
```
#

4. Upgrade Apple Store + Apple Developer + Brew packages
```ShellSession
clear && { brew unlink tfenv && softwareupdate --all --install --force && brew update-reset && brew update -q && brew upgrade -q && brew install terraform -q && brew unlink terraform && brew link tfenv && tfenv install && tfenv list && tfenv install latest && tfenv install 1.4.6 && tfenv use 1.4.6 && tfenv list && terraform -v; } >/dev/null 2>&1 && clear && echo "Upgrading All Brew packages..." && echo "All Brew packages were upgraded successfully."
```

(Optional) Install Apple 🍏 Developer Beta + Apple Simulators for iOS, watchOS and tvOS

```ShellSession
sudo gem install xcode-install && xcversion install 15.0 && xcversion update && xcversion list && xcversion simulators 
```

Enjoy ✅ 🎧

#

# See full list of available Brew packages online
```ShellSession
brew list 
```
