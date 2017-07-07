#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
from svmutil import *
import re
class svm_check_PVData():
	def train_svm(self):
		y, x = svm_read_problem('train9.txt')
		model = svm_train(y, x,'-c 100')
		svm_save_model('hhhh.txt',model)
	def check_svm(self,pvData):
		model = svm_load_model('hhhh.txt');
		yt, xt = svm_read_problem('yytest.txt')
		[p_label, acc, prob_test]=svm_predict(yt[0:],xt[0:], model)
		return p_label
	def format_convert(self,pvData):#V,I,G,T
		Vnom = float(pvData[0])/(21.5*6)
		Inom = float(pvData[1])/(6.03*3)
		Gnom = float(pvData[2])/1000
		Tnom = float(pvData[3])/100
		svm_data = '0'+' '+'1:'+str(Vnom)+' '+'2:'+str(Inom)+' '+'3:'+str(Gnom)+' '+'4:'+str(Tnom)
		return svm_data

def svm_pvfault_detect(data):
	data_check = svm_check_PVData()
	svm_data = data_check.format_convert(data)
	print(svm_data)
	write_test_data = open('yytest.txt', 'w')
	write_test_data.write(svm_data)
	write_test_data.close()
	label = data_check.check_svm(svm_data)
	return label

#zigbee_msg = [10.8,58.2,23.4,667]
#label = svm_pvfault_detect(zigbee_msg)
#print label
#a = 0.713798449612403
#b = 1.27280265339967
#c = 0.492
#d = 0.758
#data1 = str(a)+',' + str(b)+',' + str(c)+',' + str(d)
#data = re.split(',',data1)
#print data
#label = svm_pvfault_detect(data)
#print label
#data = ['0.713798449612403','1.27280265339967','0.492','0.758']
