


marks1=int(input("Enter the marks 1 :"))
marks2=int(input("Enter the marks 2 :"))
marks3=int(input("Enter the marks 3 :"))
marks4=int(input("Enter the marks 4 :"))
marks5=int(input("Enter the marks 5 :"))

total_Percentage=(100)*(marks1+marks2+marks3+marks4+marks5)/500

if(total_Percentage>=40 and marks1>=40 and marks2>=40  and marks3>=40 and marks4 >= 40 and marks5>=40 ):
    print(f"YOu are pass you percentage is {total_Percentage}")
else:
    print("You failed, try again next year")   