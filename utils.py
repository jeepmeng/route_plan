import numpy as np
import pandas as pd
import os

import matplotlib

# def loc_name_loci(name_list,loc_list):
#     pass



def dict_csv(dict,path):
# mydict = {'key1': 'a', 'key2': 'b', 'key3': 'c'}
#     path = '/Users/liufucong/Desktop/环线公交/47中学公交信息采集.xlsx'
    file_name = (os.path.split(path)[-1]).split('.')[0]+'.csv'
    cwd = os.getcwd()
    save_path = os.path.join(cwd,file_name)
    (pd.DataFrame.from_dict(data=dict, orient='index').to_csv(save_path, header=False))
    print('{}------- already saveed at --------{}'.format(file_name,save_path))


if __name__ == '__main__':
    # path = '/Users/liufucong/Desktop/环线公交/47中学公交信息采集.xlsx'
    # dict_csv(path)
    # ll = (os.path.split(path)[-1]).split('.')[0]
    # print(ll)
    # cwd = os.getcwd()
    # print(cwd)
    # path.split('.')[0]
    # path.split('/')

    print(matplotlib.matplotlib_fname())
