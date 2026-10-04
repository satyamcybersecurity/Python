# write a program to find greatest of 3 numbers entered by the user

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))

if(a >= b and a >= c):
    print("1st number is greatest", a)
elif(b >= c):
    print("2nd number is greatest", b)
else:
    print("3rd number is greatest", c)