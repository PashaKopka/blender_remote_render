import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import socket


class FileReceiver(QWidget):

    def __init__(self):
        super().__init__()
        self.infile_name = None
        self.lf = None
        self.sf = None
        self.client_socket = None
        self.back_socket = None
        self.buffer = None
        self.view = None
        self.num_bytes = None
        self.toread = None
        self.pp = None
        self.address = None
        self.conn = None

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

        self.close_connection(self.client_socket)
        self.receive_rendered_file_back()

    def close_connection(self, choosed_socket):
        choosed_socket.close()

    def choose_file(self):
        self.infile_name = QFileDialog.getOpenFileName(self, 'Open file', '')[0]

    def receive_rendered_file_back(self):
        self.back_socket = socket.socket()
        self.back_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.back_socket.bind(('localhost', 9090))
        self.back_socket.listen(1)
        self.conn, self.address = self.back_socket.accept()

        self.pp = open('image.png', 'wb')
        self.buffer = memoryview(bytearray(1024 * 1024 * 10))
        self.num_bytes = 1

        while self.num_bytes:
            self.toread = 1024 * 1024 * 10
            self.view = self.buffer[:]
            while self.toread:
                self.num_bytes = self.conn.recv_into(self.view, self.toread)
                self.view = self.view[self.num_bytes:]
                self.toread -= self.num_bytes
                if self.num_bytes == 0:
                    self.buffer = self.buffer[:-self.toread]
                    break

            self.pp.write(self.buffer)
        self.pp.close()

        self.close_connection(self.back_socket)


app = QApplication(sys.argv)
demo = FileReceiver()

demo.choose_button.clicked.connect(demo.choose_file)
demo.send_button.clicked.connect(demo.send_file_server)

demo.show()

sys.exit(app.exec_())
