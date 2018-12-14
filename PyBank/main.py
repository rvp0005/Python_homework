import os
import csv

budget_csv = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")

date= []
Total_profit= 0
nummonth= 0
change = 0
profitdiff= []
newprofit = 0
proloss = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)
    
    for row in csvreader:
        nummonth = nummonth + 1
        Total_profit += int(row[1])
        diffprofit = int(row[1]) - newprofit
        newprofit = int(row[1])
        profitdiff.append(diffprofit)
        
   
    profitdiff.pop(0)
    #print(profitdiff)

    totalprofitdiff= round((sum(profitdiff) / (nummonth - 1)),2)
    #print(totalprofitdiff)

    maxincrease= max(profitdiff)
    maxdecrease= min(profitdiff)

    print("Financial Analysis")
    print("--------------------------------------------------------")
    print(f"Total number of months is {nummonth}")
    print(f"The net profit and loss was ${Total_profit}")
    print(f"The average change in 'Profit/Losses' between months was ${totalprofitdiff}")
    print(f"The greatest increase in profits was ${maxincrease}")
    print(f"The greatest loss in profits was ${maxdecrease}")


f= open("Banking_results.txt", 'w+')
f.write("Financial Analysis\n")
f.write("--------------------------------------------------------\n")
f.write(f"Total number of months is {nummonth}\n")
f.write(f"The net profit and loss was ${Total_profit}\n")
f.write(f"The average change in 'Profit/Losses' between months was ${totalprofitdiff}\n")
f.write(f"The greatest increase in profits was ${maxincrease}\n")
f.write(f"The greatest loss in profits was ${maxdecrease}\n")