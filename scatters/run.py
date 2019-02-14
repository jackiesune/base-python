import matplotlib.pyplot as plt

from rand_walk import RandWalk


active=True
while active:
    
    rw=RandWalk(10000)
    rw.fill_walk()

    plt.scatter(rw.xvalues,rw.yvalues,s=5,edgecolor='none')
    #去掉坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    plt.show()
    message=input("Do you want to continue('q' to quit):")
    if message=='q':
        active=False

