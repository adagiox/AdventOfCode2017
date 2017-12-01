input = open('input', 'r')
input = input.read()
print (input)

if input[0] == input[input.length]:
	i = 0
	# could add check here for a sequence of the same number (infinite loop)
	while input[i] == input[input.length]:
		input += input[i]
		i++
