import os
import csv
csvpath = os.path.join('..', 'PyPoll', 'election_data2.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    csv_header = next(csvfile)
    
    # number of votes
    row_count = sum(1 for i in _csvfile_)
    # A complete list of candidates who received votes
    
    print(row_count)

    # Count how many sightings have occured within each state
#state_counts = usa_ufo_df["state"].value_counts()
#state_counts.head()