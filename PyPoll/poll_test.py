import os
import csv
candidate_raws ={}
candidates= []
csvpath = os.path.join('..', 'PyPoll', 'election_data2.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
         
    for i in csvreader:
        candidates.append(i[2])
        if i[2] not in candidate_raws:
            candidate_raws[i[2]]=1
        else:
            candidate_raws[i[2]] = candidate_raws[i[2]]+1
    row_count = len(candidates)
candidate_names =list(candidate_raws)
candidate_votes= list(candidate_raws.values())
winner_value= max(candidate_votes)

winner_name = 'n/a'
for name, votes in candidate_raws.items(): 
    if votes == winner_value:
        winner_name= name 



#printout:
print('{:*^50}'.format('Election Results'))
print('{:^30}'.format(f'The total number of votes cast was {row_count} votes!'))
print('{:^50}'.format('~'))
# The percentage of votes each candidate won
print(f'Candidate () had ()% of the vote, (x votes)')
print(f'Candidate () had ()% of the vote, (x votes)')
print(f'Candidate () had ()% of the vote, (x votes)')
print(f'Candidate () had ()% of the vote, (x votes)')
print('{:^50}'.format('~'))
#The winner of the election based on popular vote
# the winner: name
print(f'The winner was: {winner_name}')
print('{:*^50}'.format(''))

