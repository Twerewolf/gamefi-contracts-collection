'''
to get the function below as curl does
curl https://api.bscscan.com/api?module=account&action=txlist&address=0x76975bD7c484FcaCD9507fEB67A1394701d4335C&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=VUD9T6GQGXRGSJNMUMAAYVBJGY55DVHRUF > accountTxs.json&1

'''
import os
import requests


def getContracts(address, page, apikey):
    url = "https://api.bscscan.com/api?module=account&action=txlist&address={addr}&startblock=0&endblock=99999999&page={page}&offset=10&sort=asc&apikey={apikey}".format(
        addr=address,
        page=page,
        apikey=apikey)
    # print("url: {url}".format(url=url))
    command = "curl " + url + " > " + " ./code/" + address + ".html"
    print(command)
    res = os.system(command)

    print("all contract data got!")


if __name__ == '__main__':
    address = "0x76975bD7c484FcaCD9507fEB67A1394701d4335C"
    page = 1
    apikey = "VUD9T6GQGXRGSJNMUMAAYVBJGY55DVHRUF"
    getContracts(address, page, apikey)
