√

🍎

# Pre-Requisite

This will take up to a few minutes, now is a great time to go for a coffee ☕...

1. Install Homebrew
```ShellSession
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"  
```
#

3. Install Xcode + Brew including Formulae and Casks (158 packages)
```ShellSession
sudo softwareupdate --install-rosetta && sudo gem install xcode-install && xcversion update && xcversion list && brew install cask && brew install python && brew install macfuse && brew link cask && brew install cask npm node helm kubectl neofetch screenfetch minikube newman kops awscli sqlmap subfinder hashcat dnsmap nmap git git-lfs mysql burp-suite metasploit vagrant telegram-cli telegram-desktop docker-compose cmatrix tfenv jython jruby istioctl aom fb303 helm libnghttp2 six apr fbthrift icu4c libpng snappy apr-util fdupes imath libpq node argon2 fizz isl oniguruma sqlite aspell fmt istioctl libsodium openexr autoconf folly jansson libssh2 openjdk syck fontconfig jenv libtasn1 openldap bash-completion freetds jpeg libtiff openssl@1.1 telnet bdw-gc freetype jpeg-xl libtool p11-kit boost gcc libunistring pcre brotli gd libuv pcre2 tidy-html5 c-ares gdb libvmaf php unbound ca-certificates gdbm krb5 libzip pipx unixodbc gettext kubernetes-cli lua@5.3 pkg-config wangle gflags libavif lz4 protobuf watchman giflib libcbor m4 pv webp composer libconfig python-tabulate wget coreutils glog libevent mpdecimal python@3.10 xz curl gmp libffi mpfr python@3.9 yarn gnutls libfido2 mycli readline zstd grep libidn2 rtmpdump double-conversion guile liblinear emacs libmpc nettle screenresolution zsh zsh-completions && brew install --cask github telegram telegram-desktop && brew install rbenv ruby-build && brew tap anchore/grype && brew install grype && brew install go && brew install powershell && brew install jq && brew install wget && brew install --cask remoteviewer && brew install skaffold && brew install aquasecurity/trivy/trivy && brew install luarocks && brew tap snyk/tap && brew install snyk && brew install checkov && brew unlink tfenv && softwareupdate --all --install --force && brew update-reset && brew update && brew upgrade && brew unlink terraform && brew link tfenv && tfenv install && tfenv list && tfenv install latest && tfenv install 1.1.5 && tfenv use 1.1.5 && tfenv list && terraform -v 
```

#

4. Upgrade Apple Store + Apple Developer + Brew packages
```ShellSession
brew unlink tfenv && softwareupdate --all --install --force && brew update-reset && brew update && brew upgrade && brew install terraform && brew unlink terraform && brew link tfenv && tfenv install && tfenv list && tfenv install latest && tfenv install 1.1.5 && tfenv use 1.1.5 && tfenv list && terraform -v 
```

(Optional) Install Apple 🍏 Developer Beta + Apple Simulators for iOS, watchOS and tvOS

```ShellSession
sudo gem install xcode-install && xcversion install 14.3 && xcversion update && xcversion list && xcversion simulators --install='iOS 16.4' && xcversion simulators --install='watchOS 9.4' && xcversion simulators --install='tvOS 16.4' && xcversion simulators 
```

Enjoy ✅ 🎧

#

# See full list of available Brew packages online
```ShellSession
brew list 
```
