def table(n):
    """prints the multiplication table of n"""
  
    if n>0:
     for i in range(1,11):
            print(f"{n} * {i} = {n*i}")
    else:
        print("Please enter a positive number")
        return False
    
n=int(input("Enter a number to print its multiplication table: "))
print(table(n))