# server.py por Anotnio e Tiago
# Servidor TCP Iterativo

from socket import *
from sys import *
from handleFile import *

QUEUE_SIZE = 5
BUFSIZ = 8192

def calcExpr(expr):
    return expr+'@@@@@'

if len(argv) != 3:
    print "Uso correto: server <porta> <arquivo de servidores>"
    exit(1)

# Testa se tem suporte para IPv6
if not has_ipv6:
    exit(1)

# Nome simbolico para todas as interfaces disponiveis
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
        serverSocket.listen(QUEUE_SIZE)
    except error, msg:
        serverSocket.close()
        serverSocket = None
        continue
    break

if serverSocket is None:
    print 'Nao consegui abrir o socket'
    sys.exit(1)
###############################################################################


############ Variaveis para obter dados do arquivo de servidores ##############
hostName = gethostname()
hFile = HandleFile(argv[2])
myID = hFile.myServerId(hostName)
numServer = hFile.numberServers()
proximo = 'p'
###############################################################################


##################### Laco Principal ##########################################
(connectSocket, address) = serverSocket.accept()
print address
while 1:
    buff = connectSocket.recv(BUFSIZ)
    if not buff: 
        print 'Buffer vazio'
        break

    ## Sou servidor N ##
    if myID == numServer:
        buff = calcExpr(buff)    
        connectSocket.send(buff)
    else:
        print "ELSE"
        if address[0] == gethostbyname(hostName):
            print "IF"
        print "aki"


connectSocket.close()


