import matplotlib.pyplot as plt

from rand_walk import RandWalk


active=True
while active:
    
    rw=RandWalk(10000)
    rw.fill_walk()

    plt.scatter(rw.xvalues,rw.yvalues,s=5,edgecolor='none')
    plt.show()
    message=input("Do you want to continue('q' to quit):")
    if message=='q':
        active=False

