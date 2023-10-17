from sql_utils import *
from utils import *


def load_route_new(key):
    connection_route_new = new_route_connect()
    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor_route_new = connection_route_new.cursor()
    #查看对应表的key是否有值
    sql = f"select distinct {key} from detail_info"


    cursor_route_new.execute(sql)

    route_new_data=cursor_route_new.fetchall()
    print(route_new_data)
    # connection.commit()
    cursor_route_new.close()
    connection_route_new.close()



def load_route_data(table):
    connection_route_data = route_plan_connect()
    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor_route_data = connection_route_data.cursor()
    #查看对应表的key是否有值
    sql = f"select * from {table}"


    cursor_route_data.execute(sql)

    data=cursor_route_data.fetchall()
    # print(data['school_loc_y'])
    # print(data)
    # connection.commit()
    cursor_route_data.close()
    connection_route_data.close()
    return data



def insert_route_new_from_route_data():
    connection_route_data = route_plan_connect()
    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor_route_data = connection_route_data.cursor()
    #查看对应表的key是否有值
    sql = "insert sc_info.* from school_info sc_info"


    cursor_route_data.execute(sql)

    route_new_data=cursor_route_data.fetchall()
    print(route_new_data)
    # connection.commit()
    cursor_route_data.close()
    connection_route_data.close()


def aa():
    route_data = load_route_data('长新小学公交信息')
    school_name = '长春市宽城区长新小学'
    des_loc = get_loc(school_name)
    print(des_loc)
    # 125.329088, 43.923239

    connection_route_data = new_route_connect()
    # cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor_route_data = connection_route_data.cursor()
    for i in route_data:
        print(i)
        start_loc_name = i['address']
        start_loc = i['loc']
        print(start_loc)
        des_dis = i['dis']
        sql = "insert into detail_info(start_loc_name, school_name, des_dis, start_loc, des_loc) " \
              f"values ('{start_loc_name}', '{school_name}', '{des_dis}', '{start_loc}', '{des_loc}');"
        print(sql)
        cursor_route_data.execute(sql)
        connection_route_data.commit()
        # try:
        #     cursor_route_data.execute(sql)
        #     connection_route_data.commit()
        # except:
        #     connection_route_data.rollback()
    cursor_route_data.close()
    connection_route_data.close()


if __name__ == '__main__':
    load_route_new('school_name')