# -*- coding: utf-8 -*-
"""
pyder Editor

This is a temporary script file.
"""

#code to solve goodie-dilemma problem
g = dict()                                                                          #initialize a dictionary 
input_file = open('input.txt','r')                                                  #input from file

for line in input_file:                                                             #read line from input
    if line != '\n':                                                                #exclude empty lines
        a = line.split(":")                                                         #separate names of goodies and their cost
        a[1] = a[1][1:]                                                             #remove an unwanted space in cost string
        if a[1] != "":                                                              #remove lines which have no value
            if a[1][-1] == "\n":                                                    #remove endline 
                a[1] = a[1][:-1]
            g[a[0]] = int(a[1])                                                     #add the name of goodies and their cost as integer to dictionery
            
input_file.close()                                                                  #close file input


m = g["Number of employees"]                                                        #extract the number of employees
del g["Number of employees"]                                                        #once extracted, key and value deleted


s_v = sorted(g.values())                                                            #sort the cost in ascending order and add to a new list

l=len(s_v)                                                                          #number of goodies
min = s_v[-1] - s_v[0]                                                              #initialise minimum for worst case
f=0                                                                                 #f is used to store the index of the goodie with the lowest cost
for i in range((l-m)+1):                                                            #traverse through the costs
    k = s_v[i+(m-1)] - s_v[i]                                                       #calculate difference between max and min
    if k<min:                                                                       #check if difference is lowest
        min=k                                                                       #if yes, update min value
        f=i                                                                         #also update f to store the index where min cost was found

        
output_file = open('output.txt','w')                                                #write file       
output_file.write("The goodies selected for distribution are:\n")                   
output_file.write("\n")
for i in range(f,f+m):                                                              #traverse through the costs identified to come up with minimum difference
    for j in g.keys():                                                              #traverse through goodies                                                             
        if g[j] == s_v[i]:                                                          #if costs match, goodies matched
            output_file.write(j+": ")                                               #print name of goodie
            output_file.write(str(g[j]))                                            #print cost of goodie
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
output_file.write(str(min))                                                         #print the difference between max and min
output_file.close()

                  
    