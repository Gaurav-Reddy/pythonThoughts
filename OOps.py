#Compilation of Object oriented stuff in python
class first_class:
    
    var1=3 #this is a variable of a class atrribute
    def __init__(self,name,breed): #this initializes the constructor 
        self.name="rocky"
        self.breed="blsck labrodor"

    def class_function(self,var): #this is a class method
        print(var*2) 


new_object=first_class("h","g")
print(new_object.breed)
print(new_object.var1)
var2="random string"
print(new_object.class_function(var2))  #please add a self in the class function without fail


#Inheritance
class second_class(first_class):
    def use1stmethod(self):
        print()
