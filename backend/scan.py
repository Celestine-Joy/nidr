from scapy.all import sniff, wrpcap
import subprocess


files='files/'

interface = 'any'

# Define the number of packets to capture
num_packets = 500


# Capture the packets
#packets = sniff(count=num_packets)

# Save the captured packets to a pcap file
#wrpcap(files+'output.pcap', packets)



# Run tshark command to capture packets and save to a pcap file
subprocess.run(['tshark', '-i', interface, '-c', str(num_packets), '-w', files+'output.pcap'])                    
