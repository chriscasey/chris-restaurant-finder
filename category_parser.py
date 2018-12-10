

def main():
    filepath = 'categories.txt'
    raw_lines = []
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            raw_lines.append(line)
            line = fp.readline()
    for line in raw_lines:
        line_1 = line.split('(')
        line_2 = line_1[1].split(",")
        print line_2[0]


if __name__ == "__main__":
    main()
