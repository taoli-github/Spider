# _*_ coding:utf-8 _*_

import urllib.request as request
import urllib.error as url_err
import config


if __name__ == '__main__':
    url = 'http://www.python.org'

    req = request.Request(url)
    req.add_header('User-Agent', config.user_agent)
    try:
        with request.urlopen(req, timeout=5) as f:
            print(f.read().decode('utf-8'))
    except url_err.URLError as e:
        # print(e.code)
        print(e.reason)
    except url_err.HTTPError as e:
        print(e.reason)
