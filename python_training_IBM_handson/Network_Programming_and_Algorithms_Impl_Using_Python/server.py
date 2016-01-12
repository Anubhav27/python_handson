import socket


s = socket.socket()

host = socket.gethostname()
print host
port = 4000

s.bind((host,port))

s.listen(5)
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection


