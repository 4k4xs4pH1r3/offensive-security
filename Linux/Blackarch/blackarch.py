#!/usr/bin/env python3
import subprocess
import time
import logging
import configparser
import blackarch_repos
import blackarch_packages

PACMAN_CONF_FILE = "/etc/pacman.conf"
LOG_FILE = "/tmp/blackarch_installer.log"

AUR_HELPERS = {
    "yay": ["yay", "-S"],
    "paru": ["paru", "-S"],
    "bauh": ["bauh", "-c"],
    "pacaur": ["pacaur", "-S"],
}

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def run_command(command, suppress_output=False, retries=3):
    for attempt in range(retries):
        try:
            result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT if suppress_output else subprocess.PIPE,
            )
            return result.stdout.decode()
        except subprocess.CalledProcessError as e:
            logging.warning(
                f"Command failed (attempt {attempt + 1}/{retries}): {' '.join(command)}"
            )
            logging.warning(f"Error output:\n{e.stdout.decode()}")

            if attempt < retries - 1:
                time.sleep(5)
            else:
                raise


def is_helper_installed(helper):
    try:
        subprocess.run([helper, "--version"], check=True, stdout=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False


def fix_ignored_packages():
    config = configparser.ConfigParser()
    config.read(PACMAN_CONF_FILE)

    if "options" not in config or "IgnorePkg" not in config["options"]:
        return

    ignored_packages = config["options"]["IgnorePkg"].split()

    for helper, command in AUR_HELPERS.items():
        if not is_helper_installed(helper):
            logging.warning(f"AUR helper {helper} is not installed. Skipping...")
            continue

        for package in ignored_packages:
            print(f"\nTrying to fix ignored package: {package}")
            install_command = command + [package] + ["--needed", "--noconfirm"]

            try:
                run_command(install_command)
                print(f"Fixed ignored package: {package}")
                config.remove_option("options", "IgnorePkg")
                with open(PACMAN_CONF_FILE, "w") as configfile:
                    config.write(configfile)
            except subprocess.CalledProcessError:
                pass


def verify_blackarch_categories():
    categories = blackarch_packages.CATEGORIES

    for category in categories:
        try:
            subprocess.run(
                ["pacman", "-Qs", category], check=True, stdout=subprocess.DEVNULL
            )
            print(f"Category '{category}' is installed.")
        except subprocess.CalledProcessError:
            print(
                f"WARNING: Category '{category}' is not installed or incomplete. Please check the logs for details."
            )
            logging.warning(f"Category '{category}' is not installed or incomplete.")


def main():
    fix_ignored_packages()

    mirrors = blackarch_repos.fetch_mirrors()

    for mirror in mirrors:
        logging.info(f"Trying mirror: {mirror}")
        with open(blackarch_repos.MIRRORLIST_FILE, "w") as file:
            # Uncomment all and then comment all except the current mirror
            for m in mirrors:
                if m == mirror:
                    file.write(f"Server = {m}\n")
                else:
                    file.write(f"#Server = {m}\n")

        try:
            run_command(["sudo", "pacman", "-Sy"], retries=3)
        except subprocess.CalledProcessError:
            logging.warning(f"Mirror {mirror} failed, trying the next one...")
            continue  # Go to the next mirror if this one fails

        # If the mirror works, proceed with installations
        for helper, command in AUR_HELPERS.items():
            if not is_helper_installed(helper):
                logging.warning(f"AUR helper {helper} is not installed. Skipping...")
                continue

            print(f"Trying AUR helper: {helper}")
            install_command = (
                command
                + blackarch_packages.PACKAGES_TO_INSTALL
                + [
                    "--needed",
                    "--noconfirm",
                    "--disable-download-timeout",
                    "--noprogressbar",
                ]
            )

            try:
                run_command(install_command, suppress_output=True)
                print("All packages installed successfully!")

                # Verify BlackArch categories after successful installation
                verify_blackarch_categories()
                return  # Exit if installation is successful
            except subprocess.CalledProcessError:
                pass  # Move on to the next helper if this one fails

    logging.error("No working mirror found. Please check your mirrorlist and internet connection.")
    print("No working mirror found. Check the log file for details.")

if __name__ == "__main__":
    main()
