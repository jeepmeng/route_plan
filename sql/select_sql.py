from sql_utils import *



connection = test_connect()
# cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor = connection.cursor()
#查看对应表的key是否有值
sql = "select sc_info.* from school_info sc_info"


cursor.execute(sql)

data=cursor.fetchall()
print(data)
# connection.commit()
cursor.close()
connection.close()