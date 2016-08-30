from socket import *

server_port = 12000
server_socket = socket(AF_INET,SOCK_STREAM)

server_socket.bind(('',server_port))
server_socket.listen(1)     # server begins listening 

print '##### Server is ready to receive messages #####'
conn_socket, addr = server_socket.accept() # accept requests; new connection created to return
sentence = conn_socket.recv(1024)
cap_sentence = sentence.upper()
print 'message converted: ', cap_sentence
conn_socket.send(cap_sentence)
conn_socket.close()