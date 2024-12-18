import pandas as pd

dat = pd.read_csv('./snakes.csv')

print(dat.head( ))
print('grayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
print(dat.iloc[:12,:1])
print('grayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

print(dat.sort_values(by=' Game Length', ascending=False))