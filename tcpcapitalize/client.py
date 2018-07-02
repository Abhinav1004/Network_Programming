#client code
from socket import *
s=socket(AF_INET,SOCK_STREAM)

host="127.0.0.1"
port=5011
s.connect((host,port))
text=input('Enter the text you want to capitalize\n')
while text!='q':
	s.send(text.encode('utf-8'))
	data=s.recv(1024)
	print('The data recieved is %s'%(str(data.decode('utf-8'))))
	text=input('Enter the text you want to capitalize\n')

s.close()
