
a=int(input("Enter your Age : "))


# if elif elseLadder

if(a>=18):
    print("You are above the age of consent ")
    print("Good Morning")
elif(a<0):
    print(f"you are entering a invalid age : {a}")
elif(a==0):
    print("you are entering a 0 which are not a valid age")
else:
    print("you are below the age of consent")

print("End of Program")