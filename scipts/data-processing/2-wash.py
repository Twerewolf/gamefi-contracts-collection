'''
<div id="dividcode">
'''
import os
import requests
from cleanAddresses import clean
import pprint


def outbytecode(contractAddr, line):
    outfile = "{prefix}{Addr}.bytecode".format(
        prefix=prefix, Addr=contractAddr)
    outfopen = open(outfile, 'w', encoding="utf-8")
    # print("line: ",line)
    beginIdx = len("<pre class='wordwrap' style='height: 15pc;'>")
    end = "</pre>"
    endLen = len(end) + 1  # 回车符占用一个
    if (line[0:beginIdx] != "<pre class='wordwrap' style='height: 15pc;'>" and line[-endLen:] != "</pre>"):
        print("the bytecode line is not formatted as expected")
        return -1
    # print("bytecode: ",line[beginIdx:-endLen])
    outfopen.write(line[beginIdx:-endLen])
    outfopen.close()
    print("wash export {addr} bytecode finish".format(addr=contractAddr))
    return 0


if __name__ == '__main__':

    infopen = open('./cleanAddr.txt', 'r', encoding="utf-8")
    contractList = infopen.readlines()
    begin = "<div id=\"dividcode\">"
    end = "</pre>"
    prefix = "./code/"

    for contractAddr in contractList:
        print("-----------------------------------------------------------------------")
        found = False
        j = 0
        contractAddr = contractAddr[:-1]
        print("wash {addr} begin".format(addr=contractAddr))
        if (len(contractAddr) < 40):
            continue
        rawweb = prefix + contractAddr + '.html'
        f = open(rawweb, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        count = len(lines)
        if (count < 5):
            print("web code too short")
            continue

        outlines = []
        bytecodebegin = "<pre class='wordwrap' style='height: 15pc;'>"

        for i in range(count):
            if (lines[i].find(begin) != -1):
                print("found ", begin)
                j = i+1
                if (lines[j].find(bytecodebegin) != -1):
                    print("the contract is not verified, only has bytecode")

                    res = outbytecode(contractAddr=contractAddr, line=lines[j])
                    if (res == 0):
                        found = True
                    break
                break
        if (found):
            continue

        j = i+1
        # print("j is {j}".format(j=j))
        try:
            while (lines[j].find(end) == -1):
                outlines.append(lines[j])
                j += 1
                if (j == count-1):
                    break
        except IndexError:
            print(repr(IndexError))


        outfile = "{prefix}{Addr}.sol".format(prefix=prefix, Addr=contractAddr)
        outfopen = open(outfile, 'w', encoding="utf-8")
        print(len(outlines))
        outlines[0]
        beginStr = "/*"
        endStr = "}"
        outlines[0] = beginStr + outlines[0]
        outlines[-1] = outlines[-1] + endStr
        outfopen.writelines(outlines)

        outfopen.close()
        print("wash export {addr} contract finish".format(addr=contractAddr))
