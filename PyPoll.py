import csv
import os

csvpath = os.path.join("Resources", "election_results.csv")
election_results = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(csvpath) as election_data:
  file_reader = csv.reader(election_data)
  
  headers = next(file_reader)
  
  for row in file_reader:
    total_votes += 1
    candidate_name = row[2]
    if candidate_name not in candidate_options:
      candidate_options.append(candidate_name)
      candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1

with open(election_results, "w") as text_file: 
    election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n")
print(election_results, end="")
text_file.write(election_results)

for candidate_name in candidate_votes:
      votes = candidate_votes[candidate_name]
      vote_percentage = float(votes)/float(total_votes) * 100
      candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
      print(candidate_results)
      text_file.write(candidate_results)

      if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage        
        winning_candidate = candidate_name

      winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

print(winning_candidate_summary)
text_file.write(winning_candidate_summary)

