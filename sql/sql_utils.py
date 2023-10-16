from pysql import *
import pandas as pd
import json

def test_connect():
    databases_params = {
        'db_host': "1.tcp.vip.cpolar.cn",# 数据库主机地址
        "port" :21238, #
        'db_username': "root",
        'db_password': "jeepmeng2",
        'db_name': "route_new"}


    connection = connect_to_database(databases_params)
    print(connection)
    return connection


def load_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as json_file:
        school_locations = json.load(json_file)

    return school_locations






if __name__ == '__main__':
    test_connect()
