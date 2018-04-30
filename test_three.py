'''
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

'''

import test_two
import pymysql

def mysql():
	db = pymysql.connect("localhost","root","yc7171","Python_one" )
	'''
	root: 用户名,
	yc7171: 用户密码,
	Python_one: 数据库名.
	'''
	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	back_random_code = test_two.generate(5)
	for i in back_random_code:
		sql = "insert into Random_code (random_code) VALUES ('%s')" %(i)
		cursor.execute(sql)
		db.commit()
	db.close() # 关闭链接

mysql()