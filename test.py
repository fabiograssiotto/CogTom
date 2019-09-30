import pandas as pd

df = pd.DataFrame(columns = ['A','B','C'])
df.set_index(keys = ['A', 'B'], drop = False, inplace = True)

l1 = [[1,2,3], [1,3,4]]
d1 = pd.DataFrame(l1, columns = ['A','B','C'])
d1.set_index(keys = ['A', 'B'], drop = False, inplace = True)

l2 = [[1,2,10], [1,3,20]]
d2 = pd.DataFrame(l2, columns = ['A','B','C'])
d2.set_index(keys = ['A', 'B'], drop = False, inplace = True)

l3 = [[1,2,10], [1,3,20], [2,1,10]]
d3 = pd.DataFrame(l3, columns = ['A','B','C'])
d3.set_index(keys = ['A', 'B'], drop = False, inplace = True)

df = df.append(d1)