from sql_utils import *
import numpy as np

connection_route_new = new_route_connect()
# cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor_route_new = connection_route_new.cursor()
#查看对应表的key是否有值
sql = f"select distinct grid from detail_info"

cursor_route_new.execute(sql)

route_new_data=cursor_route_new.fetchall()

# print(len(route_new_data))

# loc_x = []
# loc_y = []
all_location = dict()
for i in route_new_data:
    temp_x = 0.0
    temp_y = 0.0
    print(i['grid'])
    if i['grid']:


        # sql_id = f"select id from detail_info where grid={i['grid']}"
        sql_loc_x = f"select start_loc_x from detail_info where grid='{i['grid']}'"
        sql_loc_y = f"select start_loc_y from detail_info where grid='{i['grid']}'"
        # cursor_route_new.execute(sql_id)
        # point_id_of_grid = cursor_route_new.fetchall()
        cursor_route_new.execute(sql_loc_x)
        point_x_of_grid = cursor_route_new.fetchall()
        for i_1 in point_x_of_grid:
            temp_x+=float(i_1['start_loc_x'])
        temp_x = np.round(temp_x/len(point_x_of_grid),6)
        print(len(point_x_of_grid))



        cursor_route_new.execute(sql_loc_y)
        point_y_of_grid = cursor_route_new.fetchall()
        for i_2 in point_y_of_grid:
            temp_y+=float(i_2['start_loc_y'])
        temp_y = np.round(temp_y / len(point_y_of_grid),6)
        # print(point_y_of_grid)
        all_location[i['grid']]=[temp_x,temp_y]
        print(len(point_y_of_grid))
    else:
        pass
print(all_location)


# connection_route_new.commit()
cursor_route_new.close()
connection_route_new.close()
all_location_json = json.dumps(all_location, indent=3, ensure_ascii=False)
with open('all_location.json', 'w') as f:
    f.write(all_location_json)