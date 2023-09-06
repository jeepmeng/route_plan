from main import *
import numpy as np


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


path_2 = './柳影实验学校公交信息采集.csv'

def fun_1(path):
    list = []
    df = pd.read_csv(path)
    # print(df['geo'].tolist())
    df = df[df['dis'] < 9000]
    for i in df['loc'].tolist():

        list.append(lxgh.coor_convert(i)['locations'])
    # print(list)
    return np.array(list),df


center = lxgh.get_loc('长春市宽城区柳影路1602号')

center = lxgh.coor_convert(center)
print(center['locations'])
x_normal = float(center['locations'].split(',')[0])
y_normal = float(center['locations'].split(',')[-1])


list_1,df = fun_1(path_2)
print(list_1)
list_0 = []


for i in list_1:
    list_0.append([float(i.split(',')[0])-x_normal,float(i.split(',')[1])-y_normal])

print(list_0)


n_clusters= 3
cluster = KMeans(n_clusters=n_clusters,random_state=0).fit(list_0)



y_pred = cluster.labels_#获取训练后对象的每个样本的标签
print(y_pred)
list_3 = []
for i in list_0:

    list_3.append(str(i[0])+','+str(i[-1]))

df['mapbar'],df['centroid'],df['normalize']=[list_1,y_pred,list_3]

path = './柳影实验学校公交信息采集_分类后数据.xlsx'
lxgh.dict_csv(df,path)



