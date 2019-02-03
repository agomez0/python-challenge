import os
import csv

csvpath = ('election_data.csv')

f = open("data.txt", "w")

#Prints out to console and text file
def outputPrint(text):
    f.write(text + "\n")
    print(text)

#Rounds to the third decimal place
def perc(votes):
        perc = (votes/len(all_votes)) * 100
        return("%0.3f" % (perc))

with open(csvpath, newline='') as csvfile:
    
    candidates = []
    all_votes = []
    sum0 = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    starter = 0

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        #Add all votes to a list
        all_votes.append(row[2])
        #If the current candidate is not already in the candidates list, add it
        #This list holds all candidates that are running
        if row[2] not in candidates:
            candidates.append(row[2])

    #If any of the votes match one of the candidates in the list, increase candidate's votes by 1      
    for x in range(len(all_votes)):
        if all_votes[x] == candidates[0]:
            sum0 += 1
        elif all_votes[x] == candidates[1]:
            sum1 += 1
        elif all_votes[x] == candidates[2]:
            sum2 += 1
        elif all_votes[x] == candidates[3]:
            sum3 += 1
        else:
            pass

    #Add each candidate's sum of votes to a list
    votes_list = [sum0, sum1, sum2, sum3]
    for x in range(len(votes_list)):
        #If the current candidate's sum of votes is higher then the previous, that candidate becomes the winner
        if votes_list[x] > starter:
            winner = candidates[x]
            starter = votes_list[x]

    #Print to console and text file in an efficient way
    outputPrint("Election Results")
    outputPrint("-------------------------")
    outputPrint(f"Total Votes: {len(all_votes)}")
    outputPrint("-------------------------")
    outputPrint(f"{candidates[0]}: {perc(sum0)}% ({sum0})")
    outputPrint(f"{candidates[1]}: {perc(sum1)}% ({sum1})")
    outputPrint(f"{candidates[2]}: {perc(sum2)}% ({sum2})")
    outputPrint(f"{candidates[3]}: {perc(sum3)}% ({sum3})")
    outputPrint("-------------------------")
    outputPrint(f"Winner: {winner}")
    outputPrint("-------------------------")