import sys, re

def parser(file, f_name, ignore):
	# the original overall count
	line_count, word_count, char_count = 0, 0 , 0
	# new count and the difference between the old char count
	# and the new char count
	nword_count, nchar_count, difference = 0, 0, 0

	# all the articles and sections
	art_sec = []

	# match all articles and sections
	match = re.compile(r'((?:Article|Section)\s*\d+)')

	# calculate all the counts
	for line in file:
		art_sec += re.findall(match, line)
		char_count += len(list(line))
		line_count += 1
		word_count += len(line.split())
		for word in filter(None, re.split(('\W+'), line)):
			if word.lower() not in ignore:
				nword_count += 1
			else:
				difference += len(word)
	nchar_count = char_count - difference
	
	# the total article count, total section count, and current 
	# section count
	art_count, sec_count, curr_sec = 0, 0, 0

	# Each article and the count of sections
	articlelist = []

	# calculate all the section and article counts
	for item in art_sec:
		if "Article" in item:
			if art_count != 0:
				articlelist.append("\tArticle " + str(art_count) + ": " + str(curr_sec))
				art_count += 1
				sec_count += curr_sec
				curr_sec = 0
			else:
				art_count += 1
		else:
			curr_sec += 1

	# print out all the results
	print "all: " + str(line_count) + " " + str(word_count) + " " + str(char_count) + " " + f_name
	print "proper: " + str(line_count) + " " + str(nword_count) + " " + str(nchar_count)
	print "Total Articles: " + str(art_count)
	print "Total Sections: " + str(sec_count)
	print "Total Sections per Article:"
	for article in articlelist: print article



if __name__ == '__main__':
	f_name = str(sys.argv[1])
	f = open(f_name, 'r')
	ignore = ["i", "we", "you", "they", "a", "and", "the", "that", "of", "for", "with"]
	parser(f, f_name, ignore)
