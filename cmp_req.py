"""
https://florian-dahlitz.de/articles/create-your-own-diff-tool-using-python
add to dictionary and sort
group servers together
"""
import difflib
import sys
from compare_versions import ReqDicts


file1 = open('files_2_compare/int.txt').readlines()
file2 = open('files_2_compare/prod.txt').readlines()
output_file = 'diff.html'

if output_file:
    delta = difflib.HtmlDiff().make_file(
        file1, file2,
    )
    with open(output_file, "w") as f:
        f.write(delta)
else:
    delta = difflib.ndiff(file1, file2)
    sys.stdout.writelines(delta)
