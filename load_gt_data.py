import pandas as pd
import numpy as np


def load_gt(path,colums='Unnamed: 3',head=2,end=-1):

    df = pd.read_excel(io=path)
    # print(type(df['Unnamed: 3'][2:]))
    t = df[colums][head:end].values.tolist()
    # print(len(t))
    new_t = list(set(t))
    print(len(new_t))
    return new_t
if __name__ == '__main__':
    path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'
    ll = load_gt(path)
    print(ll)