# copyright 2021

import os
import sys
import re
import csv
import platform
from shutil import copyfile
from os import listdir
from os.path import isfile, join

# The formatter formats leetcode solutions ie removing indentations, class definitions, etc. 

# # ---- find spaces only
# spaces_p = "[' '][^A-Za-z0-9.()\\{},=<>;:+-]"
# spaces_c = re.compile(spaces_p)
# ---- find variables only
params_p = r"\b(?!self,|int|str|bool|tuple|List\b)[^\s,{}:\[.*\] -]\w*"
params_c = re.compile(params_p)
# ---- find name of main function
defname_p = r"[^def ]*\w*\b[$(]"
defname_c = re.compile(defname_p)
# ---- find filename
# filename_p = ""
# filename_c = re.compile(filename_p)
# find first word in line
keyword_p = r'[ ][^A-aZ-z0-9<>=+-]'
keyword_c = re.compile(keyword_p)


# in case someone contributes code with the xrange function. Converts it to range for 3.0 users
if int(sys.version[0]) > 2:
	xrange = range

# tuple for fast lookup: replace dir to your desired location. 
fdir = tuple(os.listdir("C:\\Users\\abasp\\Documents\\GitHub\\leetspeed"))
inp = open("C:\\Users\\abasp\\Documents\\GitHub\\leetspeed\\input.txt", 'r+')
out = open("C:\\Users\\abasp\\Documents\\GitHub\\leetspeed\\output.txt", 'r+')

def main():
	filename = ''
	spaces = ' '
	def setName(f_name):
		str1 = ""
		de = defname_c.findall(f_name)[0][:-1]
		str1 = str(de) + ".py" 
		return str1
	# Gets the params inside parenthesis and deletes the unnecessary content ie string, list, etc
	def getparams(s):
		x = params_c.findall((s[s.index("(")+1:s.index(")")]))
		# print(x)
		for i in range(len(x)):
			if len(x) > 1 and i < len(x)-1 and x[i]:
				x[i] = str(x[i])
				x[i] += ','
			else:
				x[i] = str(x[i])
		def listToString(s):
			str1 = " "
			return (str1.join(s))
		s = s.replace(s[s.index("(")+1:s.index(")")],listToString(x))
		s = s.replace(s[s.index(")")+1:len(s)],':')
		return s
	def writeFile():
		for line in inp:
			# print(storeVal[2],storeVal[4]*storeVal[2],line, base)
			# # don't write line if class is present
			if "class" in line:
				continue
			if "def" in line:
				line = getparams(line)
			length = len(keyword_c.findall(line))
			line = '{} \n'.format(line.strip())
			out.write('{}{}'.format(spaces*(length - 2), line))
		inp.close()
		out.close()
	writeFile()
	# def makePy():
	# # make py file (IN-PROGRESS)
	# if filename not in fdir:
	# 	# catches value error and renames files appropriately i.e output.py,output2.py,etc
	# 	try:
	# 		int(var[len(var)-4:])
	# 		print("no files exist, making file")
	# 		copyfile("C:\\Users\\user\\Documents\\GitHub\\leetcode_solution_compare_tool\\output.txt","C:\\Users\\user\\Documents\\GitHub\\leetcode_solution_compare_tool\\{}".format(filename))
	# 	except ValueError:
	# 		print("file exists, making {}2.py".format(var))
	# else:
	# 	copyfile("C:\\Users\\user\\Documents\\GitHub\\leetcode_solution_compare_tool\\output.txt","C:\\Users\\user\\Documents\\GitHub\\leetcode_solution_compare_tool\\{}".format(filename))
if __name__ == "__main__":
	main()
