import base64
import json
import requests
from itertools import islice
import os

sspath = 'tmp'
sslinktmp = 'linktmp'

def ss(sslink):
	with open(sslinktmp,'r',encoding='utf-8') as fa:
		for ssline in islice(fa, 1, None):
			ssline = ssline.strip()
			if len(ssline) > 100:
				data = json.loads(ssline)
				passcipher = data['cipher'] + r":" + data['password']
				b_passcipher = passcipher.encode('utf-8')
				passbase64 = base64.b64encode(b_passcipher).decode('utf-8')
				ss = r"ss://" + passbase64 + '@' + str(data['server']) + r':' + str(data['port'])
				with open(sslink,'a+',encoding='utf-8') as f:
					f.write(ss + '\n')
	f.close()
	fa.close()

def ssr(sslink):
	with open(sslinktmp,'r',encoding='utf-8') as fa:
		for ssline in islice(fa, 1, None):
			ssline = ssline.strip()
			if len(ssline) > 100:
				data = json.loads(ssline)
				b_pass = data['password'].encode('utf-8')
				passbase64 = base64.b64encode(b_pass).decode('utf-8')
				str_ssr = data['server'] + ":" + str(data['port']) + ":" + data['protocol'] + ":" + data['cipher'] + ":" + data['obfs'] + ":" + passbase64
				b_ssr = str_ssr.encode('utf-8')
				ssrbase64 = base64.b64encode(b_ssr).decode('utf-8')
				ssr = r"ssr://" + ssrbase64
				with open(sslink,'a+',encoding='utf-8') as f:
					f.write(ssr + '\n')
	f.close()
	fa.close()
	
def link(sslink, type):
	with open(sslinktmp,'r',encoding='utf-8') as fa:
		for ssline in islice(fa, 1, None):
			ssline = ssline.strip()
			if len(ssline) > 100:
				data = json.loads(ssline)
				if type == 'ss':
					passcipher = data['cipher'] + r":" + data['password']
					b_passcipher = passcipher.encode('utf-8')
					passbase64 = base64.b64encode(b_passcipher).decode('utf-8')
					ss = r"ss://" + passbase64 + '@' + str(data['server']) + r':' + str(data['port'])
					with open(sslink,'a+',encoding='utf-8') as f:
						f.write(ss + '\n')
				elif type == 'ssr':
					b_pass = data['password'].encode('utf-8')
					passbase64 = base64.b64encode(b_pass).decode('utf-8')
					str_ssr = data['server'] + ":" + str(data['port']) + ":" + data['protocol'] + ":" + data['cipher'] + ":" + data['obfs'] + ":" + passbase64
					b_ssr = str_ssr.encode('utf-8')
					ssrbase64 = base64.b64encode(b_ssr).decode('utf-8')
					ssr = r"ssr://" + ssrbase64
					with open(sslink,'a+',encoding='utf-8') as f:
						f.write(ssr + '\n')
	f.close()
	fa.close()

def repurl(url):
	i = 0
	while i < 3:
		try:
			reply = requests.get(url, timeout=5).text
			return reply
		except requests.exceptions.RequestException:
			i += 1

if __name__ == '__main__':
	'''
	print("TYPE : ss,ssr")
	type = input("Please input type:")
	'''
	type = 'ssr'
	type = type.strip()
	print('[+] WATING...')
	
	#清空临时文件
	with open(sspath, 'w' , encoding = 'utf-8') as f:
		f.write('')
	f.close()
	with open(sslinktmp, 'w' , encoding = 'utf-8') as f:
		f.write('')
	f.close()
	
	#请求url
	url = 'https://xxxxxxx/proxies?type=' + type
	reply = repurl(url)
	
	#清空存放的文件夹
	sslink = type + '.txt'
	with open(sslink, 'w' , encoding = 'utf-8') as f:
		f.write('')
	f.close()
	
	#写入请求
	with open(sspath, 'a+' , encoding = 'utf-8') as f:
		f.write(reply)
	f.close()
	with open(sspath,'r',encoding='utf-8') as f:
		sslines = f.readlines()
		for ssline in sslines:
			with open(sslinktmp,'a+',encoding='utf-8') as fa:
				fa.write(ssline[1:])
	fa.close()
	f.close()
	
	#写入合成的link
	link(sslink, type)

	#删除临时文件
	if os.path.exists(sspath):# 如果文件存在
		# 删除文件，可使用以下两种方法。
		os.remove(sspath)
		#os.unlink(path)
	else:
		pass
	if os.path.exists(sslinktmp):
		os.remove(sslinktmp)
	else:
		pass
	print("[+] FINISH!")