#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:42:14 2017

@author: denya
"""
import numpy as np
import math
def center_mass(data, classes=4):
    first_len=len(data)
    table=data.copy()
#    print(data)
    li=[[i] for i in range(len(data))]
        
    for counter in range (first_len-classes):
        
        tabl=np.zeros((len(data),len(data)))
#        print(tabl)
        j=0
        for i in range(len(data)):
            tabl[i][i]=1000
            for j in range(i):
                dist=0
            
                for k in range (len(data[0])):
              
                    dist+=(data[i][k]-data[j][k])**2

                tabl[i][j]=tabl[j][i]=round((math.sqrt(dist)),2)
#        print(len(tabl),len(tabl[0]))
#        print(tabl)
        mi=np.amin(tabl)
#        print(mi)
        try:
            for ind_0,i in enumerate(tabl):
                for ind_1,j in enumerate(i):
                    if j == mi: raise StopIteration 
        except StopIteration: pass
                
        
        if ind_0>ind_1:    ind_0,ind_1=ind_1,ind_0
#        print(ind_0,ind_1)
        
        for j in range(len(data[classes-1])): 
#            print(data[ind_0],data[ind_1])
            c=len(li[ind_0])+len(li[ind_1])
            d=len(li[ind_1])
            e=len(li[ind_0])
#            print(c,len(li[ind_0]),len(li[ind_1]),"->")
            f=float(d*data[ind_0][j])
            g=float(e*data[ind_1][j])
#            print(f,g,c,"<__")
            data[ind_0][j]=float((f+g)/c)
#            print(f,g,c,"<__",data[ind_0][j])
#            print(data[ind_0],"<--")
        li[ind_0]+=li[ind_1]
        li.remove(li[ind_1])        
        data=np.delete(data,(ind_1),axis=0)
#        print(data) 
#        print(li)
    import matplotlib.pyplot as plt
    fit1=table[:,[0]]
    fit2=table[:,[-1]]
#    print(fit1,fit2)

    x=[]
    y=[]
    for i in range (classes):
        k=[]
        h=[]
        for j in li[i]:
            k.append(float(fit1[j]) )
            h.append(float(fit2[j]))
        x.append(k)
        y.append(h)
#    print(x,y)
    
        
            
    plt.figure(3)
    plt.plot(x[0], y[0], 'rs', x[1], y[1] ,'bs', x[2], y[2], 'ys', x[3], y[3], 'ks' )
    
    
    
def fill(data):
    
    tabl=np.zeros((len(data),len(data)))
#    print(tabl)
    j=0
    for i in range(len(data)):
        tabl[i][i]=1000
        for j in range(i):
            dist=0
            
            for k in range (len(data[0])):
              
                dist+=(data[i][k]-data[j][k])**2

            tabl[i][j]=tabl[j][i]=round((math.sqrt(dist)),2)
    print(len(tabl),len(tabl[0]))   
    return tabl
    
    
def nn(tabl,li):
    
#    print(tabl)
    mi=np.amin(tabl)
#    print(mi)
    try:
        for ind_0,i in enumerate(tabl):
            for ind_1,j in enumerate(i):
                if j == mi: 
                    raise StopIteration 
    except StopIteration: pass
                
#    print(ind_0,ind_1)
    if ind_0>ind_1:    ind_0,ind_1=ind_1,ind_0
    li[ind_0]+=li[ind_1]
    li.remove(li[ind_1])
    for j in range(len(tabl)):
        if j==ind_0 :
            tabl[j][ind_1]=1000
        elif j==ind_1:
            tabl[j][ind_0]=1000
#        print(j)
        else:
            tabl[j][ind_0]=min(tabl[j][ind_0],tabl[j][ind_1])
#            print(tabl[j][ind_0])
        tabl[ind_0][j]=tabl[j][ind_0]
    tabl=np.delete(tabl,(ind_1),axis=0)
    tabl=np.delete(tabl,(ind_1),axis=1)    
#    print(tabl)
    return tabl,li
    
    
def fn(tabl,li):
    
#    print(tabl)
    mi=np.amin(tabl)
#    print(mi)
    try:
        for ind_0,i in enumerate(tabl):
            for ind_1,j in enumerate(i):
                if j == mi: 
                    raise StopIteration 
    except StopIteration: pass
                
#    print(ind_0,ind_1)
    if ind_0>ind_1:    ind_0,ind_1=ind_1,ind_0
    li[ind_0]+=li[ind_1]
    li.remove(li[ind_1])
    for j in range(len(tabl)):
        if j==ind_0 :
            tabl[j][ind_1]=1000
        elif j==ind_1:
            tabl[j][ind_0]=1000
#        print(j)
        else:
            tabl[j][ind_0]=max(tabl[j][ind_0],tabl[j][ind_1])
#            print(tabl[j][ind_0])
        tabl[ind_0][j]=tabl[j][ind_0]
    tabl=np.delete(tabl,(ind_1),axis=0)
    tabl=np.delete(tabl,(ind_1),axis=1)    
#    print(tabl)
    return tabl,li
    
    
    
def main(table,classes=4):
    data=fill(table)
    li=[[i] for i in range(len(data))]
#    print(li)
#    print(data)
    for i in range (len(data)-classes):
        data,li=nn(data, li)
#    print(li)
    import matplotlib.pyplot as plt
    fit1=table[:,[0]]
    fit2=table[:,[-1]]
#    print(fit1,fit2)

    x=[]
    y=[]
    for i in range (classes):
        k=[]
        h=[]
        for j in li[i]:
            k.append(float(fit1[j]) )
            h.append(float(fit2[j]))
        x.append(k)
        y.append(h)
#    print(x,y)
    
        
            
    plt.figure(1)
    plt.plot(x[0], y[0], 'rs', x[1], y[1] ,'bs', x[2], y[2], 'ys', x[3], y[3], 'ks' )
    print("_____________")
    data=fill(table)
    li=[[i] for i in range(len(data))]
    for i in range (len(data)-classes):
        data,li=fn(data, li)
#    print(li)  
    
    fit1=table[:,[0]]
    fit2=table[:,[-1]]
#    print(fit1,fit2)
    x=[]
    y=[]
    for i in range (classes):
        k=[]
        h=[]
        for j in li[i]:
            k.append(float(fit1[j]) )
            h.append(float(fit2[j]))
        x.append(k)
        y.append(h)
    plt.figure(2)
    plt.plot(x[0], y[0], 'rs', x[1], y[1] ,'bs', x[2], y[2], 'ys', x[3], y[3], 'ks') 
    center_mass(table)
            
if __name__=="__main__":
    import sys
    data=np.random.randint(low=-20,high=20, size=(80   ,2))
#    print(data)
    if len(sys.argv)>2:
        a=sys.argv[1]
        b=sys.argv[2]
#        data=np.random.randint(low=0,high=10, size=(10,10))
    
        main(sys.argv[1],sys.argv[2])
    else:
        main(data)
        