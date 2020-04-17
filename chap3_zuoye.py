
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
    
    
# 作业2：使用多进程写一个并发http，get请求的程序
# 可设置并发数和请求总数，返回请求状态码
from multiprocessing import Process
import requests
count = 5
numprocess = 10

def httprequest(url):
    for i in range(count):
        r = requests.get(url)
        print(r.status_code)

if __name__ =="__main__":
    url = "https://www.baidu.com"
    processes = []
    for i in range(numprocess):
        p = Process(target=httprequest,args=(url,))
        processes.append(p)
        p.daemon = True
        p.start()

    for p in processes:
        p.join()

作业3、get和post的区别
GET:
(1)、GET是通过URL提交数据，因此GET可提交的数据量就跟URL所能达到的最大长度有直接关系
(2)、实际上HTTP协议对URL长度是没有限制的；限制URL长度大多是浏览器或者服务器的配置参数

POST:
(1)、HTTP协议对POST也没有任何限制，一般是受服务器配置限制或者内存大小
(2)、PHP下可以修改php.conf的postmaxsize来设置POST的大小

GET和POST的安全性
(1)、GET是通过URL方式请求，可以直接看到，明文传输;与 POST 相比，GET 的安全性较差
(2)、POST是通过header请求，可以通过开发者工具或者抓包可以看到，同样也是明文的
(3)、GET请求会保存在浏览器历史记录中，还可能会保存在web的日志中

GET幂等/POST不幂等
幂等是指同一个请求方法执行多次和仅执行一次的效果完全相同。

(1)GET编码类型application/x-www-form-url，POST编码类型encodedapplication/x-www-form-urlencoded 或 multipart/form-data。为二进制数据使用多重编码。
(2)GET对数据长度有限制，当发送数据时，GET 方法向 URL 添加数据；URL 的长度是受限制的（URL 的最大长度是 2048 个字符）。POST无限制。
(3)GET只允许 ASCII 字符。POST没有限制。也允许二进制数据。

作业4、post请求有哪几种数据格式
(1)application/json：这是最常见的 json 格式：{"input1":"xxx","input2":"ooo","remember":false}
(2)application/x-www-form-urlencoded:浏览器的原生 form 表单，如果不设置 enctype 属性，那么最终就会application/x-www-form-urlencoded 方式提交数 ：input1=xxx&input2=ooo&remember=false
(3)multipart/form-data:
(4)text/xml:这种直接传的 xml 格式
