import socket
from blender_remoote_render import renderer


class Server:

    def __init__(self):
        self.connect_client()
        self.input_blend_file = open('data/proba.blend', 'wb')
        self.buffer = memoryview(bytearray(1024 * 1024 * 10))
        self.num_bytes = 1
        self.receive_file()
        self.render()

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
        self.conn, self.addr = self.socket.accept()

    def render(self):
        self.renderer = renderer.Renderer(input_file='data/proba.blend')
        self.renderer.render()


server = Server()
