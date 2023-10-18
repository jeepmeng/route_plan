import json

from sklearn.cluster import k_means
from sql_utils import *
import numpy as np
import pandas as pd

neighbor_celect = np.zeros((525,525))
neighbor_id = np.zeros((525,525))



connection_route_new = new_route_connect()
# cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor_route_new = connection_route_new.cursor()
#查看对应表的key是否有值
# sql = f"select count(*) from detail_info"
sql_get_all = f"select * from detail_info"


cursor_route_new.execute(sql_get_all)

route_new_data=cursor_route_new.fetchall()
# print(route_new_data[0])
nei_dict = dict()
# nei_dict_json = dict()
for k in route_new_data:
    id_or = k['id']




    for i in route_new_data:
        dis = np.array([float(k['start_loc_x']), float(k['start_loc_y'])])-\
              np.array([float(i['start_loc_x']), float(i['start_loc_y'])])
        id = i['id']
        # id = str(id).replace("\'","\"")
        # print(id)
        # print(type(dis))
        # dis = np.around(dis,decimals=6)
        dist = np.linalg.norm(dis)
        # print(dist)
        dist = np.around(dist, decimals=6)
        # print(dist)

        nei_dict[str(id)] = str(dist)
    nei_dict_js = json.dumps(nei_dict)
    print(nei_dict_js)
    sql_update = f"update detail_info set neighbor='{nei_dict_js}' where id={id_or}"
    print(sql_update)
    cursor_route_new.execute(sql_update)
# print(nei_dict)
connection_route_new.commit()
cursor_route_new.close()
connection_route_new.close()


if __name__ == '__main__':
    pass
    # a = np.array([1,2])
    # b = np.array([3,4])
    # print(a-b)

    # {'542': 0.0, '543': 0.0, '544': 0.009895, '545': 0.009895}

    # a = np.array([[6., 3., 2., 8.],
    #    [8., 8., 3., 4.],
    #    [5., 3., 5., 7.]])
    # b = np.delete(a, 2,0)
    # print(a)
    # print(b)