 f.write("ELECTION RESULTS")
    f.write("-------------------------------")
    f.write(f"Candidates: {candidates}")
    f.write(f"{keys}: {values} votes | {percent}%")
    f.write(f"The winner is: ",max(winner)[1])






















#https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python
#https://www.pythonforbeginners.com/dictionary/dictionary-manipulation-in-python

import os
import csv

election_csv = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

totalvotes= 0
candidates= []
vote_count= {}
percentvotes = 0
votes=0
results=[]
votenames=[]
candnames=[]

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
        
        if row[2] in candidates and row[2] not in "vote_count":
            vote_count[row[2]] = vote_count[row[2]] + 1

    for canname in vote_count:
        votes= vote_count[canname]
        name = [canname]
        percentvotes= (round((votes/totalvotes), 2))
        results.append(percentvotes)
        votenames.append(votes)
        candnames.append(name)

    results = {"The candidate": canname}, {"Total_Votes": int(votes)}, {"Percent_of_votes": percentvotes}
    print(results)
    
    #winner= results[results.index(max())]
        
        #print(f"{name} had {votes} total votes for {percentvotes}% of the total votes")
#print(percentvotes)  
#print(vote_count2)




    #print("Election Results")
    #print("-"*10)
    #print(f"Total Votes: {totalvotes}")
    #print("-"*10)
    #print(vote) ###

    #values = dict(vote_count.values())
    #winner= (max(values))



#    for key, value in vote_count.items():
#        print(key, value)
#        results.append(value)
#    print(results)
#    winner= max(results)
#    print(winner)

    #for k in vote_count.keys():
    #    print("The candidate", k, "had", vote_count[k], "number of votes")
    

    #print("Election Results")
    #print("-"*10)
    #print(f"Total Votes: {totalvotes}")
    #print("-"*10)
    #print(vote)