import decisiontree

def main_house(trials):
    # Currently working for House
    for x in range(1, 115):
        num = "{:03}".format(x)
        print("House " + num)
        votes_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/house/H" + num + "_votes.csv"
        members_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/house/H" + num + "_members.csv"

        # result_f = open("../results/house.txt", "w")

        for x in range(trials):
            print("Trial " + str(x) + ": ", end="\t")
            array = decisiontree.main(votes_f, members_f)
            for item in array:
                print(item, end="\t")
            print()
        print()

def main_senate(trials):
    # Currently working for House
    for x in range(1, 115):
        num = "{:03}".format(x)
        print("Senate " + num)
        votes_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/senate/S" + num + "_votes.csv"
        members_f = "/Users/adityapillai/Projects/Measuring-Political-Divisiveness-by-Machine-Learning-of-Congressional-Voting-Records/data/senate/S" + num + "_members.csv"

        # result_f = open("../results/house.txt", "w")

        for x in range(trials):
            print("Trial " + str(x) + ": ", end="\t")
            array = decisiontree.main(votes_f, members_f)
            for item in array:
                print(item, end="\t")
            print()
        print()     
        
if __name__ == "__main__":
    # main_house(5)
    main_senate(5)
