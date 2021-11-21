
#In a nested loop specify the range and row number the "*" should appear until the end.

for row in range(7,0,-1):
    for nextline in range(row,0,-1):
        print("*",end="")
    print()
