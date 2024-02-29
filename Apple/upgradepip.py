import subprocess
import re
from tqdm import tqdm
from colorama import Fore, Style
import shutil
import sys

# Install missing type stubs as a prerequisite
def install_missing_stubs():
    try:
        # Check if types-tqdm is installed
        subprocess.run([sys.executable, '-m', 'pip', 'show', 'types-tqdm'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}Installing types-tqdm stubs...{Style.RESET_ALL}")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'types-tqdm'], check=True)

    try:
        # Check if types-colorama is installed
        subprocess.run([sys.executable, '-m', 'pip', 'show', 'types-colorama'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.YELLOW}Installing types-colorama stubs...{Style.RESET_ALL}")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'types-colorama'], check=True)


# Function to determine the installation method and upgrade a specific package
def upgrade_package(package):
    try:
        # Get the installation method (pip, pip2, pip3, pipx)
        method_result = subprocess.run(["pip", "show", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        installation_method = None

        if "pipx" in method_result.stdout:
            installation_method = "pipx"
        elif "pip3" in method_result.stdout:
            installation_method = "pip3"
        elif "pip2" in method_result.stdout:
            installation_method = "pip2"
        elif "pip" in method_result.stdout:
            installation_method = "pip"

        if installation_method:
            # Check if the package is already installed using the determined method
            installed_result = subprocess.run([installation_method, "show", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            if "Version" in installed_result.stdout:
                # Upgrade the package using the determined installation method
                subprocess.check_call([installation_method, "install", "--upgrade", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"{Fore.GREEN}Successfully upgraded {package} using {installation_method}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{package} not installed using {installation_method}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to determine the installation method for {package}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Failed to upgrade {package}: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred while upgrading {package}: {e}{Style.RESET_ALL}")

        
# Function to upgrade a specific package and return success or failure
def upgrade_package_result(package):
    try:
        subprocess.check_call(["pip", "install", "--upgrade", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, f"{Fore.GREEN}Successfully upgraded {package}{Style.RESET_ALL}"
    except subprocess.CalledProcessError as e:
        return False, f"{Fore.RED}Failed to upgrade {package}: {e}{Style.RESET_ALL}"
    except Exception as e:
        return False, f"{Fore.RED}An unexpected error occurred while upgrading {package}: {e}{Style.RESET_ALL}"

# Function to upgrade all installed packages and provide a summary with a colorized progress bar
def upgrade_all_packages():
    success_count = 0
    failure_count = 0
    failure_messages = []

    try:
        # Get a list of installed packages
        pip_list = subprocess.Popen(["pip", "list", "--format=freeze"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = pip_list.communicate()

        # Check if the command executed successfully
        if pip_list.returncode == 0:
            installed_packages = [line.split("==")[0] for line in out.decode("utf-8").split('\n') if line]

            # Upgrade each installed package with tqdm progress bar
            for package in tqdm(installed_packages, desc=f"{Fore.CYAN}Upgrading Packages{Style.RESET_ALL}", unit="package", bar_format="{l_bar}{bar:10}{r_bar}"):
                success, message = upgrade_package_result(package)
                if success:
                    success_count += 1
                else:
                    failure_count += 1
                    failure_messages.append(message)

        else:
            print(f"{Fore.RED}Failed to get the list of installed packages.{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

    # Print summary
    print(f"\n{Fore.GREEN}Summary:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Successfully upgraded {success_count} packages.{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed to upgrade {failure_count} packages.{Style.RESET_ALL}")
    for failure_message in failure_messages:
        print(failure_message)

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
                print(f"{Fore.YELLOW}Handling metadata for {package_with_issue}{Style.RESET_ALL}")
                success, message = upgrade_package_result(package_with_issue)
                if not success:
                    print(f"{Fore.RED}Failed to handle metadata for {package_with_issue}: {message}{Style.RESET_ALL}")
        else:
            # Continue with upgrading all installed packages if no metadata issue
            upgrade_all_packages()
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

# Call the main function if the script is executed
if __name__ == "__main__":
    main()
