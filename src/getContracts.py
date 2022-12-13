import requests
import json
import pathlib

def getContracts(slug, apiKey):
    url = "https://api.footprint.network/api/v1/protocol/{slug}/contract".format(
        slug=slug)
    print("url: ", url)
    headers = {
        "accept": "application/json",
        "API-KEY": apiKey
    }
    # print(headers["API-KEY"])
    # print("API-KEY: " ,apiKey)
 
    path = pathlib.Path('./log/{slug}.json'.format(slug=slug))
    if path.is_file() :
        result = ''
        with open('./log/{slug}.json'.format(slug=slug)) as fr:
            result = json.load(fr)
        # 如果已经存在并且成功获取过，则跳过
        if result["message"]=="success":
            return "already found"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    f = open('./log/{slug}.json'.format(slug=slug),'w',encoding='utf-8')
    json.dump(data,f) # 写入
    f.close()
    # print(data['data'][0])
    empty = []
    try:
        all = data['data']
    

        # d0 = data['data'][0]
        # print(d0['chain'])
        size = len(all)
        print("contract number: ", size)
        return all
    except:
        print(Exception)
        return empty
    
    return all


if __name__ == '__main__':
    slug = "mobox"
    getContracts(slug=slug)
