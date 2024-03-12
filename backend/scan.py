from scapy.all import sniff, wrpcap

files='files/'

# Define the number of packets to capture
num_packets = 1000

# Capture the packets
packets = sniff(count=num_packets)

# Save the captured packets to a pcap file
wrpcap(files+'output.pcap', packets)