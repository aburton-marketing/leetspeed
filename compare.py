
import re
import os
import imp
import sys
import csv
import timeit
import importlib
import subprocess
from os import listdir
from shutil import copyfile
from formatter import getparams
from formatter import defname_c
from os.path import isfile, join


# import timeit : done
# itterate through files :
# open file : done
# import formatter : done
# run timeit function on code :
# get problem number & compile speed :
# add values to database :
# close file : done

def main():

    # Default values
    user_id = None
    problem_id = None
    main_func = None
    speed = None

    # Open the output file
    fs = open("C:\\Users\\abasp\\Documents\\github\\leetspeed\\output.py", 'r+')

    # Set main_func
    for line in fs:
        if 'def' in line:
            main_func = defname_c.findall(line)[0][:-1]
            break

    Set speed
    speed = timeit.timeit(main_func, number=100000)

    fs.close()

if __name__ == "__main__":
    main()



