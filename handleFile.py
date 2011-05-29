import commands
import sys

FILE_SERVERS = 'myServers.txt'

class HandleFile:

    file = None

    def __init__(self, FILE_SERVERS):
        self.file = open(FILE_SERVERS, 'rb+')

    def myServerId(self, host):
        self.file.seek(0)
        for line in self.file:
            if (line.find(host)) != -1:
                list = line.partition(' ')
                return int(list.__getitem__(0))
        print "Host nao consta na lista"
        sys.exit(1)
 
    def numberServers(self):
        self.file.seek(0)
        for line in self.file:
            if line != '':
                lastLine = line
        try:
            list = lastLine.partition(' ')
            return int(list.__getitem__(0))
        except error, msg:
            print 'Erro ao obter numero de servidores'
            sys.exit(1)

    def nextServer(self, host):
        self.file.seek(0)
        for line in self.file:
            if line == '':
                return 0
            else:
                print 'ELSE'
                list = line.partition(' ')
                print 'N = '+list.__getitem__(1)
                if list.__getitem__(1) == host:
                    line = self.file.readline()
                    if line == '':
                        return 0
                    list = line.partition(' ')
                    return list.__getitem__(1)
                    
               
