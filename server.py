# server.py por Anotnio e Tiago
# Servidor TCP Iterativo

from socket import *
from sys import *
from handleFile import *
import re
import time

QUEUE_SIZE = 5
BUFSIZ = 8192

if len(argv) != 3:
    print "Uso correto: server <porta> <arquivo de servidores>"
    exit(1)

## Testa se tem suporte para IPv6 ##
if not has_ipv6:
    exit(1)

## Nome simbolico para todas as interfaces disponiveis ##
HOST = None
PORT = int(argv[1])
serverSocket = None

######### Aceita a primeira familia disponivel, IPv6 tem precedencia ##########
for result in getaddrinfo(HOST, PORT, AF_UNSPEC, SOCK_STREAM, 0, AI_PASSIVE):

    af, socktype, proto, canonname, addrPort = result
    try:
        serverSocket = socket(af, socktype, proto)
    except error, msg:
        serverSocket = None
        continue
    try:
        serverSocket.bind(addrPort)
        serverSocket.listen(1) #QUEUE_SIZE)
    except error, msg:
        serverSocket.close()
        serverSocket = None
        continue
    break

if serverSocket is None:
    print 'Nao consegui abrir o socket'
    exit(1)
###############################################################################


############ Variaveis para obter dados do arquivo de servidores ##############
hostName = gethostname()
hFile = HandleFile(argv[2])
myID = hFile.myServerId(hostName)
numServer = hFile.numberServers()
nxtServer = hFile.nextServer(hostName)
addrNext = (nxtServer, int(argv[1]))
###############################################################################

print 'proximo:'

print addrNext

#print '\n\n'

############### Socket para enviar msg ao proximo servidor ####################
########## Aceita primeira familia disponivel, IPv6 tem precedencia ###########
if myID != numServer:
#    sendSocket = socket(AF_INET6, SOCK_STREAM)
    for result in getaddrinfo(nxtServer, PORT, AF_UNSPEC, SOCK_STREAM, 0, AI_PASSIVE):
        af, socktype, proto, canonname, addrPort = result
        try:
            sendSocket = socket(af, socktype, proto)
            print '>>>>>>'
            print sendSocket.getsockname()
            print addrNext
            #print serverSocket.getsockname()
            print '<<<<<<'
        except error, msg:
            print 'Nao consegui abrir o socket'
            exit(1)
###############################################################################


##################### Laco Principal ##########################################
while 1:
    (clientSocket, address) = serverSocket.accept()
    print '@@@@@'
    print clientSocket.getsockname()
    print '@@@@@'
    buff = clientSocket.recv(BUFSIZ)
    if not buff:
        print 'Buffer vazio'
        break

    ## Sou servidor N ##
    if myID == numServer:
        ## Calcula expessao ##
        buff = eval(buff)
        buff = str(buff)
#        print result
 #       clientSocket.send(result)
    else:
        print "ELSE"
        ## Passa para proximo servidor ##
        IPnext = gethostbyname(nxtServer)
        sendSocket.connect(addrNext)
        print '%%%%%%%%%%%%%%%%'
        print sendSocket.getpeername()
        print '%%%%%%%%%%%%%%%%'
        data = buff
        sendSocket.send(data)
        print 'Enviei para {0} >>>> {1}'.format(nxtServer,data)
        data = sendSocket.recv(BUFSIZ)
        buff = data
        print 'Recebi da {0} >>>>> {1}'.format(nxtServer,data)
        if address[0] == gethostbyname(hostName):
            print "IF"
        else:
            print "aki"

    clientSocket.send(buff)
    
##    clientSocket.close()


#        sendSocket.close()

###############################################################################

clientSocket.close()


