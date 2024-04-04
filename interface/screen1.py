import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import QTimer


from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, pyqtSignal
from interface.packet_sniffer import PacketSnifferThread
from interface.run import run
import threading
import os
from backend.ipblock import block
from backend.ipunblk import unblock

files='files/'
assets='assets/'
backend='backend/'
interface='interface/'


class Center1(QWidget):
    incoming_count_changed = pyqtSignal(int)
    outgoing_count_changed = pyqtSignal(int)

    def __init__(self , top_bar, parent=None):
        super(Center1, self).__init__(parent)
        self.top_bar = top_bar 

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(['Time', 'Source', 'Destination', 'Protocol', 'Length'])
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.sniffer_thread = None

    def start_sniffer(self):
        self.sniffer_thread = PacketSnifferThread()
        self.sniffer_thread.packet_sniffed.connect(self.update_display)
        self.sniffer_thread.incoming_count_changed.connect(self.incoming_count_changed.emit)
        self.sniffer_thread.outgoing_count_changed.connect(self.outgoing_count_changed.emit)
        self.sniffer_thread.start()
        self.incoming_count_changed.connect(self.top_bar.update_incoming)
        self.outgoing_count_changed.connect(self.top_bar.update_outgoing)


    def update_display(self, packet):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Split the formatted packet into columns
        packet_data = packet.split(' | ')

        for col, data in enumerate(packet_data):
            item = QTableWidgetItem(data.strip())
            # Adjust the width of each column
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_position, col, item)

        # Set dark color for the text of the entire row based on the 'Protocol' value
        protocol_color = self.get_protocol_color(packet_data[3].strip())
        for col in range(self.table.columnCount()):
            item = self.table.item(row_position, col)
            item.setForeground(protocol_color)

        # Auto-scroll the table
        self.table.scrollToBottom()

    def get_protocol_color(self, protocol):
        # Assign specific dark colors for different protocols
        if protocol.lower() == 'tcp':
            return QColor(128, 0, 0)  # Dark Red
        elif protocol.lower() == 'udp':
            return QColor(0, 0, 128)  # Dark Blue
        elif protocol.lower() == 'icmp':
            return QColor(128, 0, 128)  # Dark Violet
        else:
            return QColor(0, 0, 0)  # Black


class TopBar(QWidget):
    def __init__(self, parent=None):
        super(TopBar, self).__init__(parent)

        self.logo_label = QLabel()
        pixmap = QPixmap(assets+"logo1.png") 
        scaled_pixmap = pixmap.scaled(120, 65, Qt.KeepAspectRatio)  # Scale the logo
        self.logo_label.setPixmap(scaled_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)



        self.incoming_label = QLabel("Incoming packets: 0")
        self.outgoing_label = QLabel("Outgoing packets: 0")

        self.layout = QHBoxLayout()


        self.layout.addWidget(self.incoming_label)

        self.layout.addWidget(self.logo_label)

        self.layout.addWidget(self.outgoing_label)
        self.setLayout(self.layout)

        # Apply dark theme stylesheet
        self.setStyleSheet("""
            background-color: #333;
            color: #fff;
            padding: 10px;
        """)





    def update_incoming(self, count):
        self.incoming_label.setText(f"Incoming packets: {count}")

    def update_outgoing(self, count):
        self.outgoing_label.setText(f"Outgoing packets: {count}")


class LeftBar(QWidget):
    def __init__(self, center, bottom_bar , parent=None):
        super(LeftBar, self).__init__(parent)
        self.center = center   
        self.bottom_bar = bottom_bar
        self.label1 = QLabel()
        self.label1.setPixmap(QPixmap("status_icon.png"))
        self.label1.setAlignment(Qt.AlignCenter)

        button_style = """
    QPushButton {
        color: #fff;
        background-color: #333;
        border: none;
        font-size: 16px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #444;
    }
    QPushButton:pressed {
        background-color: #532;
    }
"""
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(0, 100, 0, 0)

        self.start_button = QPushButton(QIcon("start_icon.png"), "Start")
        self.start_button.setStyleSheet(button_style)
        self.start_button.clicked.connect(self.start_clicked)
        sidebar_layout.addWidget(self.start_button)

        self.calculate_button = QPushButton(QIcon("calculationlog.png"), "Calculation log")
        self.calculate_button.setStyleSheet(button_style)
        self.calculate_button.clicked.connect(self.calculationlog_clicked)
        sidebar_layout.addWidget(self.calculate_button)

        self.attack_button = QPushButton(QIcon("Attacklog.png"), "Attack log")
        self.attack_button.setStyleSheet(button_style)
        self.attack_button.clicked.connect(self.attacklog_clicked)
        sidebar_layout.addWidget(self.attack_button)




        self.remove_button = QPushButton(QIcon("remove.png"), "Remove")
        self.remove_button.setStyleSheet(button_style)
        self.remove_button.clicked.connect(self.remove_clicked)
        sidebar_layout.addWidget(self.remove_button)









        sidebar_layout.addStretch(1)

        self.setLayout(sidebar_layout)





        # Apply dark theme stylesheet
        self.setStyleSheet("""
            background-color: #333;
            color: #fff;
            padding: 10px;
        """)


    def start_clicked(self):
        self.bottom_bar.start_network_capturing()  # Call the new method
        subprocess.Popen(["python", interface+"packet_sniffer.py"])
        threading.Thread(target=run).start()
        self.center.start_sniffer()




    def calculationlog_clicked(self):
        threading.Thread(target=self.open_gnumeric).start()

    def open_gnumeric(self):
        subprocess.Popen(['gnumeric', files+'output.csv'])

    def attacklog_clicked(self):
        threading.Thread(target=self.open_gnumeric2).start()

    def open_gnumeric2(self):
        subprocess.Popen(['gnumeric',files+'found_ips.csv'])

    def remove_clicked(self):
        file_path=files+'attack_source.csv'
        threading.Thread(target=unblock).start()
        if os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.truncate(0)





class BottomBar(QWidget):
    def __init__(self, parent=None):
        super(BottomBar, self).__init__(parent)

        bottom_bar_layout = QHBoxLayout()

        self.label1 = QLabel()
        self.label1.setText("Network Capturing Off")
        self.label1.setAlignment(Qt.AlignCenter)
        self.set_label_color("red")  # Initial color

        self.label2 = QLabel()
        self.label2.setPixmap(QPixmap("flag_icon.png"))
        self.label2.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel()
        self.label3.setPixmap(QPixmap("button_icon.png"))
        self.label3.setAlignment(Qt.AlignCenter)

        bottom_bar_layout.addWidget(self.label1)
        bottom_bar_layout.addWidget(self.label2)
        bottom_bar_layout.addWidget(self.label3)

        self.setLayout(bottom_bar_layout)

        # Apply dark theme stylesheet
        self.setStyleSheet("""
            background-color: #333;
            color: #fff;
            padding: 10px;
        """)

    def set_label_color(self, color):
        self.label1.setStyleSheet(f"background-color: {color};")

    def start_network_capturing(self):
        print("Capturing started")
        self.label1.setText("Network Capturing On")
        self.set_label_color("green")


    def normal_traffic(self):
        self.label2.setText("Normal traffic")
        self.label2.setStyleSheet("background-color: green;")
    def attack_traffic(self):
        self.label2.setText("Attack traffic")
        self.label2.setStyleSheet("background-color: red;")
    def network_filtering_on(self):

        self.label3.setText("Network filtering on")
        self.label3.setStyleSheet("background-color: green;")
    def network_filtering_off(self):
        self.label3.setText("Network filtering off")
        self.label3.setStyleSheet("background-color: blue;")







class Screen1(QWidget):
    def __init__(self, parent=None):
        super(Screen1, self).__init__(parent)

        self.setGeometry(100, 100, 800, 600)

        # Create main layout
        main_layout = QHBoxLayout()

        # Create instances of TopBar, Center1, and BottomBar
        top_bar = TopBar()
        center = Center1(top_bar)  # Pass top_bar to Center1
        self.bottom_bar = BottomBar()

        # Add left sidebar to main layout
        left_sidebar = LeftBar(center, self.bottom_bar)  # Pass center and bottom_bar to LeftBar
        main_layout.addWidget(left_sidebar)

        # Create right layout
        right_layout = QVBoxLayout()

        # Add top bar, center part, and bottom bar to right layout
        right_layout.addWidget(top_bar)
        right_layout.addWidget(center)
        right_layout.addWidget(self.bottom_bar)

        # Add right layout to main layout
        main_layout.addLayout(right_layout)

        # Set the main layout on the window
        self.setLayout(main_layout)

        # Apply dark theme stylesheet
        self.setStyleSheet("""
            background-color: #222;
            color: #fff;
        """)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_files)
        self.timer.start(10000)  # Check every 10 seconds


        self.show()

    def check_files(self):  # New method

            if not os.path.isfile(files+'attack_source.csv') or os.stat(files+'attack_source.csv').st_size == 0:
                self.bottom_bar.network_filtering_off()
            else:
                self.bottom_bar.network_filtering_on()
                threading.Thread(target=block).start()
                

            if not os.path.isfile(files+'found_ips.csv') or os.stat(files+'found_ips.csv').st_size == 0:
                self.bottom_bar.normal_traffic()
            else:
                self.bottom_bar.attack_traffic()