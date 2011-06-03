# client.py por Antonio e Tiago
# Cliente TCP

from socket import *
from sys import *
from handleLog import *

BUFSIZ = 8192
FIM = 'quit'
######################### Abre socket para o cliente ##########################
def openClientSocket():
    ## Host remoto ##
    HOST = argv[1]
    ## Porta do Servidor ##
    PORT = int(argv[2])
    clientSocket = None
    ####### Aceita a primeira familia disponivel, IPv6 tem precedencia ########
    for result in getaddrinfo(HOST, PORT, AF_UNSPEC, SOCK_STREAM):
        af, socktype, proto, canonname, addrPort = result
        try:
            clientSocket = socket(af, socktype, proto)
        except error, msg:
            clientSocket = None
            continue
        try:
            clientSocket.connect(addrPort)
        except error, msg:
            clientSocket.close()
            clientSocket = None
            continue
        break

    if clientSocket is None:
        print 'Nao consegui abrir o socket do cliente'
        exit(1)
    
    return clientSocket
###############################################################################

## Instancia para manipular arquivo de log ##
hLog = HandleLog()

SERVER = argv[1]

############################# INICIO DO CLIENTE ###############################

######## Mosta uso correto do servidor ########
if len(argv) != 3:
    print "Uso correto: client <servidor> <porta>"
    exit(1)

while True:
    expr = raw_input("Digite a expressao ou quit para sair: ");
    if expr != FIM:
        clientSocket = openClientSocket()
        hLog.newClient(SERVER)
        clientSocket.send(str(expr))
        buff = clientSocket.recv(BUFSIZ)
        hLog.receiveResultClient(SERVER, buff)
        print 'Resultado da expresao: '+buff
    else:
        clientSocket.close()
        break
            
    clientSocket.close()


