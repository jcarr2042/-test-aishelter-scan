# vulnerable_code.py

import pickle
import os

# Hardcoded AWS Secrets (triggers Secret Scanner)
AWS_ACCESS_KEY_ID = "AKIAEXAMPLE12345678"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def unsafe_load(user_input):
    # Remote Code Execution via pickle (triggers Code Scanner)
    return pickle.loads(user_input)

if __name__ == "__main__":
    payload = pickle.dumps(os.system)
    unsafe_load(payload)
