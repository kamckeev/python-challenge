import os
import csv
canidates_dict ={}
candidates= []
csvpath = os.path.join('..', 'PyPoll', 'election_data2.csv')
with open(csvpath, newline= '') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
         
    for i in csvreader:
        candidates.append(i[2])
        if i[2] not in canidates_dict:
            canidates_dict[i[2]]=1
        else:
            canidates_dict[i[2]] = canidates_dict[i[2]]+1
    row_count = len(candidates)
    

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
    print(f'The winner was: (function needed to search for greatest numbrr of votes')
    print('{:*^50}'.format(''))

