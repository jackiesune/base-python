import json
import pygal


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
first_chart.add('收盘价',closes)
first_chart.render_to_file('first_chart.svg')

    
