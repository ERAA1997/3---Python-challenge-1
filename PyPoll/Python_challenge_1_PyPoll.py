#used the import function to import modules "os" and "csv"
import os
import csv

#used to tell python where our csv file is located

csvpath = os.path.join('Resources', 'election_data.csv')

#Defining variable and empty dictionary
Total_votes = 0
Candidate_votes = {}

#opening the file and telling python what the delimiter is
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    Header = next(csvreader)

#The for loop that calculates and stores the outcomes in the empty dictionary
    for key in csvreader:
        Total_votes +=1
        if key[2] in Candidate_votes:
            key_to_update = key[2]
            current_candidate_votes = Candidate_votes[key_to_update]
            updated_candidate_votes = current_candidate_votes + 1
            Candidate_votes[key_to_update] = updated_candidate_votes
        else:
            Candidate_name = key[2]
            Candidate_votes[Candidate_name] = 1
            
#defining variables to make printing easier
Max = max(Candidate_votes, key=Candidate_votes.get)
CCS = Candidate_votes.get('Charles Casper Stockham')
DD = Candidate_votes.get('Diana DeGette')
RAD = Candidate_votes.get('Raymon Anthony Doane')       

#the list of results that will be printed in the terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {Total_votes}")
print("------------------------")
print(f"Charles Casper Stockham: {round((CCS/Total_votes)*100,3)}% ({CCS})")
print(f"Diana DeGette: {round((DD/Total_votes)*100,3)}% ({DD})")
print(f"Raymon Anthony Doane: {round((RAD/Total_votes)*100,3)}% ({RAD})")
print("------------------------")
print(f"Winner: {Max}")
print("------------------------")

#code used to create and write to a new text file, what is to be written and that following each print the next appears one line below
with open("analysis/PyPollexport.txt", "w") as f:
    f.write(f"Election Results\n")
    f.write("------------------------\n")
    f.write(f"Total Votes: {Total_votes}\n")
    f.write("------------------------\n")
    f.write(f"Charles Casper Stockham: {round((CCS/Total_votes)*100,3)}% ({CCS})\n")
    f.write(f"Diana DeGette: {round((DD/Total_votes)*100,3)}% ({DD})\n")
    f.write(f"Raymon Anthony Doane: {round((RAD/Total_votes)*100,3)}% ({RAD})\n")
    f.write("------------------------\n")
    f.write(f"Winner: {Max}\n")
    f.write("------------------------\n")