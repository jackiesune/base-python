#plots.py

#matplotlib 中的折线图
import matplotlib.pyplot as plt

listx=[1,2,3,4,5,6]
listy=[value**2 for value in listx]
#设置xy轴及标题
plt.title("the squares",fontsize=24)
plt.xlabel("x axis",fontsize=15)
plt.ylabel("y axis",fontsize=15)
plt.plot(listx,listy,linewidth=3)
plt.tick_params(axis="both",labelsize=10)

plt.show()

