import itertools
import json
import requests
import copy
# import utils



with open('./station_5_25.json', 'r') as f:
    content = f.read()
    content = json.loads(content)


with open('./st_name_sq_25.json', 'r',encoding='utf-8') as f:
    content1 = f.read()
    content1 = json.loads(content1)

new_dict =dict()
for i in content1:
    for k,v in i.items():
        new_dict[v] = k

# print(new_dict)


# print(content1)

def get_list_name(list,dict=new_dict):
    tt = []
    for i in list:
        tt.append(dict[i])

    return tt

def best_map_speed(start,*args,strategy=0,end=['125.325504,43.928104']):
    """
    :param start:起始点
    :param end: 目的点
    :param tujingdian:途经点
    :param strategy: 速度优先计算导航距离
    :return: 最佳速度优先导航路线
    """

    parameters = {'key': '73b8604da9e3019fa8334d0815532879',  # 高德Key
                  'origin': start,
                  'destination': end,
                  'waypoints': args,
                  'strategy': strategy,
                  }  # 地址参数
    url = 'https://restapi.amap.com/v3/direction/driving?'  # 高德地图地理编码API服务地址
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    lon_lat = result["route"]["paths"][0]["distance"]
    # print(result)
    time=0
    for i in result["route"]["paths"][0]["steps"]:
        time += int(i['duration'])
    # time =  result["route"]["paths"][0]["steps"][0]['duration']# 获取返回参数geocodes中的location，即经纬度
    # print(result)
    # print(lon_lat)
    return lon_lat,time

# pq = [1,2,3]
def permutation(li,num):
    # print(list(itertools.permutations(li,num )))
    return list(itertools.permutations(li,num ))


ll = []
with open('route_25.json', 'w') as f:
    for k,i in enumerate(content):
        listss = copy.deepcopy(content)
        # print(k)
        # print(i)
        # kk = content
        listss.pop(k)
        # print(listss)

        # lists1 = [1, 2, 3, 4]
        # listss = copy.deepcopy(lists1)
        # listss.pop(0)
        # lists1
        temp = permutation(listss,5)
        # print(temp)
        for i_i in temp:
            tianwei,time = best_map_speed(i,i_i)

            key = new_dict[i]+str(get_list_name(i_i))
            distance = tianwei
            temp_dict=dict()
            temp_dict[key] = {"distance":distance,'time':time}
            hh = json.dumps(temp_dict, indent=3, ensure_ascii=False)
            f.write(hh)
            # ll.append(temp_dict)

            # ll[key].append('distance':distance)
            # dict[key]
            # print(temp_dict)
            # print(str(i)+'---'+str(i_i))


# hh = json.dumps(ll, indent=3, ensure_ascii=False)
# with open('route_25.json', 'w') as f:
#     f.write(hh)
# for i in content:




