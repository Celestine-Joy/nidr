import subprocess
files='files/'
# Define the command to execute
command1 = ["sudo", "cicflowmeter", "-f", files+"output.pcap", "-c", files+"output.csv"]
# Execute the command
subprocess.run(command1)
