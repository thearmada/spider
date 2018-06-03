import urllib.request

url = 'http://www.baidu.com/'
response = urllib.request.urlopen(url = url)
ret = response.read()