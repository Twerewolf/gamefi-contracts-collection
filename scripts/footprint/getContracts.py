import requests
import json


def getContracts(slug):
    url = "https://api.footprint.network/api/v1/protocol/{slug}/contract".format(
        slug=slug)
    print("url: ", url)
    headers = {
        "accept": "application/json",
        "API-KEY": "8IGN2Qtu01++R5xnomtFFmCBUFrgXfnDMKuhmn4n+ng2HQHkNL40cXAvSDKti9T7"
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    # print(data['data'][0])
    all = data['data']
    # d0 = data['data'][0]
    # print(d0['chain'])
    size = len(all)
    print("contract number: ", size)

    return all


if __name__ == '__main__':
    slug = "mobox"
    getContracts(slug=slug)
