"""Add Checkov skip comments."""

import glob
import logging
from typing import Dict, Set

from tqdm import tqdm  # type: ignore

# Configure logging.
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global aliases and variables.
PROCESSED_FINDINGS: Dict[str, Set[str]] = {}
FAILED_RESOURCE_STR = "FAILED for resource"
CHECK_STR = "Check:"
FILE_STR = "    File: "


def add_checkov_skip(filename: str, checkov_id: str, lineno: int):
    """Add skip comment if it doesn't already exist in the file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            file_content = f.read()

        if f"# checkov:skip={checkov_id}" not in file_content:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
            lineno = max(0, min(lineno, len(lines) - 1))
            lines[lineno] = f"# checkov:skip={checkov_id}\n" + lines[lineno]
            logging.info("Updated: %s - line %s", filename, lineno + 1)
            with open(filename, "w", encoding="utf-8") as f:
                f.writelines(lines)
        else:
            logging.info(
                "Skip comment already exists in %s for %s", filename, checkov_id
            )
    except OSError as e:
        logging.exception("Error adding Checkov skip to %s: %s", filename, e)


def extract_finding_info(
    lines: list[str], lineno: int
) -> tuple[str | None, str | None, int | None]:
    """Extract finding info."""
    check_line = lines[lineno - 1]
    checkov_id = check_line.split(":")[1].strip()
    file_line = lines[lineno + 1]
    parts = file_line.split(":")
    if len(parts) < 3:
        # Suppress the warning message
        # logging.warning("Unexpected format in file line: %s", file_line)
        return None, None, None
    file_path = parts[1].strip()
    line_info = parts[2].strip()
    start_line, _ = map(int, line_info.split("-"))
    return checkov_id, file_path, start_line


def process_finding(filename: str, lines: list[str], lineno: int):
    """Process finding."""
    try:
        checkov_id, file_path, start_line = extract_finding_info(lines, lineno)
        if not checkov_id or not file_path or not start_line:
            return

        # Include start_line in finding_id
        finding_id = f"{file_path}:{checkov_id}:{start_line}"

        if finding_id in PROCESSED_FINDINGS[filename]:
            logging.debug(
                "Skipping already processed finding: %s in %s", finding_id, filename
            )
            return

        add_checkov_skip(file_path, checkov_id, start_line - 1)
        PROCESSED_FINDINGS[filename].add(finding_id)
    except OSError as e:
        logging.exception("Error processing finding in %s: %s", filename, e)


def process_file(filename: str):
    """Process file."""
    try:
        logging.info("Processing file: %s", filename)
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if filename not in PROCESSED_FINDINGS:
            PROCESSED_FINDINGS[filename] = set()
        total_findings = lines.count(FAILED_RESOURCE_STR)
        with tqdm(total=total_findings, desc="Adding skips", unit="finding") as pbar:
            for lineno, line in enumerate(lines):
                if FAILED_RESOURCE_STR in line:
                    process_finding(filename, lines, lineno)
                    pbar.update(1)
        logging.info("Finished processing file: %s", filename)
    except OSError as e:
        logging.exception("Error processing %s: %s", filename, e)


def validate_findings(files):
    """Validate if all findings were processed."""
    all_findings_processed = True
    for filename in files:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if FAILED_RESOURCE_STR in line:
                    try:
                        file_line = lines[i + 1]
                        check_line = lines[i - 1]
                        file_path = file_line.split(":")[1].strip()
                        checkov_id = check_line.split(":")[1].strip()
                        finding_id = f"{file_path}:{checkov_id}"
                        if finding_id not in PROCESSED_FINDINGS.get(filename, set()):
                            logging.error(
                                "Finding not processed: %s in %s", finding_id, filename
                            )
                            all_findings_processed = False
                    except IndexError:
                        # Suppress the error message
                        # logging.error("wrong fmt %d of %s", i + 1, filename)
                        all_findings_processed = False
    return all_findings_processed


def process_files(pattern: str):
    """Process files."""
    logging.info("Started processing files.")
    files = glob.glob(pattern)
    for filename in tqdm(files, desc="Processing files", unit="file"):
        process_file(filename)

    if validate_findings(files):
        logging.info("All findings processed successfully.")
    else:
        logging.warning("Some findings were not processed.")


if __name__ == "__main__":
    process_files("git-error-*")
