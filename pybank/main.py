#PyBank

#import modules
import os
import csv

#input data directory for sustainability purposes
print("Check your working directory. Ensure the file is within your current working directory.")
input_csv = input("Which csv would you like to analyze? Type the exact file name without extension (e.g. data).  ")

#import csv
working_csv = os.path.join(input_csv + ".csv")

#resource to read file
with open(working_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    
    #set variables to track
    total_months = 0
    total_revenue = 0
    prev_revenue = 0
    avg_revenue_change = 0
    revenue_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = " "
    greatest_decrease_month = " "

    #loop through rows of csv
    for row in csvreader:
        
        #calculate total months
        total_months = total_months + 1

        #calculate total revenue
        total_revenue = total_revenue + int(row[1])

        #calcuate monthly revenue change
        revenue_change = int(row[1]) - prev_revenue

        #calculate average revenue change
        avg_revenue_change = (int(row[1]) - prev_revenue) + avg_revenue_change

        #determine greatest increase in revenue
        if revenue_change >  greatest_increase:
            greatest_increase = revenue_change
            greatest_increase_month = row[0]

        #determine greatest decreases in revenue
        if revenue_change < greatest_decrease:
            greatest_decrease = revenue_change
            greatest_decrease_month = row[0]

        #reset previous revenue
        prev_revenue = int(row[1])

#calculate average change per month
avg_revenue_change = avg_revenue_change/total_months

#print results to terminal
print(" ")
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + format(total_revenue, ',.2f'))
print("Average Revenue Change: $" + format(avg_revenue_change, ',.2f'))
print("Greatest Increase in Revenue: " + greatest_increase_month + "($" + format(greatest_increase, ',.2f') +")")
print("Greatest Decrease in Revenue: " + greatest_decrease_month + "($" + format(greatest_decrease, ',.2f')+ ")")

#write a new file with results
results_file = (input_csv + "_results.txt")

with open(results_file, "w", newline="") as results:
    txtwriter = csv.writer(results)

