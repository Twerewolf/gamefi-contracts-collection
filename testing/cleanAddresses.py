
def clean(infile, outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")
    dirty = infopen.readlines()
    cleanLines = []
    for line in dirty:
        lowIdx = line.find("0x")
        if lowIdx != -1:
            # print(line[lowIdx:lowIdx+42])
            cleanLines.append(line[lowIdx:lowIdx+42]+'\n')
    
    outfopen.writelines(cleanLines)
    infopen.close()
    outfopen.close()

