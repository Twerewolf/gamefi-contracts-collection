# get all tx in one project(protocol)
# P.S. can set the contract_address and wallet_address
import requests
import json
import pprint
# 空格：%20
s = 'mobox'
contractAddr = '0x3203c9E46cA618C8C1cE5dC67e7e9D75f5da2377'
walletAddr = ''
url = "https://api.footprint.network/api/v2/protocol/transactions?chain=BNB%20Chain&protocol_slug={slug}&contract_address={contract_address}".format(  # &wallet_address={wallet_address}
    slug=s, contract_address=contractAddr)
# , wallet_address=walletAddr
headers = {
    "accept": "application/json",
    "API-KEY": "8IGN2Qtu01++R5xnomtFFmCBUFrgXfnDMKuhmn4n+ng2HQHkNL40cXAvSDKti9T7"
}

response = requests.get(url, headers=headers)

# print(response.text)
data = json.loads(response.text)
pprint.pprint(data)
# all_records = data['data']
# for i in all_records:
#     print(i)