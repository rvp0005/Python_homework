import os
import csv

election_csv = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

totalvotes= 0
candidates= []

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)

    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] not in candidates:
            candidates.append(row[2])
        
        for unique in candidates:
        unique_candidates_count.append(candidate.count(cands))
    
    print(Khan)
    print(Correy)
    print(candidates)
    print(totalvotes)

