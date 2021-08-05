import os
import sys
import csv
import timeit
import subprocess
import output
# import formatter
from shutil import copyfile
from os import listdir
from os.path import isfile, join


# import timeit : done
# itterate through files :
# open file : done
# import file : done
# copy code :
# run timeit function on code :
# get problem number & compile speed :
# add values to database :
# close file : done

main_func = None

fs = open("C:\\Users\\abasp\\Documents\\github\\leetspeed\\output.py", 'r+')

for line in fs:
    if 'def' in line:
        print(line)

# def compare(a=1):
#     for i in range(a):
#         pass

# print(timeit.timeit(compare, number=100000))

fs.close()





