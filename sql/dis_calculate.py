from math import asin, sqrt, cos, pi


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

    print(st_distance([125.338530, 43.947330], [125.338530, 43.944330]))
