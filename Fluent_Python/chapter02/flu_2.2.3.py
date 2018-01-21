'''
笛卡尔积 例 三种不同尺寸的T恤 每个尺寸都有两种颜色
'''
colors=['black','white']
sizes=['S','M','L']
tshirts=[(color,size) for color in colors #使用列表推导
                      for size in sizes]
print(tshirts)

for tshirt in ('%s %s'%(c,s) for c in colors #使用生成器
                             for s in sizes):
    print(tshirt)
