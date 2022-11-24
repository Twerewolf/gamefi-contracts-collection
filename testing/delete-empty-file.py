# -*- coding: UTF8 -*-
import os

infopen = open('./cleanAddr.txt', 'r', encoding="utf-8")

contractList = infopen.readlines()


def get_FileSize(filePath):
    # filePath = unicode(filePath, 'utf-8')

    if(not os.path.exists(filePath)):
        return 0
    fsize = os.path.getsize(filePath)
    print(fsize)
    # fsize = fsize/float(1024*1024)
    return fsize


for contractAddr in contractList:
    print("-----------------------------------------------------------------------")
    contractAddr = contractAddr[:-1]
    if (len(contractAddr) < 40):
        continue
    Sol = contractAddr + '.sol'
    Bin = contractAddr + '.bytecode'
    x = get_FileSize(Sol)
    y = get_FileSize(Bin)
    if x == 0:
        os.system("rm " + contractAddr +".sol")
    if y == 0:
        os.system("rm " + contractAddr +".bytecode")
        