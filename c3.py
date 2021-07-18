
a = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		a.append(line.strip())
for line in a:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	print(time)
	print(name)
