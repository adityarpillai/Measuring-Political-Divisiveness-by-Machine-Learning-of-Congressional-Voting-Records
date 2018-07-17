import sys
import pandas as pd

def main(data_file, result_file):
    df = pd.read_csv(data_file)
    df.set_index(["session", "trial"], inplace=True)
    df = df.loc[(slice(None), "mean"), :]
    df.reset_index(inplace=True)
    df.set_index("session", inplace=True)
    df.drop(columns=["trial"], inplace=True)

    return df



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: python regression.py <house.csv> <senate.csv> <result.xlsx>\n")
        exit(-1)
    house_df, senate_df = main(sys.argv[1], sys.argv[3]), main(sys.argv[2], sys.argv[3])
    writer = pd.ExcelWriter(sys.argv[3])
    house_df.to_excel(writer,'House')
    senate_df.to_excel(writer,'Senate')
    writer.save()
