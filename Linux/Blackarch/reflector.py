import subprocess
import logging

def update_mirrorlist(country=None):
    """Updates the pacman mirrorlist using reflector."""
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

