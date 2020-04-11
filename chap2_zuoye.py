# 1、递归函数列出所有文件 使用os.listdir os.isfile
def func(dirname):
    if os.path.isdir(dirname):
        for dir in os.listdir(dirname):
            dir = os.path.join(dirname,dir)
            if os.path.isfile(dir):
                print(dir)
            else:
                func(dir)

dirname = 'D:\PycharmProjects\workspace\cekai'
result = func(dirname)


# 2、练习找出单个目录中的最大文件
dirname = 'D:\PycharmProjects\workspace\cekai\chap2'
max = 0
for l in os.listdir(dirname):
    path = os.path.join(dirname, l)
    size = os.path.getsize(path)
    if size > max:
        max = size
        maxfile = path
print(maxfile,max)


# 3、练习找出目录树中的最大文件
dirname = 'D:\PycharmProjects\workspace\cekai'
g = os.walk(dirname)
max = 0

for path,dirnames,filenames in g:
    for file in filenames:
        pa = os.path.join(path,file)
        # print(pa)
        size = os.path.getsize(pa)
        if size > max:
            maxfile = pa
            max = size

print(maxfile,max)

# 4、装饰器的练习题：
def pertmit(func):
    def inner(username,password):
        if username == 'root' and password == '123456':
            print('你有权限')
            result = func(username,password)
            print(result)
        else:
            print("你没有权限")
    return inner

@pertmit
def test1(username,password):
    data1 = "123"
    return data1

@pertmit
def test2(username,password):
    data2 = "456"
    return data2

if __name__ =="__main__":
    test1('root','123456')
    test2('root', 'hhhh')