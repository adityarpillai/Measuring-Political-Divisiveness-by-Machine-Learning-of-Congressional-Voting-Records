import decisiontree
from scripts.features import get_features
import sys
import pandas as pd
import numpy as np

def main_house(excel, sessions, trials):
    
    # Create a DataFrame that is first sorted by session, then by trial
    df = pd.DataFrame(columns=["session", "trial"])
    df = df.set_index(["session", "trial"])

    # Iterate over every session upto the session (inclusive)
    for x in range(1, sessions + 1):
        print("Calculating house session " + str(x))
        # Find the num of x such that it is in a string form with 3 digits
        num = "{:03}".format(x)

        # Create link for votes file
        votes_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/house/H" + num + "_votes.csv"
        # Create link for members file
        members_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/house/H" + num + "_members.csv"

        membervotes_df = get_features(votes_f, members_f)
        membervotes_df.fillna(0, inplace=True)

        # Run a trial for trials number of times 
        for trial in range(1, trials + 1):
            print("\tOn trial #" + str(trial))
            # Run the decisiontree
            arr = decisiontree.decisiontree(membervotes_df.copy())

            # Cycle through the array and add the score
            for x in range(len(arr)):
                df.at[(num, trial), "person_" + "{:03}".format(x + 1)] = arr[x] 

        # Calculate the average and standard deviation for each trial
        average = []
        standard_dev = []

        # Iterate from person_001 to person_<trial>
        for col in df.loc[num]:
            # Get the list of col as numbers
            values = df.loc[num][col].tolist()

            # Calculate average and standard deviation on the list
            avg = np.mean(values)
            std = np.std(values)

            # Append calculated average and standard deviation to the lists
            average.append(avg)
            standard_dev.append(std)

        # Append average and standard deviation lists to the session under
        # trials "mean" and "std_dev"
        df.loc[(num, "mean"), :] = average
        df.loc[(num, "std_dev"), :] = standard_dev

    # Create an Excel Writer to write to an Excel spreadsheet
    writer = pd.ExcelWriter(excel)
    df.to_excel(writer,'House')
    writer.save()

def main_senate(excel, sessions, trials):
    
    # Create a DataFrame that is first sorted by session, then by trial
    df = pd.DataFrame(columns=["session", "trial"])
    df = df.set_index(["session", "trial"])

    # Iterate over every session upto the session (inclusive)
    for x in range(1, sessions + 1):
        print("Calculating senate session " + str(x))

        # Find the num of x such that it is in a string form with 3 digits
        num = "{:03}".format(x)

        # Create link for votes file
        votes_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/senate/S" + num + "_votes.csv"
        # Create link for members file
        members_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/senate/S" + num + "_members.csv"

        membervotes_df = get_features(votes_f, members_f)
        membervotes_df.fillna(0, inplace=True)

        # Run a trial for trials number of times 
        for trial in range(1, trials + 1):
            print("\tOn trial #" + str(trial))
            
            # Run the decisiontree
            arr = decisiontree.decisiontree(membervotes_df.copy())

            # Cycle through the array and add the score
            for x in range(len(arr)):
                df.at[(num, trial), "person_" + "{:03}".format(x + 1)] = arr[x] 

        # Calculate the average and standard deviation for each trial
        average = []
        standard_dev = []

        # Iterate from person_001 to person_<trial>
        for col in df.loc[num]:
            # Get the list of col as numbers
            values = df.loc[num][col].tolist()

            # Calculate average and standard deviation on the list
            avg = np.mean(values)
            std = np.std(values)

            # Append calculated average and standard deviation to the lists
            average.append(avg)
            standard_dev.append(std)

        # Append average and standard deviation lists to the session under
        # trials "mean" and "std_dev"
        df.loc[(num, "mean"), :] = average
        df.loc[(num, "std_dev"), :] = standard_dev

    # Create an Excel Writer to write to an Excel spreadsheet
    writer = pd.ExcelWriter(excel)
    df.to_excel(writer,'Senate')
    writer.save()
        
if __name__ == "__main__":

    main_house(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    main_senate(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
