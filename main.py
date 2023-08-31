from flask import Flask, request
import requests
import pandas as pd
import itertools


class lxgh:
    def __init__(self):
        pass


    @staticmethod
    def place_distance(addr1, addr2):
        """
        :param addr1:起始点
        :param addr2: 终止点
        :return: 两点距离
        """
        parameters = {
#             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
             'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
                      'origin': addr1,
                      'destination': addr2,
                      }  # 地址参数
        url = 'https://restapi.amap.com/v3/direction/walking?'  # 高德地图地理编码API服务地址
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
        # print("walking规划",result)
        # print(lon_lat)
        return lon_lat


if __name__ == '__main__':
    path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'
    df = pd.read_excel(io=path)
    print(type(df['Unnamed: 3'][2:]))
    t = df['Unnamed: 3'][2:].values.tolist()
    print(len(t))
    new_t = list(set(t))
    print(len(new_t))
    # pd.set_option('display.notebook_repr_html', False)