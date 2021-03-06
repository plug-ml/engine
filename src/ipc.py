import socket

LOCALHOST = 'localhost'

Socket = None
Connection = None

def send(data):
  Connection.sendall(('%s\n' % data).encode())

def send_list(data):
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

def new(port):
  global Socket
  Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  Socket.bind((LOCALHOST, port))

def start():
  global Connection
  Socket.listen(0)
  Connection, _ = Socket.accept() 
