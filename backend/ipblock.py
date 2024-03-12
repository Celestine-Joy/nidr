import os
import subprocess

def block_ip(ip_address):
    try:
        # The command to block the IP address
        command = f"sudo iptables -A INPUT -s {ip_address} -j DROP"
        
        # Execute the command
        os.system(command)
        
        print(f"IP address {ip_address} has been blocked.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with the IP address you want to block
block_ip("180.133.201.143")