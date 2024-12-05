"""Removes lines containing or starting with '# checkov' (with or without
a space after #) from YAML files."""

import os


def remove_checkov_lines(filename):
    """Removes lines containing or starting with '# checkov' (with or without
    a space after #) from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                if ("#checkov" in line or line.startswith("#checkov")) or (
                    "# checkov" in line or line.startswith("# checkov")
                ):
                    continue
                f.write(line)
        print(f"Processed: {filename}")
    except OSError as e:
        print(f"Error processing {filename}: {e}")


def main():
    """Walks through the current directory and modifies all .yaml files."""
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".yaml"):
                filename = os.path.join(root, file)
                remove_checkov_lines(filename)


if __name__ == "__main__":
    main()
