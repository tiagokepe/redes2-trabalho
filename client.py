from socket import *
from sys import *

# Set the socket parameters
hostName = gethostname()
port = int(argv[1])
addr = ('::1', port)
#addr = (gethostbyname(hostName),port)

buf = 8192

nome=raw_input('introduza nome:\t')
# Create socket
sock = socket(AF_INET6, SOCK_STREAM, 0)

def_msg = "===introduza o texto===";
print "\n",def_msg

# Send messages
while (1):
    data = raw_input(nome+'>> ')
    if not data:
        break
    else:
        data=nome+' diz:\t'+data
	data=data+'Host=\t'+hostName
        sock.sendto(data, (hostName, port))

# Close socket
sock.close()

