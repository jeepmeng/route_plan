import json

import numpy as np
import pandas as pd
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import load_gt_data as l_d


def place_distance(addr_id,des_loc='',des_name=''):#addr->起点（地名），des_name->终点
    addr = get_loc(addr_id)
    if des_loc:
        des = des_loc
    else:
        des = get_loc(des_name)

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

def loc_name_loci(addr_list,des):
    loc_id = []
    location = []
    distance = []
    for i in addr_list:
        try:
            loc, dis = place_distance(i,des)
        except KeyError:
            print("No parameters return!!!")
            continue
        else:
            loc_id.append(i)
            location.append(loc)
            distance.append(dis)
            print('id:{}, location:{}, distance:{}'.format(i, loc, dis))
    # loc = lambda x: {'id':loc_id.append(i for i in x), 'loc':location.append(lxgh.get_loc(i) for i in x),'dis':[]}
    all_loc = {'id': loc_id, 'loc': location, 'dis': distance}
    return all_loc


#路径分解
def path_refactor(path,second=False):#path="csv数据路径"，second="选择分类或拆分"
    #example
    #path = '/Users/liufucong/Desktop/环线公交 副本/长盛小学公交信息采集.xls'
    tail_text = (os.path.split(path)[1]).split('.')[0]
    exit_folder = os.path.join(os.getcwd(),tail_text)

    if not os.path.exists(exit_folder):
        os.mkdir(exit_folder)
        print('New folder.........(   {}   ).......has made!'.format(exit_folder))
    if second:
        tail_text = tail_text+'_拆分后.csv'
        return tail_text, os.path.join(exit_folder,tail_text)
    else:
        tail_text = tail_text+'_分类后.csv'
        return tail_text, os.path.join(exit_folder,tail_text)


#高德坐标转换，转mapbar
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

#获取位置坐标
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
        # return "125.298724,43.942621"
    else:

        # print(result['geocodes'][0]['location'])
        return result['geocodes'][0]['location']

#聚类
class clu():
    def __init__(self,destination,path,n_cluster=3,radius=10000):
        self.destination = destination
        # self.center_co = coor_convert(get_loc(destination))
        self.center_co = coor_convert(self.destination)

        self.path = path
        self.radius = radius
        # self.df = load_gt(path)
        # dict_csv()
        self.df = pd.read_csv(self.path)

        # self.list_co_convert = []
        self.x_normal,self.y_normal = float(self.center_co['locations'].split(',')[0]),float(self.center_co['locations'].split(',')[-1])
        self.list_co_convert = []
        self.co_convert()
        self.convert_str = []
        self.save_path_cluster = ''
        self.cluster(n_cluster)
        # self.final_split()

    #聚类
    # @staticmethod
    def cluster(self,n_clusters):
        cluster = KMeans(n_clusters=n_clusters, random_state=0).fit(self.list_co_convert)
        y_pred = cluster.label_

        for i in self.list_co_convert:
            self.convert_str.append(str(i[0]) + ',' + str(i[-1]))
        self.df['mapbar'], self.df['centroid'], self.df['normalize'] = [self.list_co_convert,
                                                                        y_pred,
                                                                        self.list_co_convert]
        save_name_cluster, self.save_path_cluster = path_refactor(self.path)
        dict_csv(self.df, save_name_cluster, self.save_path_cluster)
    #csv数据分列
    def final_split(self):
        df = pd.read_csv(self.save_path_cluster)
        # print(df.loc)

        df_id = df.id.to_frame()
        # print(df_id)

        df_id['loc_x'], df_id['loc_y'], df_id['dis'], df_id['mapbar_x'] \
            , df_id['mapbar_y'], df_id['centroid'], df_id['normalize_x'], df_id['normalize_y'] = [
            df['loc'].apply(lambda x: x.split(',')[0]),
            df['loc'].apply(lambda x: x.split(',')[-1]),
            df['dis'],
            df['mapbar'].apply(lambda x: x.split(',')[0]),
            df['mapbar'].apply(lambda x: x.split(',')[-1]),
            df['centroid'],
            df['normalize'].apply(lambda x: x.split(',')[0]),
            df['normalize'].apply(lambda x: x.split(',')[-1])]
        save_name_split,save_path_split = path_refactor(self.path,True)
        dict_csv(df_id, save_name_split, save_path_split)

    def co_convert(self):

        self.df = self.df[self.df['dis'] <= self.radius]

        for i in self.df['loc'].tolist():
            self.list_co_convert.append(self.normalize(coor_convert(i)['locations']))

    # @staticmethod
    def normalize(self,loc):
        x_y_norm = float(loc.split(',')[0]) - self.x_normal, float(loc.split(',')[1]) - self.y_normal
        return x_y_norm


#读取csv
def load_csv(path, index=False, condition=False):
    df = pd.read_csv(path)
    if condition:
        df = df[df[index]==condition]
        return df
    elif index:
        return df[index]
    else:
        return df

#保存csv文件
class dict_csv():

    def __init__(self,path,des):
        self.path = path
        self.des = des
        self.tail_text = (os.path.split(self.path)[1]).split('.')[0]
        self.file_name = (os.path.split(path)[-1]).split('.')[0] + '.csv'
        self.exist_folder = os.path.join(os.getcwd(),'data')


        if not os.path.exists(self.exist_folder):
            os.mkdir(self.exist_folder)
            print('New folder.........(   {}   ).......has made!'.format(self.exist_folder))


        self.exist_file = os.path.join(self.exist_folder, self.tail_text)
        # print(self.exist_file)
        self.save_path = os.path.join(self.exist_file,self.file_name)


        if not os.path.exists(self.exist_file):
            os.mkdir(self.exist_file)
            print('New folder.........(   {}   ).......has made!'.format(self.exist_file))
        else:
            print('Folder........ {} .........already exist!'.format(self.exist_file))
        self.save_dict()
        # if not os.path.exists(self.save_path):
        #     self.save_dict()
        # else:
        #     pass

    def save_dict(self):
        data = l_d.load_gt(self.path)
        ff = loc_name_loci(data,self.des)
        # kk = pd.DataFrame.from_dict(dict)
        pd.DataFrame.from_dict(data=ff).to_csv(os.path.join(self.save_path), header=True)
        print('{}------- already saved at --------{}'.format(self.file_name, self.path))



if __name__ == '__main__':

    path = '/Users/liufucong/Desktop/环线公交 副本'
    i = '柳影中学公交信息采集.xlsx'
    # with open('./school_location.json','r') as f:
    #     content = f.read()
    #     content = json.loads(content)
    #
    # for i in content.items():
    #     xlsx = i[0]
    #     des = i[-1]['location']
    #     claster_test = clu(destination=des,path = os.path.join(path,i[0]))
    #     dict_csv()

    # for
    dict_csv(os.path.join(path, i))
    # print(test.save_path)



    # i = '柳影中学公交信息采集.xlsx'
    # print(os.path.join(path, i))
    # df = pd.read_csv(os.path.join(path, i))
    # print(df)
    # claster_test = clu(destination="125.307175,43.937016", path=os.path.join(path, i))



