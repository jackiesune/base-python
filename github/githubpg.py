import requests
from pygal.style import LightenStyle as LS,LightColorizedStyle as LCS
import pygal

json_url="https://api.github.com/search/repositories?q=language:python&sort=stars"
limit_url="https://api.github.com/rate_limit"

reponse=requests.get(json_url)
re=reponse.json()
print(len(re['items']))
#提取数据
ddicts,names,stars=[],[],[]
pdicts=[]
for ddict in re['items']:
    names.append(ddict['name'])
    star=ddict['stargazers_count']
    stars.append(star)
    desc=ddict['description']
    purl=ddict['html_url']
    pdict={
        'value':star,'xlink':purl}
    pdicts.append(pdict)
    #某个项目无desc故需要排错
    ddicts.append({
            'value':star,
            'label':desc,
            'xlink':purl})

#设置图表格式
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=30
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.show_y_guides=False
my_config.width=1000
my_config.truncate_label=15
chart_bar=pygal.Bar(my_config,style=my_style)
chart_bar.title="Most Starts PYthon Project"
chart_bar.x_labels=names
#出现错误：'NoneType' object has no attribute 'decode'
#print(ddicts)

chart_bar.add("",pdicts)
chart_bar.render_to_file('python.svg')






