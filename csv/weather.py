from matplotlib import pyplot as plt
import csv
from datetime import datetime 

filename="sitka_weather_07-2014.csv"
with open(filename) as f:
    reader=csv.reader(f)
    head_row=next(reader)
    print(head_row)
    #打印数据头
    for index,value in enumerate(head_row):
        print(index,value)

    #只提取最高温度
    high=[]
    low=[]
    dates=[]
    for t  in reader:
        maxt=int(t[1])
        high.append(maxt)
        lowt=int(t[3])
        low.append(lowt)
        date=datetime.strptime(t[0],"%Y-%m-%d")
        dates.append(date)

    #绘制图表
    fig=plt.figure(figsize=(10,6))
    plt.title("High Temperatures-2014",fontsize=20)
    plt.xlabel('dats',fontsize=13)
    plt.ylabel("Temperature",fontsize=13)
    #自动倾斜日期
    fig.autofmt_xdate()
    plt.plot(dates,high,c='red')
    plt.plot(dates,low,c='blue')
    plt.fill_between(dates,high,low,facecolor='blue',alpha=0.15)




    plt.show()



