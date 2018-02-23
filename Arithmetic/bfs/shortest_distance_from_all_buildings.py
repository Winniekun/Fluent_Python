'''
@author：KongWeiKun
@file: shortest_distance_from_all_buildings.py
@time: 18-2-9 下午6:30
@contact: 836242657@qq.com
'''
"""

do BFS from each building, and decrement all empty place for every building visit
when grid[i][j] == -b_nums, it means that grid[i][j] are already visited from all b_nums
and use dist to record distances from b_nums
"""