from main import *


def get_loc_2(addr):  # addr->地名
    parameters = {
        #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
        # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
        'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
        'location': addr,
        # 'city': '长春市'
        # 'destination': addr2,
    }  # 地址参数

    url = 'https://restapi.amap.com/v3/geocode/regeo?'
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    print(result)
    try:
        result['regeocode'][0]['location']
    except KeyError:
        print("location request error")
        return ""
    else:

        # print(result['geocodes'][0]['location'])
        return result['geocodes'][0]['location']


path_1 = '柳影实验学校'
path_2 = '豪邦四季经典'

liuying = lxgh.get_loc('长春市宽城区柳影路1602号')
print(liuying)

# p1 = lxgh.get_loc(path_2)
p2 = lxgh.place_distance(path_2,'长春市宽城区柳影路1602号')
print(p2)


p3 = get_loc_2(p2[0])
p4 = get_loc_2(liuying)