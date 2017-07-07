#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests
url='http://192.168.1.102:9999/postPVData'
CLIENT_ID = 1
API_TOKEN = 'jRaNjyxGaepb0tEHFSlYl'
API_token ={'client_id':1,'api_token':API_TOKEN}
headers = {'content-type': 'application/json'}
def addWord(data,key,value): 
  	data[key]=value
def auth(API_token):
	token = json.dumps(API_token)
	res = requests.post(url,data=token,headers=headers)
	return res.text
def upload(data):
	data = json.dumps(data)
	headers = {'content-type': 'application/json'}
	res = requests.post(url,data=data,headers=headers)
	res = res.text.encode('utf-8')
	return eval(res)
def addItems(Items):
	data={}
	addWord(data,'station_id',Items[0])
	addWord(data,'array_id',Items[1])
	addWord(data,'client_id',CLIENT_ID )
	addWord(data,'Current',Items[3])
	addWord(data,'Voltage',Items[4])
	addWord(data,'Power',Items[5])
	addWord(data,'Temp',Items[6])
	addWord(data,'Irr',Items[7])
	addWord(data,'status_code',Items[8])
	addWord(data,'status_label',Items[9])
	addWord(data,'status_describe',Items[10])
	addWord(data,'upload_time',Items[11])
	return data
	#Items=[1,2,3,4,5,6,7,'2017-09-09 13:23:43','Normal']
def uploadToWeb(Items):
	data = addItems(Items)
	print data
	res = requests.post(url,data=json.dumps(data),headers=headers)
	#res = res.text.encode('utf-8')
	print res.text
