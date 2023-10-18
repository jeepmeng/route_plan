import json

from sklearn.cluster import k_means
from sql_utils import *
import numpy as np
import pandas as pd



connection_route_new = new_route_connect()
# cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor_route_new = connection_route_new.cursor()
#查看对应表的key是否有值
# sql = f"select count(*) from detail_info"
sql_get_all = f"select neighbor from detail_info"


cursor_route_new.execute(sql_get_all)

route_new_data=cursor_route_new.fetchone()
print(route_new_data)
print(type(route_new_data))
ll = json.loads(route_new_data['neighbor'])
print(sorted(ll.items(), key = lambda kv:(kv[1], kv[0])))




# connection_route_new.commit()
cursor_route_new.close()
connection_route_new.close()