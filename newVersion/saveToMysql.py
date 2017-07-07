#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
class Mysql_Save():
	def getDataBaseVersion(self):
		# 打开数据库连接
		try:
			db = MySQLdb.connect("localhost","root","111","mysql" )
			# 使用cursor()方法获取操作游标 
			cursor = db.cursor()
			# 使用execute方法执行SQL语句
			cursor.execute("SELECT VERSION()")
			# 使用 fetchone() 方法获取一条数据库。
			data = cursor.fetchone()
			print "Database version : %s " % data
			# 关闭数据库连接
			db.close()
		except Exception,e:
			pass
	def mysql_Connect(self):
		try:
			# 打开数据库连接
			db = MySQLdb.connect("localhost","root","111","test" )
			# 使用cursor()方法获取操作游标 
			cursor = db.cursor()
			# 如果数据表已经存在使用 execute() 方法删除表。
			#cursor.execute("DROP TABLE IF EXISTS PVData")	
			# 创建数据表SQL语句
			sql = """CREATE TABLE PVArrayData (
			Date CHAR(100), 
			Lng  CHAR(20),
			Lat  CHAR(20),
			Temp CHAR(20),
			Irr  CHAR(20),
			Vol CHAR(20),
			Cur CHAR(20),
			Power CHAR(20),
			Label CHAR(10),
			Status CHAR(10),
			PRIMARY KEY (`date`)  
			  )"""
			cursor.execute(sql)#提交到数据库执行
		   	db.commit()
			#关闭数据库连接
			db.close()
		except Exception,e:
			print 'something unexpect error happen!'
			pass
	def insertData(self,Zigbee_Data):
		print '---------------'
		try:
			#打开数据库连接
			db = MySQLdb.connect("localhost","root","111","test" )
			print '---------**-----'
		except Exception,e:
			print 'can not connect to mysql!'
		#使用cursor()方法获取操作游标 
		cursor = db.cursor()
		print '---------&&&&--'
		print 'ronghe de data',Zigbee_Data
		sql = "INSERT INTO PVArrayData(Temp, Irr, Cur,Vol, Power,Status,Label,Date,Lng, Lat) VALUES ('%s', '%s', '%s','%s','%s', '%s','%s', '%s', '%s','%s')" %(Zigbee_Data[0], Zigbee_Data[1],Zigbee_Data[2], Zigbee_Data[3],Zigbee_Data[4],Zigbee_Data[5],Zigbee_Data[6],Zigbee_Data[7],Zigbee_Data[8],Zigbee_Data[9])
		try:	   
			#执行sql语句
		   	cursor.execute(sql)
		   #提交到数据库执行
		   	db.commit()
		except Exception,e:
			print 'something unexpect error happen!'
 			#发生错误时回滚
		   	db.rollback()
			print 'error'
			pass
		# 关闭数据库连接
		db.close()
def StoreData(Zigbee_Data):
		m_nMysql = Mysql_Save()
		#m_nMysql.mysql_Connect()
		print '*******------'
		m_nMysql.insertData(Zigbee_Data)

