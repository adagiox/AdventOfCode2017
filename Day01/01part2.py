input = open('input2', 'r')
input = input.read()
input = input[:-1]

# creating a second string to check against as a hack
check = ""
for x in range(((len(input)//2)), len(input)):
    check += input[x]
for x in range(0, (len(input)//2)):
    check += input[x]

print (len(input))
print (len(check))

sum = 0

while True:
    if input[x] == check[x]:
        sum += int(input[x])
    x += 1
    if x == len(input):
        break
print (input)
print (check)
print (sum)
