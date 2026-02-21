
# Nested Loops are somewhere hard to understand by considering 'break' keyword in loop(nested loop). Things may get more worsen when using break keyword in conditions(if elif else)
# In below Two examples,

# In example 1, I demonstrate it using nested loop. In gloabl scope i used while loop and nested is for loop, It would be hard to explain what is the process
# but what I understood is a moral statement, "If while loop is in global scope, It never Terminates"

# In example 2, I again demonstrate it using nested loop. In gloabl scope i used for loop and nested loop is while loop, moral statement,
# "If for loop is in global scope It works Respectedly and break when reached"

# I have came to learn that using conditional statements in nested loop1 will only terminate the nested loop( which is loop1) and not loop0:
"""
    loop0:
        loop1:
            if_condi:
                break
            else_condi:
                ...
"""


# example : 1.1
# nothing terminates in this
a = []
while True:
    for i in range(5):
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            a.append(user)
print(n)


# example : 1.2
# enter quit or anything will run forever
b = []
while True:
    for i in range(5):
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            b.append(user)
        break
print(b)


# example : 1.3
# if entered 'quit' for once will leads to termination of program, else entered anything for 5 times will as well terminate it
c = []
while True:
    for i in range(5):
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            c.append(user)
    break
print(c)




# example : 2.1
# 5 times 'quit' will terminate it and entered anything except 'quit' will never terminate
d = []
for i in range(5):
    while True:
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            d.append(user)
print(d)


# example : 2.2
# 5 times quit or 5 times anything will terminate the program
e = []
for i in range(5):
    while True:
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            e.append(user)
        break
print(e)


# example : 2.3
f = []
# single 'quit' will terminate and entered except 'quit' runs infinite
for i in range(5):
    while True:
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            f.append(user)
    break
print(f)


