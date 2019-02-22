import os
import csv
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
   

#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
#You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: 
# Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
    months=[]
    profit=[]
    for i in csvreader:
        months.append(i[0])
        profit.append(i[1])
    #print(len(months))
 
#The net total amount of "Profit/Losses" over the entire period
    def net_profit()
        (i for i in list(profit))/2
    print()
#def net_volume()

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period