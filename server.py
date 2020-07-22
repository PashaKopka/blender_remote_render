import socket

socket = socket.socket()

socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket.bind(('localhost', 9090))
socket.listen(1)
conn, addr = socket.accept()

pp = open('data/proba.blend', 'wb')

buf = memoryview(bytearray(1024 * 1024 * 10))
nbytes = 1

while nbytes:
    toread = 1024 * 1024 * 10
    view = buf[:]
    while toread:
        nbytes = conn.recv_into(view, toread)
        view = view[nbytes:]
        toread -= nbytes
        if nbytes == 0:
            buf = buf[:-toread]
            break

    pp.write(buf)
    print('.', end='')
