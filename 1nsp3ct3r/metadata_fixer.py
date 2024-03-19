import os
import subprocess
import sys
import requests
import socket
from urllib.parse import urlparse

# Redirect stderr to /dev/null to suppress warnings
sys.stderr = open(os.devnull, 'w')

# BuiltWith API key (replace 'YOUR_API_KEY' with your actual API key)
BUILTWITH_API_KEY = "YOUR_API_KEY"

# Restore stderr after import subprocess
sys.stderr = sys.__stderr__

# Function to extract hostname from URL
def extract_hostname(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    if hostname:
        return hostname
    else:
        print("[-] Error: Could not extract hostname from URL.")
        sys.exit(1)

# Function to convert URL to IP addresses (both IPv4 and IPv6)
def url_to_ips(url):
    try:
        ipv4_addresses = set()
        ipv6_addresses = set()
        # Resolve both IPv4 and IPv6 addresses
        addr_info = socket.getaddrinfo(url, None)
        for family, _, _, _, address in addr_info:
            ip = address[0]
            if family == socket.AF_INET:
                ipv4_addresses.add(ip)
            elif family == socket.AF_INET6:
                ipv6_addresses.add(ip)
        return ipv4_addresses, ipv6_addresses
    except socket.gaierror as e:
        print(f"Error converting URL to IP: {e}")
        return set(), set()

# Function to query BuiltWith API
def query_builtwith_api(url):
    print("[+] Querying BuiltWith API...")
    try:
        response = requests.get(f"https://api.builtwith.com/v18/api.json?KEY={BUILTWITH_API_KEY}&LOOKUP={url}")
        data = response.json()
        technologies = data.get("Groups")
        if technologies:
            for group in technologies:
                if group.get("Name") == "Web Servers":
                    print("[+] Web hosting software determined from BuiltWith API:", group.get("Technologies"))
                    return
            print("[+] Web hosting software not found in BuiltWith API response.")
        else:
            print("[+] No technologies found in BuiltWith API response.")
    except Exception as e:
        print("[-] Error querying BuiltWith API:", str(e))

# Function to perform port scan using Naabu
def port_scan(url, ipv4_addresses, ipv6_addresses):
    print("[+] Performing port scan using Naabu...")
    for ip in ipv4_addresses:
        subprocess.run(["naabu", "-host", ip])
    for ip in ipv6_addresses:
        subprocess.run(["naabu", "-host", ip])

# Function to get web hosting software
def get_web_hosting_software(url):
    print("[+] Getting web hosting software...")
    try:
        response = requests.get(url)
        server_header = response.headers.get("Server")
        if server_header:
            print("[+] Web hosting software determined from HTTP headers: ", server_header)
        else:
            print("[+] Web hosting software could not be determined from HTTP headers.")
            query_builtwith_api(url)
    except Exception as e:
        print("[-] Error getting web hosting software:", str(e))
        query_builtwith_api(url)

# Function to identify WAF
def identify_waf(url):
    print("[+] Identifying WAF...")
    try:
        # Set SOCKS proxy environment variable
        env = os.environ.copy()
        env['SOCKS_PROXY'] = 'socks5://127.0.0.1:9050'
        
        # Run WhatWaf with the environment variable set
        subprocess.run(["whatwaf", "-u", url], env=env)
    except FileNotFoundError:
        print("[-] Error: WhatWaf not found. Make sure it's installed and accessible in the PATH.")
    except subprocess.CalledProcessError as e:
        print("[-] Error running WhatWaf:", e)
    
    try:
        # Run Wafw00f with the environment variable set
        subprocess.run(["wafw00f", url], env=env)
    except FileNotFoundError:
        print("[-] Error: Wafw00f not found. Make sure it's installed and accessible in the PATH.")
    except subprocess.CalledProcessError as e:
        print("[-] Error running Wafw00f:", e)

# Function for content discovery
def content_discovery(url):
    print("[+] Performing content discovery...")
    # Content discovery can be done using tools like DirBuster, Dirsearch, or Gobuster.

# Function to get URLs using WaybackPy
def get_urls(url):
    print("[+] Getting URLs from Wayback Machine...")
    try:
        # Call WaybackPy as a subprocess
        result = subprocess.run(["waybackpy", url], capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            print(output)
        else:
            print("[-] No URLs found in Wayback Machine for the given URL.")
    except Exception as e:
        print("[-] Error getting URLs from Wayback Machine:", str(e))

# Main function to execute all tasks
def main():
    target_url = "https://enterpriseportal.verizon.com/home/#/notifications"
    print("### Initial Info Gathering\n")
    hostname = extract_hostname(target_url)
    ipv4_addresses, ipv6_addresses = url_to_ips(hostname)
    port_scan(target_url, ipv4_addresses, ipv6_addresses)
    get_web_hosting_software(target_url)
    identify_waf(target_url)
    content_discovery(target_url)
    get_urls(target_url)

if __name__ == "__main__":
    main()
