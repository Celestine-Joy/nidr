import os
import csv
def unblock_ip(ip_address,i=0):
    try:
        # The command to unblock the IP address
        command = f"sudo iptables -D INPUT -s {ip_address} -j DROP"
        
        # Execute the command
        os.system(command)
        if i ==0:
            print(f"IP address {ip_address} has been unblocked.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read the IP addresses from the CSV file
def unblock():
    with open('files/attack_source.csv', 'r') as file:
        reader = csv.reader(file)
        try:
            next(reader)  # Skip the header row
        except StopIteration:
            print("The CSV file is empty.")
            return
        for row in reader:
            ip_address = row[0]
            unblock_ip(ip_address)

# Replace with the IP address you want to unblock
#unblock_ip("180.133.201.143")