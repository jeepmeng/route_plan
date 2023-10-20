from math import asin, sqrt, cos, pi
from all_cluster import *

# point_a,point_b是经纬度,格式为[lng,lat]
def st_distance(point_a, point_b):
    # 弧度
    radian = pi / 180.0
    # 地球半径
    radius = 6378137

    f = point_a[1] * radian
    h = point_b[1] * radian
    k = 2 * radius
    d = point_b[0] * radian - point_a[0] * radian
    e = (1 - cos(h - f) + (1 - cos(d)) * cos(f) * cos(h)) / 2
    return round(k * asin(sqrt(e)),1)

if __name__ == '__main__':

    # print(st_distance([125.338530, 43.947330], [125.338530, 43.944330]))
    del_point = []
    center = k_cluster()
    print(len(center))
    print(center)
    for k,i in enumerate(center):
        t = st_distance(i, [125.325504, 43.928104])
        # print(st_distance(i, [125.325504,43.928104]))
        if t>=5000:
            continue
        del_point.append(k)


    new_center=[]
    for i in del_point:
        new_center.append(center[i])
    print(new_center)

    pq = []
    for i in new_center:
        # print(st_distance(i, [125.325504, 43.928104]))
        pq.append(str(i[0]) + ',' + str(i[-1]))



    hh = json.dumps(pq, indent=3, ensure_ascii=False)
    with open('center_sq_25.json', 'w') as f:
        f.write(hh)


    # print(len(center))

