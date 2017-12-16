'''
列表推导同filter和map的比较
'''
import time

symbols='$&*@'
start=time.time()
beyond_ascii=[ord(symbol) for symbol in symbols if ord(symbol)>40]
end=time.time()
total=end-start
print(beyond_ascii,total)
stars=time.time()
next_accii=list(filter(lambda c:c>40,map(ord,symbols)))
ends=time.time()
print(next_accii,ends-stars)



