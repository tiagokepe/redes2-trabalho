from socket import *

from sys import *

if len(argv) != 2:
    print "Uso correto: servidor <porta>"
    exit(1)

if not has_ipv6:
    exit(1)

try:
    serversocket = socket(AF_INET6, SOCK_STREAM, 0)
except socket.error:
    print "Erro ao criar o socket"
    exit(1)

hostName = gethostname()
port = int(argv[1])
addr = ("localhost", port) #(gethostbyname(hostName),port)

print "Name: "+hostName

try:
    serversocket.bind(addr)
except:
    print "Nao consegui fazer o bind"
    exit(1)

serversocket.listen(5)
buff = 8192

while 1:
    (clientsocket, address) = serversocket.accept()
    (buff, addrClient) = recvfrom(8192)
    print "Dado <<<<"+buff

    if hostName == 'mumm':
	hostName='Meu nome = \t'+hostName	
	serversocket.sendto(hostName, ('macalan', 9999))

    print 'Aki = \t'+hostName


serversocket.close()
