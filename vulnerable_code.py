import os

def unsafe_system_call(user_input):
    os.system("echo " + user_input)
