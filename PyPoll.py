# The Data We Need To Retrieve.
# 1. The Total Number Of Votes Cast. 
# 2. A Complete List Of Candidates Who Received Votes. 
# 3. The Percentage Of Votes Each Candidate Won. 
# 4. The Total Number Of Votes Each Candidate Won. 
# 5. The Winner Of The Election Based On The Popular Vote.


# Add Our Dependencies.

import csv

import os



# Assign A Variable For The File To Load And The Path.

file_to_load = os.path.join("Resources", "election_results.csv")


# Create A File Name Variable To A Direct Or Indirect Path To The File.

file_to_save = os.path.join("Analysis", "election_analysis.txt")



# Initialize A Total Vote Counter.

total_votes = 0



# Candidate Options And Candidate Votes.

candidate_options = []



# Declare An Empty Dictionary.

candidate_votes = {}



# Winning Candidate And Winning Count Tracker.

winning_candidate = ""

winning_count = 0

winning_percentage = 0



# Open The Election Results And Read The File.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

   

    # Read And Print The Header Row.

    headers = next(file_reader)
    
    

    # Print Each Row In The CSV File.

    for row in file_reader:


        # Add To The Total Vote Count.

        total_votes += 1


        # Print The Candidate Name From Each Row.

        candidate_name = row[2]


        # If The Candidate Does Not Match Any Existing Candidate.

        if candidate_name not in candidate_options:


            # Add It To The List Of Candidates.

            candidate_options.append(candidate_name)


           # Begin Tracking The Vote Count For The Candidate.

            candidate_votes[candidate_name] = 0


        # Add A Vote To The Vote Count For The Candidate.

        candidate_votes[candidate_name] += 1


        # Save The Results To Our Text File.

        with open(file_to_save, "w") as txt_file:


        # Print The Final Vote Count To The Terminal.

            election_results = (

                f"\nElection Results\n"

                f"-------------------------\n"

                f"Total Votes: {total_votes:,}\n"

                f"-------------------------\n")

            print(election_results, end="")

            # Save The Final Vote Count To The Text File.

            txt_file.write(election_results)



    # Determine The Percentage Of Votes For Each Candidate By Looping Through The Counts.

    # Iterate Through The Candidate List.

    for candidate_name in candidate_votes:

        # Retrieve The Vote Count Of A Candidate.

        votes = candidate_votes[candidate_name]

        # Calculate The Percentage Of Votes.

        vote_percentage = float(votes) / float(total_votes) * 100

    

        # Print Out Name Of Each Candidate, Vote Count Of Each Candidate, And Percent Of Votes Obtained By Each Candidate.

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        print(candidate_results)

        # Save The Results Of Each Candidate To Our Text File.

        txt_file.write(candidate_results)

        # Determine The Winning Vote Count, The Name Of Winning Candidate, And The Winning Vote Percentage.

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
  
    # Print Out Results Of The Winning Candidate.

    winning_candidate_summary = (


        f"-------------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count:,}\n"

        f"Winning Percentage: {winning_percentage:.1f}%\n"

        f"-------------------------\n")


print(winning_candidate_summary)

# Save The Results Of The Winning Candidate To Our Text File.

txt_file.write(winning_candidate_summary)





    

