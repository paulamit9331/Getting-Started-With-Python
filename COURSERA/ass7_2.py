"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the 
average of those values and produce an output as shown below. Do not use the sum() function or a 
variable named sum in your solution.
"""

fname = input("Enter file name: ")
fh = open(fname)
ans = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #start = line.find(":")
    fval = float(line[line.find(":") + 1 :].lstrip())
    ans = ans + fval
    count = count + 1
print("Average spam confidence:",(ans / count))
