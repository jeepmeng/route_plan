import numpy as np
from main import *
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
path_2 = '/Users/liufucong/Downloads/route_plan/柳影实验学校公交信息采集.csv'
# list_1 = []


list_2 = []
destination = '长春市宽城区柳影实验学校'
add = lxgh.get_loc(destination)
list_2.append([float(add.split(',')[0]),float(add.split(',')[-1])])
# print(list_2)
print(list_2[0])

list = []
def fun_1(path,desti):

    df = pd.read_csv(path)
    # print(df['geo'].tolist())
    for i in df['geo'].tolist():
        # list.append([float(i.split(',')[0])-desti[0],float(i.split(',')[-1])-desti[-1]])
        list.append([float(i.split(',')[0]), float(i.split(',')[-1])])
    # print(list)
    return list

list_1 = fun_1(path_2,list_2[0])
print(list_1)
#
# # print(list_1[0]-list_2[0])
#
#
n_clusters=3
cluster = KMeans(n_clusters=n_clusters,random_state=0).fit(list_1)



centroid=cluster.cluster_centers_
print(centroid)

y_pred = cluster.labels_#获取训练后对象的每个样本的标签
print(y_pred)
# centtrod = cluster.cluster_centers_
# color=['red','pink','orange']
# fig, axi1=plt.subplots(1)
# for i in range(n_clusters):
#     axi1.scatter(list_1[y_pred==i, 0], list_1[y_pred==i, 1],
#                marker='o',
#                s=8,
#                c=color[i])
# axi1.scatter(centroid[:,0],centroid[:,1],marker='x',s=100,c='black')
# plt.show()




# X, y = make_blobs(n_samples=500, # 500个样本
#                  n_features=2, # 每个样本2个特征
#                  centers=4, # 4个中心
#                  random_state=1 #控制随机性
#                  )
# print(X.shape)