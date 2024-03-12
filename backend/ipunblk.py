import os

def unblock_ip(ip_address):
    try:
        # The command to unblock the IP address
        command = f"sudo iptables -D INPUT -s {ip_address} -j DROP"
        
        # Execute the command
        os.system(command)
        
        print(f"IP address {ip_address} has been unblocked.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with the IP address you want to unblock
unblock_ip("180.133.201.143")