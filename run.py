import matplotlib.pyplot as plt

from rand_walk import RandWalk

rw=RandWalk()
rw.fill_walk()

plt.scatter(rw.xvalues,rw.yvalues,s=5,edgecolor='none')
plt.show()
