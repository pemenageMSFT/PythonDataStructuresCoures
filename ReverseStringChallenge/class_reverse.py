# This is the way the instructor answered the challenge, mine was not correct
import stack 

string = "gninrael nIdekniL htiw tol a nrael"
reverse_string = " "
s = stack.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reverse_string += s.pop()

print(reverse_string)