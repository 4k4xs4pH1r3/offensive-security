# Droopescan    
    
    apt-get install python-pip -y && pip install droopescan
#
    droopescan scan drupal -u https://yourappservice.com -e a --debug-requests --method forbidden -t 37 --threads-identify 37 --threads-scan 37 --threads-enumerate 37 --output standard --error-log erros --debug --verb get
