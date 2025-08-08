n = int(input("Enter the value of the number : "))
i = 0
factorial = 1
for i in range(1, n+1):
    factorial = factorial*i
    # i+=1

print(f"the factorial of {n} is {factorial}")    