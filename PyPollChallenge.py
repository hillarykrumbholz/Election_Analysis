# GOALS: The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidtes who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidtae won.
# 5. The winner of the election based on popular vote.
# 6. Calculate the number of votes that were cast from each county.
# 7. Calculate the percentage of votes each county contributed to the election. 
# 8. Determine the County with the highest voter turnout. 

# Import the datetime dependency.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is, ", now)

# Add to our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources\election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create a list for the counties.
counties_options = []
# Declare the empty dictionary
counties_votes = {}

# Winning County and Tracker
winning_counties = ""
turnout_count = 0
turnout_percentage = 0

# Open the election results and read the file. 
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #print(election_data)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    #print(headers)

   # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # Print the county name from each row.
        counties_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county...
        if counties_name not in counties_options:
            # Add the county to the county list.
            counties_options.append(counties_name)
            # Begin tracking that county's voter turnout.
            counties_votes[counties_name] = 0
        # Add a vote to the county's voter turnout.    
        counties_votes[counties_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # GOAL 1: Get the total number of votes cast
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    # Mastery: Total votes printed to terminal and saved to text file
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Title for the County Votes.
    print("County Votes:")
    print("")
    # Save the County Votes header to the text file.
    txt_file.write("County Votes:\n")
    txt_file.write("\n")

    # GOAL 6 and 7: Calculate the number of votes and percentage that each county contributed to the election.
    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the counties list.
    for counties in counties_votes:
        # Retrieve voter turnout for each county.
        voter_turnout = counties_votes[counties]
        # Calculate the percentage of voter turnout
        voter_turnout_percentage = float(voter_turnout) / float(total_votes) * 100
        # Print each county's name, vote count, and percentage of votes
        counties_results = (f"{counties}: {voter_turnout_percentage: .1f}% ({voter_turnout:,})\n")
        # Mastery: Each county's total vote and percentage of vote is printed to the terminal and saves to the text file.
        print(counties_results)
        # Save the county results to the text file.
        txt_file.write(counties_results)

        # GOAL 8: Determine the county wiht the highest voter turnout.
        # Determine the winning voter turnout and county
        # Determine if the voter turnout is greater than the turnout count
        if (voter_turnout > turnout_count) and (voter_turnout_percentage > turnout_percentage):
            # If true, then set the turnout count to the voter turnout and the turnout percentage to the voter turnout percentage.
            turnout_count = voter_turnout
            winning_counties = counties
            turnout_percentage = voter_turnout_percentage

    # Print out the winning county to the terminal
    winning_counties_summary = (
        f"-------------------\n"
        f"Largest County Turnout: {winning_counties}\n"
        f"-------------------\n")
    # Mastery: The county with the highest voter turnout is printed to the terminal and saved to the text file.
    print(winning_counties_summary)
    # Save the winning county to the text file. 
    txt_file.write(winning_counties_summary)    

    # GOAL 2: Completed a list of candidates who received votes. 
    # GOAL 3 and 4: Calculate the number of votes and percentage of votes each candidate received.
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        #vote_percentage = int(votes) / int(total_votes) * 100
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
        # Mastery: Each candidate's total votes and percentage of votes are printed to the terminal and saved to the text file.
        # Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # GOAL 5: The winner of the election is determined based on popular vote.
        # Determine winning vote count and candidate
        # Determine if the vote is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage


    # To do: print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    # Mastery: The winner of the election, vote count, and winning percentage is printed to the terminal and saved to the text file. 
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate}: received {vote_percentage:.1f}% of the vote.")

    # 3. Print
    # Print the total votes
    #print(total_votes)

    # Print the candidate list.
    #print(candidate_options)

    #Print the candiate vote dictionary.
    #print(candidate_votes)

    # Print the counties list
    #print(counties_options) 

    # Print the counties vote dictionary.
    #print(counties_votes)
        
    # Close the file.
    #election_data.close()

# Create a filename variable to a direct or indorect path to the file. 
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as the text file.
#outfile = open(file_to_save, "w")
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #outfile.write("Hello World")
    #txt_file.write("Hello World")

    # Write three counties to the file.
    #txt_file.write("Counties in the Election \n")
    #txt_file.write("--------------------------- \n")
    #txt_file.write("Arapahoe \nDenver \nJefferson")

# Close the file
#file_to_save.close()
