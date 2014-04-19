import sys, re
from collections import Counter

def parser(file, f_name, ignore):
	line_count, word_count, char_count = 0, 0 , 0
	nword_count, nchar_count, difference = 0, 0, 0
	cnt = Counter()
	for line in file:
		char_count += len(list(line))
		line_count += 1
		word_count += len(line.split())
		for word in filter(None, re.split(('\W+'), line)):
			if word.lower() not in ignore:
				nword_count += 1
			else:
				difference += len(word)
				#cnt[word.lower()] += 1
	nchar_count = char_count - difference
	#print cnt
	print "all: " + str(line_count) + " " + str(word_count) + " " + str(char_count) + " " + f_name
	print "proper: " + str(line_count) + " " + str(nword_count) + " " + str(nchar_count)


if __name__ == '__main__':
	f_name = str(sys.argv[1])
	f = open(f_name, 'r')
	#ignore = ["with"]
	ignore = ["i", "we", "you", "they", "a", "and", "the", "that", "of", "for", "with"]
	parser(f, f_name, ignore)
