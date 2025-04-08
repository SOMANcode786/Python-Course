# How to use set ?
# set ka under elment repeat nahi hoty
# Unique element hoty ha / duplicate vlaue ko autmatiaclly hata daita ha
# Seraching fast hoti haa
#   if 12 in set:
#      print("!Found")
# Mutable hota haa


my_set={12,34,45,55,55,6}
print(my_set)

my_set.add("harry")
print(my_set,type(my_set))

my_set.remove("harry")
print(my_set,type(my_set))

my_set.pop()
print(my_set)
