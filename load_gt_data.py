import pandas as pd
import numpy as np


def load_gt(path,colums='Unnamed: 3',head=2,end=-1):

    df = pd.read_excel(io=path)
    # print(type(df['Unnamed: 3'][2:]))
    tt = df[colums][head:end].values.tolist()
    # print(len(t))
    # new_t = list(set(t))
    # print(len(new_t))
    return tt


def load_geo(path,colums='Unnamed: 3',head=2,end=-1):

    df = pd.read_csv(path)
    # print(type(df['Unnamed: 3'][2:]))
    tt = df[colums][head:end].values.tolist()
    # print(len(t))
    # new_t = list(set(t))
    # print(len(new_t))
    return tt

if __name__ == '__main__':
    # path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'
    # ll = load_gt(path)
    # print(ll)


    list_1 = []
    path_2 = '/Users/liufucong/Downloads/route_plan/柳影实验学校公交信息采集.csv'
    df = pd.read_csv(path_2)
    for i in df['geo'].tolist():
        list_1.append([float(i.split(',')[0]),float(i.split(',')[-1])])
    print(list_1)

    # print(df['geo'].tolist())