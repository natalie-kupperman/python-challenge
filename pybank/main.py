#import modules
import os
import cv

#import csv(s)
#budget1_csv = os.path.join("budget_data_1.csv")

#budget2_csv = os.path.join("budget_data_1.csv")

#set variables to track

total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]

#create lists to add the data
date = []
revenue = []

#resource to read file
with open(budget1_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #loop through rows of csv
    for row in csvreader:
        
        #calculate total months
        total_months = total_months + 1

        #calculate total revenue
        total_revenue = total_revenue + int(row[1])

        #calculate revenue change
        revenue_change = int(row[1]) - prev_revenue

        #reset previous revenue
        prev_revenue = int(row[1])

        #determine greatest increase in revenue
        if revenue_change >  greatest_increase[1]
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        #Add date
        split_date = row[0].split("-")
        month.append(split_date[0])
        year.append(split_date[1])

        #Add price
        price.append(row[2])

