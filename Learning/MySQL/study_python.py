import pymysql

# 连接数据库
db = pymysql.connect(
    user='root',
    password='Closer42954856',
    port=3306,
    host='localhost',
    database='mrsoft'
)

# 创建游标对象
cursor = db.cursor()

# 执行SQL语句
cursor.execute('DROP TABLE IF EXISTS books')

# 使用预处理语句创建表
sql = """
CREATE TABLE books(
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  category varchar(50) NOT NULL,
  price decimal(10, 2) DEFAULT NULL,
  publish_time date DEFAULT NULL,
  PRIMARY KEY(id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)

# 获取单条数据
""" data = cursor.fetchone()
print("Database version: %s " % data) """

# 关闭数据库连接
db.close()
