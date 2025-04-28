# unsafe_yaml_loader.py

import yaml

def unsafe_load_user_input():
    print("Paste YAML content:")
    user_input = input()

    # ❌ Vulnerable: Using unsafe yaml.load() instead of safe_load()
    data = yaml.load(user_input, Loader=yaml.Loader)

    print("Parsed data:")
    print(data)

if __name__ == "__main__":
    unsafe_load_user_input()
