# this is just an idea of elevator up or downgoing python program 
# TODO : much improvement has to brought such as parallel user prompt 
#        validation, etc.


from time import sleep
from os import system
system("clear")

idle_at_floor = 0

#will display upcoming, downcoming or already at floor
def req_at_floor(n):
    n = int(n)
    
    global idle_at_floor
    if n == idle_at_floor:
        print("Already At The Floor\n")
    elif n<0 or n>=10:
        print("Out of floor!\n")
    else:
        while idle_at_floor != n:
            sleep(1)

            #upcoming
            if n >= idle_at_floor:
                idle_at_floor += 1
                print("\u2191", idle_at_floor)
                if n == idle_at_floor:
                    print("opening the door...")
                    sleep(2)
                    print("closing the door...\n")
                    

            #downcoming
            elif n <= idle_at_floor:
                idle_at_floor -= 1
                print("\u2193", idle_at_floor)
                if n == idle_at_floor:
                    print("opening the door...")
                    sleep(2)
                    print("closing the door...\n")

while True:
    user = int(input("Enter Floor Number : "))
    req_at_floor(user)