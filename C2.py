def Read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as c:
        for line in c:
            lines.append(line.strip())
    return lines 


def Convert_file(lines):
    allen_word = 0
    allen_s = 0
    allen_g = 0
    viki_word = 0
    viki_s = 0
    viki_g = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_s += 1
            elif s[2] == '圖片':
                allen_g += 1
            else:
                for m in s[2:]:
                    allen_word += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_s += 1
            elif s[2] == '圖片':
                viki_g += 1
            else:
                for m in s[2:]:
                    viki_word += len(m)
    print('allen傳了', allen_word, '個字')
    print('allen傳了', allen_g, '個圖片')
    print('allen傳了', allen_s, '個貼圖')
    print('viki傳了', viki_word, '個字')
    print('viki傳了', viki_g, '個圖片')
    print('viki傳了', viki_s, '個貼圖')


def main():
    lines = Read_file('LINE-Viki.txt')
    Convert_file(lines)


main()
