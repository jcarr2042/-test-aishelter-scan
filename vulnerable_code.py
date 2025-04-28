import pickle
import os
import yaml

# -- Hardcoded Secrets (should trigger Secret Scanner) --
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

PRIVATE_API_KEY = "sk-test-4eC39HqLyjWDarjtT1zdp7dc"

# -- Dangerous Deserialization (should trigger Code Scanner) --
def unsafe_pickle_load(pickled_data):
    return pickle.loads(pickled_data)

# -- Unsafe YAML Loading (should trigger Code Scanner) --
def unsafe_yaml_load(yaml_data):
    return yaml.load(yaml_data)  # Using yaml.load unsafely instead of safe_load

if __name__ == "__main__":
    # Example malicious payloads
    bad_pickle = pickle.dumps(os.system)
    unsafe_pickle_load(bad_pickle)

    bad_yaml = "!!python/object/apply:os.system ['echo vulnerable']"
    unsafe_yaml_load(bad_yaml)
