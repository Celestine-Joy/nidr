import pyshark
from PyQt5.QtCore import QThread, pyqtSignal




class PacketSnifferThread(QThread):
    packet_sniffed = pyqtSignal(str)
    incoming_count_changed = pyqtSignal(int)
    outgoing_count_changed = pyqtSignal(int)

    def __init__(self):
        super(PacketSnifferThread, self).__init__()
        self.incoming_count = 0
        self.outgoing_count = 0
        print("PacketSnifferThread started")

    def run(self):
        interface = 'eth0'
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously():
            formatted_packet = self.format_packet(packet)
            self.packet_sniffed.emit(formatted_packet)

    def format_packet(self, pkt):
        time = pkt.sniff_timestamp
        source = pkt.ip.src if 'IP' in pkt else ''
        destination = pkt.ip.dst if 'IP' in pkt else ''
        
        if hasattr(pkt, 'transport_layer'):
            protocol = pkt.transport_layer
        elif hasattr(pkt, 'network_layer'):
            protocol = pkt.network_layer
        else:
            protocol = ''

        length = len(pkt)

        if source == '10.0.2.15':
            self.increment_outgoing()
        else:
            self.increment_incoming()

        formatted_packet = f"{time} | {source} | {destination} | {protocol} | {length}"
        return formatted_packet

    def increment_incoming(self):
        self.incoming_count += 1
        self.incoming_count_changed.emit(self.incoming_count)
    def increment_outgoing(self):
        self.outgoing_count += 1
        self.outgoing_count_changed.emit(self.outgoing_count)
        
