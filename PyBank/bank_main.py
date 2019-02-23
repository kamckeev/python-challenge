import os
import csv
import numpy as np
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
        profit.append(int(i[1]))
    
    #print(profit)
#The net total amount of "Profit/Losses" over the entire period

#profit_sum = 0
#for i in profit:
#    profit_sum += i
#print(profit_sum)

def list_sum(input_list):
    total = 0
    for i in input_list:
        total += i
    return(total)



change=[]
for i in range(len(profit)-1):
    this_change = profit[i+1]-profit[i]
    change.append(this_change)
    
avg_change = round(list_sum(change)/len(change),2)

#reducing avg_change to two decimal points to represent money


#The greatest increase in profits (date and amount) over the entire period
max_profit= max(change)


#The greatest decrease in losses (date and amount) over the entire period
min_profit= min(change)

#want to find the index of the min&max profits, then use that index to return a date
def profit_date(input_profit):
    profit_index=change.index(input_profit)
    month_index = profit_index+1
    #date = (months.index(month_index))
    date = months[month_index]
    return(date)
max_date = profit_date(max_profit)
min_date = profit_date(min_profit)
  #list.index(element)

#print to textfile:
#print to txt file
output_path= os.path.join('..','PyBank', 'Bank_txt.txt')
with open(output_path, "w") as textfile:
    print('{:*^50}'.format(''), file=textfile)
    print(f'Total months in study: {len(months)} months',file=textfile)
    print(f'Average change was: ${(avg_change)}', file=textfile)
    print('{:^50}'.format('~'), file=textfile)
    print(f'This is the total profit: ${(list_sum(profit))}',file=textfile)
    print(f'Maximum profit: ${max_profit} and happened in {max_date}.', file=textfile)
    print(f'Minimum profit: ${min_profit} and happened in {min_date}.', file=textfile)
    print('{:*^50}'.format(''),file=textfile)

#print to terminal:
print('{:*^50}'.format(''))
print(f'Total months in study: {len(months)} months')
print(f'Average change was: ${(avg_change)}')
print('{:^50}'.format('~'))
print(f'This is the total profit: ${(list_sum(profit))}')
print(f'Maximum profit: ${max_profit} and happened in {max_date}.')
print(f'Minimum profit: ${min_profit} and happened in {min_date}.')
print('{:*^50}'.format(''))