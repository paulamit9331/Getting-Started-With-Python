"""
9.4 Write a program to read through the mbox-short.txt and figure out who has 
sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to 
a count of the number of times they appear in the file. After the dictionary is produced, 
the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file:")
handle = open(fname)
emailCount = {}
emailList = []
for line in handle:
	if not line.startswith("From: "):	continue
	emailList.append(line.split()[1])

for email in emailList:
	emailCount[email] = emailCount.get(email, 0) + 1

maxCount = None
maxEmail = None
for email, count in emailCount.items():
	if maxCount is None or count > maxCount:
		maxCount = count
		maxEmail = email

print(maxEmail, maxCount)