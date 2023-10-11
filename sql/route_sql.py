# import pymysql
from pysql import *
import pandas as pd
import json




path = '/Users/liufucong/Desktop/环线公交 副本'
# i = '柳影中学公交信息采集.xlsx'
with open('../school_location.json', 'r') as f:
    content = f.read()
    content = json.loads(content)

# print(content['47中学公交信息采集.xlsx']['location'])



# print(gengx)

databases_params = {
    'db_host': "172.16.19.103",# 数据库主机地址
    "port" :3310, #
    'db_username': "root",
    'db_password': "jeepmeng2",
    'db_name': "route_data"}


connection = connect_to_database(databases_params)
print(connection)

cursor = connection.cursor()
context = content['47中学公交信息采集.xlsx']['location']
# context='125.337750,43.928402'
print(context)
# sql = '''ALTER TABLE 47中学公交信息 ADD COLUMN des_location VARCHAR(255) DEFAULT NULL COMMENT '目的地' AFTER dis;'''
# sql = f'UPDATE 47中学公交信息 SET des_location={context}

sql  = f"UPDATE 47中学公交信息 SET des_location= '{context}' where des_location= '{context}'"

# UPDATE 47中学公交信息 SET des_location= 'nihao'
cursor.execute(sql)
connection.commit()
connection.close()


# a = '''{}'''.format(context)
# print(a)