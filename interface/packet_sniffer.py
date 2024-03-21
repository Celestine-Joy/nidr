import subprocess
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import sys


class PacketSnifferThread(QThread):
    packet_sniffed = pyqtSignal(str)
    incoming_count_changed = pyqtSignal(int)
    outgoing_count_changed = pyqtSignal(int)


    def __init__(self):
        super(PacketSnifferThread, self).__init__()
        self.incoming_count = 0
        self.outgoing_count = 0



    def run(self):
        interface = 'any'
        command = ['tshark', '-i', interface, '-T', 'fields', '-e', 'frame.time_epoch', '-e', 'ip.src', '-e', 'ip.dst', '-e', '_ws.col.Protocol', '-e', 'frame.len', '-e', '_ws.col.Info']
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        try:
            for line in process.stdout:
                print(line.strip())  # Print the raw packet before formatting
                formatted_packet = self.format_packet(line.strip())
                if formatted_packet:
                    print(formatted_packet)
                    self.packet_sniffed.emit(formatted_packet)
        except KeyboardInterrupt:
            print("Stopping capture...")
            process.terminate()

    def increment_incoming(self):
        self.incoming_count += 1
        self.incoming_count_changed.emit(self.incoming_count)

    def increment_outgoing(self):
        self.outgoing_count += 1
        self.outgoing_count_changed.emit(self.outgoing_count)

    def format_packet(self, line):
        fields = line.split('\t')
        if len(fields) >= 6:  # Check if the line contains at least 6 fields
            time = fields[0]
            source = fields[1]
            destination = fields[2]
            protocol = fields[3]
            length = fields[4]
            info = fields[5]
            if source == '192.168.127.128':
                self.increment_outgoing()
            else:
                self.increment_incoming()

            formatted_packet = f"{time} | {source} | {destination} | {protocol} | {length} | {info}"
            return formatted_packet
        else:
            return None


    


