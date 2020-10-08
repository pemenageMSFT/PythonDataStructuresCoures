import stack 
"""
This is my solution before checking the instructor solution
"""


string = "gninrael nIdekniL htiw tol a nrael"
reverse_string = " "
s = stack.Stack()
# first list to add take items 
first_list = []
# second list to add items in reverse order 
second_list = []

# counts used for while loop 
# count first list
fl = 0
# count of second lis
sl = 0
for letter in string:
    s.push(letter)
    first_list.append(letter)
    fl += 1 
while sl < fl:
    second_list.append(first_list.pop())
    sl += 1 
print(second_list)