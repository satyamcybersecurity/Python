# write a program to find sum of first n natural numbers (using while and range)

# using while
n = int(input("enter integer :"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum = ", sum)

# using range

x = int(input("enter number :"))
sum = 0
for i in range(n + 1):
    add += i

print("total sum is :", add)