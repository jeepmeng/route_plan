from main import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def max_dis(path):
    df = pd.read_csv(path)
    # return np.array(df['dis'])
    # return df['dis'].tolist()
    return df



path = '/Users/liufucong/Desktop/环线公交 副本/柳影实验学校公交信息采集.xlsx'

# loc_name = load_gt(path)
# print(loc_name[:10])
# list_1 = []
# for i in loc_name[:10]:
#     loc = lxgh.get_loc(i)
#     list_1.append(lxgh.place_distance(loc))
#
# print(list_1)

path = './柳影实验学校公交信息采集.csv'
ll = max_dis(path)
# print(np.max(ll))
print(type(ll))
ll = ll[ll['dis']<8500]
# print(ll['dis'])
print(np.max(ll['dis']))

# ll.plot(kind = 'box',title='all',sym='r+')
# plt.show()





# plt.rcParams['figure.figsize'] = (13, 5)    #设定图片大小
# # f = plt.figure()                            #确定画布
# fig,axes=plt.subplots(1,2)
# # f.add_subplot(1,2,1)
# sns.distplot(ll, kde=False,ax=axes[0])                 #绘制频数直方图
# plt.ylabel("频数", fontsize=16)
# plt.xticks(fontsize=16)                    #设置x轴刻度值的字体大小
# plt.yticks(fontsize=16)                   #设置y轴刻度值的字体大小
# plt.title("(a)", fontsize=20)             #设置子图标题
#
#
# # f.add_subplot(1,2,2)
# sns.distplot(ll,ax=axes[1])                           #绘制密度直方图
# plt.ylabel("密度", fontsize=16)
# plt.xticks(fontsize=16)                  #设置x轴刻度值的字体大小
# plt.yticks(fontsize=16)                  #设置y轴刻度值的字体大小
# plt.title("(b)", fontsize=20)            #设置子图标题
#
# plt.subplots_adjust(wspace=0.3)         #调整两幅子图的间距
# plt.show()



