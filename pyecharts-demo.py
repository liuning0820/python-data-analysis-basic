import json
from pyecharts import Pie

file = open("./datasets/pyecharts-data/pies.json", encoding="utf8")
data = json.load(file)

print(data)

name = data['name']
sales = data['sales']
sales_volume = data['sales_volume']
pie = Pie()
pie.add("成交量", name, sales_volume)
pie.show_config()
pie.render()
