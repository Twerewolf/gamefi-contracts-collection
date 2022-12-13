from sys import argv

def clean(infile, outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")
    dirty = infopen.readlines()
    cleanLines = []
    for line in dirty:
        if line=='\n':
            continue
        else:
            cleanLines.append(line)
    
    outfopen.writelines(cleanLines)
    infopen.close()
    outfopen.close()

if __name__ == '__main__':

    clean("dirty_protocol_slugs.txt", "clean_protocol_slugs.txt")
