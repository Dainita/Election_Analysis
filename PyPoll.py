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

import csv
import os

csvpath = os.path.join("Resources", "election_results.csv")
election_results = os.path.join("Another Analysis", "election_analysis.txt")

with open(csvpath) as election_data:
  file_reader = csv.reader(election_data)
  print(election_data)

  headers = next(file_reader)
  print(headers)