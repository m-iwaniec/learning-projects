# testing internet bandwidth using speedtest.net from the Command Line
# if you do not have it installed, you must run the command below in the terminal
# pip3 install speedtest-cli

import subprocess

returned_text = subprocess.check_output("speedtest-cli", shell=True, universal_newlines=True)
print("\nSEE YOUR INTERNET SPEED BELOW:\n")
print(returned_text)
