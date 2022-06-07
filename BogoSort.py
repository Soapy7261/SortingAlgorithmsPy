import random, os
os.system ("cls") #You might need to change this to "clear" depending on your OS
output = False #Change this to True if you want to output the list if its not sorted yet, decreases performance though (;
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
    if p1 > p2:
        g2 = True
    if p2 > p3:
        g3 = True
    if p3 > p4:
        g4 = True
    if p4 == p5 + 1:
        g5 = True
    if g1 and g2 and g3 and g4 and g5 == True:
        print (f"Sorted, {p0, p1, p2, p3, p4, p5}")
        break
    if output == True:
        if g1 or g2 or g3 or g4 or g5 == False:
            print (f"Not sorted, {p0, p1, p2, p3, p4, p5}")
            #os.system ("cls") #Uncomment this if you want to clear the screen each time, decreases performance though (;
