import json
import pandas as pd
import os
from pysql import *

# 读取school_location.json文件
with open('school_location.json', 'r', encoding='utf-8') as json_file:
    school_locations = json.load(json_file)

# 遍历每个学校的CSV文件
for csv_filename, school_info in school_locations.items():
    # 从school_info中获取学校的位置信息
    school_name = school_info.get("data", "")
    school_location = school_info['location'].split(',')
    school_latitude = float(school_location[0])
    school_longitude = float(school_location[1])

    csv_file = f'D:/Pycharm/workspace/route_plan/data'
    csv_filepath = os.path.join(csv_file, school_name, csv_filename)

    # 读取CSV文件
    df = pd.read_csv(csv_filepath)
    df[['latitude', 'longitude']] = df['loc'].str.split(',', expand=True).astype(float)

    # 执行经纬度减法操作
    school_address_dis = df['dis']
    df['delta_latitude'] = df['latitude'] - school_latitude
    df['delta_longitude'] = df['longitude'] - school_longitude

    # 选择要保存的列
    cols_to_save = ['school_name','school_latitude','school_longitude']
    # cols_to_save = ['latitude', 'longitude','delta_latitude', 'delta_longitude', 'dis']

    df['school_name'] = school_name
    df['school_latitude'] = school_latitude
    df['school_longitude'] = school_longitude
    df_to_save = df[cols_to_save]

    # 将数据列和数值转换为列表
    data_columns = df_to_save.columns.tolist()
    print(data_columns)
    data_values = df_to_save.values.tolist()
    print(data_values)

    # 插入数据到数据库
    # insert_data_to_database(connection, school_name, data_columns, data_values)
    # update_data_in_database(connection,school_name,data_columns,data_values)
    try:
        update_data_in_database(connection, school_name, data_columns, data_values)
        print("Update successful")  # 添加成功消息
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()  # 如果出错，进行回滚操作

# 关闭数据库连接
connection.close()
