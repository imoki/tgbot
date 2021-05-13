import socket
import socks
import requests
import sys

url = 'https://api.telegram.org/xxxxtokenxxxxx/'
getupdates = 'getUpdates'
sendmessage = 'sendMessage'
txtpath = 'ssr-link.txt'
chat_id = 'xxxxxx'
hk = '&c=HK'

def sendmssg(text):
	text = text.strip()
	sendurl = url + sendmessage
	data ={'chat_id':chat_id, 'text':text}
	print("[+] 发送中...	", text)
	#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
	#socket.socket = socks.socksocket
	try:
		r = requests.post(sendurl, data)
		print("[+] 发送成功！")
	except:
		print("[-] 发送失败")

# 文件内一行一行的发
def sendby2bytxt():
	f = open(txtpath, 'r+', encoding='utf-8')
	textlines = f.readlines()
	for textline in textlines:
		sendmssg(textline)
	f.close()

# 文件内一行一行的发，发送指定行数
def sendby2bylinetxt(line):
	f = open(txtpath, 'r+', encoding='utf-8')
	textlines = f.readlines()
	i=0
	for textline in textlines:
		if i < int(line):
			sendmssg(textline)
		else:
			break
		i = i+1
	f.close()

# 整个文件的内容
def sendtxt():
	f = open(txtpath, 'r+', encoding='utf-8')
	textlines = f.readlines()
	f.close()
	sendurl = url + sendmessage
	strtext = ''.join(textlines)
	data ={'chat_id':chat_id, 'text':strtext}
	print("[+] 发送中...\n", strtext)
	try:
		r = requests.post(sendurl, data)
		print("[+] 发送成功！")
	except:
		print("[-] 发送失败")

# 整个文件的内容,前几行
def sendlinetxt(line):
	f = open(txtpath, 'r+', encoding='utf-8')
	textlist = f.readlines()
	textlines = []
	i = 0
	for i in range(0, int(line)):
		try:
			textlines.append(textlist[i])
			i = i+1
		except:
			break
	f.close()
	sendurl = url + sendmessage
	strtext = ''.join(textlines)
	data ={'chat_id':chat_id, 'text':strtext}
	print("[+] 发送中...\n", strtext)
	try:
		r = requests.post(sendurl, data)
		print("[+] 发送成功！")
	except:
		print("[-] 发送失败")

if __name__ == "__main__":
	#sendtxt()
	sendlinetxt(5)
	'''
	if len(sys.argv) != 2:
		print("Usage: python " + sys.argv[0] + " message")
	else:
		sendmssg(sys.argv[1])
	'''