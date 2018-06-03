import socket
import time

end_flag = 'ENDFLAG'

s = socket.socket()
host = socket.gethostname()
port = 1234

try:
    s.bind((host, port))
except OSError as e:
    print('port is occupied.', e)
    exit(-1)
else:
    s.listen(5)

while True:
    c, addr = s.accept()
    c.settimeout(1)
    print('Got connection from ', addr)

    total_data = ''
    try:
        while True:
            data = c.recv(4).decode(encoding='utf-8')
            total_data += data
            if total_data.endswith(end_flag):
                break
    except socket.timeout as e:
        print(e)

    total_data = total_data[:len(total_data) - len(end_flag)]
    print('Received data: ', total_data)

    c.send('This is server'.encode(encoding='utf-8'))
    c.close()