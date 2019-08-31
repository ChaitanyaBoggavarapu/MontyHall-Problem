# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:53:24 2019

@author: Abhilash
"""
import numpy as np
import math 


a = int(input("Enter the number of doors"))
numofiterations = int(input(("Enter the number of iterations")))
list1=['yes','no']



def montyhall(Numberofdoors,numofiterations):
    Doors = {}
    count = 0
    nocount = 0
    countingswitched = 0
    countingnonswitched = 0

    for j in range(numofiterations):
        print(j)
        randominteger = np.random.randint(a)
        print(randominteger)
        for i in range(a):
            if i==randominteger:    
                Doors[i] = 'gold'
            else:
                Doors[i] = 'goat'
        #print(Doors)
        #Ranomizing everytihing
        Askuser = np.random.randint(a) 
        #Askuser = int((input("Select the desired door"))) 
        #print(Doors[Askuser]+'selected')
        montyopen = np.random.randint(a) 
#        if(montyopen==Askuser or Doors[montyopen]=='gold'):
#             
#            montyopen = np.random.randint(a) 
#        
        #print(Doors[montyopen]+'Monty opened one of the door of goat')
        #ASking User to switch or not
        #change = str(input(("Do you want to shift type yes or no")))
        #rAndomizing select 'Yes' or 'no'
        
        while(montyopen==Askuser or Doors[montyopen]=='gold'):
            montyopen = np.random.randint(a) 
        #print(Doors[montyopen]+'Monty opened one of the door of goat')
        change = np.random.choice(list1)
        print(change)
        if (change == 'yes'):
            count = count+1
            selectnewdoor = np.random.randint(a)
            #selectnewdoor = int(input(("PLease select new door which is not monty selected")))
            while(selectnewdoor == montyopen or selectnewdoor==Askuser):
                #print("the door already monty selected")
                #selectnewdoor = int(input(("PLease change door because monty selected")))
                selectnewdoor = np.random.randint(a)
            
            if (Doors[selectnewdoor]=='gold'):
                countingswitched = countingswitched+1
        else:
            nocount=nocount+1
            
            if (Doors[Askuser]=='gold'):
                    countingnonswitched = countingnonswitched+1
    print(nocount,count,countingnonswitched,countingswitched)                    
    print(float(countingswitched/float(count)))
    print(countingnonswitched/(float(nocount)))
        

montyhall(a,numofiterations)    

x = input("press any key to exit")
