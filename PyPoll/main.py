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

    print(f"ELECTION RESULTS")
    print(f"----------------------")
    candidates=list(results.keys())
    print(f"Candidates: {candidates}.")
    print(f"Total Votes: {total}.")


    for keys, values in results.items():
        percent = round(((int(values)/total)*100), 4)
        toprint= print(f"{keys}: {values} total votes | {percent}%")


    winner = [(value, key) for key, value in results.items()]
    #winnername = (print(f"The winner is: {max(winner)[1]}"))
    winnername = max(winner)[1]
    print(f"Winner: {winnername}")

 
f= open("Election_Results.txt", 'w+')
f.write(f"ELECTION RESULTS\n")
f.write("---------------------------\n")
f.write(f"Candidates: {candidates}\n")
f.write(f"Total votes: {total}\n")
for keys, values in results.items():
        percent = round(((int(values)/total)*100), 4)
        f.write(f"{keys}: {values} total votes | {percent}% \n")
#winner = [(value, key) for key, value in results.items()]
#f.write(fwinnername= print("The winner is: ",max(winner)[1])
f.write(f"Winner: {winnername}")