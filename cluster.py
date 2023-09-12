import numpy as np
from sklearn.cluster import KMeans

from utils import *



# path = '/Users/liufucong/Desktop/环线公交 副本'
    # i = '柳影中学公交信息采集.xlsx'
with open('./school_location.json','r') as f:
    content = f.read()
    content = json.loads(content)

# for i in content.items():

id = content['长盛小学公交信息采集.xls']['location']
print(id)

test = clu(destination=id, path= '/Users/liufucong/Downloads/route_plan/data/长盛小学公交信息采集/长盛小学公交信息采集.csv')
test.cluster()
test.final_split()




# if __name__ == '__main__':
#
#     path = '/Users/liufucong/Desktop/环线公交 副本'
#     i = '柳影中学公交信息采集.xlsx'