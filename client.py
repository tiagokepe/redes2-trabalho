# client.py por Antonio e Tiago
# Cliente TCP

from socket import *
from sys import *

BUFSIZ = 8192

if len(argv) != 3:
    print "Uso correto: client <servidor> <porta>"
    exit(1)

# Host remoto
HOST = argv[1]
# Porta do Servidor
PORT = int(argv[2])
clientSocket = None

for result in getaddrinfo(HOST, PORT, AF_UNSPEC, SOCK_STREAM):
    af, socktype, proto, canonname, addrPort = result
    try:
        clientSocket = socket(af, socktype, proto)
    except error, msg:
        clientSocket = None
        continue
    try:
        clientSocket.connect(addrPort)
        print '>>>>>'
        print addrPort
        print '<<<<<'
    except error, msg:
        clientSocket.close()
        clientSocket = None
        continue
    break

if clientSocket is None:
    print 'Nao consegui abrir o socket'
    exit(1)

msg = "Digite a expressao:";
print "\n",msg

while (1):
#    clientSocket.send('Servidor Inicial')
    expr = raw_input('client>>>')
    clientSocket.send(str(expr))
    buff = clientSocket.recv(BUFSIZ)
    print 'Recebido do servidor: '+buff

clientSocket.close()


