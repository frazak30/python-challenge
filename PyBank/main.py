# Import modules
import os
import csv

# declare variables 
ave_change = 0.000
total_months = 0
total = 0
greatest_increase = 0
greatest_decrease = 0 

# declare budget list array 
budget = []

# declare budget_variance list array
budget_variance = []

# declare path to csv
csvpath = os.path.join("dataset","budget_data.csv")

#print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
      # print(row)
      # load rows into budget array
      budget.append(row)

# populate budget_variance array
for i in range(1, len(budget)):
    budget_variance.append(int(budget[i][1]) - int(budget[i - 1][1]))
    total += int(budget[i - 1][1])
    if i == (len(budget) - 1):
        total = total + int(budget[i][1])

# define function to calculate average variance
def calculate_variance():
    change = format(sum(budget_variance) / len(budget_variance), '.3f')
    return change

def find_month_variance(variance): 
    
    for x in range(0, len(budget_variance)): 
        if budget_variance[x] == int(variance): 
            return budget[x + 1][0]    
            break    
        
# calculate results
ave_change = calculate_variance()
total_months = len(budget)
greatest_increase = max(budget_variance)
greatest_decrease = min(budget_variance)

month_greatest_increase = find_month_variance(greatest_increase)
month_greatest_decrease = find_month_variance(greatest_decrease)

# print formatted results
print("Financial Analysis")
print("--" * 20)
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${ave_change}")
print(f"Greatest Increase in Profits: {month_greatest_increase} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {month_greatest_decrease} ${greatest_decrease}")


# open a new text file with "write" mode.
file = open("analyis.txt", "w")

# write the results to the text file
file.write("Financial Analysis\n")
file.write("-" * 20)
file.write(f"\nTotal Months: {total_months}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${ave_change}\n")
file.write(f"Greatest Increase in Profits: {month_greatest_increase} ${greatest_increase}\n")
file.write(f"Greatest Decrease in Profits: {month_greatest_decrease} ${greatest_decrease}\n")

# make sure the file is closed
file.close()

