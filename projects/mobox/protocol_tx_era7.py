# get all tx in one project(protocol)
# P.S. can set the contract_address and wallet_address
import requests
import json
import pprint
# 空格：%20
s = 'era7-game-of-truth'
signInAddr = '0xc7EDdc2eB5362A791E4A78EDF6f3caC0bA59F8dE'
contractAddr = '0xd67016118b086b4830f25e137b72d55790cb1869'
walletAddr = '0x23Ffb1DA16604cFC0373feEdBFa5Fe60B928D5c7' # 自己钱包地址
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
print("PROJECT:",s)
pprint.pprint(data)
# all_records = data['data']
# for i in all_records:
#     print(i)