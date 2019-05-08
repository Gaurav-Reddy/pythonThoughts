#lists in python3

items=[['rice',2,200],['flour',5,400],['chicken',1,210]]
for J in items:
	print("product: %s price: %.2f quantity: %i" % (J[0],J[2],J[1])) #thi goes into the mini array j and prints inside the array
print(items[0][0])

#list comprehensions
l=[2,4,6,8,10]
k=[i**2 for i in l]
print(k)

string="Hello this is a complex string in the python program".split()
print([[word,len(word)] for word in string])

#Take the input from the user:   
#Take the input from the user:
import math as m
import time as t
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))
print ("Start Execution : ",end="") 
print (t.ctime()) 

for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,int(num/2)):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)
print ("Stop Execution : ",end="") 
print (t.ctime())            
                        
        
       
           
   
       
