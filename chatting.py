def Read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as c:
        for line in c:
            lines.append(line.strip())
    return lines 
def Convert_file(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
		    new.append(person + ': '+ line)
	return new
def Write_file(filename, lines):
	with open(filename, 'w') as w:
		for line in lines:
			w.write(line + '\n')
	

	




def main():
    lines = Read_file('input.txt')
    lines = Convert_file(lines)
    Write_file('output.txt', lines)
    
main()
