import pandas as pd
save_path = './5_0_1.csv'
df = pd.read_csv('./柳影实验学校公交信息采集_分类后数据_5.csv')
# df_0 = df[df['centroid']]


df_0 = df[df['centroid']==0]
df_1 = df[df['centroid']==1]
frames = [df_0,df_1]
df_0_1 = pd.concat(frames)
df_0_1.to_csv(save_path, header=True)
print(df_0_1)