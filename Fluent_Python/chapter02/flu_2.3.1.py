'''
元组和记录
'''
lax_coordinates=(33.9425,-118.408056)#洛杉矶国际机场的经纬度
city,year,pop,chg,area=('Tokyo',2003,32450,0.66,8014)#东京市的一些基本信息：市民 年份 人口 人口变化 面积
traveler_ids=[('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s'%passport)

for country,_ in traveler_ids: #_表示占位符 因为元组中第二个元素没有意义相对本实验来说
    print(country)