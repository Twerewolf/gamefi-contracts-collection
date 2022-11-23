# \n就换行
def delblankline(infile, outfile):
 infopen = open(infile, 'r',encoding="utf-8")
 outfopen = open(outfile, 'w',encoding="utf-8")
 db = infopen.read()
 x = db.replace("\\n",'\n')
 y = x.replace('\\r','')
 outfopen.write(y)
 infopen.close()
 outfopen.close()
 
delblankline("module.sol", "out2.txt")