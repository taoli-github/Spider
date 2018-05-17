""" 代理 """
# _*_ coding:utf-8 _*_

import urllib.request as request


def main():
    use_proxy('219.246.33.240:8118', 'http://www.baidu.com')


def use_proxy(addr, url):
    proxy = request.ProxyHandler({'http': addr})
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    print(data)


if __name__ == '__main__':
    main()
