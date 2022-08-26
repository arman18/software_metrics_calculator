# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 21:17:55 2022

@author: arman hossain
"""

import ast

from halstead import hal_vis
from loc import loc_reader
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

filepath = 'example2.py'

with open(filepath, 'r') as src_file:
    src = src_file.read()
node = ast.parse(src)

hall = hal_vis()
hall.visit(node)
# print(hall.uniq_oprds)
for key in hall.uniq_oprds.keys():
    print(key+"()")
    print("-->unique operators: ",hall.uniq_oprts[key])
    print("-->(u1): ",len(hall.uniq_oprts[key]))
    print("-->(N1): ",hall.total_oprts[key])
    print("-->unique operands: ",hall.uniq_oprds[key])
    print("-->(u2): ",len(hall.uniq_oprds[key]))
    print("-->(N2): ",hall.total_oprts[key])
    print("-->complexit(N2): ",hall.cyclomatic[key])
    
# print(hall.total_oprds)
# print(hall.uniq_oprts)
# print(hall.total_oprts)
print(hall.cyclomatic)


loc_readr = loc_reader()
locc = loc_readr.read(src)            
                
            