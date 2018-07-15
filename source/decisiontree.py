# Necessary to read file from running this as a script
import sys, csv

# Creates a dictionary of empty lists for each of the members of congress
from collections import defaultdict

# Sklearn's decision tree implementation
from sklearn import tree

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Diagnosis of issues
from pprint import pprint

from scripts.features import get_features
from scripts.shuffle import unison_shuffle

def main():
  # print(len(sys.argv))
  if len(sys.argv) != 3:
      print("\nERROR: No filename specified, or too many command line variables.")
      print("RUN AS: decisiontree.py [votes filename] [members filename]\n")
      exit(0)

  (parties, features) = get_features(sys.argv[1], sys.argv[2])

  parties = np.array(parties)
  features = np.array(features)

  parties, features = unison_shuffle(parties, features)
  
  averages = []

  for x in range(1, 30):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features[:x], parties[:x])
    averages.append(clf.score(features, parties))

  # plt.plot(averages)
  # plt.show()
  print(averages)
   
if __name__ == "__main__":
  main()
