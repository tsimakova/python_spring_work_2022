import socket
import base64

# Нужно создать сокет, подключиться к серверу послать ему данные, принять данные и закрыть соединение.
# Метод connect, с помощью которого мы подключаемся к серверу.
# Дальше мы читаем 1024 байт данных и закрываем сокет.

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'Hi')

data = sock.recv(1024)

decodeit = open('/encode.jpg', 'wb')
decodeit.write(base64.b64decode((data)))
decodeit.close()

sock.close()
