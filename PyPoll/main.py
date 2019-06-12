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
        perc = (votes/counter) * 100
        return("%0.3f" % (perc))

with open(csvpath, newline='') as csvfile:
    
    #List for all candidates
    candidates = []
    #Dictionary for each candidate's vote count
    votes = {}
    #Initiate the vote counter
    counter = 0

    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip the header
    csv_header = next(csvreader)

    for row in csvreader:

        #Add on to the vote counter
        counter += 1
        #Candidate's name
        candidate = row[2]

        #If the candidate is not in the current candidate's list...
        if candidate not in candidates:
            #Add it to the list
            candidates.append(candidate)
            #Add it to the dictionary and set the vote count to one
            votes[candidate] = 1
        else:
            #Add one to the candidate's current vote count
            votes[candidate] +=1

    #Find the candidate with the highest vote count
    winner = max(votes, key=votes.get)

    #Print to console and text file in an efficient way
    outputPrint("Election Results")
    outputPrint("-------------------------")
    outputPrint(f"Total Votes: {counter}")
    outputPrint("-------------------------")
    for candidate in candidates:
        outputPrint(f"{candidate}: {perc(votes[candidate])}% ({votes[candidate]})")
    outputPrint("-------------------------")
    outputPrint(f"Winner: {winner}")
    outputPrint("-------------------------")