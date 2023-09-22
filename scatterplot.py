import os.path

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.notebook_repr_html=False
plt.rcParams['figure.dpi'] = 75  # 图形分辨率
sns.set_theme(style='darkgrid')  # 图形主题


# path = '/Users/liufucong/Downloads/route_plan/test/长盛小学公交信息采集_拆分后_1.5.csv'
path = '/Users/liufucong/Downloads/route_plan/hongtian.csv'
df = pd.read_csv(path)

df = df[df['normalize_x']<1]
df = df[df['normalize_y']>-0.9]
# df = df[df['normalize_x']>0.06]
print(df)


sns.scatterplot(data=df,x='normalize_x',y='normalize_y',hue='centroid')
# save_pth = (os.path.split(path)[1]).split('.')[0]+'_1.5.png'
# cwd = os.path.split(path)[0]
# print(os.path.join(save_pth,cwd))
# plt.savefig(os.path.join(cwd,save_pth))
plt.show()