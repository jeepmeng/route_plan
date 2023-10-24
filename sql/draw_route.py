import requests
from test import get_loc_2
import copy
import json


#速度优先下通过起止点和终止点，途经点给出多种最佳路线
def best_map_speed(start,end,*args,strategy=0):
    """
    :param start:起始点
    :param end: 目的点
    :param tujingdian:途经点
    :param strategy: 速度优先计算导航距离
    :return: 最佳速度优先导航路线
    """
    parameters = {
        # 'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
                  'key': 'f2cf4601a4c44261d4e62e77a6b0a0e7',
                  'origin': start,
                  'destination': end,
                  'waypoints': args,
                  'strategy': strategy,
        'show_fields':'cost,tmcs',
                  }  # 地址参数
    # url = 'https://restapi.amap.com/v3/direction/driving?'   # 高德地图地理编码API服务地址
    url = 'https://restapi.amap.com/v5/direction/driving?'  # 高德地图地理编码API服务地址
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    # lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
    lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
    output_path = result["route"]
    print(result["route"])
    # time = 0
    # for i in result["route"]["paths"][0]["steps"]:
    #     time += int(i['duration'])
    # print(result)
    # print(lon_lat)
    # return lon_lat, time, output_path
    return lon_lat, output_path

path1 =[
    '新隆家园公交站',
'宽城交警队公交站',
'长春宽城区新月花园公交站',
'新月市场公交站',
'菜市南街公交站',
'北人民大街公交站',
'长春宽城区新城社区食杂店',
'长盛小学',
'长春市第七十二中小学部',
'长春市第七十二中学（北校区）',
'长春市宽城区实验小学',
'长新小学'
]


path1_real =[
    '新隆家园公交站',
'宽城交警队公交站',
'长春宽城区新月花园公交站',
'新月市场公交站',
'菜市南街公交站',
'吉林省长春市宽城区庆丰路140号',
'吉林省长春市宽城区一心街564号',
'长盛小学',
'吉林省长春市宽城区一匡街731号',
'吉林省长春市宽城区一匡街164号',
'长春市宽城区实验小学',
'长新小学'
]



path2 =[
    '英伦小镇(公交站)(英伦小镇D区273路) ',#
'北凯旋路(公交站)(273路) ',#
'桐雨街公交站',#
'中国电信中冶蓝城自助营业厅',
'九台路公交站(z16)-中东港住宅区',
'宽城区政府公交站(G288路)' ,
'长新街公交站',#庆丰路公交站
'长春市第七十二中学（北校区）',
'长春市第七十二中小学部',
'长盛小学',
'长新小学',
'长春市宽城区实验小学'

]

# path2_real =[
#     '英伦小镇(公交站)(英伦小镇D区273路) ',#
# '北凯旋路(公交站)(273路) ',#
# '桐雨街公交站',#
# '吉林省长春市宽城区北环城路5081号',
# '宽城区政府公交站(G288路)' ,
# '九台路公交站' ,
# '庆丰路公交站' ,
# '吉林省长春市宽城区三星街20号',
# '吉林省长春市宽城区长新街134号',
# '长盛小学',
# '吉林省长春市宽城区一匡街843号',
# '长春市宽城区实验小学'
#
# ]





path3 =[
    '华大城一期公交站（Z110路）',
'华大天朗国际公交站',
'宽城区宽府路公交站',
'长春市宽城区华侨城公交站',
'长春市宽城区开关宿舍公交站',
'长春市宽城区阿波罗网咖',
'长春市宽城区密山路公交站',
'长春市宽城区长欣家园公交站',
'长春市宽城区聚旺角超市',
'长春市宽城区天光路公交站',
'长春市宽城区培智学校南门',
'长春市第七十二中学（北校区）',
'长春市第七十二中小学部',
'长盛小学',
'长新小学',
'长春市宽城区实验小学'


]



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
'长春市宽城区亚泰大街公交站（274路，Z274路）',#125.345041,43.899128
'长春市宽城区培智学校南门',#125.331496,43.920632
'长春市第七十二中学（北校区）',#125.328791,43.923203
'长春市第七十二中小学部',#125.330128,43.924254
'长盛小学',#125.319229,43.926578
# '长新小学',#125.325018,43.929893
# '长春市宽城区实验小学'#125.325453,43.927389


]



path_1 = path3_real


temp_list = []
temp_wey_points = ''
temp_wey_points_len = len(path_1)

start = get_loc_2(path_1[0])
# print(path_1[0])
# print(start)
end = get_loc_2(path_1[-1])
# print(end)
# print(path_1[-1])





wey_points = copy.deepcopy(path_1)
wey_points.pop(0)
wey_points.pop(-1)
print('wey_points------',wey_points)


for k,i in enumerate(wey_points):
    loc = get_loc_2(i)

    # for enu, wp in enumerate(i_i):
    if k < temp_wey_points_len - 1:
        temp_wey_points = temp_wey_points + str(i) + ';'
    elif k == temp_wey_points_len - 1:
        temp_wey_points = temp_wey_points + str(i)
print(temp_wey_points)



output = best_map_speed(start,end,temp_wey_points)



if __name__ == '__main__':
    pass
    lon_lat, time, output_path = best_map_speed(start, end, temp_wey_points)
    print('lon_lat-----------------',lon_lat)
    print('time-----------------', time)
    print('output_path-----------------', output_path)
    # pass

    hh = json.dumps(output_path, indent=3, ensure_ascii=False)
    # save_name = str(path1_real)+'.json'
    with open('path3_real.json', 'w') as f:
        f.write(hh)
        # f.write('\ntime={}'.format(time))
        # f.write('\nlength={}'.format(time))