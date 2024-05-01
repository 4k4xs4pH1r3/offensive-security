---
DIRB v2.22
By The Dark Raver
---

#

    sudo apt install dirb -y && cd /usr/share && git clone https://github.com/danielmiessler/SecLists.git && chmod +x /usr/share/dirb/wordlists/*.* && cd /root

#

    dirb https://arkham/ -x /usr/share/dirb/wordlists/vulns/* /usr/share/dirb/wordlists/extensions_common.txt -a random -R -w -b -l -N 301 -o /root/SA/ad/dirb_scan

#

    tail -f /root/SA/ad/dirb_scan
