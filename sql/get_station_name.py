import pandas as pd
import json
# from station_test import *
import requests


def get_station_name(addr):  # addr->地名
    kk = []
    parameters = {
        #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
        # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
        'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
        'location': addr,
        'types':'150700',
        'radius':'300',
        'offset':'1'
        # 'city': '长春市'
        # 'destination': addr2,
    }  # 地址参数

    url = 'https://restapi.amap.com/v3/place/around?'
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    print(result["pois"])

    # for i in result["pois"]:
    #     print(i["name"])
    #     # print(i["location"])
    #     kk.append({i["name"]:i["location"]})
    return result["pois"][0]["name"],result["pois"][0]["location"]


ll = []
with open('./station_5_35.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

for i in content:
    name,loc = get_station_name(i)
    ll.append({name:loc})

print(ll)

hh = json.dumps(ll, indent=3, ensure_ascii=False)
with open('st_name_sq_35.json', 'w') as f:
    f.write(hh)