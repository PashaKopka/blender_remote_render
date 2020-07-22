import os
import socket
socket = socket.socket()
socket.connect(('localhost', 9090))
sf = socket.fileno()
lf = os.open('proba.blend', os.O_RDONLY)

socket.sendfile(lf)
