import matplotlib.pyplot as plt

from rand_walk import RandWalk


active=True
while active:
    
    rw=RandWalk(10000)
    rw.fill_walk()

    #设置窗口大小
    x,y=tuple(input("please enter number to control the size of figure :").split())
    plt.figure(figsize=(int(x),int(y)))
#    plt.scatter(rw.xvalues,rw.yvalues,s=5,edgecolor='none')

    #使用cmap
    num_points=list(range(rw.num_points))
    plt.scatter(rw.xvalues,rw.yvalues,s=5,c=num_points,edgecolor='none',cmap=plt.cm.Blues)

    #标记起点和终点
    plt.scatter(0,0,s=15,c='red',edgecolor='none')
    plt.scatter(rw.xvalues[-1],rw.yvalues[-1],c='red',edgecolor='none')

    #去掉坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    plt.show()
    messag=input("Do you want to continue('q' to quit):")
    if messag=='q':
        break

