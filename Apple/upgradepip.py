# Function to upgrade a package
upgrade_package() {
  local package=$1
  if pip install --upgrade "$package" &> /dev/null; then
    echo "Successfully upgraded package: $package"
  else
    echo "Error upgrading package: $package"
    force_reinstall "$package"
  fi
}

# Function to force uninstall and reinstall a package
force_reinstall() {
  local package=$1
  echo "Force uninstalling and reinstalling $package..."
  if pip uninstall -y "$package" &> /dev/null && pip install "$package" &> /dev/null; then
    echo "Successfully reinstalled package: $package"
  else
    echo "Error reinstalling package: $package"
  fi
}

# Upgrade pip itself first
if pip install --upgrade pip &> /dev/null; then
  echo "Successfully upgraded pip."
else
  echo "Error upgrading pip."
  force_reinstall "pip"
fi

# Upgrade all other packages
pip list --outdated | grep -v '^\-e' | cut -d ' ' -f 1 | while read package; do
  upgrade_package "$package"
done
