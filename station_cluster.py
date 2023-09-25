import os
import pandas as pd
from sklearn.cluster import KMeans

def cluster(df):
    # cluster = KMeans(n_clusters=self.n_cluster, random_state=0).fit(self.list_co_convert)
    cluster = KMeans(n_clusters=5, random_state=0)
    cluster.fit(df)
    y_pred = cluster.labels_
    # print(y_pred)
    return(y_pred)
    # for i in list_co_normal:
    #     convert_str.append(str(i[0]) + ',' + str(i[-1]))
    # df['mapbar'], df['centroid'], df['normalize'] = [list_co_convert,
    #                                                                 y_pred,
    #                                                                 convert_str]
    # save_path_cluster = path_refactor(self.path)
    # dict_to_csv( df, save_path_cluster)


station = []
path = '/Users/liufucong/Downloads/route_plan/test/长盛小学公交信息采集_station.pickle'
df = pd.read_pickle(path)
# print(df['station'])
for i in df['station']:
    # print(i)
    station+=i
    # station.append(i)
print(station)

for k,i in enumerate(station):
    station[k] =float(i.split(',')[0]),float(i.split(',')[-1])
print(station)
cluster(station)
