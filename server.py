import os
import socket
import renderer
import constants
import win32com.shell.shell as shell


class Server:

    def __init__(self):
        self.toread = None
        self.view = None
        self.server_socket = None
        self.conn = None
        self.address = None
        self.renderer = None
        self.back_socket = None
        self.sf = None
        self.lf = None
        self.data = None

        self.connect_client()
        self.input_blend_file = open('data/proba.blend', 'wb')
        self.buffer = memoryview(bytearray(1024 * 1024 * 10))
        self.num_bytes = 1
        self.receive_file()
        self.render()
        self.close_connection(self.server_socket)
        self.send_rendered_file_back()

    def receive_file(self):
        while True:
            self.data = self.client_socket.recv(1024)
            if not self.data:
                break
            self.input_blend_file.write(self.data)

    def connect_client(self):
        self.client_socket = socket.socket()
        self.client_socket.connect(('35.173.69.207', 8080))
        self.sf = self.client_socket.fileno()

    def render(self):
        self.renderer = renderer.Renderer(input_file='data/proba.blend')
        self.renderer.render()

    def send_rendered_file_back(self):
        self.back_socket = socket.socket()
        self.back_socket.connect(('35.173.69.207', 8080))
        self.sf = self.back_socket.fileno()
        self.lf = open('data/image.png', 'rb')
        self.back_socket.sendfile(self.lf)
        self.lf.close()
        self.close_connection(self.back_socket)
        self.remove_files()

    def close_connection(self, choosed_socket):
        choosed_socket.close()

    def remove_files(self):
        if constants.REMOVING_FILES == 0:
            return
        os.remove('data/proba.blend')
        os.remove('data/image.png')


while True:
    server = Server()
