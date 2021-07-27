import csv
#Storing the file location
file="D:/Materials/python-challenge/PyBank/Resources.csv"

#definitions all the lists and variables needed accordingly along the script
months=[]
profits=[]
monthly_change=[]
max_change=0
min_change=0
total =0

#Reading the file and moving the pointer to first row of data
with open(file,'r',encoding="utf-8",newline="") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    #Moving the pointer to first line of the dataset
    header=next(csv_reader)       
    
    for row in csv_reader:
        #Appending the months and Profits lists accordingly
        months.append(row[0])  
        profits.append(int(row[1]))        
     #Calculating the difference of monthly profit/loss
    for i in range(len(profits)-1):           
        monthly_change.append(profits[i+1]-profits[i])
# Finding the maximum and minimum change from the list created above with differences
max_change = max(monthly_change)
min_change = min(monthly_change)      
#  Finding the months associated with the Max and Min change.( +1 because the month associated in the change is next month) 
max_month = monthly_change.index(max(monthly_change)) + 1
min_month = monthly_change.index(min(monthly_change)) + 1    

#Print Statements in the Terminal
print("Financial Analysis")
print("--------------------------")
print(f'Total Months: {len(months)}')   
print(f'Total :${sum(profits)}')
print(f'Average Change: {round(sum(monthly_change)/len(monthly_change),2)}')
print(f'Greatest Increase in Profits: {months[max_month]} (${(str(max_change))})')
print(f'Greatest Decrease in Profits: {months[min_month]} (${(str(min_change))})')

#Output file
output_file="D:/Homework/Python-Challenge1/PyBank/analysis.txt"
with open(output_file,'w') as csv_output:
    # Writing the analysis into a textfile 
    csv_output.write("Financial Analysis")
    csv_output.write("\n")
    csv_output.write(f'Total Months: {len(months)}') 
    csv_output.write("\n")
    csv_output.write(f'Average Change: {round(sum(monthly_change)/len(monthly_change),2)}')
    csv_output.write("\n")
    csv_output.write(f'Greatest Increase in Profits: {months[max_month]} (${(str(max_change))})')
    csv_output.write("\n")
    csv_output.write(f'Greatest Decrease in Profits: {months[min_month]} (${(str(min_change))})')
    csv_output.write("\n")

    
