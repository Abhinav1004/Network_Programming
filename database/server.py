#server code
import sqlite3
from socket import *

s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=5305
s.bind((host,port))
s.listen(2)
c,a=s.accept()

conn=sqlite3.connect('test.db')
cur=conn.cursor()

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

def print_table():
        cur.execute("SELECT * FROM COMPANY")
        data=cur.fetchall()

        for row in data:
                print row
					
while True:
	data=c.recv(1024)
	if not data:
		break
	cur.execute(data)
	conn.commit
	print_table()
c.close()

conn.close()
