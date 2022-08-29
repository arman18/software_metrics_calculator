# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 21:17:55 2022

@author: arman hossain
"""

import ast

#%% testing
code = '''def filter_odd(numbers):

    for numbe in numbersssss:
        hi(aaa,aaaa)
        a = a+5+3
        a = 5
        # a>3 and v<v
        ok #gfdfg
        
        
        if True:

            yield number
    class myclass:
        def hell():
            return 0'''

node = ast.parse(code)

#%% main code
import math
from halstead import hal_vis
from loc import loc_reader

filepath = 'example2.py'
src = 0
with open(filepath, 'r') as src_file:
    src = src_file.read()
node = ast.parse(src)

hall = hal_vis()
hall.visit(node)
# print(hall.uniq_oprds)
for key in hall.uniq_oprds.keys():
    h1 = len(hall.uniq_oprts[key])
    h2 = len(hall.uniq_oprds[key])
    N1 = hall.total_oprts[key]
    N2 = hall.total_oprts[key]
    h = h1 + h2
    N = N1 + N2
    volume = N * math.log(h, 2) if h != 0 else 0
    difficulty = (h1 / 2) * float(N2 / h2) if h2 != 0 else 0
    print("-------------"+key+"()-----------------")
    print("-->unique operators: ",hall.uniq_oprts[key])
    print("-->(u1): ",h1)
    print("-->(N1): ",N1)
    print("-->unique operands: ",hall.uniq_oprds[key])
    print("-->(u2): ",h2)
    print("-->(N2): ",N2)
    print("-->(h): ",h)
    print("-->(N): ",N)
    print("-->volume: ",volume)
    print("-->difficulty: ",difficulty)
    print("-->effort: ",difficulty * volume)
    
    print("-->complexity: ",hall.cyclomatic[key])

loc_readr = loc_reader()
locc = loc_readr.read(src)
print("LOC: ",locc)

            