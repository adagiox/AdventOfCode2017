test = [[5, 4, 3],[6, 1, 2], [7, 8, 9]]

def new_row(start, size):
    new_row = []
    for i in range(1, size):
        new_row.append(i + start)
    return new_row

def find_center(num):
    steps = 0
    index = test.index(num)
    print (index)
    return steps

for x in range(10):
    start = test[len(test) - 1]
    start = start[len(start) - 1]
    for i in range(len(test) - 1, -1, -1):
        test[i].append(start + 1)
        start += 1
    row_above = new_row(start, len(test[1]) + 1)
    row_above.reverse()
    test.insert(0, row_above)
    start = test[0][0]
    for i in range(len(test)):
        test[i].insert(0, start + 1)
        start += 1
    row_below = new_row(start, len(test[0]) + 1)
    test.append(row_below)
for row in test:
    print (row)

print(find_center(110))
