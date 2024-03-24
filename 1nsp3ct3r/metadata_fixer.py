import os
import sys
import logging
import warnings
import importlib.metadata as metadata_module
import subprocess
import json

def create_metadata_file(package_name, version, metadata_path):
    try:
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(metadata_path), exist_ok=True)
        
        # Touch the file to create it
        with open(metadata_path, 'a'):
            os.utime(metadata_path, None)
        logging.info(f"Created metadata file for package '{package_name}' version '{version}' at: {metadata_path}")
    except Exception as e:
        logging.error(f"An error occurred while creating metadata file: {e}")

def check_metadata_files(package_directory):
    for package in metadata_module.distributions():
        package_name = package.metadata['Name']
        version = package.version
        metadata_path = os.path.join(package_directory, f"{package_name}-{version}.dist-info", "METADATA")

        if not os.path.exists(metadata_path):
            logging.info(f"Metadata file does not exist for package '{package_name}' version '{version}' at: {metadata_path}")
            create_metadata_file(package_name, version, metadata_path)
        else:
            try:
                # Attempt to read the metadata file to catch any parsing errors
                with open(metadata_path, 'r') as file:
                    file.read()
            except Exception as e:
                logging.error(f"Error parsing metadata file for package '{package_name}' version '{version}': {e}")

def upgrade_non_standard_packages():
    # Function to check if a version conforms to PEP 440 standards
    def is_standard_version(version):
        # You can implement your own logic here to check if the version conforms to PEP 440
        return True

    # Get the Python executable path
    python_executable = sys.executable

    # Get the directory containing the Python packages
    package_directory = os.path.join(os.path.dirname(python_executable), 'lib', 'site-packages')

    # Get a list of installed packages and their versions
    try:
        output = subprocess.check_output([python_executable, '-m', 'pip', 'list', '--format=json'])
        installed_packages = json.loads(output.decode())
    except Exception as e:
        logging.error(f"Error retrieving list of installed packages: {e}")
        return

    # Iterate through installed packages
    for package in installed_packages:
        package_name = package['name']
        package_version = package['version']

        # Check if the package version is non-standard
        if not is_standard_version(package_version):
            # Upgrade the package
            print(f"Upgrading {package_name} from version {package_version}...")
            subprocess.call([python_executable, '-m', 'pip', 'install', '--upgrade', package_name])

def main():
    logging.basicConfig(level=logging.INFO)

    # Get the Python executable path
    python_executable = sys.executable

    # Get the directory containing the Python packages
    package_directory = os.path.join(os.path.dirname(python_executable), 'lib', 'site-packages')

    check_metadata_files(package_directory)
    upgrade_non_standard_packages()

if __name__ == "__main__":
    main()
    
