test = [[5, 4, 3],[6, 1, 2], [7, 8, 9]]

for x in range(1):
    row_above = []
    row_below = []
    test.insert(0, row_above)
    test.append(row_below)
    
for row in test:
    print (row)
