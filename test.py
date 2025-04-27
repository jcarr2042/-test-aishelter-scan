import subprocess
import pickle
subprocess.call('ls', shell=True)  # <- Dangerous: CodeQL flags "Command Injection Risk"

API_KEY = "sk_test_51MabcDEF1234567890exampleSecretKey"

# Insecure Deserialization - Don't use this in production
data = b"cos\nsystem\n(S'ls'\ntR."
# Insecurely loading the data
loaded_data = pickle.loads(data)
print(loaded_data)
