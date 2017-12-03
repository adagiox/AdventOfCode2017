input = open('input2', 'r')
input = input.read()
input = input[:-1]

# creating a second string to check against as a hack
check = ""
for x in range(((len(input)//2)), len(input)):
    check += input[x]
for x in range(0, (len(input)//2)):
    check += input[x]

sum = 0

for x in range(len(input)):
    if input[x] == check[x]:
        sum += int(input[x])
print (sum)
