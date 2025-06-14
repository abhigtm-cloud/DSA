def sol(a):
    for i in range(a,0,-1):
     #space 
      for j in range(a-i-1,0,-1):
         print(" ",end="")
      for j in range (2*i+1,0,-1):
            print("*",end="")
      for j in range (a-i-1,0,-1):
               print(" ",end="")
     #star
      print("\n")
    #space
      




b = int(input("Enter the test cases you want :- "))
for i in range (0,b):
   a = int(input("Enter the numbers you want to print these patterns :- "))
   sol(a)

