import commands
import sys

#FILE_SERVERS = 'myServers.txt'

class HandleFile:

    file = None

    ## Abre arquivo para manipulacao ##########################################
    def __init__(self, FILE_SERVERS):
        self.file = open(FILE_SERVERS, 'rb+')
    ###########################################################################


    ## Retorna o ID do servidor, se host nao consta na lista aborta ###########
    def myServerId(self, host):
        self.file.seek(0)
        for line in self.file:
            if (line.find(host)) != -1:
                list = line.partition(' ')
                return int(list.__getitem__(0))
        print "Host nao consta na lista"
        sys.exit(1)
    ###########################################################################

 
    ## Retorna o numero de servidores #########################################
    def numberServers(self):
        self.file.seek(0)
        try:
            num = self.file.readline()
            return int(num.rstrip('\n'))
        except error, msg:
            print 'Erro ao obter numero de servidores'
            sys.exit(1)
    ###########################################################################


    ## Retorna o proximo servidor ou retorna 0 se eh servidor N ###############
    def nextServer(self, host):
        self.file.seek(0)
        line = self.file.readline()
        ## Enquanto nao chegou no final do arquivo ############################
        while line != '':
            list = line.partition(' ')
            ## Tira \n ##
            h = list.__getitem__(2).rstrip('\n')
            ## Chegou no host, pega o proximo ##
            if h == host:
                line = self.file.readline()
                ## Se chegou no final do arquivo, nao tem proximo, servidor N #
                if line == '':
                    return 0
                try:
                    list = line.partition(' ')
                    return list.__getitem__(2).rstrip('\n')
                except error, msg:
                    print 'Erro ao obter proximo servidor'
                    sys.exit(1)

            line = self.file.readline()
    ###########################################################################
            
                    
               
