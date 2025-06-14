def sol(a):
    for i in range(0,a):
     for j in range(0,i+1):
        print("*",end="")
     print("\n")




b = int(input("Enter the test cases you want :- "))
for i in range (0,b):
   a = int(input("Enter the numbers you want to print these patterns :- "))
   sol(a)

