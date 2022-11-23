'''
to get the function below as curl does
curl https://bscscan.com/address/0xbe363cCa482e0e5e3865302cEab098D2e6BDCf51#code > code.txt&1 
'''
import os
import requests
# x = []
# x.append( "0xbe363cCa482e0e5e3865302cEab098D2e6BDCf51" )
x = "0x4eeDeDfe89dad70aB8cbf70E4dD140Ff8E6e8ce5"
url = "https://bscscan.com/address/{contractAddress}#code".format(
    contractAddress=x)
print("url: {url}".format(url=url))
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
command = "curl " + url

os.system(command)
# print(response.text)
# str_content = response.text.encode('utf-8')
f = open('./response-{contractAddress}.html'.format(contractAddress=x), 'w')
f.write(response.text)
f.close()
