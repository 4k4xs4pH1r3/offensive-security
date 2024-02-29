import subprocess
import re
import shutil

# Function to determine the installation method and upgrade a specific package
def upgrade_package(package):
    installation_methods = ["pipx", "pip3", "pip2", "pip", "brew"]

    for method in installation_methods:
        try:
            if method == "pip2" and not shutil.which("pip2"):
                continue  # Skip if pip2 is not installed, try the next method
            elif method == "brew":
                subprocess.check_call(["brew", "upgrade", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"Successfully upgraded {package} using {method}")
                return  # Break the loop if the upgrade is successful
            else:
                # Check if the package is already installed using the determined method
                installed_result = subprocess.run([method, "show", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                if "Version" in installed_result.stdout:
                    # Upgrade the package using the determined installation method
                    subprocess.check_call([method, "install", "--upgrade", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(f"Successfully upgraded {package} using {method}")
                    return  # Break the loop if the upgrade is successful
                else:
                    print(f"{package} not installed using {method}. Trying the next method...")
        except subprocess.CalledProcessError as e:
            print(f"Failed to upgrade {package} using {method}: {e}")

    print(f"Failed to upgrade {package} using any available method")


# Function to upgrade all installed packages
def upgrade_all_packages():
    try:
        # Get a list of installed packages
        pip_list = subprocess.Popen(["pip", "list", "--format=freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = pip_list.communicate()

        # Check if the command executed successfully
        if pip_list.returncode == 0:
            installed_packages = [line.split("==")[0] for line in out.decode("utf-8").split('\n') if line]

            # Upgrade each installed package
            for package in installed_packages:
                upgrade_package(package)
        else:
            print("Failed to get the list of installed packages.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to upgrade all installed packages
def main():
    try:
        # Run the command to install a package and capture the output
        result = subprocess.run(['pip', 'install', 'your_package'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the warning message is present in the output
        if "No metadata found" in result.stderr:
            # Extract the package name from the warning using regex
            match = re.search(r"'([^']+)'", result.stderr)
            if match:
                package_with_issue = match.group(1)
                print(f"Handling metadata for {package_with_issue}")
                upgrade_package(package_with_issue)
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
