input = open('input', 'r')
input = input.read()
input = input[:-1]

if input[0] == input[len(input) - 1]:
    input += input[0]

sum = 0
x = 0

while True:
    if input[x] == input[x + 1]:
        sum += int(input[x])
    x += 1
    if x + 1 >= len(input):
        break
print (sum)
