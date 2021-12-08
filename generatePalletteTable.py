# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:58:19 2021

@author: J. Bajic
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
Functions
"""
def plot_linearmap(cdict):
    newcmp = mpl.colors.LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
    rgba = newcmp(np.linspace(0, 1, 256))
    fig, ax = plt.subplots(figsize=(8, 3), constrained_layout=True)
    col = ['r', 'g', 'b']
    for xx in [0.25, 0.5, 0.75]:
        ax.axvline(xx, color='0.7', linestyle='--')
    for i in range(3):
        ax.plot(np.arange(256)/256, rgba[:, i], color=col[i])
    ax.set_xlabel('index')
    ax.set_ylabel('RGB')
    plt.show()
    
def plotPallete(cm):
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    plt.figure(figsize=(10, 1))
    fig=plt.imshow(gradient, aspect='auto', cmap=cm)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()


def generateTable(cm):
    print("const uint32_t "+pallette+"[256]={") 
    for i in range(256):
        rgba = cm(i)
        r=int(rgba[0]*255)
        g=int(rgba[1]*255)
        b=int(rgba[2]*255)
        
        c=(b<<16)+(g<<8)+r   
        k=i+1
        if ((k%10==0)):
            print("0x{:06x}".format(c)+",") 
        else:
            if(i!=255):
                print("0x{:06x}".format(c)+",",end=" ") 
            else:
                print("0x{:06x}".format(c)) 
    print("};")  

"""
End of Functions
"""

built_in=1      # set to 0 for user defined pallette

#built in pallette
pallette='hot'
#user defined  pallette
user_defined = {   # x     y  value
         'red':   [[0.0,  0.0, 0.0],
                   [0.3,  0.7, 0.7],
                   [1.0,  0.0, 0.0]],
                   
         'green': [[0.0,  0.0, 0.0],
                   [0.3, 0.7, 0.7],
                   [1.0,  0.0, 0.0]],
                   
         'blue':  [[0.0,  0.0, 1.0],
                   [0.5,  0.5, 0.5],
                   [1.0,  0.0, 0.0]]}

if(built_in):
    color_map=plt.get_cmap(pallette)
else:    
    color_map = mpl.colors.LinearSegmentedColormap('testCmap', segmentdata=user_defined, N=256)
    plot_linearmap(user_defined)
    pallette='custom'

plotPallete(color_map)
generateTable(color_map)


