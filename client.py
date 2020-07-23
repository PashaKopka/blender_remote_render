import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import socket


class Client(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

    def send_file_server(self):
        self.connect_server()
        self.sf = self.socket.fileno()
        self.lf = open('proba.blend', 'rb')

        self.socket.sendfile(self.lf)

    def connect_server(self):
        self.socket = socket.socket()
        self.socket.connect(('localhost', 9090))

    def close_connection(self):
        self.socket.close()


app = QApplication(sys.argv)
demo = Client()
demo.send_file_server()
demo.close_connection()
demo.show()

sys.exit(app.exec_())
