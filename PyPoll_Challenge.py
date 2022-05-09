# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add Our Dependencies.
import csv
import os

# Add A Variable To Load A File From A Path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add A Variable To Save The File To A Path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize A Total Vote Counter.
total_votes = 0

# Candidate Options And Candidate Votes.
candidate_options = []
candidate_votes = {}

# 1: Create A County List And County Votes Dictionary.
county_list = []
county_votes = {}


# Track The Winning Candidate, Winning Vote Count, And Winning Percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track The Largest County And County Voter Turnout.
largest_county = ""
county_votes = 0


# Read The CSV And Convert It Into A List Of Dictionaries.
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read The Header.
    header = next(reader)

    # For Each Row In The CSV File.
    for row in reader:

        # Add To The Total Vote Count.
        total_votes = total_votes + 1

        # Get The Candidate Name From Each Row.
        candidate_name = row[2]

        # 3: Extract The County Name From Each Row.
        county_name = row[2]


        # Add The Candidate Name To The Candidate List If It Does Not Match Any Existing Candidate.
        
        if candidate_name not in candidate_options:

            # Add The Candidate Name To The Candidate List.
            candidate_options.append(candidate_name)

            # Begin Tracking The Voter Count Of The Candidate.
            candidate_votes[candidate_name] = 0

        # Add A Vote To The Voter Count Of The Candidate.
        candidate_votes[candidate_name] += 1

        # 4A: Write An If Statement To Check That The County Does Not Match Any Existing County On The County List.
        if county_name not in county_list:


            # 4B: Add The Existing County To The County List.
            county_list.append(county_name)

            # 4C: Begin Tracking The Voter Count Of The County.
            candidate_votes[county_name] = 0

        # 5: Add A Vote To The Voter Count Of The County.
        candidate_votes[county_name] += 1


# Save The Results To Our Text File.
with open(file_to_save, "w") as txt_file:

    # Print The Final Vote Count To The Terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6A: Write A For Loop To Get The County Name From The County Dictionary.
    for county_name in range (county_votes): 

        # 6B: Retrieve The Voter Count Of The County.
        
        county_votes = county_votes[county_name]

        # 6C: Calculate The Percentage Of Votes From The County.
    vote_percentage = float (county_votes) / float(total_votes) * 100

         # 6D: Print The Results From The County To The Terminal.
    county_results = (
      f"{county_name}: {vote_percentage:.1f}% ({county_votes:,})\n")

    print(county_results)

         
         # 6E: Save The Vote Count Results From The County To The Terminal.


         # 6F: Write An If Statement To Indicate The Winning County And To Obtain The Vote Count From It.
    if (county_votes > county_votes):
        largest_county = county_name



    # 7: Print The County With The Largest Voter Turnout To The Terminal.
    largest_county_summary = ( 

         f"-------------------------\n"

         f"Largest: {county_name}\n"

        f"-------------------------\n")

    print(largest_county_summary)

    # 8: Save The County With The Largest Voter Turnout To A Text File.
    txt_file.write(largest_county_summary)

    # Save The Final Vote Counts For The Candidate To A Text File.
    for candidate_name in candidate_votes:

        # Retrieve Vote Count And Vote Percentage.
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print The Vote Count And The Percentage Of Votes Obtained By Each Candidate To The Terminal.
        
        print(candidate_results)
        #  Save The Results Of The Candidate To The Text File.
        txt_file.write(candidate_results)

        # Determine The Winning Vote Count, The Winning Percentage, And The Winning Candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print The Information For The Winning Candidate To The Terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save The Name Of The Winning Candidate In The Terminal.
    txt_file.write(winning_candidate_summary)
