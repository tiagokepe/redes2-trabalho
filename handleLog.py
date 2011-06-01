import sys
import time

LOGFILE = 'log'

class HandleLog:
    fileName = None
    logFile = None

    ## Abre arquivo de log para manipulacao ###################################
    def __init__(self):
#        self.fileName = 'log-'+host+'.txt'
        self.fileName = 'log-servers.txt'
        
    def newClient(self, host):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Cliente se conectou ao servidor: <",host,">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close()

    def sendResultClient(self, hostSource, hostDest, res):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Host <",hostSource,"> enviou o resultado ",res," para o client <",hostDest,">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close() 

    def receiveResultClient(self, hostSource, res):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Cliente recebeu o resultado ",res," do servidor <",hostSource,">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close() 

    def sendExprNext(self, hostSource, hostDest, expr):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Servidor <",hostSource,"> enviou expressao: ", expr," para o servidor <",hostDest, ">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close()

    def receiveExpr(self, hostSource, hostDest, res):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Servidor <",hostDest,"> recebeu expressao: ",res," do host <",hostSource,">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close()

    def sendResult(self, hostSource, hostDest, res):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Servidor <",hostSource,"> enviou o resultado ",res," para o host <",hostDest,">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close()

    def receiveResult(self, hostSource, hostDest, res):
        self.logFile = open(self.fileName, 'ab+')
        msg = [time.ctime()," - Servidor <",hostDest,"> recebeu o resultado ",res," do servidor <",hostSource,">\n"]
        self.logFile.write("".join(msg))
        self.logFile.close()

