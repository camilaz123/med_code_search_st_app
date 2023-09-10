import subprocess
import streamlit as st
import importlib

def install_and_import():
    try:
        # Try importing the module
        importlib.import_module("med_code_search")
    except ImportError:
        # Install the module if not already installed
        subprocess.check_call(["python3", "-m", "pip", "install", "--user", f"git+https://almeidava93:{st.secrets['github_token']}@github.com/almeidava93/med_code_search.git"])
    finally:
        # If the module is installed, import it
        if importlib.util.find_spec("med_code_search") is not None:
            globals()["med_code_search"] = importlib.import_module("med_code_search")
        else:
            print(f"Failed to install and import med_code_search")

install_and_import()

# # Here comes the code that will only run if numpy is installed.
# if 'med_code_search' in globals():
import med_code_search.main as main

main.app()