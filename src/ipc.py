import socket

LOCALHOST = 'localhost'

Connection = None

def send(data):
  Connection.sendall(data.encode())

def send_list(*data):
  send(','.join(list(map(str, data))))

def get():
  data = ''
  while (byte := Connection.recv(1)) != b'\n':
    data += byte.decode()
  return data

def get_list():
  data = get()
  return data.split(',')

def get_mapped_list(func):
  data = get_list()
  return list(map(func, data))

def start(port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((LOCALHOST, port))
  sock.listen(0)
  Connection, _ = sock.accept() 
