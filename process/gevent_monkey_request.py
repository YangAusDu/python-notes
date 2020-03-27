import time, gevent
from gevent import monkey
import urllib.request

monkey.patch_all()

def download(url):
    response = urllib.request.urlopen(url)
    content = response.read
    print("{} data has been downloaded".format(url))


if __name__ == "__main__":
    url = ["http://www.baidu.com", "http://www.126.com", "http://www.qq.com"]
    
    g0 = gevent.spawn(download,url[0])
    g1 = gevent.spawn(download,url[1])
    g2 = gevent.spawn(download,url[2])

    gevent.joinall([g0,g1,g2])


