
def clean(infile, outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")
    dirty = infopen.readlines()
    cleanLines = []
    for line in dirty:
        lowIdx = 0
        while lowIdx != -1:
            lowIdx = line.find("0x",lowIdx)
            # print(line[lowIdx:lowIdx+42])
            if(lowIdx!=-1):
                print("lowIdx:",lowIdx, line[lowIdx:lowIdx+42])
                cleanLines.append(line[lowIdx:lowIdx+42]+'\n')
                lowIdx += 42
    
    outfopen.writelines(cleanLines)
    infopen.close()
    outfopen.close()

if __name__ == '__main__':

    clean("./dirtyAddresses.txt", "cleanAddr.txt")
