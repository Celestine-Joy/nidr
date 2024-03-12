# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt

from interface.login_screen import LoginScreen
from interface.screen1 import Screen1

interface='interface/'
asset='assets/'
files='files/'
class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setWindowTitle('My App')
        self.resize(800, 600)

        self.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b;
                color: #b3b3b3;
            }
            QPushButton {
                background-color: #333;
                border: 1px solid #555;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton:pressed {
                background-color: #888;
            }
        """)

        self.stack_widget = QStackedWidget(self)
        self.login_screen = LoginScreen(self)
        self.screen1 = Screen1(self)

        self.logo_label = QLabel(self)
        pixmap = QPixmap(asset+'LOGO.png')
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.logo_label)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        logo_widget = QWidget()
        logo_widget.setLayout(layout)

        self.stack_widget.addWidget(logo_widget)
        self.stack_widget.addWidget(self.login_screen)
        self.stack_widget.addWidget(self.screen1)

        self.setCentralWidget(self.stack_widget)
        self.show()

        QTimer.singleShot(10000, self.finish_loading)  # Display the logo for 5 seconds

    def finish_loading(self):
        self.stack_widget.setCurrentIndex(1)  # Switch to the login screen
    

    def switch_to_screen1(self):
        # Switch to the screen1 widget
        self.stack_widget.setCurrentWidget(self.screen1)

if __name__ == '__main__':
    with open(files+'found_ips.csv', 'w') as file:
        file.write('')  # set the file content to empty
    file.close()
    app = QApplication([])
    ex = MyApp()
    app.exec_()