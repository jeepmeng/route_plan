import json
import os

import pandas as pd
import numpy as np


def load_gt(path,colums='Unnamed: 3',head=2):

    df = pd.read_excel(io=path)
    # print(df.columns)
    # print(type(df['Unnamed: 3'][2:]))
    # tt = df[colums][head:].values.tolist()
    tt = df[colums][head:].values.tolist()
    # print(len(t))
    # new_t = list(set(t))
    # print(len(new_t))
    return tt

def load_dis(path,colums='Unnamed: 3',head=2,end=-1):

    df = pd.read_excel(io=path)
    # print(type(df['Unnamed: 3'][2:]))

    tt = df[colums][head:end].values.tolist()
    # print(len(t))
    # new_t = list(set(t))
    # print(len(new_t))
    return tt


def dis_collect():
    dict = {}
    path = '/Users/liufucong/Desktop/环线公交 副本'
    ls = os.listdir(path)
    print(ls)
    for i,j in enumerate(ls):
        # if i==1:
        #     x = load_gt(os.path.join(path,j),colums='Unnamed: 4')[0]
        #     dict[j] = x
        #     print(x)
        # else:
        #     continue
        print(j)
        x = load_gt(os.path.join(path,j),colums='Unnamed: 4')[0]

        # print('...............',x)
        # if i == 0:
        #     break
        dict[j] = {'origin':x}

    # if not os.path.exists('./school_location.json'):
    #     os.mkdir('./school_location.json')
    # else:
    #     pass

    with open('school_location.json','w',encoding='utf-8') as f:
        a = json.dumps(dict, indent=True, ensure_ascii=False)
        f.write(a)


def load_geo(path,colums='Unnamed: 3',head=2,end=-1):

    df = pd.read_csv(path)
    # print(type(df['Unnamed: 3'][2:]))
    tt = df[colums][head:end].values.tolist()
    # print(len(t))
    # new_t = list(set(t))
    # print(len(new_t))
    return tt

if __name__ == '__main__':
    pass
    # path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'
    # ll = load_gt(path)
    # print(ll)


    # list_1 = []
    # path_2 = '/Users/liufucong/Downloads/route_plan/柳影实验学校公交信息采集.csv'
    # df = pd.read_csv(path_2)
    # for i in df['geo'].tolist():
    #     list_1.append([float(i.split(',')[0]),float(i.split(',')[-1])])
    # print(list_1)

    # print(df['geo'].tolist())



    # dis_collect()




