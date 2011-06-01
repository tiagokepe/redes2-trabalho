from handleLog import *

hLog = HandleLog()
hLog.newClient('mumm')

hLog.sendNext('priorat', 'macalan', '4+5')

hLog.receiveResult('macalan', 'priorat', '9')

