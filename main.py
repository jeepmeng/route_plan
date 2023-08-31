from flask import Flask, request
import requests
import pandas as pd
import itertools
from load_gt_data import load_gt


class lxgh:
    def __init__(self):
        pass

    @staticmethod
    def get_loc(addr1):
        parameters = {
            #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
            'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
            'address': addr1,
            # 'destination': addr2,
        }  # 地址参数

        url = 'https://restapi.amap.com/v3/geocode/geo?'
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        # print(result['geocodes'][0]['location'])
        return result['geocodes'][0]['location']
    @staticmethod
    def place_distance(addr,des_name = '长春市宽城柳影实验学校'):
        des = lxgh.get_loc(des_name)
        """
        :param addr1:起始点
        :param addr2: 终止点
        :return: 两点距离
        """
        parameters = {
#             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
             'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
                      'origin': addr,
                      'destination': des,
                      }  # 地址参数
        # url = 'https://restapi.amap.com/v3/direction/walking?'  # 高德地图地理编码API服务地址
        url = 'https://restapi.amap.com/v5/direction/driving?'
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        # print(result)
        lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
        # print("walking规划",result)
        # print(lon_lat)
        return lon_lat

    @staticmethod
    def loc_name_loci(addr_list):
        loc = lambda x: [{i:lxgh.get_loc(i)} for i in x]
        all_loc = loc(addr_list)
        return all_loc
if __name__ == '__main__':
    path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'
    loc_name = load_gt(path)
    print(loc_name[:10])
    ff = lxgh.loc_name_loci(loc_name[:10])
    print(ff)
    # df = pd.read_excel(io=path)
    # print(type(df['Unnamed: 3'][2:]))
    # t = df['Unnamed: 3'][2:].values.tolist()
    # print(len(t))
    # new_t = list(set(t))
    # print(len(new_t))
    # pd.set_option('display.notebook_repr_html', False)
    # addr1 = '长春市北凯旋路与桐雨街交汇'
    # addr = lxgh.get_loc(addr1)
    # addr2 = '长春市宽城柳影实验学校'
    # lxgh.get_loc(addr2)
    # addr = ['长春市北凯旋路与桐雨街交汇','长春市宽城柳影实验学校']
    # loc = lambda x:[lxgh.get_loc(i) for i in x]
    # print(loc(addr))


    # x_y = lxgh.place_distance(addr)
    # print(x_y)