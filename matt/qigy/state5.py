# stuid = {}
# stuscore = {}
# course = set()
#
# while True:
#     line = input()
#     if line == 'x':
#         break
#     words = line.split()
#     if words[-1].isnumeric():
#         score = stuscore.get(words[0])
#         if score == None:
#             score = {}
#         score[words[1]] = words[2]
#         stuscore[words[0]] = score
#         course.add(words[1])
#     else:
#         stuid[words[0]] = words[1]
#
# # 列出全部课程
# coursename = list(course)
#
# print(',', end='')
# for name in coursename:
#     print(','+name, end='')
# print()
#
# for id in stuid.keys():
#     print(id + ',' + stuid[id], end='')
#     score = stuscore[id]
#     sum = 0
#     cnt = 0
#     for name in coursename:
#         print(',',end='')
#         if name in score:
#             print(score[name], end='')
#             sum += int(score[name])
#             cnt += 1
#     print(','+str(int(sum/cnt)))

def graydays():
    vote = input("What is all vote? ")
    team2 = {6, 7, 8, 9, 10}
    vlist = list(map(int, vote.split(',')))
    voteset = set(vlist)

    return team2 - voteset
def gray(lis):
    return list(map(int, lis.split(',')))
def xi(lis):
    return len(lis) == len(set(lis))

pause = xi(gray(input('What is your')))
print(pause)