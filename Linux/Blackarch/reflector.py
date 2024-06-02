import subprocess
import logging
import geocoder
import requests

def update_mirrorlist(country=None):
    """Updates the pacman mirrorlist using reflector."""
    if not country:  # If country is not provided, try to detect it
        try:
            g = geocoder.ip('me')
            country = g.country
            logging.info("Detected country: %s", country)
        except requests.exceptions.RequestException as e:
            logging.error("Error getting location: %s", e)

    reflector_args = [
        "--latest", "10", "--sort", "rate", "--save", "/etc/pacman.d/mirrorlist",
        "--protocol", "https", "--age", "24", "--score", "100", "--fastest", "100", "--latest", "50"
    ]
    if country:
        reflector_args.extend(["--country", country])

    try:
        subprocess.run(["sudo", "reflector"] + reflector_args, check=True)
        logging.info("Mirrorlist updated successfully.")
    except subprocess.CalledProcessError as e:
        logging.error("Error updating mirrorlist: %s", e)
