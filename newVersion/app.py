#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import datetime
import time
from ZigbeeUART import *
from SVMTest import *
from saveToMysql import *
from uploadToSrv import *

IOSTIMEFORMAT = '%Y-%m-%d %X'	


#Items=[1,2,3,4,5,6,7,'2017-09-09 13:23:43','Normal']
#拼凑成Items的数据格式
def pvStatus(zig_data):
	status = zig_data[5] 
	label = zig_data[6]
	label = int(label[0])
	status_describe =["Normal","Open1","Open2","Short1","Short2","shadow1","shadow2"]
	falut =["first String","second String","third String"]
	if status!= 0 and label != 1:
	 	return status_describe[label] + "happend at the " + falut[status]
	return status_describe[label]
def upload(zig_data):
	station_id =1
	array_id = 1
	Current = zig_data[2]
	Voltage = zig_data[3]
	Power = zig_data[4]
	Temp = zig_data[0]
	Irr = zig_data[1]
	status_code = zig_data[5]
	status_label = zig_data[6]
	status_label = int(status_label[0])
	status_describe = pvStatus(zig_data)
	upload_time = zig_data[7]
	Items=[]
	Items.append(station_id)
	Items.append(array_id)
	Items.append(array_id)
	Items.append(Current)
	Items.append(Voltage)
	Items.append(Power)
	Items.append(Temp)
	Items.append(Irr)
	Items.append(status_label)
	Items.append(status_code)
	Items.append(status_describe)
	Items.append(upload_time)
	print '9999999'
	print Items
	return Items
#Items=['station_id','array_id','Current',
#'Voltage','Power','Temp','Irr',
#'upload_time','status_describe']
def loopUpload():
	#1.获取ZigBee串口数据
	zig_data = getZigBeeData()
	#2.解析数据，并进行训练，然后合并故障诊断结果
	label = svm_pvfault_detect(zig_data)
	zig_data.append(label)
	#存入数据库的字段（，，，date，lng，lat）
	curTime = time.strftime(IOSTIMEFORMAT,time.localtime());
	zig_data.append(curTime)
	zig_data.append('119.206783')
	zig_data.append('26.069738')
	#3.把合并后的结果存入数据库，并上传到监控中心网站
	#存入数据库的数据格式：[Date,Temp, Irr, Vol, Cur, Power,Status,Lng, Lat]
	StoreData(zig_data)
	Items = upload(zig_data)
	uploadToWeb(Items)
while(1):
	loopUpload()
	print 'waitting for 10 sencod'
	time.sleep(10)

