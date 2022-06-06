import socket

# Нужно создать сокет, подключиться к серверу послать ему данные, принять данные и закрыть соединение.
# Метод connect, с помощью которого мы подключаемся к серверу.
# Дальше мы читаем 1024 байт данных и закрываем сокет.

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print(data)