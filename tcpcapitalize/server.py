#server code
from socket import *
s=socket(AF_INET,SOCK_STREAM)

host="127.0.0.1"
port=5011
s.bind((host,port))
s.listen(2)
c,a=s.accept()
while True:
	data=c.recv(1024)
	if not data:
		break
	print('Data received is \n%s'%str(data.decode('utf-8')))
	data=str(data.decode('utf-8')).upper()
	c.send(data.encode('utf-8'))
c.close()

