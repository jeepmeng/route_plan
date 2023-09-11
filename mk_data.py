from utils import *








def gogo():
    path = '/Users/liufucong/Desktop/环线公交 副本'
    # i = '柳影中学公交信息采集.xlsx'
    with open('./school_location.json','r') as f:
        content = f.read()
        content = json.loads(content)

    for i in content.items():
        # xlsx = i[0]
        # print(xlsx)
        # des = i[-1]['location']
        dict_csv(os.path.join(path,i[0]),i[-1]['location'])


if __name__ == "__main__":
    gogo()

    # path = '/Users/liufucong/Desktop/环线公交 副本'
    # i = '柳影中学公交信息采集.xlsx'
    # dict_csv(os.path.join(path, i),"125.307175,43.937016")