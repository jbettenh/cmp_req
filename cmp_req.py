import difflib
import sys

file1 = open('files_2_compare/int.txt').readlines()
file2 = open('files_2_compare/prod.txt').readlines()

delta = difflib.ndiff(file1, file2)
sys.stdout.writelines(delta)