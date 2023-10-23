import os   #allows code to interact with operating systems
import csv  #states the code will be using a csv file
budget_csv_path = os.path.join("resources", "budget_data.csv")  #defining variable as path to data source

with open(budget_csv_path, 'r') as csv_file:    #making the data source a readable csv file
    budget_csv = csv.reader(csv_file)   #defining variable as readable file
    
    
    total_change = 0    #initialising total change variable as 0
    months = 1     #initialising months variable as 1 (because the loop using this variable skips the first row of the data source)
    header = next(budget_csv)   #creating variable to store header row as next row
    first_row = next(budget_csv)    #creating variable to store data source first data row (as reference for following variables)
    total_income = 0   #initialising total variable as 0
    total_income += int(first_row[1])  #COUNTING variable to store values of data values in the 2nd column of data source
    previous_value = int(first_row[1])  #TRACKING variable to store data values to manipulate data
    max_increase = int(first_row[1])    #TRACKING variable to store greatest increase in data
    max_decrease = int(first_row[1])    #TRACKING variable to store greatest decrease in data

    #for loop utilising TRACKING variables to create variables storing totals for total months, total income & change values (difference in profits between months)

    for row in budget_csv:  
        months += 1 
        current_value = int(row[1])
        change = current_value - previous_value
        total_change += change
        previous_value = int(row[1])

        #if function stored within for loop to properly track max increase & decrease in profit (change variable) values.

        if change > max_increase:   
            max_increase = change
            max_increase_date = row[0]
        elif change < max_decrease:
            max_decrease = change
            max_decrease_date = row[0]
    

average_change = total_change/(months-1)    #creates overall average change in profits across the entire data sets timeline
average_change = round(average_change,2)    #rounds the overall average change to 2 decimal places for more appropriate display of data

#final display template

print("")
print("Financial Analysis")
print("")
print("------------------------------")
print("")
print("Total Months:",months)
print("Total: $",total_income)
print("Average Change: $",average_change)
print("Greatest Increase in Profits:",max_increase_date,"$",max_increase)
print("Greatest Decrease in Profits:",max_decrease_date,"$",max_decrease)