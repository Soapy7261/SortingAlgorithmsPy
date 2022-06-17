ar = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] #Change this to change the array its sorting
sr = 0
while True:
    if sr == 9:
        sr = 0
        if ar[sr] < ar[sr+1] and ar[sr+1] < ar[sr+2] and ar[sr+2] < ar[sr+3] and ar[sr+3] < ar[sr+4] and ar[sr+4] < ar[sr+5] and ar[sr+5] < ar[sr+6] and ar[sr+6] < ar[sr+7] and ar[sr+7] < ar[sr+8] and ar[sr+8] < ar[sr+9]:
            print (ar)
            break
    if ar[sr] > ar[sr+1]:
        temp = ar[sr]
        ar[sr] = ar[sr+1]
        ar[sr+1] = temp
    sr += 1
