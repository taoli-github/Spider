""" 输出打印日志 """
import urllib.request as request


httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPHandler(debuglevel=1)

opener = request.build_opener(httphd, httpshd)
request.install_opener(opener)
print(request.urlopen('http://www.taobao.com'))
