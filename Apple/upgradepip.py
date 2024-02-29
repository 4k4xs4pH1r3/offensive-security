import os
import subprocess
import re

# Define function to upgrade all installed packages
def upgrade_all_packages():
    try:
        # Get a list of installed packages
        pip_list = subprocess.Popen(["pip", "list", "--format=freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = pip_list.communicate()

        # Check if the command executed successfully
        if pip_list.returncode == 0:
            installed_packages = [line.split("==")[0] for line in out.decode("utf-8").split('\n') if line]

            # Upgrade each installed package with --ignore-installed flag
            for package in installed_packages:
                try:
                    subprocess.check_call(["pip", "install", "--upgrade", "--ignore-installed", package])
                    print(f"Successfully upgraded {package}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to upgrade {package}: {e}")
        else:
            print("Failed to get the list of installed packages.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to upgrade all installed packages
def main():
    try:
        # Run the command to install a package and capture the output
        result = subprocess.run(['pip', 'install', 'your_package'], stderr=subprocess.PIPE, text=True)

        # Check if the warning message is present in the output
        if "No metadata found" in result.stderr:
            # Extract the package name from the warning using regex
            match = re.search(r"'([^']+)'", result.stderr)
            if match:
                package_with_issue = match.group(1)
                print(f"Handling metadata for {package_with_issue}")
                upgrade_all_packages()
            else:
                print("Failed to extract package name from the warning message.")
        else:
            # Continue with upgrading all installed packages if no metadata issue
            upgrade_all_packages()
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
