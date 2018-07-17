
# Necessary to read file from running this as a script
import sys

# Sklearn's decision tree implementation
from sklearn import neural_network

# To get a features DataFrame from the CSV files
from scripts.features import get_features

def neuralnetwork(df):
  '''
  Takes DataFrame of members of Congress and their votes
  '''

  # Create a list of features excluding party_code
  features_cols = list(df.columns)
  features_cols.remove("party_code")

  # Shuffle the DataFrame
  df = df.sample(frac=1)

  # Create an empty list of scores for the classifier
  averages = []

  # Sample upto 30 (inclusive) Congressmen
  for x in range(1, 20):
    # Create a training dataset (list) with the first x congressmen
    training_features = df.iloc[:x][features_cols]

    # Create the classifiers
    training_classifiers = df.iloc[:x]["party_code"]

    # Create a Decision Tree classifier with 
    clf = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
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
      # Get a DataFrame of features
  df = get_features(sys.argv[1], sys.argv[2])
  df = df.fillna(0)
  print(neuralnetwork(df))
  

