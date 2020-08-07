#Data that needs to be delivered
#1. total number of votes cast
#2. A complete list of candidates who received votes
#3 Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#add dependencies

import os
import csv

#assinging variable from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#####while loop to open and read the file
with open(file_to_load) as election_data:

    #To Do: read and analyze the data

    #Read the file object with the reader function

    file_reader = csv.reader(election_data)


    #print header row

    headers = next(file_reader)
    print(headers)


#Assinging a variable to a path
##Created .txt file and writing on it

file_to_save = os.path.join("analysis","election_analysis.txt")


with open(file_to_save,"w") as txt_file:
    txt_file.write("Counties in the Election \n")
    txt_file.write("------------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson ")

