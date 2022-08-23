# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 08:53:25 2022

@author: iit
"""

#!usr/bin/python3

import argparse
from builder import CFGBuilder
import ast
import collections
import math

#%% source code
filepath = "example2.py"
with open(filepath, 'r') as src_file:
    src = src_file.read()



# %% control flow diagram
from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file(filepath, "./"+filepath) # cfg is an ast.nodeVisitor

cfg.build_visual('exampleCFG', 'png',True,False)

# %% complexity
from radon.visitors import ComplexityVisitor
v = ComplexityVisitor.from_code(src)
v.functions[0].complexity


# %% halsted matrics

from metrics import h_visit_src
hal = h_visit_src(src)

h1,h2,N1,N2,h,N,volume,difficulty,effort = hal[0]

# from radon.visitors import HalsteadVisitor
# vv = HalsteadVisitor.from_code(src)

# %% raw line of code
# loc, lloc, sloc, comments, multi, blank, single_comments
from radon.raw import analyze
metcs = analyze(src)
loc = metcs.loc - metcs.single_comments - metcs.blank