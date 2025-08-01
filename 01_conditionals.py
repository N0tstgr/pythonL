#if elif else ladder 

a = int(input("Enter the age : "))
if(a>=18):
    print("YOu are above the age of consent")
    print("Hello")


elif(a<0):
    print("you are entering an invalid age ")
elif(a==0):
    print("you are entering 0 which is not a valid age ")

else:
    print("You are below the age of consent")
    print("bye")


print("this is the ending of the program")

