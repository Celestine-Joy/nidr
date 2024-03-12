from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal

assets='assets/'

class LoginScreen(QWidget):
     # Define a new signal
    def __init__(self, app):
        super(LoginScreen, self).__init__()
        self.app = app
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins around the layout
        layout.setAlignment(Qt.AlignCenter)
        

        # Create the logo and login form inside a QGroupBox
        group_box = QGroupBox()

        group_box.setMaximumWidth(400) 
        group_layout = QVBoxLayout(group_box)

        group_layout.setAlignment(Qt.AlignCenter)

        # Add logo to the group layout
        logo_label = QLabel()
        pixmap = QPixmap(assets+"logo1.png")  # Replace with your logo path
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(120, 65, Qt.KeepAspectRatio)  # Scale the logo
            logo_label.setPixmap(scaled_pixmap)
            logo_label.setAlignment(Qt.AlignCenter)
        else:
            QMessageBox.warning(self, "Warning", "Failed to load logo image!")
        group_layout.addWidget(logo_label)

        # Set the stylesheet
        group_box.setStyleSheet(self.get_stylesheet())

        

        # Add the rest of the widgets to the group layout
        self.username_edit = QLineEdit()
        self.username_edit.setPlaceholderText("Username")
        self.username_edit.setFont(QFont("Roboto", 12))  # Change font
        group_layout.addWidget(self.username_edit)

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setPlaceholderText("Password")
        self.password_edit.setFont(QFont("Roboto", 12))  # Change font
        group_layout.addWidget(self.password_edit)

        login_button = QPushButton("Login")
        login_button.setFont(QFont("Roboto", 14))  # Change font
        login_button.clicked.connect(self.validate_credentials)
        group_layout.addWidget(login_button)

        forgot_password_link = QLabel("<a href='#'>Forgot Password?</a>")  # Add forgot password link
        forgot_password_link.setOpenExternalLinks(True)
        forgot_password_link.setTextInteractionFlags(Qt.TextBrowserInteraction)
        forgot_password_link.setStyleSheet("font-size: 12px; color: #2271b1;")  # Make link clickable
        group_layout.addWidget(forgot_password_link)


        layout.addWidget(group_box)

       

    def validate_credentials(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        if username == "admin" and password == "password":
             # Emit the signal when login is successful
            self.app.switch_to_screen1()
        else:
            QMessageBox.warning(self, "Error", "Invalid Username or Password")

    def get_stylesheet(self):
        stylesheet = """
    QGroupBox {
        border: 2px solid gray;
        border-radius: 5px;
        margin: 0; /* Remove margins */
        padding: 10px; /* Add padding for a bit of space */
    }

    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px 0 3px;
    }
    """
        return stylesheet