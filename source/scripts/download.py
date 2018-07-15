import urllib.request



def download():
    # Currently working for House
    for x in range(1, 115):
        num = "{:03}".format(x)
        votes_url = "https://voteview.com/static/data/out/votes/S" + num + "_votes.csv"
        # print(votes_url)
        votes_f = "/data/senate/S" + num + "_votes.csv"
        urllib.request.urlretrieve(votes_url, votes_f)
        members_url = "https://voteview.com/static/data/out/members/S" + num + "_members.csv"
        members_f = "/data/senate/S" + num + "_members.csv"
        urllib.request.urlretrieve(members_url, members_f)

download()