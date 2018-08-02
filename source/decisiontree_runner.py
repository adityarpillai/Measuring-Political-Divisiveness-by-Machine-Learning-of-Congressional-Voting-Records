import decisiontree
from scripts.features import get_features
import sys
import pandas as pd
import numpy as np

BASE_FILE_LOCATION = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/"

def main_house(sessions, trials):
    """ Returns a DataFrame of test results in the House.
    
    sessions: number of sessions to test from 001 to sessions (inclusive).
    trials: number of trials of classification per session (randomized order of
                training data)

    DataFrame takes the format of 

    session	trial	person_001	    person_002      ...
    001	    1	    0.567164179	    0.567164179     ...
	        2	    0.567164179	    0.567164179     ...
	        3	    0.432835821	    0.52238806      ...
	        4	    0.432835821	    0.432835821     ...
	        5	    0.567164179	    0.567164179     ...
	        mean	0.513432836	    0.531343284     ...
	        std_dev	0.065807187	    0.05221748      ...
    002     1           ...             ...         ...
    ...     ...         ...             ...         ...

    where person_001, person_002, person_n is the training size used and the
    variable measured is the successrate of the DecisionTree model.

    """
    # Create a DataFrame that is first sorted by session, then by trial
    df = pd.DataFrame(columns=["session", "trial"])
    df = df.set_index(["session", "trial"])

    # Iterate over every session upto the session (inclusive)
    for x in range(1, sessions + 1):
        print("Calculating house session " + str(x))
        # Find the num of x such that it is in a string form with 3 digits
        num = "{:03}".format(x)

        # Create link for votes file
        dataframe_f = BASE_FILE_LOCATION + "compiled_data/house/H" + num + "_dataframe.csv"

        membervotes_df = pd.read_csv(dataframe_f)

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

    return df 

def main_senate(sessions, trials):
    """ Returns a DataFrame of test results in the House.
    
    sessions: number of sessions to test from 001 to sessions (inclusive).
    trials: number of trials of classification per session (randomized order of
                training data)

    DataFrame takes the format of 

    session	trial	person_001	    person_002      ...
    001	    1	    0.567164179	    0.567164179     ...
	        2	    0.567164179	    0.567164179     ...
	        3	    0.432835821	    0.52238806      ...
	        4	    0.432835821	    0.432835821     ...
	        5	    0.567164179	    0.567164179     ...
	        mean	0.513432836	    0.531343284     ...
	        std_dev	0.065807187	    0.05221748      ...
    002     1           ...             ...         ...
    ...     ...         ...             ...         ...

    where person_001, person_002, person_n is the training size used and the
    variable measured is the successrate of the DecisionTree model.

    """
    
    # Create a DataFrame that is first sorted by session, then by trial
    df = pd.DataFrame(columns=["session", "trial"])
    df = df.set_index(["session", "trial"])

    # Iterate over every session upto the session (inclusive)
    for x in range(1, sessions + 1):
        print("Calculating senate session " + str(x))

        # Find the num of x such that it is in a string form with 3 digits
        num = "{:03}".format(x)

        # Create link for votes file
        dataframe_f = BASE_FILE_LOCATION + "compiled_data/senate/S" + num + "_dataframe.csv"

        membervotes_df = pd.read_csv(dataframe_f)

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

    return df
        
if __name__ == "__main__":

    writer = pd.ExcelWriter(sys.argv[1] + ".xlsx")
    
    house_df = main_house(int(sys.argv[2]), int(sys.argv[3]))
    house_df.to_csv(sys.argv[1] + "_house.csv")
    house_df.to_excel(writer,'House')
    senate_df = main_senate(int(sys.argv[2]), int(sys.argv[3]))
    senate_df.to_csv(sys.argv[1] + "_senate.csv")
    senate_df.to_excel(writer,'Senate')
    writer.save()
    
