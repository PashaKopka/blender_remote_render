import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import socket


class Client(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.choose_button = QPushButton('Choose file', self)
        self.send_button = QPushButton('Send', self)
        self.send_button.move(100, 0)

    def connect_server(self):
        self.client_socket = socket.socket()
        self.client_socket.connect(('localhost', 9090))

    def send_file_server(self):
        self.connect_server()
        self.sf = self.client_socket.fileno()
        self.lf = open(self.infile_name, 'rb')

        self.client_socket.sendfile(self.lf)

        self.close_connection()

    def close_connection(self):
        self.client_socket.close()

    def choose_file(self):
        self.infile_name = QFileDialog.getOpenFileName(self, 'Open file', '')[0]


app = QApplication(sys.argv)
demo = Client()

demo.choose_button.clicked.connect(demo.choose_file)
demo.send_button.clicked.connect(demo.send_file_server)

demo.show()

sys.exit(app.exec_())
