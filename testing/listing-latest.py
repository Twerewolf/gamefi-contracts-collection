import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
# ?start=1&limit=50&sort=market_cap&cryptocurrency_type=all&tag=all
payload={}
parameters = {
  'start':'1',
  'limit':'50',
  # 'sort':'market_cap',
  'cryptocurrency_type':'all',
  'tag':'all'
}
headers = {
  'X-CMC_PRO_API_KEY': '3192c5fa-2b0f-49a8-9f8c-2ca57de6c442',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload,params=parameters)

# print(response.text)
# str_content = response.text.encode('utf-8')
f = open('./response.json','w')
f.write(response.text)
f.close()