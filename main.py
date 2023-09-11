from flask import Flask, request
import requests
import pandas as pd
import itertools
from load_gt_data import load_gt
# from utils import dict_csv
import os
from utils import *

class lxgh:
    def __init__(self):
        pass


    #获取坐标
    @staticmethod
    def get_loc(addr):#addr->地名
        parameters = {
            #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
            # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
            'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
            'address': '长春市'+addr,
            # 'city':'长春市'
            # 'destination': addr2,
        }  # 地址参数

        url = 'https://restapi.amap.com/v3/geocode/geo?'
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        try:
            result['geocodes'][0]['location']
        except KeyError:
            print("location request error")
            return "125.298724,43.942621"
        else:


        # print(result['geocodes'][0]['location'])
            return result['geocodes'][0]['location']

    #获取距离
    @staticmethod
    def place_distance(addr_id,des_name = '长春市宽城区柳影路1602号'):#addr->起点（地名），des_name->终点
        addr = lxgh.get_loc(addr_id)
        des = lxgh.get_loc(des_name)

        parameters = {
#             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
#              'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
            'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
                      'origin': addr,
                      'destination': des,
                      }  # 地址参数
        # url = 'https://restapi.amap.com/v3/direction/walking?'  # 高德地图地理编码API服务地址
        # print(parameters)
        url = 'https://restapi.amap.com/v5/direction/driving?'
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        # print(result)
        # print(result)
        try:
            lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
        except KeyError:
            print("route request error")

            return "125.298724,43.942621","0"
        else:
        # print("walking规划",result)
        # print(lon_lat)
            return addr,lon_lat

    #返回[{地名：位置坐标}, ...]
    @staticmethod
    def loc_name_loci(addr_list):
        loc_id = []
        location = []
        distance = []
        for i in addr_list:
            try:
                loc,dis = lxgh.place_distance(i)
            except KeyError:
                print("No parameters return!!!")
                continue
            else:
                loc_id.append(i)
                location.append(loc)
                distance.append(dis)
                print('id:{}, location:{}, distance:{}'.format(i,loc,dis))
        # loc = lambda x: {'id':loc_id.append(i for i in x), 'loc':location.append(lxgh.get_loc(i) for i in x),'dis':[]}
        all_loc = {'id':loc_id,'loc':location,'dis':distance}
        return all_loc

    @staticmethod
    def coor_convert(loc):
        parameters = {
            #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
            # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
            'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
            'locations': loc,
            'coordsys': 'mapbar'
            # 'destination': addr2,
        }  # 地址参数

        url = 'https://restapi.amap.com/v3/assistant/coordinate/convert?'
        result = requests.get(url, parameters)  # GET方式请求
        result = result.json()
        # try:
        #     result['geocodes'][0]['location']
        # except KeyError:
        #     print("location request error")
        #     return ""
        # else:
        #
        #     # print(result['geocodes'][0]['location'])
        #     return result['geocodes'][0]['location']

        return result



    @staticmethod
    def dict_csv(dict, path):
        # mydict = {'key1': 'a', 'key2': 'b', 'key3': 'c'}
        #     path = '/Users/liufucong/Desktop/环线公交/47中学公交信息采集.xlsx'
        file_name = (os.path.split(path)[-1]).split('.')[0] + '.csv'
        cwd = os.getcwd()
        save_path = os.path.join(cwd, file_name)
        # pd.DataFrame.from_dict(data=dict, orient='index',columns=['geo']).to_csv(save_path, header=False)
        # kk = pd.DataFrame.from_dict(dict, orient='index',columns=['geo','dis'])
        kk = pd.DataFrame.from_dict(dict)
        print(kk)
        kk.to_csv(save_path, header=True)
        print('{}------- already saveed at --------{}'.format(file_name, save_path))



if __name__ == '__main__':
    path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'
    # loc_name = load_gt(path)
    # print(loc_name[:10])
    # ff = lxgh.loc_name_loci(loc_name)
    # print(ff)
    # lxgh.dict_csv(ff,path)
    test = clu(3,'长春市宽城区柳影路1602号',path)