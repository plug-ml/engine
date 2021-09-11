import socket

LOCALHOST = 'localhost'

Connection = None

def send(data):
  Connection.sendall(data.encode())

def get():
  data = ''
  while (byte := Connection.recv(1)) != b'\n':
    data += byte.decode()
  return data

def start(port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((LOCALHOST, port))
  sock.listen(0)
  Connection, _ = sock.accept() 
