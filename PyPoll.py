# Data to be retrieved
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
# Steps
# Open the data file.
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

import os
import csv

dir(csv)

csvpath = os.path.join('resources', 'election_results.csv')
print("\nfilepath = "+ csvpath)

with open(csvpath, "r") as election_data:
    lines = election_data.read()
    print(lines)
    print(type(lines))
