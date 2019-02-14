from dices import Dice
import pygal

dices6=Dice()
dices10=Dice(10)
result=[]
for num_roll in range(1000):
    r6=dices6.throw()
    r10=dices10.throw()
    r=r6+r10
    result.append(r)

#统计次数
fre=[]
for s in range(1,dices6.num_sides+dices10.num_sides+1):
    re=result.count(s)
    fre.append(re)

#制作图表
gallery=pygal.Bar()
gallery.title="one six sides dice"
gallery.x_labels=list(range(1,dices6.num_sides+dices10.num_sides+1))
gallery.x_title="sides"
gallery.y_title="frequecy"

gallery.add("D6+D10",fre)
gallery.render_to_file('dice_six and ten.svg')



