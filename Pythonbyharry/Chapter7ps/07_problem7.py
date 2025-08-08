'''  for n = 3  
         *
        ***
       ***** '''
'''for n = 5
    *
   ***
  *****
 *******
*********   

'''



n = int(input("Enter the value :"))
for i in range(1, n+1):
  print(" "* (n-i), end="")
  print("*"* (2*i-1), end="")
  print("\n")





