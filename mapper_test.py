#!/usr/bin/env python3

#from itertools import groupby
#from operator import itemgetter
import sys
import re

stop_words = {"some", "don", "she", "wasn't", "didn't", "once", "it", "between", "which", "s", "these",
			  "such", "me", "few", "from", "will", "same", "whom", "needn", "very", "through", "are", "she's", "we", "down", "off", "against",
			  "here", "o", "above", "when", "him", "he", "if", "am", "who", "haven't", "do", "has", "should", "you", "mustn't", "a", "again", "had", "up",
			  "ve", "weren", "yours", "their", "only", "her", "them", "aren", "not", "shouldn", "ourselves", "your", "too", "hasn", "most", "until", "d", "did", "all", "ma", "won't",
			  "no", "after", "wouldn", "didn", "of", "with", "t", "you'd", "couldn", "so", "doesn", "wouldn't", "ours", "there", "don't", "hadn", "needn't", "aren't", "its", "now",
			  "mightn", "yourselves", "you'll", "doing", "can", "but", "you've", "in", "other", "wasn", "and", "further", "won", "own", "they", "an", "how", "this", "because", "than",
			  "hadn't", "before", "were", "just", "as", "having", "isn", "himself", "during", "what", "couldn't", "ain", "into", "shouldn't", "weren't", "does", "was", "is", "that'll",
			  "about", "nor", "themselves", "while", "y", "mustn", "you're", "myself", "where", "at", "yourself", "doesn't", "itself", "i", "re", "each", "why", "those", "theirs", "to",
			  "both", "that", "his", "below", "ll", "mightn't", "should've", "haven", "it's", "any", "out", "being",
			  "shan", "then", "isn't", "herself", "hasn't", "under", "have", "on", "hers", "m", "over", "our", "shan't", "for", "more", "be", "or", "the", "my", "by", "been", }

def main():

    doc_count = 0
    for line in sys.stdin:

        line = line.lower()

        try:
            classes, sentence = line.split(' \t')

        except ValueError:
            continue
        try:
            classes = classes.split(',')
        except ValueError:
            continue

        for c in classes:

            words = sentence.split(' ')

            for word in words[2:]:

                temp = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', word)
                for w in temp:

                    # print(w)

                    if not w == '' and not w.isdigit() and w not in stop_words:
                        # w = stem.stem(w)
                        print('%d %s %s\t%d' % (doc_count, c, w, 1))

            doc_count += 1

            # print('%s %s\t%d' % (c,'~', 1))

if __name__ == "__main__":
	main()