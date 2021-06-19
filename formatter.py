# copyright 2021

import os
import sys
import re
import csv
import platform
import regexp as rp
import routes as fl
import getparams as gp
from shutil import copyfile
from os import listdir
from os.path import isfile, join
# from ctypes import * 

# in case someone contributes code with the xrange function. Converts it to range for 3.0 users
if int(sys.version[0]) > 2:
	xrange = range

# tuple for fast lookup: to replace dir to your desired location. 
fdir = tuple(os.listdir("C:\\Users\\user\\Documents\\GitHub\\leetcode_solution_compare_tool"))

def main():
	fs = fl.inp
	fsw = fl.out
	base,res = 0,0
	filename = ''
	# returns the number of spaces needed to maintain indentation after lines are stripped
	def _getspaces(line, base, res):
		f = rp.spaces_c.findall(line)
		w = len(f)*2
		if base == 0:
			base = max(w,base)
		elif base != 0:
			base = min(w,base)
		s = ''
		res = w - base
		for i in range(res):
			s += ' '
		return [s,base,w,res]
	for line in fs:
		if "class" in line:
			continue
		else:
			base = 4
		if "def" in line:
			line = gp.getparams(line)
			filename = gp.setName(line)
		base = _getspaces(line,base,res)[1]
		lineSpace = _getspaces(line,base,res)[0]
		line = '{} \n'.format(line.strip())
		fsw.write('{}{}'.format(lineSpace,line))
	fs.close()
	fsw.close()

	# make py file (IN-PROGRESS)
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