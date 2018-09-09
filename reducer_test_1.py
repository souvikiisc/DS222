#!/usr/bin/env python3

#from itertools import groupby
#from operator import itemgetter
import sys
import math



totalw_class_count = dict()
prior_count = dict()
p_word_count = dict()
vocab = set()
classes = set()

def load_values():

	f = open('ref1','r')


	for line in f.readlines():
		try:
			cl, word, count = line.split('\t')
		except ValueError:
			continue

		try:
			count = int(count)
		except ValueError:
			continue

		p_word_count[(cl, word)] = count
		vocab.add(word)

	f.close()

	f = open('ref2', 'r')

	for line in f.readlines():

		try:
			cl, count = line.split('\t')
		except ValueError:
			continue
		try:
			count = int(count)
		except ValueError:
			continue

		prior_count[cl] = count
		classes.add(cl)

	f.close()

	f = open('ref3', 'r')

	for line in f.readlines():

		try:
			cl, count = line.split('\t')
		except ValueError:
			continue

		try:
			count = int(count)
		except ValueError:
			continue

		totalw_class_count[cl] = count
	f.close()




def main(separator='\t'):

	load_values()

	total_docs = 0

	for v in prior_count.values():
		total_docs += v

	class_prob = dict()

	current_class = None
	current_word = None
	word = None
	word_count = 0
	class_count = 0
	class_word_count = dict()
	current_doc_n = -1

	acc = 0
	doc_count = 0
	# current_doc = None
	# current_doc_count = 0

	results = dict()

	vocab_visited = set()

	for line in sys.stdin:

		# print(line)

		#line = line.strip()

		try:
			key, count = line.split('\t', 1)
		except ValueError:
			continue

		try:
			doc_n, c, word = key.split()
		except ValueError:
			continue

		try:
			doc_n = int(doc_n)

		except ValueError:
			continue

		try:
			count = int(count)

		except ValueError:
			continue

		vocab_visited.add(word)

		if not results.__contains__((doc_n, c)):
			temp = dict()
			for cl in classes:
				temp[cl] = math.log(float(prior_count[cl]) / total_docs) + float(math.log(float(p_word_count.get((cl, word), 0.0) + 1) / (totalw_class_count.get(cl, 0) + len(vocab))))

			results[(doc_n,c)] = temp

		else:
			temp = results.get((doc_n, c))

			for cl in classes:
				temp[cl] +=  float(math.log(float(p_word_count.get((cl, word), 0.0) + 1) / (totalw_class_count.get(cl, 0) + len(vocab))))

			results[(doc_n, c)] = temp


	# vocab_not_visited = set()

	# for w in vocab:
	# 	if w not in vocab_visited:
	# 		vocab_not_visited.add(w)
	#
	# print(len(vocab_not_visited))
	# print(len(vocab))

	# for w in vocab_not_visited:
	#
	# 	for key in results.keys():
	#
	# 		temp = results.get(key)
	#
	# 		for cl in classes:
	# 			temp[cl] += float(math.log(float(p_word_count.get((cl, w), 0.0) + 1) / (totalw_class_count.get(cl, 0) + len(vocab))))
	#
	# 		results[key] = temp



	prev_key = None
	prev_count = -1

	keys = list(results.keys())

	sorted_keys = sorted(keys, key = lambda x : x[0])

	for key in sorted_keys:

		if(prev_key != key[0]):
			prev_key = key[0]
			doc_count += 1
			prev_count = 0

		t = results[key]

		pred_key = max(t.keys(), key = lambda k : t[k])

		if pred_key == key[1] and prev_count == 0:
			acc += 1
			prev_count = 1

	print('%s\t%f'%('accuracy', (float(acc)/doc_count)))



	#print ('%s\t%d' % ('class_count', class_count))





if __name__ == "__main__":
	main()
