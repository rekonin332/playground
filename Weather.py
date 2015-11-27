from urllib.request import urlopen
def myWeather():
	with urlopen('http://flash.weather.com.cn/wmaps/xml/china.xml') as res:
		for line in res:
		    line = line.decode('utf-8')
		    if 'chongqing' in line or 'fujian' in line or 'sichuan' in line:
			    print(line)
