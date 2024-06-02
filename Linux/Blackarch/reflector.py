import logging
import subprocess

import geocoder
import requests


def update_mirrorlist(country=None):
    """Updates the pacman mirrorlist using reflector, optionally filtering by country."""

    if not country:
        try:
            g = geocoder.ip("me")
            country = g.country
            logging.info("Detected country: %s", country)
        except (
            requests.exceptions.RequestException,
            geocoder.api.exceptions.GeocoderError,
        ) as e:
            logging.warning("Error getting location, using all mirrors: %s", e)

    reflector_args = [
        "--latest",
        "10",
        "--sort",
        "rate",
        "--save",
        "/etc/pacman.d/mirrorlist",
        "--protocol",
        "https",
        "--age",
        "24",
        "--score",
        "100",
        "--fastest",
        "100",
        "--latest",
        "50",
    ]

    if country:
        reflector_args.extend(["--country", country])

    logging.info(
        "Updating mirrorlist with arguments: %s", reflector_args
    )  # Log the arguments

    try:
        result = subprocess.run(
            ["sudo", "reflector"] + reflector_args,
            capture_output=True,
            text=True,
            check=True,
        )
        logging.info("Mirrorlist updated successfully. Output:\n%s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Error updating mirrorlist: %s", e.stderr)
