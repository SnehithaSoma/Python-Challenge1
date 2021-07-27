import csv

#Storing the file location
file="D:/Materials/python-challenge1/PyPoll/Resources.csv"
#Defining variables needed accordingly while calculating the votes and winner
votes=0
correy_votes=0
li_votes=0
o_votes=0
khan_votes=0
max_votes = 0
#Reading the file and moving the pointer to the first row of the election dataset
with open(file,'r',encoding="utf-8",newline="") as csv_file:
    csv_reader= csv.reader(csv_file,delimiter=",")
    header=next(csv_reader)
    for row in csv_reader:
        #Calculating total number of votes
        votes = votes+1
       #Calculating individual votes of all the candidates 
        if row[2]=="Khan":
            khan_votes += 1
        if row[2]=="Correy":
            correy_votes += 1
        if row[2]=="Li":
            li_votes +=1
        if row[2]=="O'Tooley":
            o_votes +=1

    candidates_votes= {"Khan": khan_votes, "Correy": correy_votes,"Li": li_votes,"O'Tooley":o_votes} 

#Finding the winner with maximum number of votes
    for candidate,value in candidates_votes.items():
        if value > max_votes:
            max_votes=value
            winner=candidate

 #Function to calculate the vote percentage           
def percentage (part, whole):
    return 100 * float(part)/float(whole)        

#Print Statements
print('\n')
print(f'Election Results')
print(f'-------------------------------')
print(f'Total Votes: {votes}')
print(f'Khan: {percentage(khan_votes,votes):.3f}%  ({khan_votes})')
print(f'Correy: {percentage(correy_votes,votes):.3f}%  ({correy_votes})')
print(f'Li: {percentage(li_votes,votes):.3f}%  ({li_votes})')
print(f'O Tooley: {percentage(o_votes,votes):.3f}%  ({o_votes})')
print("-----------------------------")
print(f'Winner: {winner}')
print("-----------------------------")


# Output File
output_file="D:/Homework/Python-Challenge1/PyPoll/analysis.txt"
with open(output_file,'w') as output_file:
    output_file.write('\n')
    output_file.write(f'Election Results' + '\n')
    output_file.write(f'-------------------------------' +'\n')
    output_file.write(f'Total Votes: {votes}' + '\n')
    output_file.write(f'Khan: {percentage(khan_votes,votes):.3f}%  ({khan_votes})' +'\n')
    output_file.write(f'Correy: {percentage(correy_votes,votes):.3f}%  ({correy_votes})' +'\n')
    output_file.write(f'Li: {percentage(li_votes,votes):.3f}%  ({li_votes})'+'\n')
    output_file.write(f'O Tooley: {percentage(o_votes,votes):.3f}%  ({o_votes})'+'\n')      
    output_file.write("-----------------------------"+'\n')
    output_file.write(f'Winner: {winner}'+'\n')
    output_file.write("-----------------------------")