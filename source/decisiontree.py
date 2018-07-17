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

def decisiontree(votes, members):
  # Get a DataFrame of features
  df = get_features(votes, members)
  df = df.fillna(0)

  # Create a list of features excluding party_code
  features_cols = list(df.columns)
  features_cols.remove("party_code")

  # Shuffle the DataFrame
  df = df.sample(frac=1)

  # Create an empty list of scores for the classifier
  averages = []

  # Sample upto 30 (inclusive) Congressmen
  for x in range(1, 31):
    # Create a training dataset (list) with the first x congressmen
    training_features = df.iloc[:x][features_cols]

    # Create the classifiers
    training_classifiers = df.iloc[:x]["party_code"]

    # Create a Decision Tree classifier with 
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(training_features, training_classifiers)

    # Define test values
    test_features = df[:][features_cols]
    test_classifiers = df[:]["party_code"]

    # Run score and append it to averages
    averages.append(clf.score(test_features, test_classifiers))

  return averages 
   
if __name__ == "__main__":
  if len(sys.argv) != 3:
      print("\nERROR: No filename specified, or too many command line variables.")
      print("RUN AS: decisiontree.py [votes filename] [members filename]\n")
      exit(0)
  print(decisiontree(sys.argv[1], sys.argv[2]))
  
