# write a program to find factorial of first n numbers (using for and while)

# using while
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print("factorial : ", fact)

# using for 

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial :", fact)