def sort(first:int, second:int, third:int, fourth:int, fifth:int, sixth:int, seventh:int, eighth:int, ninth:int, tenth:int):
    import time, os
    com = 0
    sleep = 0.1 #Change this time to how long you wanna want between messages
    clea = "cls" #You might need to change this to "clear" depending on your OS
    os.system (clea)
    print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
    time.sleep(sleep)
    os.system (clea)
    for i in range (50):
        if first > second:
            var = first
            first = second
            second = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if second > third:
            var = second
            second = third
            third = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if third > fourth:
            var = third
            third = fourth
            fourth = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if fourth > fifth:
            var = fourth
            fourth = fifth
            fifth = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if fifth > sixth:
            var = fifth
            fifth = sixth
            sixth = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if sixth > seventh:
            var = sixth
            sixth = seventh
            seventh = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if seventh > eighth:
            var = seventh
            seventh = eighth
            eighth = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if eighth > ninth:
            var = eighth
            eighth = ninth
            ninth = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
        if ninth > tenth:
            var = ninth
            ninth = tenth
            tenth = var
            com = com + 1
            print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSwaps: {com}")
            time.sleep(sleep)
            os.system (clea)
    print (f"{first} {second} {third} {fourth} {fifth} {sixth} {seventh} {eighth} {ninth} {tenth}\nSort finished, total swaps: {com}")
import random
range2 = 0
range3 = 9
sort(random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3), random.randint(range2, range3))
