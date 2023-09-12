import utils
import pandas as pd
import os
from sklearn.cluster import KMeans
import json
import utils
import numpy as np
def subset():


    path = '/Users/liufucong/Downloads/route_plan/data/长盛小学公交信息采集/长盛小学公交信息采集_拆分后.csv'

    save_pth = (os.path.split(path)[1]).split('.')[0]
    cwd = os.path.split(path)[0]
    print(os.path.join(save_pth,cwd))



    for i in range(3):
        df = pd.read_csv(path)
        df = df[df['centroid']==i]
        save_pth = (os.path.split(path)[1]).split('.')[0]+'_分簇_'+str(i)+'.csv'
        df.to_csv(os.path.join(cwd,save_pth))


def seb_cluster():
    list_1 = []
    with open('./school_location.json', 'r') as f:
        content = f.read()
        content = json.loads(content)


    loc = content['长盛小学公交信息采集.xls']['location']
    print(loc)
    loc_0 = float((utils.coor_convert(loc)['locations']).split(',')[0])
    list_1.append(loc_0)
    loc_1 = float((utils.coor_convert(loc)['locations']).split(',')[1])
    list_1.append(loc_1)
    print(list_1)
    path = '/Users/liufucong/Downloads/route_plan/data/长盛小学公交信息采集/长盛小学公交信息采集_拆分后_分簇_2.csv'
    df = pd.read_csv(path)
    # df['normalize_x','normalize_y']



    cluster = KMeans(n_clusters=5, random_state=0)
    cluster.fit(df[['normalize_x','normalize_y']])
    y_pred = cluster.labels_
    centtrod = cluster.cluster_centers_
    print(y_pred)
    print(type(centtrod))
    print(centtrod+np.array(list_1))


if __name__ == '__main__':
    seb_cluster()