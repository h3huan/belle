import random

import matplotlib.pyplot as plt


plt.figure(figsize=(8,8), dpi=300)

x = range(60)
y = [random.uniform(13,20) for i in x]
y2= [random.uniform(12, 25) for i in x]

plt.plot(x, y, label='homostella', linestyle='-.')
plt.plot(x, y2, label='poison', linestyle='--')

y_tick = range(40)
x_tick_l = ['xi{}e'.format(i) for i in x]
plt.yticks(y_tick[::5])
plt.xticks(x[::5], x_tick_l[::5])

plt.title('octopus')
plt.grid(True, alpha=0.3)

plt.legend()

plt.show()