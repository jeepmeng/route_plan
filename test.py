
import requests



path3_real =[
'华大城一期公交站（Z110路）',#125.333856,43.956194
'华大天朗国际公交站（Z110路）',#125.344367,43.950086
'宽城区宽府路公交站（G8路，Z110路，123路）',#125.330062,43.942557
'宽城区庆丰路公交站（G8路，Z110路，123路）',#125.318977,43.874111
'长春市宽城区华侨城公交站（G8路，G21路，Z110路，123路）',#125.340908,43.932803
'长春市宽城区开关宿舍公交站（G11路）',#125.337159,43.927224
'长春市宽城区劳模会馆公交站（G10路，G11路，G21路）',#125.349006,43.930739
'长春市宽城区团山街公交站（G10路，G11路，G21路）',#125.355312,43.922259
'长春市宽城区密山路公交站（G10路）',#125.322792,43.878319
'长春市宽城区福山路公交站（G10路）',#125.360290,43.931243
'长春市宽城区金美程家园东区（西2门对面停靠）',#125.349003,43.921807
'长春市宽城区钻石村公交站（274路，Z274路）',#125.346145,43.921428
'长春市宽城区天光路公交站（G8路，G11路，Z110路）',#125.332757,43.920230
'长春市宽城区呗亚泰大街公交站（274路，Z274路）',#125.345041,43.899128
'长春市宽城区培智学校南门',#125.331496,43.920632
'长春市第七十二中学（北校区）',#125.328791,43.923203
'长春市第七十二中小学部',#125.330128,43.924254
'长盛小学',#125.319229,43.926578
'长新小学',#125.325018,43.929893
'长春市宽城区实验小学'#125.325453,43.927389


]

def get_loc_2(addr):  # addr->地名
    parameters = {
        #             'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
        # 'key': '74ed60f0267e195ede2bad10c9619c21',  # 高德Key
        'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
        'address': addr,
        'city': '长春市'
        # 'destination': addr2,
    }  # 地址参数

    url = 'https://restapi.amap.com/v3/geocode/geo?'
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    # print(result)
    try:
        result['geocodes'][0]['location']
    except KeyError:
        print("location request error")
        return ""
    else:

        # print(result['geocodes'][0]['location'])
        return result['geocodes'][0]['location']


# path = '/Users/liufucong/Downloads/route_plan/test/长盛小学公交信息采集_分类后.csv'
# df = pd.read_csv(path)
# ll= np.array(df['dis'])
# print(np.mean(ll))
# print(np.max(ll))
# df = df[df['dis']<=np.mean(ll)*1.5]
# print(df)
if __name__ == '__main__':



    # for i in path3_real:
    #     # addrs = '宽城区团山街公交站'
    #     a = get_loc_2(i)
    #     print(a)


    # for i in path3_real:
    #     print(i)

    name = '长春市宽城区福山路公交站'
    print(get_loc_2(name))