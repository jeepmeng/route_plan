import requests
import utils
import pandas as pd
import json



def get_station(addr):  # addr->地名
    kk = []
    parameters = {
        #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
        # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
        'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
        'location': addr,
        'types':'150700',
        'radius':'800',
        'offset':'3'
        # 'city': '长春市'
        # 'destination': addr2,
    }  # 地址参数

    url = 'https://restapi.amap.com/v3/place/around?'
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    # print(result["pois"])

    for i in result["pois"]:

        kk.append(i["location"])
    return kk


def load_json():

    with open('./school_location.json','r') as f:
            content = f.read()
            content = json.loads(content)
    return content

def load_csv(path, index=False, condition=False):
    df = pd.read_csv(path)
    return df

if __name__ == '__main__':
    # a = load_json()
    # for _, key in a.items():
    #     print(key)
    #     print(key['location'])



    station = []
    path = '/Users/liufucong/Downloads/route_plan/test/长盛小学公交信息采集.csv'
    df = load_csv(path)
    # print(df['loc'].tolist())
    for i in df['loc']:
        print(get_station(i))
        # print(type(get_station(i)))
        station.append(get_station(i))
    print(station)
    df['station'] = station
    df.to_pickle('./test/长盛小学公交信息采集_station.pickle')


