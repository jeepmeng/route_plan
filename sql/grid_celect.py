import pandas as pd
from sql_utils import *


with open('./grid_json.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

# print(content.items())
# for i in content.items():
#     print(i)
#     grid = i[0]
    # print(
    # print(i[-1][2])

connection_route_new = new_route_connect()
# cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor_route_new = connection_route_new.cursor()
#查看对应表的key是否有值
sql = f"select id, start_loc_x, start_loc_y from detail_info"


cursor_route_new.execute(sql)

route_new_data=cursor_route_new.fetchall()
print(route_new_data)

for i in content.items():
    # grid = i[0]
    for k in route_new_data:
        if i[-1][2]>=float(k['start_loc_x'])>=i[-1][0] and \
            i[-1][-1]>=float(k['start_loc_y'])>=i[-1][1]:

            sql_grid = f"update detail_info " \
                  f"set grid='{i[0]}'" \
                  f"where id = '{k['id']}'"
            cursor_route_new.execute(sql_grid)
#
            print(sql_grid)
# print(route_new_data)
connection_route_new.commit()
cursor_route_new.close()
connection_route_new.close()