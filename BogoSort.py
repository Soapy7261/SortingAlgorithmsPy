import random, os
os.system ("cls")
output = True #Change this to True if you want to output the list if its not sorted yet, decreases performance though (;
comparsions = 0
comparon = True #Turn this to False if you don't want to trade comparsions
while True:
    g1, g2, g3, g4, g5 = False, False, False, False, False
    p0 = random.randint(0,5)
    p1 = random.randint(0,5)
    p2 = random.randint(0,5)
    p3 = random.randint(0,5)
    p4 = random.randint(0,5)
    p5 = random.randint(0,5)
    if p0 > p1:
        g1 = True
        if comparon == True:
            comparsions += 1
    if p1 > p2:
        g2 = True
        if comparon == True:
            comparsions += 1
    if p2 > p3:
        g3 = True
        if comparon == True:
            comparsions += 1
    if p3 > p4:
        g4 = True
        if comparon == True:
            comparsions += 1
    if p4 > p5:
        g5 = True
        if comparon == True:
            comparsions += 1
    if g1 and g2 and g3 and g4 and g5 == True:
        if comparon == True:
            print (f"Sorted, {p0, p1, p2, p3, p4, p5} Comparsions: {comparsions}")
        if comparon == False:
            print (f"Sorted, {p0, p1, p2, p3, p4, p5}")
        break
    if output == True:
        if g1 or g2 or g3 or g4 or g5 == False:
            print (f"Not sorted, {p0, p1, p2, p3, p4, p5}")
            #os.system ("cls") #Uncomment this if you want to clear the screen each time, decreases performance a lot though (;
