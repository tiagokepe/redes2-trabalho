from socket import *

from sys import *

if len(argv) != 2:
    print "Uso correto: servidor <porta>"
    exit(1)

try:
    sock_descr = socket(AF_INET6, SOCK_STREAM)
except socket.error:
    print "Erro ao criar o socket"
    exit(1)

host = '127.0.0.1'
port = int(argv[1])
addr = (host,port)

print "Nome: "+str(sock_descr.getsockname())

#sock_descr.bind(addr)

sock_descr.close()

#print "Porta: " + porta

