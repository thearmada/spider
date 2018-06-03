import urllib.request

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com/'
headers = {
	'User-Agent': 'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
}

request = urllib.request.Request(url=url)
request.add_header('User-Agent', 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0')
response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
