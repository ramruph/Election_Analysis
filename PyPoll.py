#Data that needs to be delivered
#1. total number of votes cast
#2. A complete list of candidates who received votes
#3 Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#add dependencies

import os
import csv
#assining variable from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#assining variable to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Candidate list
candiatate_options = []

#Candidate dictionary
candidate_votes = {}

#1. initialize total votes counter
total_votes = 0

#Determine the winning candidate
winning_candidate = ""
winning_count = 0
winning_percent = 0

#Open election results and read the file 
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read header row
    headers = next(file_reader)
    print(headers)
 
    #Print each row in the CSV file
    for row in file_reader: 
        #increment total votes count
        total_votes += 1
       
        #print the candidate name for each row   
        candidate_name = row[2]

        #If candidate does not match existing candidate 
        if candidate_name not in candiatate_options:
            
            #add name to list
            candiatate_options.append(candidate_name)

            candidate_votes[candidate_name]= 0

        candidate_votes[candidate_name] += 1


with open(file_to_save, "w") as txt_file:
    election_results=("Election Results\n"
    "-----------------------\n"
    "Total Votes: {:,} \n"
    "-----------------------\n".format(total_votes))

    print(election_results)

    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = ("\n {} : {:.1f} % ({:,}) \n".format(candidate_name,vote_percentage,votes))

        #print each candidate and their vote count AND PERCENTAGE
        print(candidate_results)
        
        txt_file.write(candidate_results)


        if (votes>winning_count) and (vote_percentage>winning_percent):

            winning_count = votes

            winning_percent = vote_percentage

            winning_candidate = candidate_name

            win_summary =("--------------------------------------------------------\n"
            "Winner: {}\n"
            "Winning Vote Count: {:,}\n"
            "Winning Percentage: {:.1f}%\n"
            "--------------------------------------------------------".format(winning_candidate,winning_count,winning_percent))    
    
    print(win_summary)

    txt_file.write(win_summary)

#Created .txt file and writing on it




