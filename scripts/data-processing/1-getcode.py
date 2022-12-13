'''
to get the function below as curl does
curl https://bscscan.com/address/0xbe363cCa482e0e5e3865302cEab098D2e6BDCf51#code > code.txt&1 
'''
import os
import requests
from cleanAddresses import clean
clean("./dirtyAddresses.txt", "cleanAddr.txt")

infopen = open('./miss.txt', 'r', encoding="utf-8")
contractList = infopen.readlines()

for i in contractList:
    if (i[-1] == '\n'):
        contractAddr = i[:-1]
    else:
        contractAddr = i
    url = "https://bscscan.com/address/{contractAddress}#code".format(
        contractAddress=contractAddr)
    print("url: ", url)
    # if()
    if len(contractAddr) < 1:
        continue
    command = "curl " + url + " > " + " ./code/" + contractAddr + ".html"

    res = os.system(command)

print("all contract web data got!")
