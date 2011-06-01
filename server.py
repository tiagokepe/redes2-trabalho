# server.py por Anotnio e Tiago
# Servidor TCP Iterativo

from socket import *
from sys import *
from handleFile import *
from handleLog import *
import re
import time

## Constantes ##
QUEUE_SIZE = 5
BUFSIZ = 8192

################### Abre socket de escuta para o servidor #####################
def openListenSocket():
    ## Nome simbolico para todas as interfaces disponiveis ##
    HOST = None
    PORT = int(argv[1])
    serverSocket = None
    ####### Aceita a primeira familia disponivel, IPv6 tem precedencia ########
    for result in getaddrinfo(HOST, PORT, AF_UNSPEC, SOCK_STREAM, 0, AI_PASSIVE):

        af, socktype, proto, canonname, addrPort = result
        try:
            serverSocket = socket(af, socktype, proto)
        except error, msg:
            serverSocket = None
            continue
        try:
            serverSocket.bind(addrPort)
            serverSocket.listen(QUEUE_SIZE)
        except error, msg:
            serverSocket.close()
            serverSocket = None
            continue
        break

    if serverSocket is None:
        print 'Nao consegui abrir o socket de escuta'
        exit(1)

    return serverSocket
###############################################################################


############## Abrir socket para enviar ao proximo servidor ###################
def openSocketNext(nextHost):
    ## Nome simbolico para todas as interfaces disponiveis ##
    HOST = nextHost
    PORT = int(argv[1])
    sock = None

    for res in getaddrinfo(HOST, PORT, AF_UNSPEC, SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            sock = socket(af, socktype, proto)
        except error, msg:
            sock = None
            continue
        try:
            sock.connect(sa)
        except error, msg:
            sock.close()
            sock = None
            continue
        break
    if sock is None:
        print 'Nao consegui abrir o socket de atendimento'
        exit(1)
    
    return sock
###############################################################################



########################### Inicio do Servidor ################################

## Mosta uso correto do servidor ##
if len(argv) != 3:
    print "Uso correto: server <porta> <arquivo de servidores>"
    exit(1)

## Testa se tem suporte para IPv6 ##
if not has_ipv6:
    exit(1)

############ Variaveis para obter dados do arquivo de servidores ##############
hostName = gethostname()
hFile = HandleFile(argv[2])
myID = hFile.myServerId(hostName)
numServer = hFile.numberServers()
nxtServer = hFile.nextServer(hostName)
###############################################################################

######## Socket de escuta ########
serverSocket = openListenSocket()

## Instancia para manipular arquivo de log ##
hLog = HandleLog()

##################### Laco Principal ##########################################
while 1:
    (clientSocket, addrClient) = serverSocket.accept()
    print "End client: "+str(addrClient)
#    addrServer = clientSocket.getpeername()
    addrServer = clientSocket.getsockname()
    print "End Server: "+str(addrServer)

    print 'Inicio'
    buff = clientSocket.recv(BUFSIZ)
    ## Cliente se conectou a esse servidor ##
    if addrClient[0] == gethostbyname(hostName):
        hLog.newClient(hostName)
    else:
        hLog.receiveExpr(addrClient[0], hostName, buff)

    if not buff:
        print 'Buffer vazio'
        break

    ## Sou servidor N ##
    if myID == numServer:
        ## Calcula expessao ##
        buff = eval(buff)
        buff = str(buff)
    else:
        ## Passa para proximo servidor ##
        IPnext = gethostbyname(nxtServer)
        ## Abrindo socket com o proximo servidor ##
#        time.sleep(1)
        sendSocket = openSocketNext(nxtServer)
        addrNext = sendSocket.getpeername()
        hLog.sendExprNext(hostName, addrNext[0], buff)
        sendSocket.send(buff)
        buff = sendSocket.recv(BUFSIZ)
        hLog.receiveResult(addrNext[0], hostName, buff)

        sendSocket.close()

    if addrClient[0] != gethostbyname(hostName):
        hLog.sendResult(hostName, addrClient[0], buff)
    else:
        hLog.sendResultClient(hostName, addrClient[0], buff)

    clientSocket.send(buff)
###############################################################################

clientSocket.close()


