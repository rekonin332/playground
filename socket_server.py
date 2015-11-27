import socket
import threading
import time
''''''

s = socket.socket()

s.bind(('127.0.0.1',9997))

s.listen(5)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()

    t = threading.Thread(target=tcplink,args=(sock, addr))
    t.start()


