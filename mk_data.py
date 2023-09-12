from utils import *


def test_demo():
    path = '/Users/liufucong/Desktop/环线公交 副本'
    # i = '柳影中学公交信息采集.xlsx'
    with open('./school_location.json', 'r') as f:
        content = f.read()
        content = json.loads(content)
    path = os.path.join(path, '长盛小学公交信息采集.xls')

    print(path)
    loc = content['长盛小学公交信息采集.xls']['location']
    print(loc)
    dict_csv(path, loc, '/Users/liufucong/Downloads/route_plan/test')




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
    # gogo()

    test_demo()
    # path = '/Users/liufucong/Desktop/环线公交 副本'
    # i = '柳影中学公交信息采集.xlsx'
    # dict_csv(os.path.join(path, i),"125.307175,43.937016")