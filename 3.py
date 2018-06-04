import urllib.request
import urllib.parse

kw = '日本'
data = {
	'wd': kw
}

data = urllib.parse.urlencode(data)

url = 'https://www.baidu.com/s?' + data

headers = {
	'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

with open('haha.html', 'wb') as fp:
	fp.write(response.read())