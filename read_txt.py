from sklearn.cluster import DBSCAN
from geopy import distance
from utils import *



import pandas as pd
def find_all_lon_lat(filepath):
    a = many_split_race(filepath)
    all_coord_x = []
    all_coord_y = []
    all_coord = []
    for j in a.values:
        coord_x = float(j[2].split(",")[0])
        coord_Y = float(j[2].split(",")[1])
        all_coord_x.append(coord_x)
        all_coord_y.append(coord_Y)
        # temp = (coord_x,coord_Y)
        all_coord.append([coord_x,coord_Y])
        # all_coord.append(temp)
    print(all_coord)
    clustering = DBSCAN(eps=0.01, min_samples=2).fit(all_coord)
    print(clustering.labels_)
    # return sorted(all_coord_x),sorted(all_coord_y)
    return clustering.labels_, all_coord_x, all_coord_y




def find_all_place_dis(filepath):
    a = many_split_race(filepath)
    all_dis_1 = {}
    all_dis_2 = {}
    all_dis_3 = {}
    all_dis_many = {}
    for j in a.values:
        coord_x = float(j[2].split(",")[0])
        coord_Y = float(j[2].split(",")[1])
        # print(coord_x,coord_Y)
        dis = dis1(coord_x,coord_Y,125.325018,43.929893)
        # print("地点",j[1],"距离：",dis)
        if 1000>= dis >0:
            all_dis_1[j[1]]=dis
        if 2000>=dis>1000:
            all_dis_2[j[1]]=dis
        if 3000>=dis>2000:
            all_dis_3[j[1]]=dis
        if dis>3000:
            all_dis_many[j[1]]=dis
    print(sorted(all_dis_1.items(), key=lambda x: x[1]))
    print(sorted(all_dis_2.items(), key=lambda x: x[1]))
    print(sorted(all_dis_3.items(), key=lambda x: x[1]))
    print(sorted(all_dis_many.items(), key=lambda x: x[1]))
    return all_dis_1,all_dis_2,all_dis_3,all_dis_many
# find_all_place_dis("./data/长新小学公交信息采集/长新小学公交信息采集.csv")


def many_split_race(file_path):
    result = pd.read_csv(file_path)
    result.dropna(how='any', axis=0)
    return result


def dis1(xlon,xlat,ylon,ylat):
    """
    :param xlon:1-经度
    :param xlat: 1-维度
    :param ylon: 2-经度
    :param ylat: 2-维度
    :return:
    """
    old=(xlat,xlon)
    new=(ylat,ylon)
    d=distance.great_circle(old, new).m
    s=round(float(d),2)
    return s


if __name__ == '__main__':
    with open('./school_location.json', 'r') as f:
        content = f.read()
        content = json.loads(content)

    loc = content['长盛小学公交信息采集.xls']['location']
    print(loc)

    centroid, x, y = find_all_lon_lat("/Users/liufucong/Downloads/route_plan/data/长新小学公交信息采集/长新小学公交信息采集.csv")
    # print(np.array(x)-25)
    # print(b)
    norm_x = np.array(x) - float(loc.split(',')[0])
    norm_y = np.array(y) - float(loc.split(',')[-1])

    dict = {'centroid':centroid,'normalize_x':norm_x,'normalize_y':norm_y}
    print(dict)
    #
    pd.DataFrame.from_dict(data=dict).to_csv('./hongtian.csv', header=True)