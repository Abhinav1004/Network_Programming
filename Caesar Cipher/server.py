#Server Caesar Cipher Code
import string
from socket import *
host=gethostname()
port=5401
s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(2)
c,a=s.accept()

def rotate(l,n):
        return l[n:]+l[:n]

def decrypt(ciph,key):
        s=string.ascii_lowercase
        c=list(ciph)
        dn=rotate(s,-key)
        decr=[]
        for i in c:
                if i in s:
                        ind=s.index(i)
                        decr.append(dn[ind])
                else:
                        decr.append(' ')
        decr=''.join(decr)
        return decr

while True:
	print('Receiving the text')	
	data=c.recv(1024)
	print('Receiving the key')
	key=int(c.recv(1024))	
	if not data:
		break
	print('The encrypted data is %s'%str(data))
	decn=decrypt(data,key)	
	c.send(decn)
c.close()
