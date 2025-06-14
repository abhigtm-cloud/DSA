def sol(a):
    for i in range(1,a+1):
     for j in range(1,i+1):
        print(j,end="")
     print("\n")




b = int(input("Enter the test cases you want :- "))
for i in range (0,b):
   a = int(input("Enter the numbers you want to print these patterns :- "))
   sol(a)
