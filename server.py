import socket
import threading

HEADER=64
PORT=5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
  print(f"[SERVER] new connection by {addr}")

  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)
      if msg == DISCONNECT_MESSAGE:
        connected = False
      print(f"[{addr}] {msg}")
      conn.send("Msg Received".encode(FORMAT))
  conn.close()



def start():
  server.listen()
  while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr)) 
    thread.start()
    print(f"[SERVER] active connection, {threading.active_count() - 1}")

print(f"[SERVER] starting server on address {ADDR}")
start()