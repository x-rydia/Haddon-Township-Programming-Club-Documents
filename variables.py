#When we solve an equation 2x=10 in math class, we call x a variable with an unknown value. 
#We willl use variables slightly differently in python, we will declare them with a value immediatley
#such that:

x = 5

#Notice that that code did not have a '#' before it, having '#' before a piece of code denotes a comment.
#A comment is code that is not treated as code by your computer. Feel free to write anything in a comment.
#but keep it SFW, you dont want to hurt your computer's feelings. They are sensitive, lmao. 

#We can reasign a value to x by redeclaring the variable
x = 5
print(x)
x = 7
print(x)

#OUTPUT:
#5
#7

#the function 'print()' displays an output in the command line. In the parenthesees, it takes an argument
#an argument is something that is passed into a funciton to get an output of some form.

#variables can also store text in the form of what we call a string
x = 'my string'

#strings must be surrounded in either single quotes or double quotes.
#this statement would cause a crash:
x = 'my_string"

#a variable name can be almost anything. You should always use descriptive variable names so that we can tell what is going into a 
#variable. 

message = 'Attack at dawn!'
greeting = 'Hello sir!' 

#IGNORE IF YOU ARE NEW TO PROGRAMMING:
# an f-string is a new feature in python that allows for dynamic generation of strings, such that a varibale
# is passed into the string.
x = 69
f_string = f'A Very Nice Number is {x}'
print(f_string)
#Output:
'''A Very Nice Number is 69'''
#an array can also be passed into an f-string such that
my_array = [None, False, 'hello bob', 42, '42', 'Nice', 'RSA', 'priv_key']
for i in range(len(my_array)):
  print(Element {i}: {my_array[i]})
#any expression can be passed into an f-string, including boolean expressions
my_array = [None, False, 'hello bob', 42, '42', 'Nice', 'RSA', 'priv_key']
for i in range(len(my_array)):
  print(Element {i}: {my_array[i] if type(my_array[i}==int))
                                              
                                                 
