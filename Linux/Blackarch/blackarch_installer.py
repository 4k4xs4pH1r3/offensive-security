#!/usr/bin/env python3
"""Automates BlackArch installation on Arch Linux.

Handles problematic packages, mirror selection, and dependency resolution.
"""

import configparser
import logging
import os
import subprocess
import time
import typing

import blackarch_packages
import blackarch_repos
import helpers
import missing_helpers
import problematic_packages
import reflector

# --- Constants ---
PACMAN_CONF = "/etc/pacman.conf"
LOG_FILE = "/tmp/blackarch_installer.log"


# --- Functions ---
def run_command(
    command: list[str], suppress_output=False, retries=3
) -> typing.Optional[str]:
    """Runs a shell command with optional retries and output suppression."""
    for attempt in range(retries):
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT if suppress_output else subprocess.PIPE,
                encoding="utf-8",
            )
            return result.stdout  # Return the standard output
        except subprocess.CalledProcessError as e:
            logging.warning(
                "Command '%s' failed (attempt %d/%d):",
                " ".join(command),
                attempt + 1,
                retries,
            )
            logging.warning("Error output:\n%s", e.stdout)  # Log error output
            if attempt < retries - 1:
                time.sleep(5)
            else:
                raise


def is_helper_installed(helper: str) -> bool:
    """Checks if the given AUR helper is installed."""
    if helper == "pacman":
        return True
    try:
        subprocess.run([helper, "--version"], check=True, stdout=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False


def get_current_country() -> typing.Optional[str]:
    """Attempts to determine the user's current country using geolocation."""
    try:
        g = geocoder.ip("me")
        return g.country
    except (
        requests.exceptions.RequestException,
        geocoder.api.exceptions.GeocoderError,
    ) as e:
        logging.error("Error getting location: %s", e)
        return None


def install_with_mirror_and_helper(mirror: str, helper: str) -> bool:
    """Attempts to install BlackArch packages using a specific mirror and helper."""
    with open(blackarch_repos.MIRRORLIST_FILE, "w", encoding="utf-8") as file:
        file.write(f"Server = {mirror}\n")

    try:
        run_command(["sudo", "pacman", "-Sy"], retries=3)
        run_command(
            helpers.AUR_HELPERS[helper]
            + blackarch_packages.PACKAGES_TO_INSTALL
            + [
                "--needed",
                "--noconfirm",
                "--disable-download-timeout",
                "--noprogressbar",
            ],
            suppress_output=True,
        )
        print("All packages installed successfully!")
        verify_blackarch_categories()
        reflector.update_mirrorlist(get_current_country())
        return True
    except subprocess.CalledProcessError:
        return False


# --- Main Execution ---

with open(LOG_FILE, "w"):  # Clear log file
    pass

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

missing_helpers.main()  # Install any missing helpers
problematic_packages.fix_problematic_packages()  # Fix problematic packages first
mirrors = blackarch_repos.fetch_mirrors()

for mirror in mirrors:
    logging.info("Trying mirror: %s", mirror)
    for helper in AUR_HELPERS:
        if is_helper_installed(helper):
            print(f"Trying AUR helper: {helper}")
            if install_with_mirror_and_helper(mirror, helper):
                exit(0)

logging.error("No working mirror found. Check mirrorlist & connection.")
print("No working mirror found. Check the log file for details.")
