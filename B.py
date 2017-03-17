
import turtle

def main():
    """Queue programm with turtles. it creates menu, """
    
    q=True
    li=[]

    colors=["blue","green","red", "white","black","violet","olive","brown","blue","green"]
    print '\n Menu:\nP- Print\nA- append new input element\n'\
          'N- del first in queue\nL- find and del input string\n'\
          'M- location in memory\nS- sort queue\nQ- quit'
          
    
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")  
#    pr_tu(li,colors)
    while q==True:
        
       
        seq=raw_input("make choise :")
        seq=seq.upper()
        
        if seq=="P":
            
            if len(li)==1:
#                s=str(li)
                print "here your queue :",li[0]
            elif li!=[]:
                s=' '.join(li)
                print "here your queue :",s            
            
            else: print("queue is empty")
            
            
        elif seq=="A":
            if len(li)!=10:
                elem=raw_input("enter new string :")
                if elem!="":  li.append(elem)
            else: print"queue is full -please, try later"
            
            wn.clearscreen()
            wn.bgcolor("lightgreen") 
            
            pr_tu(li,colors)
            
                
        elif seq=="N":
            
            dup=[]
            for i in li:
                dup.append(i)
                
            help_list=[]
            k=colors[0]

            for i,el in enumerate(li):
                
                if i>0:    
                   help_list.append(el)
                   
                   colors[i-1]=colors[i]
            
            li=help_list
            colors[i]=k

            wn.clearscreen()
            wn.bgcolor("lightgreen")  
            
            pr_tu(li,colors)
        
                
        elif seq=="L":
            
            dup=[]
            for i in li:
                dup.append(i)
                
            k=False
            str_leave=raw_input("enter new string ")
            if str_leave!="":
                for i, el in enumerate(li):
                    if el==str_leave:
                        k=True
                        break
                    
            if k==True:
                help_list=[]
                for j,el in enumerate(li):
                    if j!=i: help_list.append(el)
                    else: pass
                li=help_list
            else: print 'There is no such string'
            
            if k==True:
                some=colors[i]
                for j in range(i,len (li)+1):
                    if j>i:
                        colors[j-1]=colors[j]
                colors[j]=some
           
            
            wn.clearscreen()
            wn.bgcolor("lightgreen")  
        
            pr_tu(li,colors)
                
        elif seq=="S": 
            
            for i in range (len (li)):
                for j in range (len(li)-1,i,-1):
                    if myestimate(li[j],li[j-1]):
                        li[j],li[j-1]=li[j-1],li[j]
                        colors[j],colors[j-1]=colors[j-1],colors[j]
            print(li)
            
            wn.clearscreen()
            wn.bgcolor("lightgreen")  
            pr_tu(li,colors)
                    
        elif seq=="M":
            print id(li)
            
        elif seq=="Q":
            q=False
            
        else: pass
        
    wn.exitonclick()
    
def pr_tu(li,colors):
    """creation and stapping turtle""" 
    tess = turtle.Turtle()
    tess.reset()
            
    for i in range(len(li)):
                
        tess.color(colors[i])
        tess.shape("turtle")
        tess.penup()
        tess.forward(-40)
        tess.stamp()
    
    
def myestimate(a,b, i=0):
    """Own function for estimation strings"""
    a=str(a).lower()
    b=str(b).lower()
    
    if len(a)==len(b):  k= True
    elif len(a)>len(b): k= False
    else:               k= True
    
    if i<min(len(a),len(b)):
        
        if a[i]==b[i]:  return myestimate(a,b, i+1)
        elif a[i]<b[i]: k= True  
        elif a[i]>b[i]: k= False
   
    return k
    
    
    
if __name__=="__main__":
    import sys
    
    if len(sys.argv)>0:
        main()
#      
    else:
        main()
        