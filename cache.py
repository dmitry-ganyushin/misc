import socket

domainMap={}
domainList=[]
maxCacheSize=3
def getItem(domainname):
    if domainname in domainMap:
        ipaddr = domainMap[domainname]
    else:
        domainList.append(domainname)
        ipaddr = socket.gethostbyname(domainname)
        domainMap[domainname] = ipaddr
        if(len(domainList) > maxCacheSize):
            name = domainList.pop(0)
            domainMap.pop(name)    
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




