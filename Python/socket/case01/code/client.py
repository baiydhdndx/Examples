import socket

end_flag = 'ENDFLAG'

s = socket.socket()
host = socket.gethostname()
port = 1234
s.settimeout(1)

try:
    s.connect((host, port))
except ConnectionRefusedError as e:
    print('port is closed. ', e)
    exit(-1)
except socket.timeout as e:
    print('host is unreached. ', e)
    exit(-2)

s.send('Hello, this is client.'.encode(encoding='utf-8'))
s.send(end_flag.encode(encoding='utf-8'))

total_data = ''
while True:
    data = s.recv(1024).decode(encoding='utf-8')
    if not data:
        break
    total_data += data

print('Received data: ', total_data)
