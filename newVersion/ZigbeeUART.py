#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import serial 
import re 
class ZigBeeData():
	def readSerial(self):
		sStr = 'Z'
		flag = 1
		try:
			ser = serial.Serial(port='/dev/ttyUSB0',baudrate=9600,parity=serial.PARITY_ODD,stopbits=serial.STOPBITS_ONE,bytesize=serial.SEVENBITS)
		except Exception,e:
			print('open serial failed.')
			exit(1)
		print("connected to: " + ser.portstr)
		while flag:
	    		line = ser.readline()
			try:		
				if line.index(sStr) == 43:
					flag = 0
					return line
			except Exception,e:
				pass
		ser.close()	
		#分离数据
	def splitPv_Message(self,ZigBee_data):
		array_param =[]
		PvMessage = re.split(',',ZigBee_data)
		#split data
		array_cur = float(PvMessage[1])+float(PvMessage[2])+float(PvMessage[3])
		array_vol = float(PvMessage[4])
		array_Temp = float(PvMessage[5])
		array_Irr = float(PvMessage[6])
		array_cur = float('%.2f' %array_cur)
		array_vol = float('%.2f' %array_vol)
		array_power =  float('%.2f' % (array_vol * array_cur))
		array_Temp = float('%.2f' %array_Temp)
		array_Irr = float('%.2f' %array_Irr)
		s = PvMessage[7];
		array_status = int(s[0])
		array_param.append(array_Temp)
		array_param.append(array_Irr)
		array_param.append(array_cur)
		array_param.append(array_vol)
		array_param.append(array_power)
		array_param.append(array_status)
		return array_param

#rmc ='$PV,A,17.8,84,90.6,1.393'
def getZigBeeData():
	pvdata = ZigBeeData()
	rmc = pvdata.readSerial()
	print rmc
	array_msg = pvdata.splitPv_Message(rmc)
	return array_msg
	#ZigMessage = pvdata.parsePvMessage(splitMessage)
#	print ZigMessage
	#return ZigMessage
#print msg
