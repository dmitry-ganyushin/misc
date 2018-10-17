import socket
from collections import OrderedDict

domainMap=OrderedDict()
maxCacheSize=3
def getItem(domainname):
    if domainname in domainMap:
        ipaddr = domainMap[domainname]
    else:
        ipaddr = socket.gethostbyname(domainname)
        domainMap[domainname] = ipaddr
        if(len(domainMap) > maxCacheSize):
            k=list(domainMap.keys())
            domainMap.pop(k[0])    
    return ipaddr

def printCache():
    print("#################Cache############################")
    for k,v in domainMap.items():
        print (k + "->" + v)
    print("##################################################")

##test

print(getItem("gmail.com"))
printCache()
print(getItem("mail.com"))
printCache()
print(getItem("gmx.de"))
printCache()
print(getItem("gmx.net"))
printCache()
print(getItem("gmx.net"))
printCache()
print(getItem("gmx.net"))
printCache()




