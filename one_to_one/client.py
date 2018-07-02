#client code

from socket import *
s=socket(AF_INET,SOCK_STREAM)

host=gethostname()
port=5402

s.connect((host,port))
text=input('Enter the text')
while text!='q':
	s.send(text.encode('utf-8'))
	data=s.recv(1024)
	print('The data received is %s'%str(data.decode('utf-8')))
	text=input('Enter the text')
s.close()
	


