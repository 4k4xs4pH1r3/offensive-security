import yaml

# Load the YAML file
with open("x.yaml", "r") as f:
    data = yaml.safe_load(f)

# Process dependencies, handling both strings and dictionaries
new_dependencies = []
for item in data["dependencies"]:
    if isinstance(item, str):
        package_name = item.split("=")[0]
        new_dependencies.append(package_name)
    elif isinstance(item, dict):
        # Assuming each dictionary has one key-value pair
        package_name = list(item.keys())[0].split("=")[0]
        new_dependencies.append(package_name)

# Update the dependencies in the data
data["dependencies"] = new_dependencies

# Write the modified data back to the YAML file
with open("x.yaml", "w") as f:
    yaml.dump(data, f, indent=2)  # Added indent for better readability
