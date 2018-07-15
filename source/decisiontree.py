# Necessary to read file from running this as a script
import sys, csv

# Sklearn's decision tree implementation
from sklearn import tree

if len(sys.argv) != 2:
    print("ERROR: decisiontree.py [filename]")
    exit

