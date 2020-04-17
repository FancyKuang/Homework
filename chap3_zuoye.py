
# 作业1: 使用多线程写一个并发http，get请求的程序，
# 可设置并发数和请求总数，返回请求状态码

import threading
import requests

count = 10
url = "https://www.baidu.com"
numthreads = 20
def httprequest(url):
    for i in range(count):
        r = requests.get(url)
        print(r.status_code)

if __name__ == "__main__":
    threads = []
    for i in range(numthreads):
        t = threading.Thread(target=httprequest,args=(url,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()