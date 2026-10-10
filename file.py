# create a new file "practice.txt" using python and add the following data in it
"""
hi everyone 
we are learning File I/O
using java
i like programming in java
"""

with open("Practice.txt", "w") as f:
    f.write("Hi everyone \n We are learning File I/O \n using java. \n I like programming in java")


# now replace all occurences of "java" with "python" in above file

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)