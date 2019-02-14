import json
import pygal
import math

filename='btc_close_2017_requests.json'
with open(filename) as f:
    datas=json.load(f)
#提取信息
dates,months,weeks,weekdays,closes=[],[],[],[],[]
for ddict in datas:
    date=ddict['date']
    month=int(ddict['month'])
    week=int(ddict['week'])
    weekday=ddict['weekday']
    close=int(float(ddict['close']))
#   print("{} is nonth {} week {},{},the close price is {} RMB".format(date,month,week,weekday,close))
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)

#设置图表
N=20
first_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
first_chart.x_labels=dates
first_chart.x_title="日期"
first_chart.x_labels_major=dates[::N]
closes_log=[math.log10(_) for _ in closes]
first_chart.add('收盘价',closes_log)
first_chart.render_to_file('first_chart_log.svg')

#from operator import itemgetter
from itertools import groupby

def line_charts(x_data,y_data,filename,y_legend):
    xy_map=[]
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list=[v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    xvalue,yvalue=[*zip(*xy_map)]
    line_chart=pygal.Line()
    line_chart.title=filename
    line_chart.x_labels=xvalue
    line_chart.add(y_legend,yvalue)
    line_chart.render_to_file(filename+'.svg')
    return line_chart

id_month=dates.index('2017-12-01')
line_chart_month=line_charts(months[:id_month],closes[:id_month],'收盘月日均值','月日均值')
    
