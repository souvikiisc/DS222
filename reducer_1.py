#!/usr/bin/env python3

#from itertools import groupby
#from operator import itemgetter
import sys



def main(separator='\t'):

	current_class = None
	current_word = None
	word = None
	word_count = 0
	class_count = 0

	class_word_count = 0
	bow = set()

	current_doc = None
	current_doc_count = 0

	prev_doc = None

	for line in sys.stdin:

		#print(line)

		#line = line.strip()



		try:
			key, count = line.split('\t', 1)
		except ValueError:
			continue

		try:
			c, word = key.split()
		except ValueError:
			continue

		try:
			count = int(count)

		except ValueError:
			continue

		if c == 'doc_count_unique':

			prev_doc = c

			if current_doc == word:
				current_doc_count += 1
			else:
				if current_doc:
					print('%s\t%s\t%d' % ('doc_count', current_doc, current_doc_count))

				current_doc_count = 1
				current_doc = word
			continue

		if(prev_doc == 'doc_count_unique'):
			print('%s\t%s\t%d' % ('doc_count', current_doc, current_doc_count))
			prev_doc = None

		if current_class != c:
			if current_class:
				print('%s\t%s\t%d' % ('class_total_word_count', current_class, class_word_count))
				#print('%s\t%s\t%d' % ('class_count', current_class, class_count))
			current_class = c
			class_count += 1

			class_word_count = 0


		if current_word == word:
			word_count += count

		else:

			if current_word:
				class_word_count += word_count
				print ('%s\t%s\t%s\t%d' % ('class_word_count', current_class, current_word, word_count))

			current_word = word
			word_count = count

	if current_word == word:
		print ('%s\t%s\t%s\t%d' % ('class_word_count',current_class, current_word, word_count))

	if current_doc == word:
		print('%s\t%s\t%d' % ('doc_count', current_doc, current_doc_count))

	if current_class == c:
		print ('%s\t%s\t%d' % ('class_total_word_count', c, class_word_count))

	#print ('%s\t%d' % ('class_count', class_count))





if __name__ == "__main__":
	main()
