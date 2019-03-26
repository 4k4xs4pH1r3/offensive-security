
 ҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉Borned To Learn Something, dedicated to my C4N6 mentors, in honor to 0x00H4C|<£ and 
to The CyberNinja passion of https://github.com/sh1nta & https://github.com/Daniels8989

    # rl++
     __________________
    < TLS >
     ------------
       \   ,__,
        \  (oo)____
           (__)    )\
              ||--|| *

 
[!] legal disclaimer: Usage of this for attacking targets without prior mutual consent is illegal.
It is the end user's responsibility to obey all applicable local, state and federal laws. 
Developers assume no liability and are not responsible for any misuse or damage caused by this program.
#
# Pre-Requisites:
 
Storage: 500 GB 
Memory RAM: 16 GB
CPU: 1 Socket - 4 Cores (AMD Pro A10 / Intel i5 7th gen)
GPU: 1 GB

# 1. Let's convert you in an Ninja Hacker

Installing in your Ubuntu 18: Metasploit Framerwork & Nmap with aprox 604 NSE scripts (Vuln + Vulners + Vulscan for identify the CVE's). 

       sudo apt-get autoclean && apt-get clean cache && sudo apt update && apt install git screen wine64 wine32 neofetch screenfetch synaptic lsb-release software-properties-common curl dirmngr apt-transport-https jq postgresql nginx sslstrip hping3 hashcat openvpn network-manager-openvpn-gnome resolvconf nmap net-tools ssh gcc python-dev python-setuptools python-setuptools python-dev build-essential python-pip python3-pip gparted compiz steghide httrack mesa-utils ethtool build-essential linux-headers-$(uname -r) lm-sensors hddtemp xsensors macchanger -y && cd /usr/share/nmap/scripts && git clone https://github.com/scipag/vulscan && git clone https://github.com/vulnersCom/nmap-vulners.git && cd vulscan/utilities/updater/ && chmod +x updateFiles.sh && ./updateFiles.sh && neofetch && cd /opt/metasploit/common/share/nmap/scripts && git clone https://github.com/scipag/vulscan && git clone https://github.com/vulnersCom/nmap-vulners.git && cd vulscan/utilities/updater/ && chmod +x updateFiles.sh && ./updateFiles.sh && screenfetch && sudo apt-get install aptitude -y && sudo aptitude safe-upgrade -y && sudo apt-get install --fix-broken && apt-get update --fix-missing && sudo apt-get update && apt-get full-upgrade && apt-get autoremove -y && apt-get install apt-file -y && apt-get install -y && /etc/init.d/kmod start && sensors-detect && cd /usr/share && mkdir OWASP-WebScarab && git clone https://github.com/OWASP/OWASP-WebScarab.git && cd /usr/share && mkdir webscarab-ng && cd webscarab-ng && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/webscarab-ng/WebScarab-ng-0.2.1.one-jar.zip && unzip WebScarab-ng-0.2.1.one-jar.zip && sudo add-apt-repository ppa:oibaf/graphics-drivers && sudo apt update -y && sudo apt dist-upgrade -y && sudo dpkg --configure -a && sudo grub-mkconfig && cd && neofetch && sudo reboot
       
       sudo pip install --no-cache-dir -U crcmod
       
    
For display help for the individual scripts use this option
   
    --script-help=$scriptname
   
To get an easy list of the installed scripts, use 

    locate nse | grep script
#
       
Set DNS
       
    rm -r /etc/resolv.conf && nano /etc/resolv.conf
       
    #P
    nameserver 139.99.96.146
    nameserver 37.59.40.15
    nameserver 185.121.177.177 

    # Round Robin
    options rotate
       

#
For do this more dynamic let's see in parallel some https://nmap.org/movies/

The main objective of this automation were designed Extrictly and Limited only for educational purposes.

#
Only authorized DevSecOps, can use this due to your client/target boundary concerns.

#
#
This PoC include

- Comprehensive OS guesses, Uptime, Ports, Services Device type per host detection, based on fingerprints match
- Vulnerabilities Discovery based on Network Traceroute and Services version on each port
- Host Footprinting based on TCP/IP Sequence Prediction and thumbprint over ipv4 & ipv6
- Firewall / IDS Evasion and Spoofing with accurate miscellaneous Options



# Configure Metasploit Framework 5 

(omnibus Nightly):

    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
    chmod 755 msfinstall && \
    ./msfinstall

Configure the services and database of Metasploit Framework 5:

    su 
    update-rc.d postgresql enable && update-rc.d nginx enable && service postgresql start 
    su postgres
    createuser root -P
    createdb —owner=root msfdb
    exit
   
 Verify that services are running and initiate the database of Metasploit Framework 5. (for repair use "msfdb reinit")
    
    service --status-all
    msfdb init

It's time to open Metasploit Framework 5 (Tested in Ubuntu Cosmic + Bionic Beaver & Kali Linux)
   
    /opt/metasploit-framework/bin/./msfconsole

In Parrot:

    /usr/share/metasploit-framework/./msfconsole
    
Update and Check Metasploit Framework 5:

    msfupdate
    db_status
    db_rebuild_cache
    load nexpose
    load nessus
    


#   

# 4. Create and Save your workspace with real time notifier enabled

    workspace -a tls
    
    setg Prompt tls (%grn%W/%whiS%S/%grnJ%J)
    setg ConsoleLogging y
    setg LogLevel 5
    setg SessionLogging y
    setg TimestampOutput true
    save

Make a backup each time that you need of each one of your workspaces by separately

    db_export -f xml /root/msfuExported.xml

Importing a file from an earlier scan (This is done using db_import followed by the path to our file.)

    db_import /root/msfu/nmapScan

    

#
The db_nmap sessions will be saved in xml for you can restart an early scan using
    
    msfconsole
    db_nmap --resume /root/.msf4/local/file.xml
    
The history of Metasploit commands are here:

    /root/.msf4/history
    
 For delete and old scan logs execute
    
    rm -r /root/.msf4/local/*.*


Print host interfaces and routes (for debugging)

     db_nmap --iflist
    
#
Scan Types

Full & Polite recorded in the msf db with verbosity enabled for an domain/ip

    db_nmap --save --privileged -sY -sZ -g 20 --script=auth,banner,broadcast,brute,default,discovery,dos,exploit,external,intrusive,malware,safe,smb-vuln-regsvc-dos.nse,version,vuln,nmap-vulners,vulscan --script-args vulscandb=cve.csv,exploitdb.csv,openvas.csv,osvdb.csv,scipvuldb.csv,securityfocus.csv,securitytracker.csv,xforce.csv,randomseed,smbbasic,smbport,smbsign,smbdomain,smbhash,smbnoguest,smbpassword,smbtype,smbusername -A -f -D RND -sV -sC --script-updatedb --script-trace -O --osscan-guess -vvv --max-retries 0 --min-hostgroup 7 --max-hostgroup 1337 --max-parallelism 137 --min-parallelism 2 --max-rtt-timeout 100ms --host-timeout 30m --randomize-hosts -sN -Pn -p443 --allports --version-all --mtu 8 --version-trace --open --reason  -O --osscan-guess --traceroute --packet-trace -T2 -v yourdomain.com -vv -dd -oA /root/new_r7nmapScan -oS /root/new_r7nmapScan_sk

Default 
        
     -sS -sV -O -T4 -v --traceroute

Default, force ipv6

    -sS -sV -O -T4 -v -6 --traceroute

Default Aggresive 

    -A -sS -sV -O -T4 -v --traceroute

Default, base nse script
    
    --script=default,safe -sS -sV -O -T4 -v --traceroute 

Default, base nse script, force ipv6 

    --script=default,safe -sS -sV -O -T4 -v -6 --traceroute

#

Quick Scan 

    -T4 --traceroute

Intense scan, no ping

    -T4 -A -v -Pn --traceroute

Intense scan, all TCP Ports 

    -T4 -A -v -PE -PS22,25,80 -PA21,23,80,3389 --traceroute

Intense scan UDP
    
    -sS -sU -T4 -v --traceroute

For ipv6 add
    
    -6

Specify a DNS Server
    
    -sL --dns-server

For slow comprehensive scan

    -sS -sU -T4 -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --traceroute    
#
#

#
#
#
Search exploits

    searchsploit apache 2.2.15

Show hosts in an workspace

    hosts

Check PTR's

    host -v -T 192.168.1.37
    
Show Operating System of a host

    host -v -V 192.168.1.37

Lists all hosts in a domain, using AXFR

    host -l yourdomain.com
#   
#    

Close Multi Handler Port Conenction for rexploit

     lsof -i :6865
     kill -p PID

For monitoring
    
    tasks

#
#
#
[*] Available Framework plugins:
    
    request
    sounds
    openvas
    ips_filter
    nexpose
    beholder
    komand
    msfd
    db_credcollect
    token_adduser
    alias
    session_tagger
    aggregator
    sample
    auto_add_route
    ffautoregen
    wmap
    libnotify
    wiki
    nessus
    session_notifier
    pcap_log
    rssfeed
    sqlmap
    thread
    token_hunter
    event_tester
    socket_logger
    msgrpc
    db_tracker
    lab

#
#
#
#
#
#



Content updates include new and revised checks for vulnerabilities, patch verification, and security policy compliance.
They also include improvements to accuracy, fingerprinting and vulnerability scanning.

© 2010-2019 Rapid7 Inc, Boston, MA | Rapid7 Support Center  

#
#
#
If you are interested in learn more, install this app 
    
    NmapSi4 
 
 Is a complete Qt5-based Gui with the design goals to provide a complete nmap interface for users.
 in order to manage al option of this power security net scanner and search services vulnerability. 
 Take a look https://github.com/nmapsi4/nmapsi4
 
#
Tips

    netstat -b -a -o
    
    dnsscan site.com
    
    hping3 -s 192.168.3.7 -p 80 --flood
    
    more .bash_history > bash_history.txt
    
-----------------

#
#
#


   
    
 ҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉҉Borned To Learn Something, dedicated to my C4N6 mentors, in honor to 0x00H4C|<£ and 
to The CyberNinja passion of https://github.com/sh1nta & https://github.com/Daniels8989
