import sys, csv
from collections import defaultdict
from pprint import pprint

# Takes in both votes and information about members of Congress to create both a list for classifications and a list of features for each member of Congress

# sys.argv[1] = votes csv file
# sys.argv[2] = members csv file

def get_features():
    if(len(sys.argv) != 3):
        print("\npython features.py [votes csv] [members csv]\n")
        exit(-1)

    # Open the votes file
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

    # Open the party file and save it to the party_information list
    with open(sys.argv[2], 'r') as f:
        reader = csv.reader(f)
        party_information = list(reader)

    # Create a dictionary of party members to their party codes
    party_dict = dict()
    for person in party_information:
        party_dict[person[2]] = person[6]
    
    features = []
    votes = []

    # Add each member of Congress to two lists (one for their classification and one for their features)
    for member in congresspeoples:
        features.append(party_dict[member])
        votes.append(congresspeoples[member])

    return(features, votes)

if __name__ == "__main__":
    get_features()