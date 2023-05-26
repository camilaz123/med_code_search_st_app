import subprocess
import sys
import streamlit as st
import time
import importlib

# try:
#     import med_code_search.main as main

# # This block executes only on the first run when your package isn't installed
# except ModuleNotFoundError as e:
#     sleep_time = 120
#     dependency_warning = st.warning(
#         f"Installing dependencies, this takes {sleep_time} seconds."
#     )
#     subprocess.Popen(
#         [
#             f"{sys.executable} -m pip install git+https://{st.secrets['github_token']}@github.com/almeidava93/med_code_search.git",
#         ],
#         shell=True,
#     )

#     # wait for subprocess to install package before running your actual code below
#     time.sleep(sleep_time)
#     # remove the installing dependency warning
#     dependency_warning.empty()

def install_and_import():
    try:
        # Try importing the module
        importlib.import_module("med_code_search")
    except ImportError:
        # Install the module if not already installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"git+https://{st.secrets['github_token']}@github.com/almeidava93/med_code_search.git"])
    finally:
        # If the module is installed, import it
        if importlib.util.find_spec("med_code_search") is not None:
            globals()["med_code_search"] = importlib.import_module("med_code_search")
        else:
            print(f"Failed to install and import med_code_search")

install_and_import()

# Here comes the code that will only run if numpy is installed.
if 'med_code_search' in globals():
    import med_code_search.main as main

    main.app()