import socket
import renderer


class Server:

    def __init__(self):
        self.toread = None
        self.view = None
        self.socket = None
        self.conn = None
        self.address = None
        self.renderer = None
        self.back_socket = None
        self.sf = None
        self.lf = None

        self.connect_client()
        self.input_blend_file = open('data/proba.blend', 'wb')
        self.buffer = memoryview(bytearray(1024 * 1024 * 10))
        self.num_bytes = 1
        self.receive_file()
        self.render()
        self.socket.close()
        self.send_rendered_file_back()

    def receive_file(self):
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

            self.input_blend_file.write(self.buffer)

    def connect_client(self):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(('localhost', 9090))
        self.socket.listen(1)
        self.conn, self.address = self.socket.accept()

    def render(self):
        self.renderer = renderer.Renderer(input_file='data/proba.blend')
        self.renderer.render()

    def send_rendered_file_back(self):
        self.back_socket = socket.socket()
        self.back_socket.connect(('localhost', 9090))
        self.sf = self.back_socket.fileno()
        self.lf = open('data/image.png', 'rb')
        self.back_socket.sendfile(self.lf)


server = Server()
