import csv
import os

file_to_load = os.path.join("Resources/election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = "" 
winning_count = 0
winning_percentage = 0
counties_options = []
counties_votes = {}
winning_counties = ""
turnout_count = 0
turnout_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        counties_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
         
        if counties_name not in counties_options:
            counties_options.append(counties_name)
            counties_votes[counties_name] = 0
        counties_votes[counties_name] += 1

with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    print("County Votes:")
    txt_file.write("County Votes:\n")

    for counties in counties_votes:
        voter_turnout = counties_votes[counties]
        voter_turnout_percentage = float(voter_turnout) / float(total_votes) * 100
        counties_results = (f"{counties}: {voter_turnout_percentage: .1f}% ({voter_turnout:,})\n")
        print(counties_results)
        txt_file.write(counties_results)

        if (voter_turnout > turnout_count) and (voter_turnout_percentage > turnout_percentage):
            turnout_count = voter_turnout
            winning_counties = counties
            turnout_percentage = voter_turnout_percentage

    winning_counties_summary = (
        f"-------------------\n"
        f"Largest County Turnout: {winning_counties}\n"
        f"-------------------\n")
    print(winning_counties_summary)
    txt_file.write(winning_counties_summary)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage =  float(votes) / float(total_votes) * 100
        #print(f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate 
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    #print(counties_options)
    #print(counties_votes)
