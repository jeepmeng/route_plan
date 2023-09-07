import pandas as pd
import numpy as np
from main import *

path = './柳影实验学校公交信息采集_分类后数据_5.csv'
df = pd.read_csv(path)
# print(df.loc)

df_id = df.id.to_frame()
print(df_id)

df_id['loc_x'],df_id['loc_y'],df_id['dis'],df_id['mapbar_x']\
    ,df_id['mapbar_y'],df_id['centroid'],df_id['normalize_x'],df_id['normalize_y'] = [df['loc'].apply(lambda x: x.split(',')[0]),
                                                                                      df['loc'].apply(lambda x: x.split(',')[-1]),
                                                                                      df['dis'],
                                                                                      df['mapbar'].apply(lambda x: x.split(',')[0]),
                                                                                      df['mapbar'].apply(lambda x: x.split(',')[-1]),
                                                                                      df['centroid'],
                                                                                      df['normalize'].apply(lambda x: x.split(',')[0]),
                                                                                      df['normalize'].apply(lambda x: x.split(',')[-1])]
print(df_id)

path_1 = './柳影实验学校公交信息采集_拆分后_5.csv'
lxgh.dict_csv(df_id,path_1)