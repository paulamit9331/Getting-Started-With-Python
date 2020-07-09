# count the no of times a name will occur
"""
names = ['amit', 'anindya', 'akash', 'nilanjan', 'debmalya']
count = {}

for name in names:
	if not name in dic:
		count[name] = 1
	else:
		count[name] = count[name] + 1

print(count)
"""
# or we can use below process ->

names = ['amit', 'anindya', 'akash', 'nilanjan', 'debmalya']
count = {}

for name in names:
	count[name] = count.get(name, 0) + 1	# if name doesn't exist set count[name] = 0; otherwise add 1 to the previous count

print(count)