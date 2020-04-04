def add_record():
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    record = {}
    record['name'] = name
    record['phone'] =  phone
    return record

def query_record():
    """根据姓名或者id查询"""
    result = []
    while 1:
        choice = input("请输入查询方式:(1:id,2:姓名,q/Q:退出)")
        if choice == '1':
            id  = input("请输入查询的id:")
            for i in range(len(record_list)):
                if i == int(id)-1:
                    # 查询id从1开始
                    result.append(record_list[i])
            return result
        elif choice == '2':
            name = input("请输入要查询的姓名:")
            for record in record_list:
                if record['name'] == name:
                    result.append(record)
            return result
        elif choice.lower() == 'q':
            print("退出查询操作！")
            break
        else:
            print("输入有误，请重新输入查询操作！")


def change_record():
    """根据姓名或者id修改通讯录"""
    global record_list
    while 1:
        choice = input("请输入修改方式:(1:id,2:姓名,q/Q:退出)")
        if choice == '1':
            id  = input("请输入修改的id:")
            if int(id)-1 in range(len(record_list)):
                phone = input("请输入修改后的电话号码：")
                record_list[int(id)-1]['phone'] = phone
                return record_list[int(id)-1]
            else:
                print("找不到该id")
        elif choice == '2':
            name = input("请输入要修改人的姓名:")
            for record in record_list:
                if record['name'] == name:
                    print("要被修改的数据是：",record)
                    phone = input("请输入修改后的电话号码：")
                    record['phone'] = phone
                    return record
        elif choice.lower() == 'q':
            print("退出查询操作！")
            break
        else:
            print("输入有误，请重新输入查询操作！")

    return

def delete_record():
    """根据姓名或者id删除通讯录"""
    global record_list
    while 1:
        choice = input("请输入删除方式:(1:id,2:姓名,q/Q:退出)")
        if choice == '1':
            id = input("请输入删除的id:")
            if int(id) - 1 in range(len(record_list)):
                del_record = record_list.pop(int(id)-1)
                print("被删除的数据是：",del_record)
            else:
                print("找不到该id")
        elif choice == '2':
            name = input("请输入要删除人的姓名:")
            for i in range(len(record_list)):
                if record_list[i]['name'] == name:
                    del_record = record_list.pop(i)
                    print("被删除的数据是：", del_record)
        elif choice.lower() == 'q':
            print("退出删除操作！")
            break
        else:
            print("输入有误，请重新输入查询操作！")

if __name__ == "__main__":
    menu = """
    通讯录
    1.添加
    2.查找
    3.删除
    4.修改
    5.退出      
    """
    print(menu)
    record_list = []
    while 1:
        oper = input("请输入操作：")
        if oper == '1':
            record = add_record()
            record_list.append(record)
            print("添加成功",record)
            print(record_list)
        elif oper == '2':
            result = query_record()
            if result == []:
                print("没有找到")
            else:
                print(result)
        elif oper == '3':
            result = change_record()
            if result is None:
                print("修改失败")
            else:
                print(result)
        elif oper == '4':
            delete_record()
        elif oper == '5':
            print("退出！")
            break
        else:
            print("输入有误,请重新输入！")
    print("通讯录最后的结果：",record_list)

