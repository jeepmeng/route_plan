import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.notebook_repr_html=False
plt.rcParams['figure.dpi'] = 75  # 图形分辨率
sns.set_theme(style='darkgrid')  # 图形主题


path = './柳影实验学校公交信息采集_拆分后.csv'
df = pd.read_csv(path)

df = df[df['normalize_x']<0.06]
df = df[df['normalize_y']>-0.04]
# df = df[df['normalize_x']>0.06]
print(df)


sns.scatterplot(data=df,x='normalize_x',y='normalize_y',hue='centroid')
plt.savefig('./柳影实验学校.png')
plt.show()