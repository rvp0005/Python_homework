#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period



import os
import csv

budget_csv = os.path.join("..", "..", "Instructions", "PyBank", "Resources", "budget_data.csv")

date= []
proloss= 0
nummonth= 0

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)
    
    for row in csvreader:
        nummonth = nummonth + 1
        proloss += int(row[1])
        maxincrease= max(row[1])
        


    print("Financial Analysis")
    print("-------------------------------------------------------------------------------------")
    print(f"Total number of months is {nummonth}")
    print(f"The net profit and loss was {proloss}")
    print(f"The average change in 'Profit/Losses' between months was {proloss / nummonth}")
    print(f"The greatest increase in profits was {maxincrease}")


