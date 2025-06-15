def sol(a):
    start = 0
    for i in range(0,a):
        if i%2==0:
            start=1
        else:
            start=0
        for j in range(0,i):
            print(start,end="")
            start = 1- start
        print("\n")



b = int(input("Enter the test cases you want :- "))
for i in range (0,b):
   a = int(input("Enter the numbers you want to print these patterns :- "))
   sol(a)

