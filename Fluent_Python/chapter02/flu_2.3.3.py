'''
用嵌套元组来获取经纬度
'''
metro_areas=[
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi', 'IN', 21.935, (28.613889, 77.208889)),
]
print('{:14} |{:^9}|{:^9}'.format('city','lat','long.'))#组成头格式
fmt='{:15}|{:9.4f}|{:9.4f}'
for name,cc,pop,(latitude,longtitude) in metro_areas:
    if longtitude>=0:
        print(fmt.format(name,latitude,longtitude))
