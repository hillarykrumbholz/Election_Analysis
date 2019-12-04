# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidtes who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidtae won.
# 5. The winner of the election based on popular vote.

# Import the datetime dependency.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is, ", now)

# Add to our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources\election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file. 
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    #print(election_data)

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)
    

# Close the file.
election_data.close()

# Create a filename variable to a direct or indorect path to the file. 
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode will write data to the file.
#open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as the text file.
#outfile = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #outfile.write("Hello World")
    #txt_file.write("Hello World")

    # Write three counties to the file.
    txt_file.write("Counties in the Election \n")
    txt_file.write("--------------------------- \n")
    txt_file.write("Arapahoe \nDenver \nJefferson")

# Close the file
file_to_save.close()
