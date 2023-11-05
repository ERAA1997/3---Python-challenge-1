#used the import function to import modules "os" and "csv"

import os
import csv

#used to tell python where our csv file is located

csvpath = os.path.join('Resources', 'budget_data.csv')

#Defining the variables that will be used in the for loop
Total_Months = 0
Total = 0
Average_Change = 0.0
Greatest_increase = 0
Greatest_increase_month = ""
Greatest_decrease = 0
Greatest_decrease_month = ""
Previous_profit = 0
Total_change = 0

#opening the file and telling python what the delimiter is
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    Header = next(csvreader)
    
#The for loop that calculates and stores the outcomes in the variables above
    for row in csvreader:
        month = row[0]
        amount = int(row[1])
        Total_Months +=1 
        Total += amount
        if Total_Months >1:
            change =  amount - Previous_profit
            Total_change += change
            if change > Greatest_increase:
                Greatest_increase = change
                Greatest_increase_month = month
            if change < Greatest_decrease:
                Greatest_decrease = change
                Greatest_decrease_month = month      
        Previous_profit = amount 

#the list of results that will be printed in the terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${round(Total_change/(Total_Months - 1),2)}")
print(f"Greatest Increase in Profits {Greatest_increase_month} ${Greatest_increase}")
print(f"Greatest Decrease in Profits {Greatest_decrease_month} ${Greatest_decrease}")

#code used to create and write to a new text file, what is to be written and that following each print the next appears one line below
with open("analysis/PyBankexport.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("------------------------\n")
    f.write(f"Total Months: {Total_Months}\n")
    f.write(f"Total: ${Total}\n")
    f.write(f"Average Change: ${round(Total_change/(Total_Months - 1),2)}\n")
    f.write(f"Greatest Increase in Profits {Greatest_increase_month} ${Greatest_increase}\n")
    f.write(f"Greatest Decrease in Profits {Greatest_decrease_month} ${Greatest_decrease}\n")