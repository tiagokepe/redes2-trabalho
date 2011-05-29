from handleFile import *

h = HandleFile('myServers.txt')

p = h.nextServer('mumm')

print p

h.file.seek(0)
line = h.file.readline()

print line
