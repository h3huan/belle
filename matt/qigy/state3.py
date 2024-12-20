# inp = input('your nums')
#
# lista = list(map(int, inp.split()))
# print(lista)
#
#
# a = sum(lista)/len(lista)
# grid=[]
#
# for i in range(0, len(lista)):
#     if lista[i] > a:
#         grid.append(lista[i])
#     else:
#         continue
# print(grid)

def cod():
    while True:  # 无限循环，直到输入合法
        gj = input('请输入18位身份证号码: ')

        # 检查输入是否合法
        if len(gj) != 18:
            print("错误: 身份证号码长度必须为18位。")
            continue
        if not gj[:17].isdigit():
            print("错误: 前17位必须是数字。")
            continue
        if gj[17] not in '0123456789X':
            print("错误: 最后一位必须是数字或'X'。")
            continue

        # 如果输入合法
        print("身份证号码格式正确!")
        return gj


def fin():
    cod()
    avgi = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    mi = [1,0,'X',9,8,7,6,5,4,3,2]
    for i in range(0,len(cod())):
        z = 0
        z += cod()[i]*avgi[i]
    n = z % 11
    if n==mi[n]:
        print('right')
    else:
        print('wrong')

fin()