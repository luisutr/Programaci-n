import pandas as pd
import matplotlib.pyplot as plt

df = (pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
}))



print(df)


# columnas
df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
#plt.show()

df[['age']].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=0.8)
#plt.show()

# a simple line plot
df.plot(kind='bar',x='name',y='age')
#plt.show()

# Line plot with multiple '
ax = plt.gca()
#plt.show()

df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)
#plt.show()

df.plot(kind='bar',x='name',y='age')
#plt.show()

# the plot gets saved to 'output.png'
plt.savefig('output.png')

#barras por grupo
df.groupby('state')['name'].nunique().plot(kind='bar')
#plt.show()

#Stacked bar plot with two-level group by
df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)
#plt.show()

df.groupby(['gender','state']).size().unstack().plot(kind='bar',stacked=True)
#plt.show()


