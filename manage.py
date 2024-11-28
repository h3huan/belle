from student import *
class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()
        while True:

            self.show_menu()

            menu_num = int(input('question??'))

            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        print('you jb who')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')
    def add_student(self):
        name = input('u jb who')
        age = input('R u transgender?')
        tel = input('vx？')

        stu = Student(name, age, tel)
        self.student_list.append(stu)

        print(self.student_list)
        print(stu)

    def del_student(self):
        del_name = input('誰かが殺す？')
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print('誰もいない')
        print(self.student_list)

    def modify_student(self):
        mod = input('life will change:')
        for i in self.student_list:
            i.name = input('6666666')
            i.gender = input('11')
            i.tel = input('？')
            print(f'你又被人骗了喔喔{i.name},整个世界变了{i.gender}，可能她的快乐来自于我的痛苦{i.tel}')
            break
        else:
            print('现在怎么办？')
    def search_student(self):
        search = input('今天一点都没多去琢磨')
        for i in self.student_list:
            if i.name == search:
                print(f'我已经把{i.name}这{i.gender}设置成不可见了，{i.tel}不删是因为纯粹信息的角度还有价值')
                break
            else:
                print('搞不到我就 2 年内不谈恋爱')

    def show_student(self):
        print('你的名字\t这\t识别方法是')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def save_student(self):
        # 1. 打开文件
        f = open('student.data', 'w')

        # 2. 文件写入数据
        # 2.1 [学员对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()
        print('done')

    def load_student(self):
        # 尝试以"r"模式打开数据文件，文件不存在则提示用户；文件存在（没有异常）则读取数据
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 1. 读取数据
            data = f.read()

            # 2. 文件中读取的数据都是字符串且字符串内部为字典数据，故需要转换数据类型再转换字典为对象后存储到学员列表
            new_list = eval(data)
            print(new_list)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            # 3. 关闭文件
            print('发生什么了？我不知道。')
            f.close()

