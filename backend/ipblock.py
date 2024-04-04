import os
import csv
from backend.ipunblk import unblock_ip
#import subprocess

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
#block_ip("180.133.201.143")

# Read the IP addresses from the CSV file
def block():
    with open('files/attack_source.csv', 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)  # Skip the header row
        except StopIteration:
            print("The CSV file is empty.")
            return
        for row in reader:
            ip_address = row[0]
            unblock_ip(ip_address,1)
            block_ip(ip_address)
