'''
to get the function below as curl does
curl https://bscscan.com/address/0xbe363cCa482e0e5e3865302cEab098D2e6BDCf51#code > code.txt&1 
'''
import os
import requests
from cleanAddresses import clean
# x = []
# x.append( "0xbe363cCa482e0e5e3865302cEab098D2e6BDCf51" )
clean("./contractAddresses.txt", "cleanAddr.txt")
infopen = open('./cleanAddr.txt', 'r', encoding="utf-8")
contractList = infopen.readlines()

for i in contractList:
    # contractAddr = "0x4eeDeDfe89dad70aB8cbf70E4dD140Ff8E6e8ce5"
    # contractList.append(contractAddr)
    contractAddr = i[:-1]
    url = "https://bscscan.com/address/{contractAddress}#code".format(
        contractAddress=contractAddr)
    print("url: {url}".format(url=url))
    # if()
    if len(contractAddr)<1 :
        continue
    command = "curl " + url + " > " + contractAddr + ".html"

    res = os.system(command)
    # print("os system res: ", res)
# ?start=1&limit=50&sort=market_cap&cryptocurrency_type=all&tag=all
# payload={}
# parameters = {
#   'start':'1',
#   'limit':'50',
#   # 'sort':'market_cap',
#   'cryptocurrency_type':'all',
#   'tag':'all'
# }
# headers = {
#   'X-CMC_PRO_API_KEY': '3192c5fa-2b0f-49a8-9f8c-2ca57de6c442',
#   'Accept': 'application/json'
# }

# response = requests.request("GET", url)


# str_content = response.text.encode('utf-8')
# f = open('./response-{contractAddress}.html'.format(contractAddress=x), 'w')
# f.write(response.text)
# f.close()
