# a = [1,2,3,4,5,6,7,8,9]
#
# for i in range(len(a)):
#     print('*'*a[i])

def find_departed():
    people = list(range(1, 31))  # 编号从 1 到 30
    departed = []  # 存储离开人员的编号
    index = 1  # 当前报数的索引
    print(people)

    while len(departed) < 10:  # 直到有 10 人离开
        i = 0  # 重置内部索引
        while i < len(people):  # 遍历当前的人员列表
            print('baoshu',index)
            if index == 9:  # 报数到 10
                departed.append(people[i])  # 加入离开列表
                people.pop(i)  # 移除该人员
                index = 1  # 重置报数
                i -= 1  # 调整索引，避免跳过元素
            else:
                index += 1
            i += 1  # 正常前进索引

    return departed


# 输出离开的前 10 人编号
# print("离开的前10人编号:", find_departed())


