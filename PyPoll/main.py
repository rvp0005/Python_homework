#https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python

import os
import csv

election_csv = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

totalvotes= 0
#makes a list called candidates
candidates= []
#makes a dictionary called vote counts
#each key will be a candidate and it'll keep track of votes per candidate as it moves through the rows
vote_count= {}
vote_count2={}
percentvotes = 0

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)

    for row in csvreader:
        #will tally up total number of votes as it goes row by row
        totalvotes = totalvotes + 1

        #If the third column (who they voted for) isn't yet in the candidates list or dictionary "vote count"
        #then add the candidates name to the candidate list and add the candidate to the dictionary "vote_count" plus add one vote
       # if row[2] not in candidates and row[2] not in "vote_count":
        if row[2] not in candidates and row[2] not in "vote_count":
            candidates.append(row[2])
            vote_count[row[2]] = 1        
        
        #but if the candidate is already in the list, then simply just add one to to the vote count dictionary
        if row[2] in candidates and row[2] not in "vote_count":
            vote_count[row[2]] = vote_count[row[2]] + 1
    
    numcand = len(vote_count)

#to calculate percent votes for each candidate
    for canname in vote_count:
        votes= vote_count[canname]
        name = canname
        percentvotes=str(round((votes/totalvotes), 2))
        #vote_count2 = {"name": canname}, {"votes": votes}, {"percent_votes": percentvotes}
        print(f"{name} had {votes} total votes for {percentvotes}% of the total votes")

    #print(candidates)
    #print(totalvotes)
   

