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

import geocoder  # Geolocation library
import requests  # HTTP library for geolocation

import blackarch_packages
import blackarch_repos
import helpers
import reflector  # Import the reflector module

# --- Global Variables ---
PACMAN_CONF = "/etc/pacman.conf"
LOG_FILE = "/tmp/blackarch_installer.log"

AUR_HELPERS = helpers.AUR_HELPERS

# --- Functions ---
def run_command(
    command: list[str],
    suppress_output: bool = False,
    retries: int = 3,
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
                " ".join(command), attempt + 1, retries
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


def fix_ignored_packages():
    """Fixes packages in pacman.conf's IgnorePkg section."""
    config = configparser.ConfigParser()
    config.read(PACMAN_CONF)

    if "options" not in config or "IgnorePkg" not in config["options"]:
        return  # No ignored packages

    ignored_packages = config["options"]["IgnorePkg"].split()
    for helper, command in AUR_HELPERS.items():
        if not is_helper_installed(helper):
            logging.warning("Helper %s not installed. Skipping...", helper)
            continue

        for package in ignored_packages:
            print(f"Fixing ignored package: {package}")
            install_command = command + [package] + ["--needed", "--noconfirm"]
            try:
                run_command(install_command)
                print(f"Fixed: {package}")
                config.remove_option("options", "IgnorePkg")
                with open(PACMAN_CONF, "w", encoding="utf-8") as configfile:
                    config.write(configfile)
            except subprocess.CalledProcessError:
                pass  


def verify_blackarch_categories():
    """Verifies BlackArch category installations."""

    for category in blackarch_packages.CATEGORIES:
        try:
            subprocess.run(
                ["pacman", "-Qs", category], check=True, stdout=subprocess.DEVNULL
            )
            print(f"Category '{category}' installed.")
        except subprocess.CalledProcessError:
            msg = (
                f"WARNING: Category '{category}' not installed or incomplete."
            )
            print(msg)
            logging.warning(msg)

def get_current_country():
    """Attempts to determine the user's current country using geolocation."""
    try:
        g = geocoder.ip("me")
        return g.country
    except requests.exceptions.RequestException as e:
        logging.error("Error getting location: %s", e)
        return None
    
# --- Main Execution ---
with open(LOG_FILE, "w"):  # Clear log file
    pass

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Install any missing helpers
subprocess.run(["sudo", "python", os.path.join(os.path.dirname(__file__), "helpers.py")], check=True)

fix_ignored_packages()
mirrors = blackarch_repos.fetch_mirrors()

current_country = get_current_country()


for mirror in mirrors:
    logging.info("Trying mirror: %s", mirror)
    with open(blackarch_repos.MIRRORLIST_FILE, "w", encoding="utf-8") as file:
        file.write(f"Server = {mirror}\n")  # Use only the current mirror

    try:
        run_command(["sudo", "pacman", "-Sy"], retries=3)
    except subprocess.CalledProcessError:
        logging.warning("Mirror %s failed, trying next...", mirror)
        continue  # Go to the next mirror if this one fails

    # If the mirror works, proceed with installations
    for helper, command in AUR_HELPERS.items():
        if not is_helper_installed(helper):
            logging.warning("Helper %s not installed...", helper)
            continue

        print(f"Trying AUR helper: {helper}")
        install_command = command + blackarch_packages.PACKAGES_TO_INSTALL + ["--needed", "--noconfirm", "--disable-download-timeout", "--noprogressbar"]

        try:
            run_command(install_command, suppress_output=True)
            print("All packages installed successfully!")

            verify_blackarch_categories()
            
            reflector.update_mirrorlist(current_country)
            return  # Exit if installation is successful
        except subprocess.CalledProcessError:
            pass  # Move on to the next helper if this one fails

logging.error("No working mirror found. Check mirrorlist & connection.")
print("No working mirror found. Check the log file for details.")

