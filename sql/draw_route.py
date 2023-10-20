import requests

#速度优先下通过起止点和终止点，途经点给出多种最佳路线
def best_map_speed(start,end,*args,strategy=0):
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
    url = 'https://restapi.amap.com/v3/direction/walking?'  # 高德地图地理编码API服务地址
    result = requests.get(url, parameters)  # GET方式请求
    result = result.json()
    lon_lat = result["route"]["paths"][0]["distance"]  # 获取返回参数geocodes中的location，即经纬度
    # print(result)
    # print(lon_lat)
    return lon_lat