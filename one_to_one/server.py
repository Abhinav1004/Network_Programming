#server code

from socket import *
s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=5402
s.bind((host,port))
s.listen(5)

c,a=s.accept()
data=c.recv(1024)
while True:
	if not data:
		break
	print('The received data is %s'%str(data.decode('utf-8')))
	data=str(data.decode('utf-8')).upper()
	c.send(data.encode('utf-8'))
	data=c.recv(1024)
c.close()

