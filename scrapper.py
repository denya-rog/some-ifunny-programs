# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:03:25 2017

@author: denya-rog

Modul for searching e-mails
"""

import re
import urllib2
import sys  


def scraper(url, depth=1, out_emails=[]):
    
    """Make recursive function , that takes one obligatory argument- URL, 
    and have depth arg - how many steps thrue links will make function 
    and our  list of e-mails that will be retrned"""
    
    if depth > 0:  
        
        try:   #catching problems with url 
            response = urllib2.urlopen(url)
            
        except:
            print("not walid URL")
            return out_emails
            
        page_source = response.read()
        
        #searching for all http and https urls on website
        urls = set(re.findall(r'href=[\'"](http[^\'" >]+)', page_source))
        #searching for all emails on site
        emails = re.findall(r'([-a-z0-9._]+@[-a-z0-9]+\.[-a-z0-9]+)+',page_source)      
        out_emails += emails
        
        if urls != []:      #block of recursion for all urls 
            for i in urls:
                scraper(i, depth-1, out_emails)
                
        else:
            return out_emails
            
    return set(out_emails)
            

if __name__ == "__main__":
    try:
        if sys.argv[1][:4]!="http":
            print ("not so good url")
            sys.argv[1]="https://"+sys.argv[1]
    except:
        print("There are no console parametrs. Will be used https://ru.wikipedia.org")
        out = scraper("https://ru.wikipedia.org", 2)
    
    if len(sys.argv) >= 3 and type(int(sys.argv[2])) == int:
        
        out = scraper(sys.argv[1], int(sys.argv[2]))
        
    elif len(sys.argv) == 2 :
        print ("there is no parametr depth. Will we used ony for this site")
        out = scraper(sys.argv[1])
        
    print ("Found emails:")    
    for i in out:
        print i
    
