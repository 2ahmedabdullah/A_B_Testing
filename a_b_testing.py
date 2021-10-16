#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:35:37 2021

@author: abdul
"""

#Web design EXAMPLE

import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd


def original_difference(total_A, total_B, con_A, con_B):
    web_total = np.array([total_A, total_B])
    conversion = np.array([con_A, con_B])
    conversion_rate = (conversion/web_total*100.0)
    diff = conversion_rate[0] - conversion_rate[1]
    
    tab= [['', 'Web A', 'Web B'],
           ['Total',total_A, total_B],
           ['No Convertion', total_A-con_A, total_B-con_B],
           ['Convertion',con_A, con_B],
           ['Convertion Rate',round(conversion_rate[0],2), round(conversion_rate[1],2)]]
    table=pd.DataFrame(tab[1:], columns=tab[0])
    print(table)
    return diff

#simulation

def samples_difference(total_A, total_B, con_A, con_B, k):
    diffs=[]
    zeros = np.zeros((total_A + total_B)-(con_A + con_B))
    ones = np.ones(con_A + con_B)
    add = np.concatenate((ones,zeros),axis=0)
    np.random.shuffle(add)
    for j in range(0,k):
        sample1 = random.sample(list(add), total_A)
        sample2 = random.sample(list(add), total_B)
        web_total = np.array([total_A, total_B])
        conversion = np.array([sum(sample1), sum(sample2)])
        conversion_rate = (conversion/web_total*100.0)
        diff = conversion_rate[0] - conversion_rate[1]
        diffs.append(diff)
    return diffs


web_A_total = 1200
web_B_total =  1800

conversion_A = 90
conversion_B =  100

permuatations = 1000

diff1 = original_difference(web_A_total, web_B_total, conversion_A, conversion_B)

diff2 = samples_difference(web_A_total, web_B_total, conversion_A, conversion_B, permuatations)


if diff1<0:
    h = [x for x in diff2 if x<diff1]
else:
    h = [x for x in diff2 if x>diff1]

p_value= len(h)/permuatations



plt.hist(diff2, color='blue')
plt.axvline(x=diff1, color='red')
plt.show()
print('p_value:', p_value) 

#if the red line is far away from the mean of the distributuion we can conclude that
#there is a significant difference in conversation rates of the TWO Websites










