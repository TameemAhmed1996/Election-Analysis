# The Data we need to Retrieve.
# 1. The Total Number Of Votes cast. 
# 2. A Complete List of Candidates who Received Votes. 
# 3. The Percentage of Votes each Candidate Won. 
# 4. The Total Number Of Votes each Candidate Won. 
# 5. The Winner of The Election based on The Popular Vote.

# Add our Dependencies.

import csv

import os

# Assign A Variable for The File to Load and The Path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Create A File Name Variable to A Direct Or Indirect Path to The File.

file_to_save = os.path.join("Analysis", "election_analysis.txt")


# Open The Election Results and Read The File.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

   
    # Read And Print The Header Row.

    headers = next(file_reader)
    
    print(headers)

    

