import subprocess
import re
import pkg_resources

# Define function to upgrade a specific package
def upgrade_package(package):
    try:
        subprocess.check_call(["pip", "install", "--upgrade", package])
        print(f"Successfully upgraded {package}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to upgrade {package}: {e}")

# Define function to upgrade all installed packages
def upgrade_all_packages():
    try:
        installed_distributions = [d for d in pkg_resources.working_set]

        # Upgrade each installed package
        for dist in installed_distributions:
            upgrade_package(dist.project_name)
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to upgrade all installed packages
def main():
    try:
        # Run the command to install pipdeptree and capture the output
        subprocess.run(['pip', 'install', 'pipdeptree'], stderr=subprocess.PIPE, text=True)
        subprocess.run(['pipx', 'install', 'pipdeptree'], stderr=subprocess.PIPE, text=True)

        # Run the command to get the dependencies of all installed packages
        subprocess.run(['pipdeptree', '--warn silence', '--warn silence', '-p'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Upgrade all installed packages
        upgrade_all_packages()
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
