a = int(input("Enter the number : "))
for i in range(3, a):
    if(a%i) == 0:
        print("This is  not the prime number")
        break
    else:
        print("this is the prime number")