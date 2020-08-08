# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge starter code."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties_list = []

counties_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
large_tunout = ""
large_votes = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        counties_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if counties_name not in counties_list:

            # 4b: Add the existing county to the list of counties.
            counties_list.append(counties_name)

            # 4c: Begin tracking the county's vote count.
            counties_votes[counties_name] = 0

        # 5: Add a vote to that county's vote count.
        counties_votes[counties_name] += 1
        

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        "\nElection Results\n"
        "------------------------------------\n"
        "Total Votes: {:,}\n"
        "------------------------------------\n\n"
        "County Votes:\n".format(total_votes))

    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a repetition statement to get the county from the county dictionary.
    for counties_name in counties_votes:
        # 6b: Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
        countyvote = counties_votes.get(counties_name)
        # 6c: Calculate the percent of total votes for the county.

        county_percent = float(countyvote)/float(total_votes) * 100
         # 6d: Print the county results to the terminal.
        county_results = ("{} : {:.1f} %  ({:,})\n".format(counties_name, county_percent, countyvote))

        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (countyvote> large_votes):

            large_votes = countyvote
            large_tunout = counties_name

# 7: Print the county with the largest turnout to the terminal.
    lturn = ("\n-------------------------------------\n"
    "Largest County Turnout: {} \n"
    "------------------------------------\n".format(large_tunout))

    print(lturn)
    # 8: Save the county with the largest turnout to a text file.

    txt_file.write(lturn)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = ("\n{}: {:.1f}% ({:,})\n".format(candidate_name,vote_percentage,votes))


        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        "------------------------------------\n"
        "Winner: {}\n"
        "Winning Vote Count: {:,}\n"
        "Winning Percentage: {:.1f}%\n"
        "------------------------------------\n".format(winning_candidate,winning_count,winning_percentage))

    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
