#Client Caesar Cipher Code
import string
from socket import *
s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=5401
s.connect((host,port))

def rotate(l,n):
        return l[n:]+l[:n]

text=raw_input("Enter the plain text")
key=int(raw_input("Enter the value of key"))#should be an integer between 0-26

def encrypt(text,key):
        s=string.ascii_lowercase
        s=list(s)
        en=rotate(s,key)
        t=list(text)
        ciph=[]

        for i in t:
                if i in s:
                        ind=s.index(i)
                        ciph.append(en[ind])
                else:
                        ciph.append(' ')

        ciph=''.join(ciph)
        return ciph
while True:
	print('Sending the encrypted text\n')	
	s.send(encrypt(text,key))
	print('Sending the key')
	s.send(str(key))
	print('Receiving the decrypted text')
	data=s.recv(1024)
	print('The decrypted text is %s'%(str(data)))
	choice=raw_input('Do you want to enter again(y/n)')
	if choice=='n':
		break
	else:
		text=raw_input('Enter the plain text')
		key=int(raw_input('Enter the value of the key'))


s.close()

	

