import csv

file = r"C:\Users\kekoj\Data Analytics Class\Module Challenges\Challenge 3\PyBank\Resources\budget_data.csv"
dates = []  
profits_losses = [] 
changes = [] 

greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None)

    
    previous_profit_loss = None

    for row in csvreader:
        Date = row[header.index("Date")]

        if Date:
            dates.append(Date)
            profit_loss = int(row[1])
            profits_losses.append(profit_loss)

            
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes.append(change) 

                if change > greatest_increase_amount:
                    greatest_increase_date = Date
                    greatest_increase_amount = change

                if change < greatest_decrease_amount:
                    greatest_decrease_date = Date
                    greatest_decrease_amount = change

            previous_profit_loss = profit_loss


total = len(dates)
totalPL = sum(profits_losses)

if total > 1:
    average_change = sum(changes[1:]) / (total - 1)
else:
    average_change = 0  

print(f"Total Months: {total}")
print(f"Total: ${totalPL}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

output_text = f"Total Months: {total}\n"
output_text += f"Total: ${totalPL}\n"
output_text += f"Average Change: ${average_change:.2f}\n"
output_text += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
output_text += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n"

output_file_path = r"C:\Users\kekoj\Data Analytics Class\Module Challenges\Challenge 3\PyBank\Resources\financial_analysis.txt"
with open(output_file_path, 'w') as output_file:
    output_file.write(output_text)