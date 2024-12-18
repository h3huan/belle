import numpy as np
import matplotlib.pyplot as plt

fis = np.array([[1,2,3,4,5,6,7,8,9],
               [11,12,13,14,15,16,17,18,19],
               [21,22,23, 24, 25, 26, 27, 28,29]])

print(fis[1][2])
# x1 = np.random.normal(0, 1, 100000000)
#
# plt.figure(figsize=(10, 10), dpi=300)
#
# plt.hist(x=x1, bins=10000)
#
# plt.show()

al = np.array([[44,334,3445],
               [34,24,543]])
bl = np.array([[44,334,34],
               [45,53,234]])
lv = np.cross(al,bl)
print(lv)