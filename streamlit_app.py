import subprocess
import sys
import logging
import streamlit as st

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Define the GitHub token and repository URL
GITHUB_TOKEN = st.secrets["github_token"]
REPO_URL = "github.com/almeidava93/med_code_search"

# Install the package
try:
    logging.info("Attempting to install med_code_search package.")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            f"git+https://{GITHUB_TOKEN}@{REPO_URL}.git"
        ],
        check=True,
    )
    logging.info("Successfully installed med_code_search package.")
except subprocess.CalledProcessError:
    logging.error("Failed to install med_code_search package.")
    sys.exit(1)

# Import and use the package
try:
    from med_code_search.main import app  # Replace with the actual import
    logging.info("Successfully imported app() from med_code_search.main")
    
    # Use the imported function
    app()  # Replace with the actual function call
    logging.info("Successfully executed some_function.")
except ImportError:
    logging.error("Could not import the package or function.")
    sys.exit(1)
