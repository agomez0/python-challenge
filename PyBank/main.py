import os
import csv

csvpath = ('budget_data.csv')
f = open("data.txt", "w")

#Prints out to console and text file
def outputPrint(text):
    f.write(text + "\n")
    print(text)

with open(csvpath, newline='') as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header row first
    csv_header = next(csvreader)
    
    profitlist = []
    total = 0
    previous_amt = 0
    greatesti = 0
    greatestd = 0

    for row in csvreader:

        #Cast profit amount into an integer
        amount = int(row[1])
        #Add up total profit for all months
        total = amount + total
        #Add profit from every month to a list
        profitlist.append(amount)

        #Change in profit
        current_change = amount - previous_amt

        #If the current change in profit is greater than the greatest increase so far then...
        if current_change > greatesti:
            #Current month becomes the one to hold the greatest increase
            greatesti = current_change
            gimonth = row[0]

        #If the current change in profit is less than the greatest decrease so far then...
        elif current_change < greatestd:
            #Current month becomes the one to hold the greatest decrease
            greatestd = current_change
            gdmonth = row[0]

        #stores profit amount of current row to find change in profit of the following month
        previous_amt = int(row[1])

    #Subtracts the last profit value from the first    
    avg_delta = profitlist[len(profitlist)-1] - profitlist[0]

    #Print to console and text file in an efficient way
    outputPrint("Financial Analysis")
    outputPrint("----------------------------")
    outputPrint(f"Total months: {len(profitlist)}")
    outputPrint(f"Total: ${total}")
    outputPrint(f"Average Change: ${round(avg_delta/(len(profitlist) - 1), 2)}")
    outputPrint(f"Greatest Increase in Profits: {gimonth} (${greatesti})")
    outputPrint(f"Greatest Decrease in Profits: {gdmonth} (${greatestd})")