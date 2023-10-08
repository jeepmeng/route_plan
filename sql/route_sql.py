# import pymysql
from pysql import *


databases_params = {
    'db_host': "172.16.19.103",# 数据库主机地址
    "port" :3310, #
    'db_username': "root",
    'db_password': "jeepmeng2",
    'db_name': "route_data"}


connection = connect_to_database(databases_params)
print(connection)

cursor = connection.cursor()

sql = '''ALTER TABLE 47中学公交信息 ADD COLUMN des_location VARCHAR(255) DEFAULT NULL COMMENT '目的地' AFTER dis;'''


cursor.execute(sql)

connection.close()