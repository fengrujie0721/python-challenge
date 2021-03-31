import csv
import os

from dateutil.parser import parse
csvpath=os.path.join("resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    monthnumber=0
    total_profit_or_loss=0
    start_date="Jan-2010"
    end_date="Jan-2010"
    greatest_increase=0
    greatest_decrease= 0

    for row in csvreader:
        
        print(row)
        monthnumber+=1
        total_profit_or_loss+=int(row[1])
        if parse(str(row[0]))<=parse(start_date):
            start_date=row[0]
            start_profit_or_loss=int(row[1])
        if parse(str(row[0]))>=parse(end_date):
            end_date=row[0]
            end_profit_or_loss=int(row[1])
            
        if int(row[1])>int(greatest_increase):
            greatest_increase=row[1]
            greatest_increase_month=row[0]
        if int(row[1])<int(greatest_decrease):
            greatest_decrease=row[1]
            greatest_decrease_month=row[0]
    average_change=round((end_profit_or_loss-start_profit_or_loss)/monthnumber,2)
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total Months: {monthnumber}")
    print(f"Total: ${total_profit_or_loss}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    

    
    
    