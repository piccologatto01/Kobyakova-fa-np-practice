import socket
import threading

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''
def router():
	data = conn.recv(1024)
	msg += data.decode()
	conn.send(data)
	if not data:
		conn.close()

while True:
	t = threading.Thread(router)
	t.start()
	

print(msg)

conn.close()
