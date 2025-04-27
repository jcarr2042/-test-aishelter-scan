import subprocess
subprocess.call('ls', shell=True)  # <- Dangerous: CodeQL flags "Command Injection Risk"

API_KEY = "sk_test_51MabcDEF1234567890exampleSecretKey"
