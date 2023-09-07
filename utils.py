import numpy as np
import pandas as pd
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# def loc_name_loci(name_list,loc_list):
#     pass

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
    return result


def get_loc(addr):  # addr->地名
    parameters = {
        #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
        # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
        'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
        'address': '长春市' + addr,
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


class cluster():
    def __init__(self,destination,path,radius=10000):
        self.center_co = coor_convert(get_loc(destination))
        self.destination = destination
        # self.path = path
        self.radius = radius
        self.df = pd.read_csv(path)

        # self.list_co_convert = []
        self.x_normal,self.y_normal = float(self.center_co['locations'].split(',')[0]),float(self.center_co['locations'].split(',')[-1])
        self.list_co_convert = []
        self.co_convert()
    # @staticmethod
    def cluster(self,n_clusters,id='长春市'):

        cluster = KMeans(n_clusters=n_clusters, random_state=0).fit(self.list_co_convert)
        y_pred = cluster.label_

        for i in list_0:
            list_3.append(str(i[0]) + ',' + str(i[-1]))




        return

    def co_convert(self):

        self.df = self.df[self.df['dis'] <= self.radius]

        for i in self.df['loc'].tolist():
            self.list_co_convert.append(self.normalize(coor_convert(i)['locations']))


    # @staticmethod
    def normalize(self,loc):
        x_y_norm = float(loc.split(',')[0]) - self.x_normal, float(loc.split(',')[1]) - self.y_normal
        return x_y_norm



def load_csv(path, index=False, condition=False):
    df = pd.read_csv(path)
    if condition:
        df = df[df[index]==condition]
        return df
    elif index:
        return df[index]
    else:
        return df


def dict_csv(dict,path):
# mydict = {'key1': 'a', 'key2': 'b', 'key3': 'c'}
#     path = '/Users/liufucong/Desktop/环线公交/47中学公交信息采集.xlsx'
    file_name = (os.path.split(path)[-1]).split('.')[0]+'.csv'
    cwd = os.getcwd()
    save_path = os.path.join(cwd,file_name)
    (pd.DataFrame.from_dict(data=dict, orient='index').to_csv(save_path, header=False))
    print('{}------- already saveed at --------{}'.format(file_name,save_path))


if __name__ == '__main__':
    # path = '/Users/liufucong/Desktop/环线公交/47中学公交信息采集.xlsx'
    # dict_csv(path)
    # ll = (os.path.split(path)[-1]).split('.')[0]
    # print(ll)
    # cwd = os.getcwd()
    # print(cwd)
    # path.split('.')[0]
    # path.split('/')

    print(matplotlib.matplotlib_fname())
