import subprocess
import os 
import pickle 

# 🚨 HIGH severity real-world vulnerability: Command Injection
def run_command(user_input):
    # Bad: directly interpolating untrusted input into a shell command
    cmd = "echo " + user_input
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    user_input = input("Enter your command: ")
    run_command(user_input)
