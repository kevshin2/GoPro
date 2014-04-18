import sys

def parser(file, f_name):
	line_count = 0
	word_count = 0
	char_count = 0
	for line in file:
		line_count += 1
		word_count += len(line.split())
		char_count += len(list(line))
	print str(line_count) + " " + str(word_count) + " " + str(char_count) + " " + f_name


if __name__ == '__main__':
	f_name = str(sys.argv[1])
	f = open(f_name, 'r')
	parser(f, f_name)