
import requests


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

    addrs = '宽城区团山街公交站'
    a = get_loc_2(addrs)
    print(a)