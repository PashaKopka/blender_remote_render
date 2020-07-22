import socket
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import os
import socket


class Client(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

    def send_file_server(self):
        self.socket = socket.socket()
        self.socket.connect(('localhost', 9090))

        self.sf = self.socket.fileno()
        self.lf = open('proba.blend', 'rb')

        self.socket.sendfile(self.lf)


app = QApplication(sys.argv)
demo = Client()
demo.send_file_server()
demo.show()

sys.exit(app.exec_())
