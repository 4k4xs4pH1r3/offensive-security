import configparser
import logging

import blackarch_packages
from blackarch_installer import AUR_HELPERS, is_helper_installed, run_command, PACMAN_CONF  # Assuming blackarch_installer.py is in the same directory

def fix_problematic_packages():
    """
    Identifies and fixes problematic packages by adding them to IgnorePkg, attempting to fix,
    then removing from IgnorePkg.
    """
    config = configparser.ConfigParser()
    config.read(PACMAN_CONF)

    problematic_packages = []
    for package in blackarch_packages.PACKAGES_TO_INSTALL:
        for helper, command in AUR_HELPERS.items():
            if not is_helper_installed(helper):
                continue

            install_command = command + [package] + ["--needed", "--noconfirm"]
            try:
                run_command(install_command)  
                break  # If successful, move to the next package
            except subprocess.CalledProcessError as e:
                logging.warning(f"Error installing '{package}' with {helper}: {e.stdout}")
                problematic_packages.append(package)  
    
    # If there are problematic packages, add them to IgnorePkg
    if problematic_packages:
        print(f"Found problematic packages: {problematic_packages}")
        if "options" not in config:
            config["options"] = {}
        config["options"]["IgnorePkg"] = " ".join(problematic_packages)

        with open(PACMAN_CONF, "w", encoding="utf-8") as configfile:
            config.write(configfile)

        fix_problematic_packages()  # Recursively call fix_ignored_packages to attempt fixing them