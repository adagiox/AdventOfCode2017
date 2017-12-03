lines = []
with open('input') as file:
	for line in file:
		line = line[:-1]
		lines.append(line.split('\t'))
checksum = []
for row in lines:
	row = list(map(int, row))
	for x in range(len(row)):
		for num in row:
			if (row[x] != num) and (row[x] % num == 0):
				checksum.append(row[x] / num)
				print (row[x] / num)

print (sum(checksum))
