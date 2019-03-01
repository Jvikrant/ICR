# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:32:01 2018

@author: jdhruwa
"""

#plotting image

def plot_image(polygons):
    
    text2=""
    for polygon in polygons:
        text     =polygon[1]
        text2    +="\n"+polygon[1]
    print(text2)
    
    return text2
    
    
