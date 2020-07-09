fname = input("Enter the file nsme: ");
try:
	fhand = open(fname);	# to open the file
except:
	print("Can't open file")
	quit()	
inp = fhand.read();			# to read all the characters in the file including '\n'

print(inp[: 20]);			# prints upto index 19

#for line in fhand:			# prints thw every lines which starts with "From: " in the fhand
#	if line.startswith("From: "):
#		print(line)			# as print includes extra new line so we have to modify it

for line in fhand:
	line = line.rstrip();
	if not line.startswith("From: "):
		continue;
	print(line)