# write a program to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary and add one by one.

marks = {}
x = int(input("enter phy :"))
marks.update({"phy" : x})

y = int(input("enter chem :"))
marks.update({"chem" : y})

z = int(input("enter maths :"))
marks.update({"maths" : z})

print(marks)

