import pymysql  # 导入pymysql库，用于与MySQL数据库交互

# 配置数据库连接信息
databases_params = {
    'db_host': "192.168.220.131",# 数据库主机地址
    "port" :3310, #
    'db_username': "root",
    'db_password': "123456",
    'db_name': "route_data"
}
def connect_to_database(params):
    # 连接到数据库
    connection = pymysql.connect(
        host=params['db_host'],
        user=params['db_username'],
        port=params['port'],
        password=params['db_password'],
        db=params['db_name'],
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor  # 设置游标类型为字典游标，以返回字典形式的查询结果
    )
    return connection

# def close_connection(connection):
#     # 关闭数据库连接
#     connection.close()

def databases_selet(connection, query, params=None): #数据库>>指令
    # 执行数据库查询操作
    cursor = connection.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()  # 获取查询结果并以字典列表的形式返回
    cursor.close()
    return result


def databases_insert(connection, insert_query, data):
    # 执行数据库插入操作
    cursor = connection.cursor()

    # Insert the data into the database
    cursor.execute(insert_query, data)

    connection.commit()  # 提交事务
    cursor.close()

def insert_data_to_database(connection, school_name, data_columns, data_values):
    # 构建插入查询语句，包括所有列
    insert_query = f'INSERT INTO {school_name} ({", ".join(data_columns)}) ' \
                   f'VALUES ({", ".join(["%s"] * len(data_columns))})'

    try:
        with connection.cursor() as cursor:
            # 插入数据
            for data_row in data_values:
                cursor.execute(insert_query, data_row)

        # 提交更改
        connection.commit()

    finally:
        # 不在函数内关闭连接
        pass


def update_data_in_database(connection, table_name, data_columns, data_values):
    """
    更新数据库中的数据。

    Args:
        connection: 数据库连接对象。
        table_name: 要更新的表的名称。
        data_columns: 列名的列表，用于确定要更新的列。
        data_values: 包含多行数据的列表，每行数据与列名一一对应。
    """
    try:
        with connection.cursor() as cursor:
            # 构建完整的 UPDATE 查询
            update_query = f'UPDATE {table_name} SET '

            # 构建 SET 子句，将每列名与数据值组合
            for col in data_columns:
                update_query += f'{col} = %s, '
            # 去掉最后一个逗号和空格
            update_query = update_query[:-2]

            # 执行更新操作，传递参数作为元组
            cursor.executemany(update_query, data_values)

        # 提交更改
        connection.commit()

    finally:
        # 不需要在函数内关闭连接
        pass

if __name__ == '__main__':
# 连接到数据库
    connection = connect_to_database(databases_params)
    print(connection)  # 打印连接对象，可以用于执行数据库操作
# sql_1= 'select * from test'
#
# FT_1 = databases_selet(connection,sql_1)
# print(FT_1)