# to find the maximum occuring words in a file of text and to find maximum counted word and print it


# to store all the words and its occurance count
fname = input('Enter a file name: ')
fh = open(fname)
count = {}

for line in fh:
	words = line.split()		# split doesn't need rstrip()
	for word in words:
		count[word] = count.get(word, 0) + 1

print(count)

# to find the maximum occuring word and its count
maxcount = None
maxword = None

for word, num in count.items():
	if maxcount is None or num > maxcount:
		maxcount = num
		maxword = word

print(maxword, maxcount)