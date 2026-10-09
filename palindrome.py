# write a program to check if a list contains a palindrome of elements. [1, 2, 3, 2, 1]

list = [1, 2, 3, 2, 1]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Palindrome")
else:
    print("not palindrome")