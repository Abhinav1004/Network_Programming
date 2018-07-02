
#client code
import sqlite3
from socket import *
s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=5305

s.connect((host,port))
message=raw_input('Enter the command')

conn=sqlite3.connect('test.db')
cur=conn.cursor()

def print_table():
	cur.execute("SELECT * FROM COMPANY")
	data=cur.fetchall()
	for row in data:
		print row

while True:
	s.send(message)
	print_table()
	choice=raw_input('Do you want to enter again(y/n)')
	if choice=='n':
		break
	else:
		message=raw_input('Enter the command')
s.close()

