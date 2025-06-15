def sol(a):
    for i in range(1, a + 1):
     
        for j in range(1, i + 1):
            print(j, end=" ")

        
        space_count = 2 * a - (2 * i)

        for s in range(0,space_count):
            print("  ", end="")  

        for j in range(i, 0, -1):
            print(j, end=" ")

        print() 


# Driver code
b = int(input("Enter the test cases you want: "))
for _ in range(b):
    a = int(input("Enter the number of rows you want to print these patterns: "))
    sol(a)
