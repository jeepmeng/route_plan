from pysql import *
import pandas as pd
import json


databases_params = {
    'db_host': "172.16.19.103",# 数据库主机地址
    "port" :3310, #
    'db_username': "root",
    'db_password': "jeepmeng2",
    'db_name': "route_new"}


connection = connect_to_database(databases_params)
cursor = connection.cursor()




# path = '/Users/liufucong/Desktop/环线公交 副本'
# i = '柳影中学公交信息采集.xlsx'
with open('../school_location.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

for i in content.keys():
    school_name = content[i]["origin"]
    school_id = content[i]["school_id"]
    school_loc_x = float(content[i]["location"].split(',')[0])
    school_loc_y = float(content[i]["location"].split(',')[-1])
    print(i)

    sql = f"INSERT school_info SET school_doc = '{str(i)}'," \
          f"school_name = '{school_name}'," \
          f"school_id = '{school_id}'," \
          f"school_loc_x = '{school_loc_x}'," \
          f"school_loc_y = '{school_loc_y}'"
    cursor.execute(sql)
    # break
    connection.commit()
connection.close()