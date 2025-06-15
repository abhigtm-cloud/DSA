def sol(a):
    for i in range(0,a-1):
     #space 
      for j in range(0,a-i-1):
         print(" ",end="")
      for j in range (0,2*i+1):
            print("*",end="")
      for j in range (0,a-i-1):
               print(" ",end="")
     #star
      print("\n")
    for i in range(0,a):
     #space 
      for j in range(0,i):
         print(" ",end="")
      for j in range (0,2*a-(2*i+1)):
            print("*",end="")
      for j in range (0,i):
               print(" ",end="")
     #star
      print("\n")
    #space
      




b = int(input("Enter the test cases you want :- "))
for i in range (0,b):
   a = int(input("Enter the numbers you want to print these patterns :- "))
   sol(a)

