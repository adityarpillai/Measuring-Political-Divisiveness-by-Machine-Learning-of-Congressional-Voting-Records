# Necessary to read file from running this as a script
import sys, csv

# Creates a dictionary of empty lists for each of the members of congress
from collections import defaultdict

# Sklearn's decision tree implementation
from sklearn import tree

# Diagnosis of issues
from pprint import pprint

def main():
  # print(len(sys.argv))
  if len(sys.argv) != 2:
      print("\nERROR: No filename specified, or too many command line variables.")
      print("RUN AS: decisiontree.py [filename]\n")
      exit(0)

  # Reads CSV file passed through sys args
  with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

  total_rollcalls = int(data[len(data) - 1][2])
  # print([0] * total_rollcalls)
  congresspeoples = defaultdict(lambda: [0] * total_rollcalls)

  # Create a dictionary where the key is the icpsr of the congressperson and the pair is the list of their votes
  for vote in data[1:]:
    # Unused
    session = vote[0]
    chamber = vote[1]
    probability = vote[5]

    # Used
    rollnumber = int(vote[2]) # An identifier for what was voted on
    icpsr = vote[3] # An identiier for the person that was voting
    cast_code = int(vote[4]) # How they voted
    (congresspeoples[icpsr])[rollnumber - 1] = cast_code

  # Testing to show if length of each congressperson is the same
  # for key in congresspeoples:
  #   print(key, end=" ")
  #   print(len(congresspeoples[key]))

  # pprint(congresspeoples)
  
  
  # for person in congresspeoples:


   
if __name__ == "__main__":
  main()
