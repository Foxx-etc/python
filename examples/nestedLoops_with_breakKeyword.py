
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


# example : 1
n = []
while True:
    for i in range(5):
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            n.append(user)

print(n)




# # example : 2
p = []
for i in range(5):
    while True:
        user = input("Enter : ")
        if user == 'quit':
            break
        else:
            p.append(user)

print(p)

