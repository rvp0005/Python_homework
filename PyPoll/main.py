import os
import csv

election_csv = os.path.join("..", "..", "Instructions", "PyPoll", "Resources", "election_data.csv")

results = {}
total = 0
candidates=[]

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)

    for row in csvreader:
        total = total + 1
        if row[2] not in results:
            results[row[2]] = 1 

        else:
            results[row[2]] = results[row[2]] + 1

    candidates=list(results.keys())
    print(f"The candidates with votes were: {candidates}.")
    print(f"The total number of votes cast was {total}.")
    for keys, values in results.items():
        percent = round(((int(values)/total)*100), 4)
        print (f"{keys}: {values} total votes | {percent}%")
    winner = [(value, key) for key, value in results.items()]
    print("The winner is: ",max(winner)[1])
