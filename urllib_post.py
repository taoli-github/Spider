# _*_ coding:utf-8 _*_

import urllib.request as request
import urllib.error as url_err
import urllib.parse as parser
import config


if __name__ == '__main__':
    url = 'http://www.iqianyue.com/mypost'
    data = parser.urlencode({'name':'litao', 'pass': '123456'}).encode('utf-8')
    req = request.Request(url, data)

    with request.urlopen(req, timeout=5) as f:
        print(f.read().decode('utf-8'))
