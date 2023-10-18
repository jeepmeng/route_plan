from sql.sql_utils import *
import numpy as np
from sklearn.cluster import KMeans


connection_route_new = new_route_connect()
# cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor_route_new = connection_route_new.cursor()
#查看对应表的key是否有值
sql = "select * from detail_info"


cursor_route_new.execute(sql)
# for i in range(10):
route_new_data=cursor_route_new.fetchall()
# i = 0
# while route_new_data:
for i in route_new_data:
    des_loc_x = float(i['des_loc'].split(',')[0])
    des_loc_y = float(i['des_loc'].split(',')[-1])
    insert_sql = f"update detail_info "\
                f"set des_loc_x={des_loc_x}, des_loc_y={des_loc_y} "\
                f"where id = {i['id']} ;"
    print(i['id'])
    print(insert_sql)
    cursor_route_new.execute(insert_sql)
connection_route_new.commit()
    # route_new_data = cursor_route_new.fetchone()
    # print(route_new_data)

cursor_route_new.close()
connection_route_new.close()