import os
import csv

election_csv = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

totalvotes= 0
#makes a list called candidates
candidates= []
#makes a dictionary called vote counts
#each key will be a candidate and it'll keep track of votes per candidate as it moves through the rows
vote_count= {}

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)

    for row in csvreader:
        #will tally up total number of votes as it goes row by row
        totalvotes = totalvotes + 1

        #If the third column (who they voted for) isn't yet in the candidates list or dictionary "vote count"
        #then add the candidates name to the candidate list and add the candidate to the dictionary "vote_count" plus add one vote
        if row[2] not in candidates and row[2] not in "vote_count":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        
        #but if the candidate is already in the list, then simply just add one to to the vote count dictionary
        elif row[2] in candidates and row[2] not in "vote_count":
            vote_count[row[2]] = vote_count[row[2]] + 1

#to calculate percent votes for each candidate
    for numvotes in vote_count:
        votes= vote_count[numvotes]
        print(votes/totalvotes)

    print(candidates)
    print(totalvotes)
    print(vote_count)

