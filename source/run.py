import decisiontree

def main_house():
    # Currently working for House
    for x in range(1, 115):
        num = "{:03}".format(x)
        votes_f = "../data/house/H" + num + "_votes.csv"
        members_f = "../data/house/H" + num + "_members.csv"
        print(decisiontree.main(votes_f, members_f))
        
if __name__ == "__main__":
    main_house()
