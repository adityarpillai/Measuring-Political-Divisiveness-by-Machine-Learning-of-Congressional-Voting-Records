# sys is only needed when running from file directly, so it can read argv
import sys

# importing pandas to use dataframe
import pandas as pd

# possibly not needed
from collections import defaultdict

def get_features(votes_file, party_file):
    """ 
        Takes in VoteView's votes and party files for any given chamber and
        returns a Pandas Dataframe of data of congressmen, party code, and 
        votes.

        |  icpsr  |  party_code  |  Vote 1  |  ...  |  Vote N  |
        |  12345  |    Code 1    |    9     |  ...  |     0    |

        icpsr is the identification for members of Congress, and party_code is
        the identification for parties of Congress.

        Documentation for the data in the CSV files are available at VoteView's 
        CSV documentation.

        https://voteview.com/static/docs/csv_docs.html
    """

    '''
        Open both files so errors appear before time-intensive calculations are
        made.

        The votes_df DataFrame follows the following (example) format:
           congress chamber  rollnumber  icpsr  cast_code   prob
        0         1   House           1    154          6   61.1
        1         1   House           1    259          9   99.6
        2         1   House           1    379          1  100.0
        3         1   House           1    649          1   59.2
        4         1   House           1    786          1   97.7

        The party_df DataFrame follows the following (yet another example
        format:
           congress    chamber  icpsr  ...  party_code  ...  
        0         1  President  99869  ...        5000  ...
        1         1      House   4766  ...        5000  ...
        3         1      House   8457  ...        5000
        4         1      House   9062  ...        5000  ...
    '''
    votes_df = pd.read_csv(votes_file)
    party_df = pd.read_csv(party_file)

    # Search through the party_df DataFrame by the icpsr so that we can quickly
    # get access to party codes later
    party_df = party_df.set_index("icpsr")

    '''
        Create a new DataFrame that follows this format:
        |  icpsr  |  party_code  |  vote_1  |  ...  |  vote_n  |
        |  12345  |    Code 1    |    9     |  ...  |     0    |

        This DataFrame can be searched by icpsr.
    '''
    # Create only icpsr and party_code columns, as vote_1 ... vote_n will be
    # added later. Also, set_index to be icpsr.
    df = pd.DataFrame(columns=["icpsr", "party_code"])
    df = df.set_index("icpsr")

    # Cycle through every vote and add it to a new DataFrame
    for vote in votes_df.iterrows():

        # Get second value from the tuple of (index, data)
        vote = vote[1]

        # Temporarily store icpsr
        icpsr = vote["icpsr"]
        
        # Check if icpsr already exists in the indices of the df
        if not (icpsr in df.index):
            # Create it since it doesn't already exist
            
            # Find the party code in the party_df DataFrame
            party_code = party_df.loc[icpsr]["party_code"]

            # Add the party code to the df
            df.at[icpsr, "party_code"] = party_code
        
        # Now add the current vote's cast code to that congressperson's 
        # vote_<rollnumber>
        df.at[icpsr, "vote_" + str(vote["rollnumber"])] = vote["cast_code"]
        
    # Return the df
    return df
    
    # Create a list of icpsr's excluding 
    
    # for person in party_df:

if __name__ == "__main__":
    """
        If features.py is called directly, it will output the results of 
        get_features with the votes file and members file being the first and
        second argument vectors, respectively.
    """

    # Ensure that there are two 
    if(len(sys.argv) != 3):
        print("Usage: python features.py <votes.csv> <members.csv>\n")
        exit(-1)
    
    print(get_features(sys.argv[1], sys.argv[2]))