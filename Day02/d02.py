lines = []
with open('input') as file:
	for line in file:
		line = line[:-1]
		lines.append(line.split('\t'))
checksum = []
for row in lines:
	row = list(map(int, row))
	checksum.append(max(row) - min(row))

print (sum(checksum))
