"""
info = "from anindya1.sarkar@aot.edu.in on 5th April at 19:57"		# I want to extract the substring -> "aot.edu.in"

sindex = info.find('@');			# to get the distinct character index before aot.edu.in
lindex = info.find(' ', sindex);	# to find a space starting from '@' to find the last index

req = info[sindex + 1 : lindex]
print(req)
"""
# or we can use the below code:

info = "from anindya1.sarkar@aot.edu.in on 5th April at 19:57"

sinfo = info.split()[1].split('@')[1]
print(sinfo)