# -*- coding: utf-8 -*-

url_black = 'https://www.jdsports.ie/product/adidas-originals-superstar/016655_jdsportsie/'
url_gray = 'https://www.jdsports.ie/product/white-adidas-originals-superstar/103225_jdsportsie/'

import requests
import re
import keyring
import smtplib
from email.mime.text import MIMEText


'''
Host: www.jdsports.ie
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: language=en; mt.v=2.1381472200.1555269700987; 49746=; gdprsettings={"performance":true,"remarketing":true,"social":true}; crl8.fpcuid=de11585f-4c97-476b-84c3-3eb03f83e6a2; _ga=GA1.2.1876046275.1555269707; cto_lwid=cb3d231d-af83-4295-aa7f-ccd977fd9cfa; _gcl_au=1.1.820513888.1555269707; _fbp=fb.1.1555269707051.1730463024; cto_idcpy=ae59c8ab-1868-4daf-86e2-9f8361d955d3; _scid=0de6043c-3ddb-4809-beeb-6c97e0ae35d7; session.ID=BB070F40C666401C85865D931D2B8D2F; session.present=1; mt.menCategoryVisits=3; mt.assumedGender=man; _taggstar_vid=a1777af4-5eea-11e9-a40b-e5368b85050e; __atuvc=7%7C16%2C0%7C17%2C0%7C18%2C13%7C19; mt.favouriteBrand=adidas_originals; mt.brandVisits=%7B%22adidas_originals%22:%7B%22brand%22:%22adidas_originals%22,%22timesVisited%22:20%7D,%22adidas%22:%7B%22brand%22:%22adidas%22,%22timesVisited%22:1%7D,%22adidas_skateboarding%22:%7B%22brand%22:%22adidas_skateboarding%22,%22timesVisited%22:1%7D%7D; trackingID=841B341D8B5C4333B50DE728E09C23A2; akavpau_VP1=1557343399~id=38e1f004fbbd19337a4cdb9c83d7df20; sc.ASP.NET_SESSIONID=lyxfknoidrdgl3wxjnjqoat5; ak_bmsc=EEB094D055F7594730F649CD8F172FD858DDDE3132180000EC20D35C59E0C111~pl4Etv3ZTZY0/lymLfn4umrtoq9EVXg7l7JXp7I/PvIlG/l1NKl2RPG0/TDZgncjEc8FpUG5wwXw+8pAod0H3tmT4iZ6ZUjBtJ+L5nwrFJ21hwrv0dDJRwc0PkPNej4Q+cxn2yDiqQGwnOJK5xGgd3Hx3WLfq0WFNq7YriHQo/bntYyGAoeA7/zcOUnkqFrx2kf9DfbCnwjjpNxso5XnV3dhFiDJP+S94dwD+im8OR4YmKFFLQofmHnLwd9uu//zE3; bm_sv=4D43EE8B96E8C92A565D8B8258E38D55~gJdTInIjrpygHme16jfGeFuw9nfrQNhXBg9lYNKusnmTKZqPv1sjFERI8nzCObPy48Gj2TQH4l6a5NzPe1sITp/o+lGdM5kaQqj4Uy5dNxIdFkgVrA3HQIO5ZNAQ+laICHVM0Pd2ncUohQi1Zsqw400uZGlfXvmbJ1MDFDNN3no=; _gid=GA1.2.391115182.1557340515; _taggstar_ses=88d55091-71c4-11e9-b124-3bf2b2a8b5f6; __atuvs=5cd329211475b7a2003
Upgrade-Insecure-Requests: 1
If-Modified-Since: Wed, 08 May 2019 19:18:16 GMT
If-None-Match: 26ab550dc51dcc90379c7db50c6bcb10
Cache-Control: max-age=0
'''

mail_host = 'smtp.163.com'
username = 'jiajia330013@163.com'
service = '163'
password = keyring.get_password(service,username)

def get_password(service,username):
	return keyring.get_password(service,username)

sender = 'jiajia330013@163.com'
receiver = '284759181@qq.com'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:66.0) Gecko/20100101 Firefox/66.0'}

def snd_mail(username,password,contents):

	#设置email信息
	#邮件内容设置
	message = MIMEText(contents,'plain','utf-8')
	#邮件主题       
	message['Subject'] = 'Adidas Superstar query result'
	#发送方信息
	message['From'] = sender
	#接受方信息     
	message['To'] = receiver[0]
	try:
		smtpObj = smtplib.SMTP()
		#连接到服务器
		smtpObj.connect(mail_host,25)
		#登录到服务器
		smtpObj.login(username,password)
		#发送
		smtpObj.sendmail(sender,receiver,message.as_string())
		#退出
		smtpObj.quit() 
		print('success')
	except smtplib.SMTPException as e:
	    print('error',e) #打印错误

def parse_url(url,headers):
	data = requests.get(url, headers = headers)

	reg_price = r'itemprop="price" content="(.+?)">'
	re.compile(reg_price)
	price_list = re.findall(reg_price,str(data.content))
	print(price_list)
	if float(price_list[0]) < 70.00:
		contents = 'less than 70'
		# print(contents)
	else:
		contents = ("equal or greater than 70, the price is %f" % float(price_list[0])) 
		# print(contents)
	return contents

if __name__ == '__main__':
	password = get_password(service,username)
	contents = parse_url(url_gray,headers)
	snd_mail(username,password,contents)
