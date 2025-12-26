"""
Docstring for s1_development_environment.Load_shell_var
This is to test loading shell variables into Python environment.
"""
from dotenv import load_dotenv
load_dotenv()
import os
VAR_NAME = "KIA"
try:    
    print(os.environ[VAR_NAME])
except KeyError:
    print(f"{VAR_NAME} not found in environment variables.")
    print("Noooooooo!")
