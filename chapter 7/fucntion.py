
# two type of function 
#   Abstraction  jsy print function ha hmmy pata nahi ka is ka pichy kon sa code ha
#   decomptsition   make function to build all probelm


# COMPONENT OF FUNCTION:
 
# --def-- 
# you will maek a functin in python use def keyword

# --identifiesr--
# def fucntion name bracket(parameter) and you put a colon :
#   "also put a docstring(which mean documentation string this is a reading manual for you function) to assist for reader and user "
#    Function body 
#    return 

# name(argument)


def is_even(x):
     """check if x i even or not"""
     if x%2==0:
         return True
     
     elif x%2 !=0:
         print(f"{x} is odd number") 
         return False 
 

print(is_even(3))