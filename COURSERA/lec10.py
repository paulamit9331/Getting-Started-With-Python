# read through lines in a text file and find top 10 occuring words and print it

fname = input("Enter file name: ")
handle = open(fname)
count = {}

for line in handle:
	words = lst.split()
	for word in words:
		count[word] = count.get(word, 0) + 1
"""
words = []
for key, val in count.items():
	words.append((val, key))

words = sorted(words, reverse = True)

or we can write the commented code as :
"""

words = sorted([(val, key) for key, val in count.items()], reverse = True)

for val, key in words[: 10]:
	print(key, val)