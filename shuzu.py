import os
import pandas as pd

import json


def load_csv(path, index=False, condition=False):
    df = pd.read_csv(path)
    return df
# def all load_csv()




if __name__ == '__main__':
    pth = './data'
    pwd = os.listdir(pth)
    # print(pwd)
    for i in pwd:
        if i.startswith('.DS'):
            continue
        pwd_file = os.path.join(pth,i)
        file = os.listdir(pwd_file)
        # print(file)
        for j in file:
            if j.endswith('采集.csv'):
                # print(os.path.join(pwd_file,j))
                df = load_csv(os.path.join(pwd_file,j))
                # print(df['loc'].tolist())
                # print(os.path.join(pwd_file,j).split('.'))
                save_path = '.'+os.path.join(pwd_file,j).split('.')[1] + '.json'
                # print(save_path)
                with open(save_path, 'w') as f:
                    f.write(json.dumps(df['loc'].tolist()))


    # path = '/Users/liufucong/Downloads/route_plan/data/72中小学部公交信息采集/72中小学部公交信息采集.csv'
    # cwd, file = os.path.split(path)
    # print(cwd)
    # df = load_csv(path)
    # # print(df['loc'].tolist())
    # save_path = path.split('.')[0]+'.json'
    # print(save_path)
    # with open(save_path,'w') as f:
    #     f.write(json.dumps(df['loc'].tolist()))