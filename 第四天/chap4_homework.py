import requests
from bs4 import BeautifulSoup
import threading,queue

lock = threading.Lock()
start_page = "http://www.163.com"  #定义一个首页
domain = "163.com"  #定义一个域名
url_queue = queue.Queue()   #定义一个队列
seen = set()  #集合 集合中的元素不能重复的，此处的目的是去重
seen.add(start_page)
url_queue.put(start_page)

def extract_urls(url):
    urls = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")

    for e in soup.findAll('a'):
        print(e.attrs)  #e.attrs返回标签的属性，以字典形式返回所有值
        url = e.attrs.get('href','#')  #如果获取的a标签中href没有值，就给默认值#
        urls.append(url)
    return urls

def producer():
    while True:
        if not url_queue.empty():
            current_url = url_queue.get()
            print(current_url)
            for next_url in extract_urls(current_url):
                if next_url not in seen and domain in next_url:  # 去重，并且域名是163.com
                    seen.add(next_url)
                    url_queue.put(next_url)
                else:
                    break

def consumer():
    while True:
        try:
            data =url_queue.get(block=False)
        except queue.Empty:
            break
        with lock:
            print(data)

if __name__=="__main__":
    producerthreads = []
    consumerthreads = []
    for i in range(3):
        t = threading.Thread(target=producer)
        producerthreads.append(t)
        t.start()
    for i in range(3):
        t = threading.Thread(target=consumer)
        consumerthreads.append(t)
        t.start()

    for t in producerthreads:
        t.join()
    for t in consumerthreads:
        t.join()
