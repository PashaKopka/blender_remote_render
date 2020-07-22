import socket

server_socket = socket.socket()

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('localhost', 9090))
server_socket.listen(1)
conn, addr = server_socket.accept()

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
