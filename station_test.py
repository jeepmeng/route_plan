import requests

def get_station(addr):  # addr->地名
    parameters = {
        #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
        # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
        'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
        'location': addr,
        'types':'150700',
        'radius':'5000',
        'offset':'5'
        # 'city': '长春市'
        # 'destination': addr2,
    }  # 地址参数

    url = 'https://restapi.amap.com/v3/place/around?'
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    # print(result["pois"])
    for i in result["pois"]:
        print(i["name"])
        print(i["location"])
        # print(result["pois" ][i]["name"])
        # print(result["pois" ][i]["location" ])
    # try:
    #     result['regeocode'][0]['location']
    # except KeyError:
    #     print("location request error")
    #     return ""
    # else:
    #
    #     # print(result['geocodes'][0]['location'])
    #     return result['geocodes'][0]['location']



get_station('125.319229,43.926578')